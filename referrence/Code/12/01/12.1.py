# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/15  17:18 
# 文件名称   ：12.1.py
# 开发工具   ：PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.setWindowTitle("使用QPainter绘制图形") # 设置窗口标题
        self.resize(300,120) # 设置窗口大小

    def paintEvent(self,event):
        painter=QPainter(self) # 创建绘图对象
        painter.setPen(Qt.red) # 设置画笔
        painter.drawEllipse(80, 10, 50, 30) # 绘制一个椭圆
        painter.drawRect(180, 10, 50, 30) # 绘制一个矩形
        painter.drawLine(80, 70, 200, 70) # 绘制直线
        painter.drawText(90,100,"敢想敢为  注重细节") # 绘制文本

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())