# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/8  8:56 
# 文件名称   ：9.3.py
# 开发工具   ：PyCharm

from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI() # 初始化窗口

    def initUI(self):
        form=QFormLayout() # 创建表单布局
        # 创建并设置标签文本
        label1=QLabel()
        label1.setText("用户名：")
        # 创建输入文本框
        text1=QLineEdit()
        # 创建并设置标签文本
        label2 = QLabel()
        label2.setText("密码：")
        # 创建输入文本框
        text2 = QLineEdit()
        # 创建“登录”和“取消”按钮
        btn1=QPushButton()
        btn1.setText("登录")
        btn2 = QPushButton()
        btn2.setText("取消")
        # 将上面创建的6个控件分为3行添加到表单布局中
        form.addRow(label1,text1)
        form.addRow(label2,text2)
        # vlayout = QVBoxLayout() # 创建垂直布局管理器
        # vlayout.addWidget(text2) # 向垂直布局中添加密码输入框
        # vlayout.addWidget(QLabel("密码只能输入8位")) # 向垂直布局中添加提示标签
        # form.addRow(label2, vlayout) # 将垂直布局嵌套进表单布局中
        form.addRow(btn1,btn2)
        # form.addRow(btn1)
        # form.addRow(btn2)

        # # 设置标签总在文本框的上方
        # form.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.setLayout(form) # 设置表单布局

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())