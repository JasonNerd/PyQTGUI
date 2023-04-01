# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.16.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 141, 287))
        self.page.setObjectName("page")
        self.toolButton = QtWidgets.QToolButton(self.page)
        self.toolButton.setGeometry(QtCore.QRect(0, 0, 91, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("图标/01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(96, 96))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.page)
        self.toolButton_2.setGeometry(QtCore.QRect(0, 49, 91, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("图标/02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.page)
        self.toolButton_3.setGeometry(QtCore.QRect(0, 103, 91, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("图标/03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolBox.addItem(self.page, "")
        # 同学设置
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 141, 287))
        self.page_2.setObjectName("page_2")
        self.toolButton_4 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_4.setGeometry(QtCore.QRect(0, 0, 91, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("图标/04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolBox.addItem(self.page_2, "")
        # 同事设置
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.toolButton_5 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_5.setGeometry(QtCore.QRect(0, 1, 91, 51))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("图标/05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon4)
        self.toolButton_5.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_5.setAutoRaise(True)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_6.setGeometry(QtCore.QRect(0, 50, 91, 51))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("图标/06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon5)
        self.toolButton_6.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolBox.addItem(self.page_3, "")
        # 陌生人设置
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.toolButton_7 = QtWidgets.QToolButton(self.page_4)
        self.toolButton_7.setGeometry(QtCore.QRect(0, 7, 91, 51))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("图标/07.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon6)
        self.toolButton_7.setIconSize(QtCore.QSize(96, 96))
        self.toolButton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_7.setAutoRaise(True)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolBox.addItem(self.page_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0) # 默认选择第一个页面，即我的好友
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我的QQ"))
        self.toolButton.setText(_translate("MainWindow", "宋江"))
        self.toolButton_2.setText(_translate("MainWindow", "卢俊义"))
        self.toolButton_3.setText(_translate("MainWindow", "吴用"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "我的好友"))
        self.toolButton_4.setText(_translate("MainWindow", "林冲"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "同学"))
        self.toolButton_5.setText(_translate("MainWindow", "鲁智深"))
        self.toolButton_6.setText(_translate("MainWindow", "武松"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "同事"))
        self.toolButton_7.setText(_translate("MainWindow", "方腊"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "陌生人"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # 只显示关闭按钮
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程