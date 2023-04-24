from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    cwWidth = 360
    cwHeight = 600
    pages = []

    # 第 i 号 页面, 页面标题 title, 页面内容数目 cnt
    def newPage(self, i, title, cnt):
        pg = QtWidgets.QWidget()
        pg.setGeometry(QtCore.QRect(2, 2, self.cwWidth-4, int(self.cwHeight*10//11)))
        pg.setObjectName("page_"+str(i))
        for i in range(cnt):
            btn = QtWidgets.QToolButton(pg)
            btn.setText(title+str(i))
            btn.setGeometry(20, 51*i+5, 70, 50)
        return pg


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.cwWidth, self.cwHeight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 创建ToolBox工具盒
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(2, 2, self.cwWidth-4, self.cwHeight-4))
        self.toolBox.setObjectName("toolBox")
        # 创建 ToolBox 的几个下拉界面
        pg_sizes = [5, 3, 2, 4, 3]
        titles = ["同学", "朋友", "家人", "同事", "其他"]
        for i in range(len(pg_sizes)):
            pg = self.newPage(i, titles[i], pg_sizes[i])
            self.toolBox.addItem(pg, titles[i])
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBox.setCurrentIndex(0) # 默认选择第一个页面


import sys
if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
   ui = Ui_MainWindow() # 创建PyQt设计的窗体对象
   ui.setupUi(MainWindow) # 调用PyQt窗体的方法对窗体对象进行初始化设置
   MainWindow.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)  # 只显示关闭按钮
   MainWindow.show() # 显示窗体
   sys.exit(app.exec()) # 程序关闭时退出进程