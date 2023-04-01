# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '8.2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 323)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建一个按钮控件
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 91, 23))
        self.pushButton.setObjectName("pushButton")
        # 创建一个ListWidget列表，用来显示选择的图片文件
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 331, 261))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为按钮的clicked信号绑定槽函数
        self.pushButton.clicked.connect(self.bindList)

    def bindList(self):
        from PyQt5.QtWidgets import QFileDialog
        dir =QFileDialog() # 创建文件对话框
        dir.setFileMode(QFileDialog.ExistingFiles) # 设置多选
        dir.setDirectory('C:\\') # 设置初始路径为C盘
        # 设置只显示图片文件
        dir.setNameFilter('图片文件(*.jpg *.png *.bmp *.ico *.gif)')
        if dir.exec_(): # 判断是否选择了文件
            self.listWidget.addItems(dir.selectedFiles()) # 将选择的文件显示在列表中

        # files, filetype = QFileDialog.getOpenFileNames(None, '打开', 'C:\\', '图片文件(*.jpg *.png *.bmp *.ico *.gif)')
        # self.listWidget.addItems(files)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程