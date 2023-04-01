# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.7.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap,QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(225, 121)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 83, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QIcon(QPixmap("login.ico"))) # 为登录按钮设置图标
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(29, 22, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(29, 52, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(79, 18, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(78, 50, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # 设置文本框为密码
        self.lineEdit_2.setValidator(QtGui.QIntValidator(10000000, 99999999))  # 设置只能输入8位数字
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 83, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(QIcon(QPixmap("exit.ico")))  # 为退出按钮设置图标
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        # 为登录按钮的clicked信号绑定自定义槽函数
        self.pushButton.clicked.connect(self.login)
        # 为退出按钮的clicked信号绑定MainWindow窗口自带的close槽函数
        self.pushButton_2.clicked.connect(MainWindow.close)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def login(self):
        from PyQt5.QtWidgets import QMessageBox
        # 使用information()方法弹出信息提示框
        QMessageBox.information(MainWindow, "登录信息", "用户名："+self.lineEdit.text()+"  密码："+self.lineEdit_2.text(), QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "系统登录"))
            self.pushButton.setText(_translate("MainWindow", "登录"))
            self.label.setText(_translate("MainWindow", "用户名："))
            self.label_2.setText(_translate("MainWindow", "密  码："))
            self.pushButton_2.setText(_translate("MainWindow", "退出"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程