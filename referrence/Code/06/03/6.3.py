# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6.3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(313, 196)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建横向滑块
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 10, 231, 22))
        self.horizontalSlider.setMinimum(8) # 设置最小值为8
        self.horizontalSlider.setMaximum(72) # 设置最大值为72
        self.horizontalSlider.setSingleStep(1) # 设置通过鼠标拖动时的步长值
        self.horizontalSlider.setPageStep(1) # 设置通过鼠标点击时的步长值
        self.horizontalSlider.setProperty("value", 8) # 设置默认值为8
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal) # 设置滑块为横向滑块
        # 设置在滑块上方显示刻度
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(3) # 设置刻度的间隔
        self.horizontalSlider.setObjectName("horizontalSlider")
        # 创建垂直滑块
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(270, 20, 22, 171))
        self.verticalSlider.setMinimum(8) # 设置最小值为8
        self.verticalSlider.setMaximum(72) # 设置最大值为72
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical) # 设置滑块为垂直滑块
        self.verticalSlider.setInvertedAppearance(True) # 设置刻度反方向显示
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksRight) # 设置在滑块右侧显示刻度
        self.verticalSlider.setTickInterval(3) # 设置刻度的间隔
        self.verticalSlider.setObjectName("verticalSlider")
        # 创建一个水平布局管理器，主要用来放置显示文字的Label
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 251, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 创建Label控件，用来显示文字
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter) # 设置文字居中对齐
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label) # 将Label添加到水平布局管理器中
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为横向滑块绑定valueChanged信号，在值发生更改是发射
        self.horizontalSlider.valueChanged.connect(self.setfontsize)
    # 定义槽函数，根据横向滑块的值改变垂直滑块的值和Label控件的字体大小
    def setfontsize(self):
        value = self.horizontalSlider.value()
        self.verticalSlider.setValue(value)
        self.label.setFont(QtGui.QFont("楷体", value))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "敢想敢为，注重细节"))

import sys
# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.show() # 显示窗体
   sys.exit(app.exec_()) # 程序关闭时退出进程