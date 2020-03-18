# -*- coding:utf-8 -*-
"""
 享元模式
"""


class Coffee:
    name = ''
    price = 0

    def __init__(self, name):
        self.name = name
        self.price = len(name)  # 在实际业务中，咖啡价格应该是由配置表进行配置，或者调用接口获取等方式得到，此处为说明享元模式，将咖啡价格定为名称长度，只是一种简化

    def show(self):
        print ('Coffee Name:%s price：%s' % (self.name, self.price))


# 咖啡工厂
class CoffeeFactory():
    coffee_dict = {}

    def getCoffee(self, name):
        if self.coffee_dict.has_key(name) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def getCoffeeCount(self):
        return len(self.coffee_dict)


class Customer:
    coffee_factory = ''
    name = ''

    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffer_name):
        print ('%s ordered a cup of coffee:%s' % (self.name, coffer_name))
        return self.coffee_factory.getCoffee(coffer_name)


# 假设业务中短时间内有多人订了咖啡，业务模拟如下
if __name__ == '__main__':
    coffee_factory = CoffeeFactory()
    customer_1 = Customer('A client', coffee_factory)
    customer_2 = Customer('B client', coffee_factory)
    customer_3 = Customer('C client', coffee_factory)
    c1_app = customer_1.order('cappuccino')
    c1_app.show()
    c2_app = customer_2.order('mocha')
    c2_app.show()
    c3_app = customer_3.order('cappuccino')
    c3_app.show()
    print ('Num of Coffee Instance:%s' % coffee_factory.getCoffeeCount())
