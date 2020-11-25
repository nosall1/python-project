#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/3
 菜单条，工具栏，状态栏
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction=QAction(QIcon('exit24.png'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar=self.menuBar()
        fileMenu=menubar.addMenu('$File')
        fileMenu.addAction(exitAction)

        toolbar=self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Main window')
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())