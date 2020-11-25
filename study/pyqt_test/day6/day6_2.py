#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/4
"""
import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col=QColor(0,0,0)
        self.btn=QPushButton('Dialog',self)
        self.btn.move(20,20)

        self.btn.clicked.connect(self.showDialog)
        self.frm=QFrame(self)
        self.frm.setStyleSheet('QWidget {background-color:%s}'%col.name())
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300,300,250,180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        # 初始化QFrame的颜色为黑色
        col=QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget {background-color:%s}'%col.name())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())