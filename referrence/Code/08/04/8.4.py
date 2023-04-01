# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '8.4.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(210, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 添加“姓名”标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 16))
        self.label.setObjectName("label")
        # 添加输入姓名的文本框
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        # 添加“年龄”标签
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 56, 41, 16))
        self.label_2.setObjectName("label_2")
        # 添加输入年龄的文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 56, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        # 添加“班级”标签
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 41, 16))
        self.label_3.setObjectName("label_3")
        # 添加输入班级的文本框
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 90, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        # 添加“分数”标签
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 126, 41, 16))
        self.label_4.setObjectName("label_4")
        # 添加输入分数的文本框
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 126, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为“姓名”文本框的按下回车信号绑定槽函数，获取用户输入的姓名
        self.lineEdit.returnPressed.connect(self.getname)
        # 为“年龄”文本框的按下回车信号绑定槽函数，获取用户输入的年龄
        self.lineEdit_2.returnPressed.connect(self.getage)
        # 为“班级”文本框的按下回车信号绑定槽函数，获取用户选择的班级
        self.lineEdit_3.returnPressed.connect(self.getgrade)
        # 为“分数”文本框的按下回车信号绑定槽函数，获取用户输入的分数
        self.lineEdit_4.returnPressed.connect(self.getscore)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "录入学生信息"))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_2.setText(_translate("MainWindow", "年龄："))
        self.label_3.setText(_translate("MainWindow", "班级："))
        self.label_4.setText(_translate("MainWindow", "分数："))

    # 自定义获取姓名的槽函数
    def getname(self):
        # 弹出可以输入字符串的输入框
        name,ok = QInputDialog.getText(MainWindow, "姓名", "请输入姓名", QtWidgets.QLineEdit.Normal, "明日科技")
        if ok: # 判断是否单击了OK按钮
            self.lineEdit.setText(name) # 获取输入对话框中的字符串，显示在文本框中

    # 自定义获取年龄的槽函数
    def getage(self):
        # 弹出可以选择或输入年龄的输入框
        age,ok = QInputDialog.getInt(MainWindow, "年龄", "请选择年龄", 20,1,100,1)
        if ok: # 判断是否单击了OK按钮
            self.lineEdit_2.setText(str(age)) # 获取输入对话框中的年龄，显示在文本框中

    # 自定义获取班级的槽函数
    def getgrade(self):
        # 弹出可以选择班级的输入框
        grade,ok = QInputDialog.getItem(MainWindow, "班级", "请选择班级", ('三年一班','三年二班','三年三班'),0,False)
        if ok: # 判断是否单击了OK按钮
            self.lineEdit_3.setText(grade) # 获取输入对话框中选择的班级，显示在文本框中

    # 自定义获取分数的槽函数
    def getscore(self):
        # 弹出可以选择或输入分数的输入框，模板保留2位小数
        scroe,ok = QInputDialog.getDouble(MainWindow, "分数", "请选择分数",0.01,0,100,2)
        if ok: # 判断是否单击了OK按钮
            self.lineEdit_4.setText(str(scroe)) # 获取输入对话框中的分数，显示在文本框中


# 主方法
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = Ui_MainWindow() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_()) # 程序关闭时退出进程