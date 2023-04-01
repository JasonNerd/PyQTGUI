# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(268, 115)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 268, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.open)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # from PyQt5.QtWidgets import QDesktopWidget # 导入屏幕类
        # screen=QDesktopWidget().screenGeometry() # 获取屏幕大小
        # width =screen.width() # 获取屏幕的宽
        # height =screen.height() # 获取屏幕的高

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "打开"))


    def open(self):
        import untitled2,untitled3,untitled4
        self.second = untitled2.Ui_MainWindow()  # 创建第2个窗体对象
        self.second.show()  # 显示窗体
        self.third = untitled3.Ui_MainWindow()  # 创建第3个窗体对象
        self.third.show()  # 显示窗体
        self.fouth = untitled4.Ui_MainWindow()  # 创建第4个窗体对象
        self.fouth.show()  # 显示窗体


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程