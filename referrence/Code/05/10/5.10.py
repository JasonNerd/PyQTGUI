# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.10.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(215, 128)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(75, 44, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)  # 设置文本框为密码
        self.lineEdit_2.setValidator(QtGui.QIntValidator(10000000, 99999999))  # 设置只能输入8位数字
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(113, 97, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(76, 12, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(33, 97, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(26, 46, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(26, 16, 54, 12))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(36, 73, 61, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True) # 设置管理员单选按钮默认选中
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(106, 73, 71, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        # 为登录按钮的clicked信号绑定自定义槽函数
        self.pushButton.clicked.connect(self.login)
        # 为退出按钮的clicked信号绑定MainWindow窗口自带的close槽函数
        self.pushButton_2.clicked.connect(MainWindow.close)

        # 为单选按钮的toggled信号绑定自定义槽函数
        self.radioButton.toggled.connect(self.select)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def login(self):
        # 使用information()方法弹出信息提示框
        QMessageBox.information(MainWindow, "登录信息", "用户名："+self.lineEdit.text()+"  密码："+self.lineEdit_2.text(), QMessageBox.Ok)

    # 自定义槽函数，用来判断用户登录身份
    def select(self):
        if self.radioButton.isChecked(): # 判断是否为管理员登录
            QMessageBox.information(MainWindow, "提示","您选择的是 管理员  登录", QMessageBox.Ok)
        elif self.radioButton_2.isChecked(): # 判断是否为普通用户登录
            QMessageBox.information(MainWindow, "提示", "您选择的是 普通用户  登录", QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "系统登录"))
        self.pushButton_2.setText(_translate("MainWindow", "重置"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label_2.setText(_translate("MainWindow", "密  码："))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.radioButton.setText(_translate("MainWindow", "管理员"))
        self.radioButton_2.setText(_translate("MainWindow", "普通用户"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程