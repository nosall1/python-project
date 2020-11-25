#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/7/25
"""
import sys
from PyQt5.QtWidgets import QApplication,QWidget
class GUI():
    def __init__(self):
        self.initUI()

    def initUI(self):
        self.win=QWidget()
        self.win.setWindowTitle('xlj')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    gui=GUI()
    gui.win.show()
    sys.exit(app.exec_())