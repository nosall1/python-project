# -*- coding:utf-8 -*-
"""
 建造者模式
"""


# 主餐
class Burger():
    name = ''
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class cheeseBurger(Burger):
    def __init__(self):
        self.name = 'cheese burger'
        self.price = 10.0


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = 'spicy chicken burger'
        self.price = 15.0


# 小食
class Snack():
    name = ''
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = 'chips'
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = 'chicken wings'
        self.price = 12.0


# 饮料
class Beverage():
    name = ''
    price = 0.0
    type = 'BEVERAGE'

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = 'coke'
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = 'milk'
        self.price = 5.0


class orderBuilder():
    bBurger = ''
    bSnack = ''
    bBeverage = ''

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSanck):
        self.bSnack = xSanck

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return order(self)


class order():
    burger = ''
    snack = ''
    beverage = ''

    def __init__(self,orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        # type: () -> object
        print ('Burrage:%s' % self.burger.getName())
        print ('Snack:%s' % self.snack.getName())
        print ('Beverage:%s' % self.beverage.getName())


if __name__ == '__main__':
    order_builder = orderBuilder()
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())
    order_1 = order_builder.build()
    order_1.show()
