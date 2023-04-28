
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
    
    def addFuncToolBar(self):
        # 定义互动选项
        self.open = QtGui.QAction("打开")
        self.close = QtGui.QAction("关闭")
        # 定义标准控件
        self.combobox = QtWidgets.QComboBox()
        self.positions = ["总经理", "副总经理", "人事部经理", "财务部经理", "部门经理", "普通员工"]
        self.combobox.addItems(self.positions)
        # 加入工具栏
        self.toolBar.addActions([self.open, self.close])
        self.toolBar.addWidget(self.combobox)
        # 调整工具栏图标大小
        # self.toolBar.setIconSize(QtCore.QSize(28, 28))
    
    def toolClick(self, m):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self.centralwidget, "提示", m.text(), QMessageBox.StandardButton.Ok)
    
    def itemClick(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self.centralwidget, "提示", self.combobox.currentText(), QMessageBox.StandardButton.Ok)

    def apply(self):
        self.addFuncToolBar()
        self.toolBar.actionTriggered[QtGui.QAction].connect(self.toolClick)
        self.combobox.currentTextChanged.connect(self.itemClick)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
