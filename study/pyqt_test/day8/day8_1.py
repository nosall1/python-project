#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/5
 QPixmap是用于处理图像的控件
"""
import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox=QHBoxLayout(self)
        pixmap=QPixmap('icon.png')

        lbl=QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300,200)
        self.setWindowTitle('Red Rock')
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())