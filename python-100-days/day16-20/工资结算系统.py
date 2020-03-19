#-*- coding:utf-8 -*-
"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod


# 员工抽象类
class Employee(metaclass=ABCMeta):
    def __init__(self,name):
        self.name=name

    """
      @abstractmethod：抽象方法，含abstractmethod方法的类不能实例化，继承了含abstractmethod方法的子类必须复写所有abstractmethod装饰的方法，未被装饰的可以不重写
      @ property：方法伪装属性，方法返回值及属性值，被装饰方法不能有参数，必须实例化后调用，类不能调用
      @ classmethod：类方法，可以通过实例对象和类对象调用，被该函数修饰的方法第一个参数代表类本身常用cls，被修饰函数内可调用类属性，不能调用实例属性
      @staticmethod：静态方法，可以通过实例对象和类对象调用，被装饰函数可无参数，被装饰函数内部通过类名.属性引用类属性或类方法，不能引用实例属性
     """

    @abstractmethod
    def get_salary(self):
        # 结算月薪(抽象方法)
        pass

# 部门经理
class Manager(Employee):
    def get_salary(self):
        return 15000.0

# 程序员
class Programmer(Employee):
    def __init__(self,name,working_hour=0):
        self.working_hour=working_hour
        super().__init__(name)
    def get_salary(self):
        return 200.0*self.working_hour

# 销售员
class Salesman(Employee):
    def __init__(self,name,sales=0.0):
        self.sales=sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0+self.sales*0.05

# 创建员工的工厂（工厂模式-通过工厂实现对象使用者和对象之间的解耦合）
class EmployeeFactory():
    @staticmethod
    def create(emp_type,*args,**kwargs):
        # 创建员工
        all_emp_types={'M':Manager,'P':Programmer,'S':Salesman}
        cls=all_emp_types[emp_type.upper()]
        return cls(*args,**kwargs) if cls else None

def main():
    emps=[
        EmployeeFactory.create('M','曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(emp.name,":","%.2f"%emp.get_salary(),'元')

if __name__ == '__main__':
    main()