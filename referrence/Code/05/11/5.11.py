# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.11.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(211, 139)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(22, 19, 101, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(122, 19, 101, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(22, 49, 101, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(122, 49, 101, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(22, 78, 101, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 106, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.getvalue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getvalue(self):
        oper="" # 记录用户权限
        if self.checkBox.isChecked(): # 判断复选框是否选中
            oper+=self.checkBox.text() # 记录选中的权限
        if self.checkBox_2.isChecked():
            oper +='\n'+ self.checkBox_2.text()
        if self.checkBox_3.isChecked():
            oper+='\n'+ self.checkBox_3.text()
        if self.checkBox_4.isChecked():
            oper+='\n'+ self.checkBox_4.text()
        if self.checkBox_5.isChecked():
            oper+='\n'+ self.checkBox_5.text()
        from  PyQt5.QtWidgets import QMessageBox
        # 使用information()方法弹出信息提示，显示所有选择的权限
        QMessageBox.information(MainWindow, "提示", "您选择的权限如下：\n"+oper, QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设置用户权限"))
        self.checkBox.setText(_translate("MainWindow", "基本信息管理"))
        self.checkBox_2.setText(_translate("MainWindow", "进货管理"))
        self.checkBox_3.setText(_translate("MainWindow", "销售管理"))
        self.checkBox_4.setText(_translate("MainWindow", "库存管理"))
        self.checkBox_5.setText(_translate("MainWindow", "系统管理"))
        self.pushButton.setText(_translate("MainWindow", "设置"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程