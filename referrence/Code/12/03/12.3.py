# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/16  11:15 
# 文件名称   ：12.3.py
# 开发工具   ：PyCharm

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QPoint

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.setWindowTitle("画刷的设置") # 设置窗口标题
        self.resize(430,250) # 设置窗口大小

    def paintEvent(self,event):
        painter=QPainter(self) # 创建绘图对象
        brush=QBrush() # 创建画刷对象

        # 创建第1列的矩形及标识文字
        # 设置第1个矩形的画刷
        brush.setColor(Qt.red) # 设置画刷颜色为红色
        brush.setStyle(Qt.SolidPattern) # 设置画刷样式为纯色样式
        painter.setBrush(brush) # 设置画刷
        painter.drawRect(10, 10, 30, 30) # 绘制矩形
        painter.drawText(50, 30, "纯色样式")  # 绘制标识文本
        # 设置第2个矩形的画刷
        brush.setColor(Qt.blue)  # 设置画刷颜色为蓝色
        brush.setStyle(Qt.Dense1Pattern)  # 设置画刷样式为密度样式1
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(10, 50, 30, 30)  # 绘制矩形
        painter.drawText(50, 70, "密度样式1")  # 绘制标识文本
        # 设置第3个矩形的画刷
        brush.setColor(Qt.cyan)  # 设置画刷颜色为青色
        brush.setStyle(Qt.Dense2Pattern)  # 设置画刷样式为密度样式2
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(10, 90, 30, 30)  # 绘制矩形
        painter.drawText(50, 110, "密度样式2")  # 绘制标识文本
        # 设置第4个矩形的画刷
        brush.setColor(Qt.green)  # 设置画刷颜色为绿色
        brush.setStyle(Qt.Dense3Pattern)  # 设置画刷样式为密度样式3
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(10, 130, 30, 30)  # 绘制矩形
        painter.drawText(50, 150, "密度样式3")  # 绘制标识文本
        # 设置第5个矩形的画刷
        brush.setColor(Qt.black)  # 设置画刷颜色为黑色
        brush.setStyle(Qt.Dense4Pattern)  # 设置画刷样式为密度样式4
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(10, 170, 30, 30)  # 绘制矩形
        painter.drawText(50, 190, "密度样式4")  # 绘制标识文本
        # 设置第6个矩形的画刷
        brush.setColor(Qt.darkMagenta)  # 设置画刷颜色为洋红色
        brush.setStyle(Qt.Dense5Pattern)  # 设置画刷样式为密度样式5
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(10, 210, 30, 30)  # 绘制矩形
        painter.drawText(50, 230, "密度样式5")  # 绘制标识文本

        # 创建第2列的矩形及标识文字
        # 设置第1个矩形的画刷
        brush.setColor(Qt.red) # 设置画刷颜色为红色
        brush.setStyle(Qt.Dense6Pattern) # 设置画刷样式为密度样式6
        painter.setBrush(brush) # 设置画刷
        painter.drawRect(150, 10, 30, 30) # 绘制矩形
        painter.drawText(190, 30, "密度样式6")  # 绘制标识文本
        # 设置第2个矩形的画刷
        brush.setColor(Qt.blue)  # 设置画刷颜色为蓝色
        brush.setStyle(Qt.Dense7Pattern)  # 设置画刷样式为密度样式7
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(150, 50, 30, 30)  # 绘制矩形
        painter.drawText(190, 70, "密度样式7")  # 绘制标识文本
        # 设置第3个矩形的画刷
        brush.setColor(Qt.cyan)  # 设置画刷颜色为青色
        brush.setStyle(Qt.HorPattern)  # 设置画刷样式为水平线样式
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(150, 90, 30, 30)  # 绘制矩形
        painter.drawText(190, 110, "水平线样式")  # 绘制标识文本
        # 设置第4个矩形的画刷
        brush.setColor(Qt.green)  # 设置画刷颜色为绿色
        brush.setStyle(Qt.VerPattern)  # 设置画刷样式为垂直线样式
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(150, 130, 30, 30)  # 绘制矩形
        painter.drawText(190, 150, "垂直线样式")  # 绘制标识文本
        # 设置第5个矩形的画刷
        brush.setColor(Qt.black)  # 设置画刷颜色为黑色
        brush.setStyle(Qt.CrossPattern)  # 设置画刷样式为交叉线样式
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(150, 170, 30, 30)  # 绘制矩形
        painter.drawText(190, 190, "交叉线样式")  # 绘制标识文本
        # 设置第6个矩形的画刷
        brush.setColor(Qt.darkMagenta)  # 设置画刷颜色为洋红色
        brush.setStyle(Qt.DiagCrossPattern)  # 设置画刷样式为斜线交叉线样式
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(150, 210, 30, 30)  # 绘制矩形
        painter.drawText(190, 230, "斜线交叉线样式")  # 绘制标识文本

        # 创建第3列的矩形及标识文字
        # 设置第1个矩形的画刷
        brush.setColor(Qt.red) # 设置画刷颜色为红色
        brush.setStyle(Qt.BDiagPattern) # 设置画刷样式为反斜线样式
        painter.setBrush(brush) # 设置画刷
        painter.drawRect(300, 10, 30, 30) # 绘制矩形
        painter.drawText(340, 30, "反斜线样式")  # 绘制标识文本
        # 设置第2个矩形的画刷
        brush.setColor(Qt.blue)  # 设置画刷颜色为蓝色
        brush.setStyle(Qt.FDiagPattern)  # 设置画刷样式为斜线样式
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(300, 50, 30, 30)  # 绘制矩形
        painter.drawText(340, 70, "斜线样式")  # 绘制标识文本
        # 设置第3个矩形的画刷
        # 设置线性渐变区域
        linearGradient= QLinearGradient(QPoint(300, 90), QPoint(330, 120))
        linearGradient.setColorAt(0, Qt.red) # 设置渐变色1
        linearGradient.setColorAt(1, Qt.yellow) # 设置渐变色2
        linearbrush=QBrush(linearGradient) # 创建线性渐变画刷
        linearbrush.setStyle(Qt.LinearGradientPattern)  # 设置画刷样式为线性渐变样式
        painter.setBrush(linearbrush)  # 设置画刷
        painter.drawRect(300, 90, 30, 30)  # 绘制矩形
        painter.drawText(340, 110, "线性渐变样式")  # 绘制标识文本
        # 设置第4个矩形的画刷
        # 设置锥形渐变区域
        conicalGradient = QConicalGradient(315,145,0)
        # 将要渐变的区域分为6个区域，分别设置颜色
        conicalGradient.setColorAt(0, Qt.red)
        conicalGradient.setColorAt(0.2, Qt.yellow)
        conicalGradient.setColorAt(0.4, Qt.blue)
        conicalGradient.setColorAt(0.6, Qt.green)
        conicalGradient.setColorAt(0.8, Qt.magenta)
        conicalGradient.setColorAt(1.0, Qt.cyan)
        conicalbrush=QBrush(conicalGradient) # 创建锥形渐变画刷
        conicalbrush.setStyle(Qt.ConicalGradientPattern)  # 设置画刷样式为锥形渐变样式
        painter.setBrush(conicalbrush)  # 设置画刷
        painter.drawRect(300, 130, 30, 30)  # 绘制矩形
        painter.drawText(340, 150, "锥形渐变样式")  # 绘制标识文本
        # 设置第5个矩形的画刷
        # 设置放射渐变区域
        radialGradient=QRadialGradient(QPoint(315, 185), 15)
        radialGradient.setColorAt(0, Qt.green) # 设置中心点颜色
        radialGradient.setColorAt(0.5, Qt.yellow) # 设置内圈颜色
        radialGradient.setColorAt(1, Qt.darkMagenta) # 设置外圈颜色
        radialbrush=QBrush(radialGradient) # 创建放射渐变画刷
        radialbrush.setStyle(Qt.RadialGradientPattern)  # 设置画刷样式为放射渐变样式
        painter.setBrush(radialbrush)  # 设置画刷
        painter.drawRect(300, 170, 30, 30)  # 绘制矩形
        painter.drawText(340, 190, "放射渐变样式")  # 绘制标识文本
        # 设置第6个矩形的画刷
        brush.setStyle(Qt.TexturePattern)  # 设置画刷样式为纹理样式
        brush.setTexture(QPixmap("test.jpg")) # 设置作为纹理的图片
        painter.setBrush(brush)  # 设置画刷
        painter.drawRect(300, 210, 30, 30)  # 绘制矩形
        painter.drawText(340, 230, "纹理样式")  # 绘制标识文本


if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())