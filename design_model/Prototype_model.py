# -*- coding:utf-8 -*-
"""
 原型模式
"""
from copy import copy, deepcopy


# 图层对象
class simpleLayer:
    background = [0, 0, 0, 0]
    content = 'blank'

    def getContent(self):
        return self.content

    def getBackground(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


# 新建图层，填充蓝底并画一只狗
if __name__ == '__main__':
    dog_layer = simpleLayer()
    dog_layer.paint('Dog')
    dog_layer.fillBackground([0, 0, 255, 0])
    print ('Background:', dog_layer.getBackground())
    print ('Painting:', dog_layer.getContent())
    another_dog_layer = dog_layer.clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint('Puppy')
    print ('Original Background:', dog_layer.getBackground())
    print ('Original Painting:', dog_layer.getContent())
    print ('Copy Bakground:', another_dog_layer.getBackground())
    print ('Copy Painting:', another_dog_layer.getContent())
