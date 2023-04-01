# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.7.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(522, 182)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 添加水平分割线，并设置显示样式为Sunken，表示有下沉显示的边框阴影
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(70, 50, 261, 16))
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken) # 设置分割线显示样式
        self.line_1.setLineWidth(8)
        self.line_1.setMidLineWidth(8)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine) # 设置水平分割线
        self.line_1.setObjectName("line_1")
        # 添加水平分割线，并设置显示样式为Plain，表示无阴影
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 80, 261, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)# 设置分割线显示样式
        self.line_2.setLineWidth(8)
        self.line_2.setMidLineWidth(8)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)# 设置水平分割线
        self.line_2.setObjectName("line_2")
        # 添加水平分割线，并设置显示样式为Raised，表示有凸起显示的边框阴影
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(70, 110, 261, 16))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)# 设置分割线显示样式
        self.line_3.setLineWidth(8)
        self.line_3.setMidLineWidth(8)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)# 设置水平分割线
        self.line_3.setObjectName("line_3")
        # 添加垂直分割线，并设置显示样式为Sunken，表示有下沉显示的边框阴影
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(370, 50, 16, 101))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken) # 设置分割线显示样式
        self.line_4.setLineWidth(4)
        self.line_4.setMidLineWidth(4)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine) # 设置垂直分割线
        self.line_4.setObjectName("line_4")
        # 添加垂直分割线，并设置显示样式为Plain，表示无阴影
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(430, 50, 16, 101))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain) # 设置分割线显示样式
        self.line_5.setLineWidth(4)
        self.line_5.setMidLineWidth(4)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine) # 设置垂直分割线
        self.line_5.setObjectName("line_5")
        # 添加垂直分割线，并设置显示样式为Raised，表示有凸起显示的边框阴影
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(480, 50, 16, 101))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Raised) # 设置分割线显示样式
        self.line_6.setLineWidth(4)
        self.line_6.setMidLineWidth(4)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine) # 设置垂直分割线
        self.line_6.setObjectName("line_6")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 51, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.label_3.setObjectName("label_3")

        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(330, 0, 20, 191))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 160, 51, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 160, 51, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 160, 51, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sunken："))
        self.label_2.setText(_translate("MainWindow", "Plain："))
        self.label_3.setText(_translate("MainWindow", "Raised："))
        self.label_4.setText(_translate("MainWindow", "Sunken"))
        self.label_5.setText(_translate("MainWindow", "Plain"))
        self.label_6.setText(_translate("MainWindow", "Raised"))
        self.label_7.setText(_translate("MainWindow", "水平分割线"))
        self.label_8.setText(_translate("MainWindow", "垂直分割线"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程