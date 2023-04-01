# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/图标 (7).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)

        # MainWindow.setStyleSheet("#MainWindow{background-color:red}") # 设置背景颜色
        # MainWindow.setStyleSheet("#MainWindow{border-image:url(image/back.jpg)}") # 设置背景图片


        # # 使用QPalette设置窗口背景颜色
        # palette=QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.Background,Qt.red)
        # MainWindow.setPalette(palette)

        # # 使用QPalette设置窗口背景图片
        # MainWindow.resize(252, 100)
        # palette = QtGui.QPalette()
        # palette.setBrush(QtGui.QPalette.Background, QBrush(QPixmap("./image/back.jpg")))
        # MainWindow.setPalette(palette)

        # # 使用QPalette设置窗口背景图片(自动适应窗体大小)
        # MainWindow.resize(252, 100)
        # palette = QtGui.QPalette()
        # palette.setBrush(MainWindow.backgroundRole(), QBrush(
        #     QPixmap("image/back.jpg").scaled(MainWindow.size(), QtCore.Qt.IgnoreAspectRatio,
        #                                      QtCore.Qt.SmoothTransformation)))
        # MainWindow.setPalette(palette)

        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 252, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "标题栏"))


import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程

