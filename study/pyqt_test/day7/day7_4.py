#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/4
 进度条
"""
import sys

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar=QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.btn=QPushButton('start',self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.doAction)

        self.timer=QBasicTimer()
        self.step=0

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self,e):
        if self.step>=100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step=self.step+1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('start')
        else:
            self.timer.start(100,self)
            self.btn.setText('stop')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())