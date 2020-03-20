from io import BytesIO

import xlwt
from django.contrib.admin.utils import quote
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from vote1.models import Subject,Teacher,User
from vote1.form import RegisterForm,LoginForm
import random
from vote1.create_captcha import Captcha
# Create your views here.
# 查看所有学科
def show_subjects(request):
    subjects=Subject.objects.all()
    return render(request,'subject.html',{'subjects':subjects})

# 显示指定学科的信息
def show_teachers(request):
    try:
        sno=int(request.GET['sno'])
        subject=Subject.objects.get(no=sno)
        teachers=subject.teacher_set.all()
        return render(request,'teachers.html',{'subject':subject,'teachers':teachers})
    except(KeyError,ValueError,Subject.DoesNotExist):
        return redirect('/')

# 好评
def prise_or_criticize(request):
    try:
        tno=int(request.GET['tno'])
        teacher=Teacher.objects.get(no=tno)
        if request.path.startswith('/praise'):
            teacher.good_count+=1
        else:
            teacher.bad_count+=1
        teacher.save()
        data={'code':200,'hint':'操作成功'}
    except(KeyError,ValueError,Teacher.DoseNotExist):
        data={'code':404,'hint':'操作失败'}
    return JsonResponse(data)

# 登录
def login(request:HttpRequest):
    hint=''
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            # 对验证码的正确性进行验证
            captcha_from_user=form.cleaned_data['captcha']
            captcha_from_sess=request.session.get('captcha','')
            if captcha_from_sess.lower()!=captcha_from_user.lower():
                hint='请输入正确的验证码'
            else:
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=User.objects.filter(username=username,password=password).first()
                if user:
                    # 登录成功后将用户编号和用户名保存在session中
                    request.session['userid']=user.no
                    request.session['username']=user.username
                    return redirect('/')
                else:
                    hint='用户名或密码错误'
        else:
            hint='请输入有效的登录信息'
    return render(request,'login.html',{'hint':hint})
# 注册
def register(request):
    page,hint='register.html',''
    if request.method=='POST':
        form=RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            page='login.html'
            hint='注册成功，请登录'
        else:
            hint='请输入有效的注册信息'
    return render(request,page,{'hint':hint})

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def get_captcha_text(length=4):
    selected_chars=random.choices(ALL_CHARS,k=length)
    return ''.join(selected_chars)

# 获取验证码
def get_captcha(request):
    captcha_text=get_captcha_text()
    request.session['captcha']=captcha_text
    image=Captcha.instance().generate(captcha_text)
    return HttpResponse(image,content_type='image/png')
# 注销
def logout(request):
    request.session.flush()
    return redirect('/')

# 创建工作薄
def export_teachers_excel(request):
    wb=xlwt.Workbook()
    # 添加工作表
    sheet=wb.add_sheet('老师信息表')
    # 查询所有老师的信息
    queryset=Teacher.objects.all()
    # 向excel表单中写入表头
    colnames=('姓名', '介绍', '好评数', '差评数', '学科')
    for index,name in enumerate(colnames):
        sheet.write(0,index,name)
    # 向单元格中写入老师的数据
    props=('name','detail','good_count','bad_count','subject')
    for row,teacher in enumerate(queryset):
        for col,prop in enumerate(props):
            value=getattr(teacher,prop,'')
            if isinstance(value,Subject):
                value=value.name
                print(value)
            sheet.write(row+1,col,value)
    # 保存excel
    buffer=BytesIO()
    wb.save(buffer)
    # 将二进制数据写入响应的消息体中并设置MIME类型
    resp=HttpResponse(buffer.getvalue(),content_type='application/vnd.ms-excel')
    # 中文文件名需要处理成百分号编码
    filename=quote('11.xls')
    # 通过响应头告知浏览器下载该文件以及对应的文件名
    resp['content-disposition'] = f'attachment; filename="{filename}"'
    return resp

def echarts(request):
    return render(request,'teachers_data.html')
# 查询所有老师的信息
def get_teachers_data(request):
    queryset=Teacher.objects.all()
    # 用生成式将老师的名字放在一个列表中
    names=[teacher.name for teacher in queryset]
    good=[teacher.good_count for teacher in queryset]
    bad=[teacher.bad_count for teacher in queryset]
    return JsonResponse({'names':names,'good':good,'bad':bad})