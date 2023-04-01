# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/16  14:19 
# 文件名称   ：12.4.py
# 开发工具   ：PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter,QFont
from PyQt5.QtCore import Qt
import random

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.setWindowTitle("绘制验证码") # 设置窗口标题
        self.resize(150,60) # 设置窗口大小

    # 定义存储数字、字母的列表，用来从中生成验证码
    char = []
    for i in range(48, 58):  # 添加0——9的数字
        char.append(chr(i))
    for i in range(65, 91):  # 添加A——Z的大写字母
        char.append(chr(i))
    for i in range(97, 123):  # 添加a——z的小写字母
        char.append(chr(i))

    # 生成随机数字或字母
    def rndChar(self):
        return self.char[random.randint(0, len((self.char)))]

    def paintEvent(self,event):
        painter=QPainter(self) # 创建绘图对象
        painter.drawRect(10,10, 100, 30)
        # 绘制干扰线（此处设置20条干扰线，可以随意设置）
        painter.setPen(Qt.red)
        for i in range(20):
            painter.drawLine(
                    random.randint(10, 110), random.randint(10, 40),
                    random.randint(10, 110), random.randint(10, 40)
            )
        painter.setPen(Qt.green)
        # 绘制噪点（此处设置500个噪点，可以随意设置）
        for i in range(500):
            painter.drawPoint(random.randint(10, 110), random.randint(10, 40))
        painter.setPen(Qt.black) # 设置画笔
        font=QFont() # 创建字体对象
        font.setFamily("楷体") # 设置字体
        font.setPointSize(15) # 设置文字大小
        font.setBold(True) # 设置粗体
        font.setUnderline(True) # 设置下划线
        painter.setFont(font)
        for i in range(4):
            painter.drawText(30 * i + 10, 30,str(self.rndChar())) # 绘制文本

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())