#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/7/23
"""
import sys
from PyQt5.QtWidgets import *

app=QApplication(sys.argv)
win=QWidget()
win.resize(450,150)
win.move(0,300)
win.setWindowTitle('xlj')
win.show()

sys.exit(app.exec_())

print(1)