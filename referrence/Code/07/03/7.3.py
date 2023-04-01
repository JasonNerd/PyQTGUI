# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '7.3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 107)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # 添加一个状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.label=QtWidgets.QLabel() # 创建一个Label控件
        # self.label.setText('版权所有：吉林省明日科技有限公司') # 设置Label的文本
        # self.statusbar.addWidget(self.label) # 将Label控件添加到状态栏中
        # self.statusbar.showMessage('当前登录用户：mr', 0)  # 在状态栏中显示临时信息

        # self.statusbar.clearMessage() # 清除状态栏中的临时信息

        timer = QtCore.QTimer(MainWindow) # 创建一个QTimer计时器对象
        timer.timeout.connect(self.showtime) # 发射timeout信号，与自定义槽函数关联
        timer.start() # 启动计时器
    # 自定义槽函数，用来在状态栏中显示当前日期时间
    def showtime(self):
        datetime = QtCore.QDateTime.currentDateTime() # 获取当前日期时间
        text = datetime.toString("yyyy-MM-dd HH:mm:ss") # 对日期时间进行格式化
        self.statusbar.showMessage('当前日期时间：'+text, 0) # 在状态栏中显示日期时间

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程