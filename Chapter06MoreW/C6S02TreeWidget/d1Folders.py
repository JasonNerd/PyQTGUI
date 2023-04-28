
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 374)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 512, 376))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def apply(self):
        #设置垂直滚动条为按需显示
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        #设置水平滚动条为按需显示
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        #设置双击或者按下回车键时，使树节点可编辑
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|
                                      QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        #设置树节点为单选
        self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        #设置选中节点时为整行选中
        self.treeView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        #设置自动展开的延时为-1，表示自动展开不可用
        self.treeView.setAutoExpandDelay(-1)
        #设置是否可以展开项
        self.treeView.setItemsExpandable(True)
        # 设置单击头部可排序
        self.treeView.setSortingEnabled(True)
        #设置自动换行
        self.treeView.setWordWrap(True)
        #设置不隐藏头部
        self.treeView.setHeaderHidden(False)
        #设置双击可以展开节点
        self.treeView.setExpandsOnDoubleClick(True)
        # 设置显示头部
        self.treeView.header().setVisible(True)
        #创建存储文件系统的模型
        model = QtGui.QFileSystemModel()
        #为树控件设置数据模型
        self.treeView.setModel(model)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
    # for i in QtCore.QAbstractItemModel.__subclasses__():
    #     print(i)