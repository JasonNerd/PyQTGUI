# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/16  10:36 
# 文件名称   ：12.2.py
# 开发工具   ：PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter,QPen,QColor
from PyQt5.QtCore import Qt

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.setWindowTitle("画笔的设置") # 设置窗口标题
        self.resize(300,120) # 设置窗口大小

    def paintEvent(self,event):
        painter=QPainter(self) # 创建绘图对象
        pen=QPen() # 创建画笔对象
        # 设置第1条直线的画笔
        pen.setColor(Qt.red) # 设置画笔颜色为红色
        pen.setStyle(Qt.SolidLine) # 设置画笔样式为正常直线
        pen.setWidth(1) # 设置画笔宽度
        painter.setPen(pen) # 设置画笔
        painter.drawLine(80, 10, 200, 10) # 绘制直线
        # 设置第2条直线的画笔
        pen.setColor(Qt.blue)  # 设置画笔颜色为蓝色
        pen.setStyle(Qt.DashLine)  # 设置画笔样式为由一些像素分割的短线
        pen.setWidth(2)  # 设置画笔宽度
        painter.setPen(pen)  # 设置画笔
        painter.drawLine(80, 30, 200, 30)  # 绘制直线
        # 设置第3条直线的画笔
        pen.setColor(Qt.cyan)  # 设置画笔颜色为青色
        pen.setStyle(Qt.DotLine)  # 设置画笔样式为由一些像素分割的点
        pen.setWidth(3)  # 设置画笔宽度
        painter.setPen(pen)  # 设置画笔
        painter.drawLine(80, 50, 200, 50)  # 绘制直线
        # 设置第4条直线的画笔
        pen.setColor(Qt.green)  # 设置画笔颜色为绿色
        pen.setStyle(Qt.DashDotLine)  # 设置画笔样式为交替出现的短线和点
        pen.setWidth(4)  # 设置画笔宽度
        painter.setPen(pen)  # 设置画笔
        painter.drawLine(80, 70, 200, 70)  # 绘制直线
        # 设置第5条直线的画笔
        pen.setColor(Qt.black)  # 设置画笔颜色为黑色
        pen.setStyle(Qt.DashDotDotLine)  # 设置画笔样式为交替出现的短线和两个点
        pen.setWidth(5)  # 设置画笔宽度
        painter.setPen(pen)  # 设置画笔
        painter.drawLine(80, 90, 200, 90)  # 绘制直线
        # 设置第6条直线的画笔
        pen.setColor(QColor(48,235,100))  # 自定义画笔颜色
        pen.setStyle(Qt.CustomDashLine)  # 设置画笔样式为自定义样式
        pen.setDashPattern([1,3,2,3]) # 设置自定义的画笔样式
        pen.setWidth(6)  # 设置画笔宽度
        painter.setPen(pen)  # 设置画笔
        painter.drawLine(80, 110, 200, 110)  # 绘制直线

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())