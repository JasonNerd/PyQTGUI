# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/16  15:39 
# 文件名称   ：12.5.py
# 开发工具   ：PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter,QPixmap

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.setWindowTitle("绘制公司Logo") # 设置窗口标题
        self.resize(300,120) # 设置窗口大小

    def paintEvent(self,event):
        painter=QPainter(self) # 创建绘图对象
        painter.drawPixmap(10, 10, QPixmap("logo.jpg")) # 默认大小
        # painter.drawPixmap(10, 10, 290, 110, QPixmap("logo.jpg")) # 指定大小

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())