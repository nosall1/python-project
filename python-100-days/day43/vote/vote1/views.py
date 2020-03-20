from django.http import JsonResponse
from django.shortcuts import render, redirect
from vote1.models import Subject,Teacher
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