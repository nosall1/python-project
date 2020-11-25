#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/3
 发出信号
"""
import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    # 创建closeapp的信号
    closeApp=pyqtSignal()

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c=Communicate()
        #连接着QMainWindow的close()插槽
        self.c.closeApp.connect(self.close)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())