from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 600, 480))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setColumnCount(2) # 设置树结构中的列数
        self.treeWidget.setHeaderLabels(['姓名','职务']) # 设置列标题名

        dict= {'任正非':'华为董事长','马云':'阿里巴巴创始人','马化腾':'腾讯CEO','李彦宏':'百度CEO','董明珠':'格力董事长'}
        root=QTreeWidgetItem(self.treeWidget) # 创建节点
        root.setText(0,'组织结构')           # 设置顶级节点文本
        for key,value in dict.items():      # 遍历字典
            child=QTreeWidgetItem(root)     # 创建子节点
            child.setText(0,key)        # 设置第一列的值
            child.setText(1,value)      # 设置第二列的值
            # 设置图标
            if key=='任正非':
                child.setIcon(0, QtGui.QIcon('../src/logos/华为.jpg'))
            elif key=='马云':
                child.setIcon(0, QtGui.QIcon('../src/logos/阿里巴巴.jpg'))
            elif key=='马化腾':
                child.setIcon(0, QtGui.QIcon('../src/logos/腾讯.jpg'))
            elif key=='李彦宏':
                child.setIcon(0, QtGui.QIcon('../src/logos/百度.jpg'))
            elif key=='董明珠':
                child.setIcon(0, QtGui.QIcon('../src/logos/格力.jpg'))
            # 设置复选框，并且选中
            child.setCheckState(0, QtCore.Qt.CheckState.Checked)

        self.treeWidget.addTopLevelItem(root)               # 将创建的树节点添加到树控件中
        self.treeWidget.setAlternatingRowColors(True)       # 设置隔行变色
        self.treeWidget.expandAll()                         # 展开所有树节点
        self.treeWidget.clicked.connect(self.gettreetext)   # 为树控件绑定单击信号
        MainWindow.setCentralWidget(self.centralwidget)

    def gettreetext(self,index):
        item=self.treeWidget.currentItem() # 获取当前选中项
        QtWidgets.QMessageBox.information(MainWindow, '提示', f'您选择的是：{item.text(0)} -- {item.text(1)}', 
                                          QtWidgets.QMessageBox.StandardButton.Ok)


# 主方法，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
   import sys
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(MainWindow)
   MainWindow.show()
   sys.exit(app.exec())