# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '11.5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import  QFile,QFileInfo,QIODevice,QTextStream
import os
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 293)
        MainWindow.setWindowTitle("将现有问题存放到不同的文件中")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 分组框
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 331, 91))
        self.groupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.groupBox.setObjectName("groupBox")
        # 选择文件标签
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setStyleSheet("color: rgb(0, 0, 0);") # 设置字体为黑色
        self.label.setObjectName("label")
        # 显示选择的文件路径
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        # “选择”按钮
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(260, 20, 61, 23))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        # 输入创建路径标签
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(19, 52, 81, 16))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        # 输入创建路径的文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(109, 52, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # “创建”按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(259, 52, 61, 23))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        # 显示创建的文件列表及大小
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 105, 331, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2) # 设置列数
        # 设置第一列的标题
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("文件名")
        # 设置第二列的标题
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("文件大小")
        self.tableWidget.setColumnWidth(0, 100) # 设置第一列宽度
        # 设置最后一列自动填充容器
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 设置分组框、标签及按钮的文本
        self.groupBox.setTitle("基础设置")
        self.label.setText("选择文件：")
        self.label_2.setText("输入创建路径：")
        self.pushButton.setText("选择")
        self.pushButton_2.setText("创建")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为“选择”按钮的clicked信号绑定槽函数
        self.pushButton.clicked.connect(self.getfile)
        # 为“创建”按钮的clicked信号绑定槽函数
        self.pushButton_2.clicked.connect(self.getpath)

    # 选择文件并显示在文本框中
    def getfile(self):
        dir =QFileDialog() # 创建文件对话框
        dir.setDirectory('C:\\') # 设置初始路径为C盘
        # 设置只显示文本文件
        dir.setNameFilter('文本文件(*.txt)')
        if dir.exec_(): # 判断是否选择了文件
            self.lineEdit.setText(dir.selectedFiles()[0]) # 将选择的文件显示在文本框中


    # 选择路径，根据日期创建文件，并写入选择的文件中的文本
    def getpath(self):
        try:
            path=self.lineEdit_2.text() # 记录创建路径
            if self.lineEdit_2.text() !="": # 判断路径不为空
                list = [] # 定义列表，用来按行记录选择的文件中的文本
                file =QFile(self.lineEdit.text()) # 创建QFile文件对象
                if file.open(QIODevice.ReadOnly): # 以只读方式打开文件
                    read = QTextStream(file) # 创建文本流
                    read.setCodec("utf-8") # 设置写入编码
                    while not read.atEnd(): # 如果未读取完
                        list.append(read.readLine()) # 按行记录遍历到的文本
                if not os.path.exists(path):  # 判断要创建的文件的路径是否存在，没有则创建文件夹
                    os.makedirs(path) # 创建文件夹
                for i in range(len(list)): # 遍历已经记录的文本数据列表
                    # 获取当前时间，用来作为文件名
                    mytime = str(datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S"))
                    files = path + mytime + str(i) + '.txt'  # 在指定路径下创建txt文本文件
                    file = QFile(files) # 创建QFile文件对象
                    file.open(QIODevice.ReadWrite | QIODevice.Text) # 以读写和文本模式打开文件
                    file.write(bytes(list[i], encoding = "utf8")  ) # 向文件中写入数据
                    file.close() # 关闭文件
                filelist=os.listdir(path) # 遍历文件夹
                flag=0 # 定义标识，用来指定在表格中的哪行插入数据
                for f in filelist: # 遍历文件列表
                    file=QFileInfo(f) # 创建对象，用来获取文件信息
                    if file.fileName().endswith(".txt"): # 判断是否为.txt文本文件
                        self.tableWidget.insertRow(flag)  # 添加新行
                        # 设置第一列的值为文件名
                        self.tableWidget.setItem(flag, 0, QtWidgets.QTableWidgetItem(file.fileName()))
                        # 设置第二列的值为文件大小
                        self.tableWidget.setItem(flag, 1, QtWidgets.QTableWidgetItem(str(file.size())+"B"))
                        flag +=1 # 标识加1
        except Exception as e:
            print(e)
# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程