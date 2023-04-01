# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/3  15:43 
# 文件名称   ：Demo.py
# 开发工具   ：PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 水平布局
        hlayout=QHBoxLayout()
        btn1=QPushButton()
        btn1.setText('按钮1')
        btn2 = QPushButton()
        btn2.setText('按钮2')
        btn3 = QPushButton()
        btn3.setText('按钮3')
        btn4 = QPushButton()
        btn4.setText('按钮4')
        hlayout.addStretch(1)
        hlayout.addWidget(btn1)
        # hlayout.addSpacing(10)
        hlayout.addStretch(1)
        hlayout.addWidget(btn2)
        hlayout.addStretch(1)
        hlayout.addWidget(btn3)
        hlayout.addStretch(1)
        hlayout.addWidget(btn4)
        self.setLayout(hlayout)

        # # 垂直布局
        # vlayout=QVBoxLayout()
        # btn1=QPushButton()
        # btn1.setText('按钮1')
        # btn2 = QPushButton()
        # btn2.setText('按钮2')
        # btn3 = QPushButton()
        # btn3.setText('按钮3')
        # btn4 = QPushButton()
        # btn4.setText('按钮4')
        # vlayout.addWidget(btn1)
        # vlayout.addWidget(btn1, 1, QtCore.Qt.AlignVCenter)  # 指定伸缩量和对齐方式添加控件
        # vlayout.addSpacing(10) # 设置两个控件之间的间距
        # vlayout.addWidget(btn2)
        # vlayout.addWidget(btn3)
        # vlayout.addWidget(btn4)
        # self.setLayout(vlayout)

        # grid=QGridLayout()
        #
        #
        # self.setLayout(grid)

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())
