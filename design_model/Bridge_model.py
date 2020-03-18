# -*- coding:utf-8 -*-
"""
 桥梁模式
"""


# 形状
class Shape:
    name = ''
    param = ''

    def __init__(self, *param):
        pass

    def getName(self):
        return self.name

    def getParam(self):
        return self.name, self.param


# 画笔
class Pen:
    shape = ''
    type = ''

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        pass


# 矩形
class Rectangle(Shape):
    def __init__(self, long, width):
        self.name = "Rectangle"
        self.param = 'Long:%s width:%s' % (long, width)
        print ('Create a rectangle:%s' % self.param)


# 圆形
class Circle(Shape):
    def __init__(self, radius):
        self.name = 'Circle'
        self.param = 'Radius:%s' % radius
        print ('Create a circle:%s' % self.param)


class NormalPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = 'Normal Line'

    def draw(self):
        print ('DRAWING %s:%s----PARAMS:%s' % (self.type, self.shape.getName(), self.shape.getParam()))


class BrushPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = 'Brush Line'

    def draw(self):
        print ('DRAWING %s:%s----PARAMS:%s' % (self.type, self.shape.getName(), self.shape.getParam()))


if __name__ == '__main__':
    normal_pen = NormalPen(Rectangle('20cm', '10cm'))
    brush_pen = BrushPen(Circle('15cm'))
    normal_pen.draw()
    brush_pen.draw()
