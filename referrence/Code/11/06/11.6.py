# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '11.6.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import  QDir
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 252)
        MainWindow.setWindowTitle("QDir应用") # 设置标题
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 输入路径标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 10, 61, 16))
        self.label.setObjectName("label")
        self.label.setText("输入路径：")
        # 输入路径的文本框
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(84, 10, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        # 确定按钮，根据判断输入路径是否存在，如果不存在，则创建
        # 如果存在，获取其中的所有文件夹
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(304, 10, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("确定")
        # 表格，显示指定路径下的所有文件夹
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(14, 40, 351, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("路径")
        self.tableWidget.verticalHeader().setVisible(False) # 隐藏垂直标题栏
        # 设置自动填充容器
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # 设置新文件夹名称标签
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("设置新文件夹名称：")
        # 输入新文件夹名称
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 220, 81, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # 重命名按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 220, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("重命名")
        # 删除按钮
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 220, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("删除")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.getpath)
        self.pushButton_2.clicked.connect(self.rename)
        self.pushButton_3.clicked.connect(self.delete)
        self.tableWidget.itemClicked.connect(self.getItem)


    def getItem(self,item): # 获取选中的表格内容
        self.select=item.text()

    # 获取指定路径下的所有文件夹
    def getpath(self):
        self.tableWidget.setRowCount(0) # 清空表格中的所有行
        path=self.lineEdit.text() # 记录输入的路径
        if path !="": # 判断路径不为空
            dir = QDir() # 创建QDir对象
            if not dir.exists(path): # 判断路径是否存在
                dir.mkdir(path) # 创建文件夹
            dir=QDir(path) # 创建QDir对象
            flag = 0 # 定义标识，用来指定在表格中的哪行插入数据
            # 遍历指定路径下的所有子文件夹
            for d in dir.entryList(QDir.Dirs | QDir.NoDotAndDotDot):
                self.tableWidget.insertRow(flag)  # 添加新行
                # 设置第一列的值为文件夹全路径（包括文件夹名）
                self.tableWidget.setItem(flag, 0, QtWidgets.QTableWidgetItem(os.path.join(path,d)))
                flag += 1  # 标识加1
    # 重命名文件夹
    def rename(self):
        newname=self.lineEdit_2.text() # 记录新文件夹名
        if newname !="": # 判断新文件夹名是否不为空
            if self.select !="": # 判断是否选择了要重命名的文件夹
                dir=QDir() # 创建QDir对象
                # 对选中的文件夹进行重命名
                dir.rename(self.select,os.path.join(self.lineEdit.text(),newname))
                QtWidgets.QMessageBox.information(MainWindow,"提示","重命名文件夹成功！")
                self.getpath() # 更新表格
    # 删除文件夹
    def delete(self):
        if self.select !="": # 判断是否选择了要删除的文件夹
            dir=QDir()  # 创建QDir对象
            dir.rmdir(self.select) # 删除选中的文件夹
            QtWidgets.QMessageBox.information(MainWindow, "提示", "成功删除文件夹！")
            self.getpath() # 更新表格
# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程