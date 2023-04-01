# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/8  10:40 
# 文件名称   ：9.4.py
# 开发工具   ：PyCharm

from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI() # 初始化窗口

    def initUI(self):
        self.setWindowTitle("微信交流")
        grid=QGridLayout() # 创建网格布局
        # 创建顶部时间栏
        label1 = QLabel()
        # 显示当前日期时间
        label1.setText(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss"))
        # 第1行第1列到第1行第4列添加标签控件，并设置居中对齐
        grid.addWidget(label1, 0, 0, 1, 4, QtCore.Qt.AlignCenter)

        # 创建对方用户头像、昵称及信息，并在网格中嵌套垂直布局显示
        label2=QLabel()
        label2.setPixmap(QtGui.QPixmap("images/head1.png"))
        vlayout1=QVBoxLayout()
        vlayout1.addWidget(QLabel("马云"))
        vlayout1.addWidget(QLabel("老马，在不在，最近还好吗？"))
        grid.addWidget(label2, 1, 0, QtCore.Qt.AlignRight)
        grid.addLayout(vlayout1, 1, 1)


        # 创建自己的头像、昵称及信息，并在网格中嵌套垂直布局显示
        label3=QLabel()
        label3.setPixmap(QtGui.QPixmap("images/head2.png"))
        vlayout2=QVBoxLayout()
        vlayout2.addWidget(QLabel("马化腾"))
        vlayout2.addWidget(QLabel("还行吧，最近经济不太景气啊！"))
        grid.addWidget(label3, 2, 3, QtCore.Qt.AlignLeft)
        grid.addLayout(vlayout2, 2, 2)

        # 创建对方用户头像、昵称及第2条信息，并在网格中嵌套垂直布局显示
        label4=QLabel()
        label4.setPixmap(QtGui.QPixmap("images/head1.png"))
        label4.resize(24,24)
        vlayout3=QVBoxLayout()
        vlayout3.addWidget(QLabel("马云"))
        vlayout3.addWidget(QLabel("嗯，都差不多，一起度过难关吧……"))
        grid.addWidget(label4, 3, 0, QtCore.Qt.AlignRight)
        grid.addLayout(vlayout3, 3, 1)

        # 创建输入框，并设置宽度和高度，跨列添加到网格布局中
        text=QTextEdit()
        text.setFixedWidth(500)
        text.setFixedHeight(80)
        # 第1行第1列到第1行第4列添加标签控件，并设置居中对齐
        grid.addWidget(text, 4, 0, 1, 4, QtCore.Qt.AlignCenter)

        # 添加“发送”按钮
        grid.addWidget(QPushButton("发送"), 5, 3, QtCore.Qt.AlignRight)



        self.setLayout(grid) # 设置网格布局

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())