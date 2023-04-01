# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.17.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(293, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 10, 248, 197))
        self.calendarWidget.setSelectedDate(QtCore.QDate(2020, 3, 23)) # 设置默认选中的日期
        self.calendarWidget.setMinimumDate(QtCore.QDate(1752, 9, 14)) # 设置最小日期
        self.calendarWidget.setMaximumDate(QtCore.QDate(9999, 12, 31)) # 设置最大日期
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday) # 设置每周第一天为星期一
        self.calendarWidget.setGridVisible(True) # 设置网格线课件
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection) # 设置可以选中单个日期
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames) # 设置水平表头为简短形式，即“周一”形式
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers) # 设置垂直表头为周数
        self.calendarWidget.setNavigationBarVisible(True) # 设置显示导航栏
        self.calendarWidget.setDateEditEnabled(True) # 设置日期可以编辑
        self.calendarWidget.setObjectName("calendarWidget")
        # 选中日期变化时显示选择的日期
        self.calendarWidget.selectionChanged.connect(self.getdate)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # # 获取当前系统日期时间（或日期，或时间）
        # datetime= QtCore.QDateTime.currentDateTime() # 获取当前系统日期时间
        # date=QtCore.QDate.currentDate() # 获取当前日期
        # time=QtCore.QTime.currentTime() # 获取当前时间
        # print(datetime,date,time)

    def getdate(self):
        from PyQt5.QtWidgets import QMessageBox
        date=QtCore.QDate(self.calendarWidget.selectedDate()) # 获取当前选中日期的QDate对象
        year=date.year() # 获取年份
        month=date.month() # 获取月份
        day=date.day() # 获取日
        QMessageBox.information(MainWindow, "提示", str(year)+"-"+str(month)+"-"+str(day), QMessageBox.Ok)

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