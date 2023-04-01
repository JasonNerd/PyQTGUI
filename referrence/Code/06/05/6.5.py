# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 197)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建一个TreeView树视图
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 421, 201))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        model = QtGui.QStandardItemModel() # 创建数据模型
        model.setHorizontalHeaderLabels(['年级','班级','姓名','分数'])
        name=['马云','马化腾','李彦宏','王兴','刘强东','董明珠','张一鸣','任正非','丁磊','程维'] # 姓名列表
        score=[65,89,45,68,90,100,99,76,85,73] # 分数列表
        import  random
        # 设置数据
        for i in range(0,6):
            # 一级节点：年级，只设第1列的数据
            grade = QtGui.QStandardItem(("%s年级")%(i + 1))
            model.appendRow(grade) # 一级节点
            for j in range(0,4):
                # 二级节点：班级、姓名、分数
                itemClass = QtGui.QStandardItem(("%s班")%(j+1))
                itemName = QtGui.QStandardItem(name[random.randrange(10)])
                itemScore = QtGui.QStandardItem(str(score[random.randrange(10)]))
                grade.appendRow([QtGui.QStandardItem(""),itemClass,itemName,itemScore]) # 将二级节点添加到一级节点上

        self.treeView.setModel(model) # 为TreeVIew设置数据模型

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