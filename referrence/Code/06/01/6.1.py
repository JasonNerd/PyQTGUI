# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 259)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 10, 201, 31))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(50, 180, 201, 31))
        self.progressBar_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar_2.setProperty("value", -1)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(20, 10, 31, 201))
        self.progressBar_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_3.setProperty("value", -1)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar_3.setTextVisible(True)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_1 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_1.setGeometry(QtCore.QRect(250, 10, 31, 201))
        self.progressBar_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar_1.setProperty("value", -1)
        self.progressBar_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.progressBar_1.setTextVisible(True)
        self.progressBar_1.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_1.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_1.setObjectName("progressBar_1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 220, 101, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QBasicTimer() # 创建定时器对象
        # 为按钮绑定单击信号
        self.pushButton.clicked.connect(self.running)
    # 控制进度条的滚动效果
    def running(self):
        if self.timer.isActive(): # 判断计时器是否开启
            self.timer.stop() # 停止计时器
            self.pushButton.setText('开始')# 设置按钮的文本
            # 设置4个进度条的最大值为100
            self.progressBar.setMaximum(100)
            self.progressBar_1.setMaximum(100)
            self.progressBar_2.setMaximum(100)
            self.progressBar_3.setMaximum(100)
        else:
            self.timer.start(100,MainWindow) # 启动计时器
            self.pushButton.setText('停止') # 设置按钮的文本
            # 将4个进度条的最大值和最小值都设置为0，以便显示循环滚动的效果
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(0)
            self.progressBar_1.setInvertedAppearance(True) # 设置进度反方向显示
            self.progressBar_1.setMinimum(0)
            self.progressBar_1.setMaximum(0)
            self.progressBar_2.setMinimum(0)
            self.progressBar_2.setMaximum(0)
            self.progressBar_3.setMinimum(0)
            self.progressBar_3.setMaximum(0)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "跑马灯效果"))
        self.pushButton.setText(_translate("MainWindow", "开始"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程