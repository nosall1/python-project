#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/8/1
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 每一个pyqt5应用程序必须创建一个应用程序对象，sys.argv参数是一个列表，从命令行输入参数
    app=QApplication(sys.argv)
    # Qwiget部件是pyqt5所有用户界面对象的基类，他提供默认构造函数，默认构造函数没有父类
    w=QWidget()
    # resize()方法移动窗口的大小
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('simple')
    w.show()

    sys.exit(app.exec_())
