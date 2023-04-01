# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '13.3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtCore import *  # 导入线程相关模块

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 267)
        MainWindow.setWindowTitle("龟兔赛跑") # 设置窗口标题
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建兔子比赛标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 91, 21))
        self.label.setObjectName("label")
        self.label.setText("兔子的比赛记录")
        # 显示兔子的比赛记录
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 161, 191))
        self.textEdit.setObjectName("textEdit")
        # 创建乌龟比赛标签
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("乌龟的比赛记录")
        # 显示乌龟的比赛记录
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 40, 161, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        # 创建“开始比赛”按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("开始比赛")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.r=Rabbit() # 创建兔子线程对象
        self.r.sinOut.connect(self.rabbit) # 将线程信号连接到槽函数
        self.t = Tortoise() # 创建乌龟线程对象
        self.t.sinOut.connect(self.tortoise) # 将线程信号连接到槽函数
        self.pushButton.clicked.connect(self.start) # 开始两个线程

    def start(self):
        self.r.start() # 启动兔子线程
        self.t.start() # 启动乌龟线程

    # 显示兔子的跑步距离
    def rabbit(self,str):
        self.textEdit.setPlainText(self.textEdit.toPlainText() + str)

    # 显示乌龟的跑步距离
    def tortoise(self, str):
        self.textEdit_2.setPlainText(self.textEdit_2.toPlainText() + str)

class Rabbit(QThread): # 创建兔子线程类
    sinOut=pyqtSignal(str) # 自定义信号，用来发射兔子比赛动态
    def __init__(self):
        super(Rabbit,self).__init__()
    # 重写run()方法
    def run(self):
        for i in range(1,11):
            # 循环10次模拟赛跑的过程
            QThread.msleep(100) # 线程休眠0.1秒，模拟兔子在跑步
            self.sinOut.emit("\n  兔子跑了" + str(i) + "0米") # 显示兔子的跑步距离
            if i == 9:
                self.sinOut.emit("\n  兔子在睡觉") # 当跑了90米时开始睡觉
                QThread.sleep(5) # 线程休眠5秒
            if i == 10:
                self.sinOut.emit("\n  兔子到达终点") # 显示兔子到达了终点

class Tortoise(QThread): # 创建乌龟线程类
    sinOut=pyqtSignal(str) # 自定义信号，用来发射乌龟比赛动态
    def __init__(self):
        super(Tortoise,self).__init__()
    # 重写run()方法
    def run(self):
        for i in range(1,11):
            QThread.msleep(500) # 线程休眠0.5秒，模拟乌龟在跑步
            self.sinOut.emit("\n  乌龟跑了" + str(i) + "0米")
            if i == 10:
                self.sinOut.emit("\n  乌龟到达终点")
# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程