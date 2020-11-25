#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/5
 QSplitter,用户可以拖动子控件边界来调整子控件的尺寸
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QSplitter, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox=QHBoxLayout(self)

        topleft=QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topRight=QFrame(self)
        topRight.setFrameShape(QFrame.StyledPanel)

        bottom=QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1=QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topRight)

        splitter2=QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QSplitter')
        self.show()

    def onChanged(self,text):
        self.lbl.setText(text)
        self.adjustSize()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())