# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.6.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 260, 150))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setColumnCount(2) # 设置树结构中的列数
        self.treeWidget.setHeaderLabels(['姓名','职务']) # 设置列标题名
        root=QTreeWidgetItem(self.treeWidget) # 创建节点
        root.setText(0,'组织结构') # 设置顶级节点文本
        # 定义字典，存储树中显示的数据
        dict= {'任正非':'华为董事长','马云':'阿里巴巴创始人','马化腾':'腾讯CEO','李彦宏':'百度CEO','董明珠':'格力董事长'}
        for key,value in dict.items(): # 遍历字典
            child=QTreeWidgetItem(root) # 创建子节点
            child.setText(0,key) # 设置第一列的值
            child.setText(1,value) # 设置第二列的值
            # 为节点设置图标
            if key=='任正非':
                child.setIcon(0,QtGui.QIcon('images/华为.jpg'))
            elif key=='马云':
                child.setIcon(0,QtGui.QIcon('images/阿里巴巴.jpg'))
            elif key=='马化腾':
                child.setIcon(0,QtGui.QIcon('images/腾讯.png'))
            elif key=='李彦宏':
                child.setIcon(0,QtGui.QIcon('images/百度.jpg'))
            elif key=='董明珠':
                child.setIcon(0,QtGui.QIcon('images/格力.jpeg'))
            child.setCheckState(0,QtCore.Qt.Checked) # 为节点设置复选框，并且选中
        self.treeWidget.addTopLevelItem(root) # 将创建的树节点添加到树控件中
        self.treeWidget.setAlternatingRowColors(True) # 设置隔行变色
        self.treeWidget.expandAll() # 展开所有树节点
        self.treeWidget.clicked.connect(self.gettreetext)  # 为树控件绑定单击信号

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def gettreetext(self,index):
        item=self.treeWidget.currentItem() # 获取当前选中项
        # 弹出提示框，显示选中项的文本
        QtWidgets.QMessageBox.information(MainWindow,'提示','您选择的是：%s -- %s'%(item.text(0),item.text(1)),QtWidgets.QMessageBox.Ok)

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