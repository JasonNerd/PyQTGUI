# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.16.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def alignbtn(self, pg, i, title):
        btn = QtWidgets.QToolButton(pg)
        btn.setGeometry(QtCore.QRect(20, 50*i+2, 70, 50))
        btn.setText(title+"__"+str(i))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(142, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建ToolBox工具盒
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 141, 391))
        self.toolBox.setObjectName("toolBox")
        # 我的好友设置
        page = QtWidgets.QWidget()
        page.setGeometry(QtCore.QRect(0, 0, 141, 287))
        page.setObjectName("page")
        self.alignbtn(page, 0, "好友")
        self.alignbtn(page, 1, "好友")
        self.alignbtn(page, 2, "好友")
        self.alignbtn(page, 3, "好友")
        self.toolBox.addItem(page, "好友")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBox.setCurrentIndex(0) # 默认选择第一个页面，即我的好友


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)  # 只显示关闭按钮
   MainWindow.show() # 显示窗体
   sys.exit(app.exec()) # 程序关闭时退出进程