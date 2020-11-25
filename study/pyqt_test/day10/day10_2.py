#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/7
 画点
"""
import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('Points')
        self.show()
    def paintEvent(self, e):
        qp=QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self,qp):
        qp.setPen(Qt.red)
        size=self.size()

        for i in range(1000):
            x=random.randint(1,size.width()-1)
            y=random.randint(1,size.height()-1)

            qp.drawPoint(x,y)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())