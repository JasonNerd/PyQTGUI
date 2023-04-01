# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/10  16:02 
# 文件名称   ：11.4.py
# 开发工具   ：PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300) # 设置窗口大小
        MainWindow.setWindowTitle("遍历文件夹") # 设置窗口标题
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 添加表格
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 501, 270))
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
        item.setText("详细信息")
        self.tableWidget.setColumnWidth(0, 100) # 设置第一列宽度
        # 设置最后一列自动填充容器
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # 创建选择路径按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        # 为按钮设置字体
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("选择路径")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 关联“选择路径”的clicked信号
        self.pushButton.clicked.connect(self.getinfo)

    # 选择路径，并获取其中的所有文件信息显示在表格中
    def getinfo(self):
        try:
            import os
            # dir_path即为选择的文件夹的绝对路径，第二形参为对话框标题，第三个为对话框打开后默认的路径
            self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", os.getcwd())
            if self.dir_path !="":
                self.list = os.listdir(self.dir_path)  # 列出文件夹下所有的目录与文件
                flag=0 # 标识插入新行的位置
                for i in range(0, len(self.list)):  # 遍历文件列表
                    # 拼接路径和文件名
                    filepath = os.path.join(self.dir_path, self.list[i])
                    self.tableWidget.insertRow(flag)  # 添加新行
                    # 设置第一列的值为文件（夹）名
                    self.tableWidget.setItem(flag, 0, QtWidgets.QTableWidgetItem(self.list[i]))
                    # 设置第二列的值为文件或文件夹的完整路径
                    self.tableWidget.setItem(flag, 1, QtWidgets.QTableWidgetItem(filepath))
                    flag+=1 # 计算下一个新行插入位置
        except Exception as e:
            print(e)

# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程