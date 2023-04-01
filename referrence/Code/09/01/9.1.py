# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/7  12:54 
# 文件名称   ：9.1.py
# 开发工具   ：PyCharm

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI() # 初始化窗口

    def initUI(self):
        grid=QGridLayout() # 创建网格布局
        # 创建并设置标签文本
        label1=QLabel()
        label1.setText("用户名:")
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
        # 第一行第一列添加标签控件，并设置左对齐
        grid.addWidget(label1,0,0,QtCore.Qt.AlignLeft)
        # 第一行第二列添加输入文本框控件，并设置左对齐
        grid.addWidget(text1, 0, 1, QtCore.Qt.AlignLeft)
        # 第二行第一列添加标签控件，并设置左对齐
        grid.addWidget(label2, 1, 0, QtCore.Qt.AlignLeft)
        # 第二行第二列添加输入文本框控件，并设置左对齐
        grid.addWidget(text2, 1, 1, QtCore.Qt.AlignLeft)
        # 第三行第一列添加按钮控件，并设置居中对齐
        grid.addWidget(btn1, 2, 0, QtCore.Qt.AlignCenter)
        # 第三行第二列添加按钮控件，并设置居中对齐
        grid.addWidget(btn2, 2, 1, QtCore.Qt.AlignCenter)
        self.setLayout(grid) # 设置网格布局

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())