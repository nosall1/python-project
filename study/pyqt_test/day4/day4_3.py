#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/2
 工具栏
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAxtion=QAction(QIcon('exit24.png'),'Exit',self)
        exitAxtion.setShortcut('Ctrl+Q')
        exitAxtion.triggered.connect(qApp.quit)

        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitAxtion)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('ToolBar')
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())