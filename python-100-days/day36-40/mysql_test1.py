#-*- coding:utf-8 -*-
import pymysql

# 增加一个部门
def add_dept(cursor,no,name,loc):
    result=cursor.execute('insert into tb_dept values (%s,%s,%s)',(no,name,loc))
    return result
# 删除一个部门
def del_dept(cursor,no):
    result=cursor.execute('delete from tb_dept where dno=%s',(no,))
    return result
# 更新一个部门
def update_dept(cursor,no,name,loc):
    result=cursor.execute('update tb_dept set dname=%s,dloc=%s where dno=%s',(name,loc,no))
    return result
def main():
    no=int(input('编号：'))
    name=input('名字：')
    loc=input('所在地：')
    # 1.创建数据库连接对象
    con=pymysql.connect(host='localhost',port=3306,database='hrs',charset='utf8',user='root',password='1111111')
    try:
        # 1.通过连接对象获取游标
        with con.cursor() as cursor:
            # 通过游标执行sql并获得执行结果
            result=cursor.execute('insert into tb_dept values (%s,%s,%s)',(no,name,loc))
        if result==1:
            print('添加成功')
        # 4.操作成功提交事物
        con.commit()
    finally:
        # 5.关闭连接，释放资源
        con.close()
if __name__ == '__main__':
    main()