#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/1
 增加图标
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300,300,300,220)
        # 设置窗口的标题
        self.setWindowTitle('icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('web.png'))
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())