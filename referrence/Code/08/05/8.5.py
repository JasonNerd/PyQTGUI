# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '8.5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFontDialog,QColorDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 166)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 添加“设置字体”按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        # 添加一个水平布局管理器，主要为了使TextEdit控件位于该区域中
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 401, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 添加标签控件，用来体现设置的字体和颜色
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("label")
        self.horizontalLayout.addWidget(self.textEdit)
        # 添加“设置颜色”按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为“设置字体”按钮的clicked信号关联槽函数
        self.pushButton.clicked.connect(self.setfont)
        # 为“设置颜色”按钮的clicked信号关联槽函数
        self.pushButton_2.clicked.connect(self.setcolor)

    def setfont(self):
        font, ok = QFontDialog.getFont() # 字体对话框
        if ok: # 如果选择了字体
            self.textEdit.setFont(font) # 将选择的字体作为标签的字体

    def setcolor(self):
        color = QColorDialog.getColor()  # 颜色对话框
        if color.isValid():  # 判断颜色是否有效
            self.textEdit.setTextColor(color)  # 将选择的颜色作为标签的字体

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "设置字体"))
        self.textEdit.setText(_translate("MainWindow", "敢想敢为"))
        self.pushButton_2.setText(_translate("MainWindow", "设置颜色"))
# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程