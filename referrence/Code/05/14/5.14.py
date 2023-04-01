# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.14.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 350, 200))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 设置列表中可以多选
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # 设置选中方式为整行选中
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 设置以列表形式显示数据
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setWordWrap(True) # 设置自动换行
        from collections import OrderedDict
        # 定义有序字典，作为List列表的数据源
        dict=OrderedDict({'第1名':'战狼2,2017年上映，票房56.83亿','第2名':'哪吒之魔童降世，2019年上映，票房50.12亿',
                          '第3名':'流浪地球，2019年上映，票房46.86亿','第4名':'复仇者联盟：终局之战，2019年上映，票房42.50亿',
                          '第5名':'红海行动，2018年上映，票房36.51亿','第6名':'唐人街探案2，2018年上映，票房33.98亿',
                          '第7名': '美人鱼，2016年上映，票房33.86亿', '第8名': '我和我的祖国，2019年上映，票房31.71亿',
                          '第9名': '我不是药神，2018年上映，票房31.00亿', '第10名': '中国机长，2019年上映，票房29.13亿'})
        for key,value in dict.items():# 遍历字典，并分别获取到键值
            self.item = QtWidgets.QListWidgetItem(self.listWidget)# 创建列表项
            self.item.setText(key+'：'+value) # 设置项文本
            self.item.setToolTip(value)  # 设置提示文字
        self.listWidget.itemClicked.connect(self.gettext)

    # 自定义槽函数，获取列表选中项的值
    def gettext(self,item):
        if item.isSelected(): # 判断项是否选中
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.information(MainWindow,"提示","您选择的是："+item.text(),QMessageBox.Ok)

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