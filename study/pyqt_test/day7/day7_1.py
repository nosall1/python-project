#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/4
 复选框控件
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb=QCheckBox('Show title',self)
        cb.move(20,20)
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self,state):

        if state==Qt.Checked:
            self.setWindowTitle('QcheckBox')
        else:
            self.setWindowTitle('')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

