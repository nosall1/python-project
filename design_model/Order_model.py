# -*- coding:utf-8 -*-
"""
 命令模式
"""


class backSys():
    def cook(self, dish):
        pass


class mainFoodSys(backSys):
    def cook(self, dish):
        print ('MAINFOOD:Cook %s' % dish)


class coolDishSys(backSys):
    def cook(self, dish):
        print ('COOLDISH:Cook %s' % dish)


class hotDishSys(backSys):
    def cook(self, dish):
        print ('HOTDISH:Cook %s' % dish)


class waiterSys():
    menu_map = dict()
    commandList = []

    def setOrder(self, command):
        print ('WAITER:Add dish')
        self.commandList.append(command)

    def cancelOrder(self, command):
        print ('WAITER:Cancel order...')
        self.commandList.remove(command)

    def notity(self):
        print ('WAITER:Nofify...')
        for command in self.commandList:
            command.execute()


# 命令类
class Command():
    receiver = None

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        pass


class foodCommand(Command):
    dish = ''

    def __init__(self, receiver, dish):
        self.receiver = receiver
        self.dish = dish

    def execute(self):
        self.receiver.cook(self.dish)


class mainFoodCommand(foodCommand):
    pass


class coolDishCommand(foodCommand):
    pass


class hotDishCommand(foodCommand):
    pass


class menuAll:
    menu_map = dict()

    def loadMenu(self):  # 加载菜单
        self.menu_map['hot'] = ['Yu-Shiang Shredded Pork', 'Sauteed Tofu,Home Style', 'Sauteed Snow Peas']
        self.menu_map['cool'] = ['Cucumber', 'Preserved egg']
        self.menu_map['main'] = ['Rice', 'Pie']

    def isHot(self, dish):
        if dish in self.menu_map['hot']:
            return True
        return False

    def isCool(self, dish):
        if dish in self.menu_map['cool']:
            return True
        return False

    def isMain(self, dish):
        if dish in self.menu_map['main']:
            return True
        return False


if __name__ == '__main__':
    dish_list = ['Yu-Shiang Shredded Pork', 'Sauteed Tofu,Home Style', 'Cucumber', 'Rice']
    waiter_sys = waiterSys()
    main_food_sys = mainFoodSys()
    cool_dish_sys = coolDishSys()
    hot_dish_sys = hotDishSys()
    menu = menuAll()
    menu.loadMenu()
    for dish in dish_list:
        if menu.isCool(dish):
            cmd = coolDishCommand(cool_dish_sys, dish)
        elif menu.isHot(dish):
            cmd = hotDishCommand(hot_dish_sys, dish)
        elif menu.isMain(dish):
            cmd = mainFoodCommand(main_food_sys, dish)
        else:
            continue
        waiter_sys.setOrder(cmd)

    waiter_sys.notity()
