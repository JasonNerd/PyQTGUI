# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/10  13:38 
# 文件名称   ：11.3.py
# 开发工具   ：PyCharm


from PyQt5 import QtCore
from PyQt5.QtWidgets import *

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI() # 初始化窗口

    def initUI(self):
        self.setWindowTitle("获取文件信息")
        grid=QGridLayout() # 创建网格布局

        # 创建标签
        label1 = QLabel()
        label1.setText("选择路径：")
        grid.addWidget(label1, 0, 0, QtCore.Qt.AlignLeft)
        # 创建显示选中文件的文本框
        self.text1 = QLineEdit()
        grid.addWidget(self.text1, 0, 1, 1, 3, QtCore.Qt.AlignLeft)
        # 创建选择按钮
        btn1 = QPushButton()
        btn1.setText("选择")
        btn1.clicked.connect(self.getInfo)
        grid.addWidget(btn1, 0, 4, QtCore.Qt.AlignCenter)
        # 显示文件信息的文本浏览器
        self.text2=QTextBrowser()
        grid.addWidget(self.text2, 1, 0, 1, 5, QtCore.Qt.AlignLeft)
        self.setLayout(grid) # 设置网格布局

    def getInfo(self):
        file = QFileDialog()  # 创建文件对话框
        file.setDirectory('C:\\')  # 设置初始路径为C盘
        if file.exec_():  # 判断是否选择了文件
            filename=file.selectedFiles()[0] # 获取选择的文件
            self.text1.setText(filename)# 将选择的文件显示在文本框中
            import os,time # 导入模块
            fileinfo=os.stat(filename) # 获取文件信息
            self.text2.setText("文件完整路径："+ os.path.abspath("filename")
                    +"\n文件大小："+ str(fileinfo.st_size)+" 字节"
                    +"\n最后一次访问时间：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(fileinfo.st_atime))
                    +"\n最后一次修改时间：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(fileinfo.st_mtime))
                    +"\n最后一次状态变化时间：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(fileinfo.st_ctime)))

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())
