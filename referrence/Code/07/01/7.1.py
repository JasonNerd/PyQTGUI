# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '7.1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 115)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menuBar = MainWindow.menuBar()
        # 添加菜单栏
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 344, 23))
        self.menuBar.setObjectName("menuBar")
        # 添加“文件”菜单
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu.setTitle("文件")
        # 添加“编辑”菜单
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_2.setTitle("编辑")
        MainWindow.setMenuBar(self.menuBar)
        # 添加“新建”菜单
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        self.actionxinjian.setEnabled(True) # 设置菜单可用
        # 为菜单设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/new.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionxinjian.setIcon(icon)
        # 设置菜单为Windows快捷键
        self.actionxinjian.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionxinjian.setIconVisibleInMenu(True) # 设置图标可见
        self.actionxinjian.setObjectName("actionxinjian")
        self.actionxinjian.setText("新建(&N)") # 设置菜单文本
        self.actionxinjian.setIconText("新建") # 设置图标文本
        self.actionxinjian.setToolTip("新建") # 设置提示文本
        self.actionxinjian.setShortcut("Ctrl+N") # 设置快捷键
        # 添加“打开”菜单
        self.actiondakai = QtWidgets.QAction(MainWindow)
        # 为菜单设置图标
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondakai.setIcon(icon1)
        self.actiondakai.setObjectName("actiondakai")
        self.actiondakai.setText("打开(&O)") # 设置菜单文本
        self.actiondakai.setIconText("打开") # 设置图标文本
        self.actiondakai.setToolTip("打开") # 设置提示文本
        self.actiondakai.setShortcut("Ctrl+O") # 设置快捷键
        # 添加“关闭”菜单
        self.actionclose = QtWidgets.QAction(MainWindow)
        # 为菜单设置图标
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionclose.setIcon(icon2)
        self.actionclose.setObjectName("actionclose")
        self.actionclose.setText("关闭(&C)") # 设置菜单文本
        self.actionclose.setIconText("关闭") # 设置图标文本
        self.actionclose.setToolTip("关闭") # 设置提示文本
        self.actionclose.setShortcut("Ctrl+M") # 设置快捷键

        self.menu.addAction(self.actionxinjian) # 在“文件”菜单中添加“新建”菜单项
        self.menu.addAction(self.actiondakai) # 在“文件”菜单中添加“打开”菜单项
        self.menu.addSeparator() # 添加分割线
        self.menu.addAction(self.actionclose) # 在“文件”菜单中添加“关闭”菜单项

        self.menuBar.addAction(self.menu.menuAction())  # 将“文件”菜单的菜单项添加到菜单栏中
        self.menuBar.addAction(self.menu_2.menuAction())  # 将“编辑”菜单的菜单项添加到菜单栏中

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为菜单中的QAction绑定triggered信号
        self.menu.triggered[QtWidgets.QAction].connect(self.getmenu)
    #
    #     # 单独为“新建”菜单绑定triggered信号
    #     self.actionxinjian.triggered.connect(self.getmenu)
    #
    # def getmenu(self):
    #     from PyQt5.QtWidgets import QMessageBox
    #     # 使用information()方法弹出信息提示框
    #     QMessageBox.information(MainWindow,"提示","您选择的是"+self.actionxinjian.text(),QMessageBox.Ok)

    def getmenu(self,m):
        from PyQt5.QtWidgets import QMessageBox
        # 使用information()方法弹出信息提示框
        QMessageBox.information(MainWindow,"提示","您选择的是"+m.text(),QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程