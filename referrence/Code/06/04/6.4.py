# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget) # 创建书对象
        self.treeView.setGeometry(QtCore.QRect(0, 0, 471, 281)) # 设置坐标位置和大小
        # 设置垂直滚动条为按需显示
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        # 设置水平滚动条为按需显示
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        # 设置双击或者按下回车键时，使树节点可编辑
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection) # 设置树节点为单选
        self.treeView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) # 设置选中节点时为整行选中
        self.treeView.setAutoExpandDelay(-1) # 设置自动展开的延时为-1，表示自动展开不可用
        self.treeView.setItemsExpandable(True) # 设置是否可以展开项
        self.treeView.setSortingEnabled(True) # 设置单击头部可排序
        self.treeView.setWordWrap(True) # 设置自动换行
        self.treeView.setHeaderHidden(False) # 设置不隐藏头部
        self.treeView.setExpandsOnDoubleClick(True) # 设置双击可以展开节点
        self.treeView.setObjectName("treeView")
        self.treeView.header().setVisible(True) # 设置显示头部
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        model =QtWidgets.QDirModel() # 创建存储文件系统的模型
        self.treeView.setModel(model) # 为树控件设置数据模型

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