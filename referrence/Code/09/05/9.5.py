# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '9.5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 274) # 设置窗口大小
        MainWindow.setWindowTitle("MDI窗口") # 设置窗口标题
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建MDI窗口区域
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 481, 251))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        # 创建菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 23))
        self.menubar.setObjectName("menubar")
        # 设置主菜单
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu.setTitle("子窗体操作")
        MainWindow.setMenuBar(self.menubar)
        # 设置新建菜单项
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        self.actionxinjian.setObjectName("actionxinjian")
        self.actionxinjian.setText("新建")
        # 设置平铺菜单项
        self.actionpingpu = QtWidgets.QAction(MainWindow)
        self.actionpingpu.setObjectName("actionpingpu")
        self.actionpingpu.setText("平铺显示")
        # 设置级联菜单项
        self.actionjilian = QtWidgets.QAction(MainWindow)
        self.actionjilian.setObjectName("actionjilian")
        self.actionjilian.setText("级联显示")
        # 将新建的3个菜单项添加到主菜单中
        self.menu.addAction(self.actionxinjian)
        self.menu.addAction(self.actionpingpu)
        self.menu.addAction(self.actionjilian)
        # 将设置完成的主菜单添加到菜单栏中
        self.menubar.addAction(self.menu.menuAction())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为菜单项关联信号
        self.menubar.triggered[QAction].connect(self.action)

    count=0 # 定义变量，用来表示新建的子窗口个数
    # 自定义槽函数，根据选择的菜单执行相应操作
    def action(self,m):
        if m.text()=="新建":
            sub=QMdiSubWindow() # 创建子窗口对象
            self.count = self.count + 1 # 记录子窗口个数
            # 设置子窗口标题
            sub.setWindowTitle("子窗口"+str(self.count))
            # 在子窗口中添加一个标签，并设置文本
            sub.setWidget(QLabel("这是第 %d 个子窗口"%self.count))
            self.mdiArea.addSubWindow(sub) # 将新建的子窗口添加到MDI区域
            sub.show() # 显示子窗口
        elif m.text()=="平铺显示":
            self.mdiArea.tileSubWindows() # 对子窗口平铺排列
        elif m.text()=="级联显示":
            self.mdiArea.cascadeSubWindows() # 对子窗口级联排列

# 主方法
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程