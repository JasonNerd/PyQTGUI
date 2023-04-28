
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setStyleSheet("background-color: rgb(135, 39, 122);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 720, 22))
        self.menuBar.setStyleSheet("background-color: rgb(81, 2, 121);\n" "font: 11pt '微软雅黑';\n"
"color: rgb(188, 179, 184);")
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(parent=self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_5 = QtWidgets.QMenu(parent=self.menu_3)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menuBar)
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtGui.QAction(parent=MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtGui.QAction(parent=MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtGui.QAction(parent=MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtGui.QAction(parent=MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtGui.QAction(parent=MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_13 = QtGui.QAction(parent=MainWindow)
        self.action_13.setCheckable(True)
        self.action_13.setObjectName("action_13")
        self.action_14 = QtGui.QAction(parent=MainWindow)
        self.action_14.setCheckable(True)
        self.action_14.setObjectName("action_14")
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menu.addAction(self.action_7)
        self.menu_2.addAction(self.action_8)
        self.menu_2.addAction(self.action_9)
        self.menu_5.addAction(self.action_13)
        self.menu_5.addAction(self.action_14)
        self.menu_3.addAction(self.action_10)
        self.menu_3.addAction(self.action_11)
        self.menu_3.addAction(self.menu_5.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "菜单栏"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "视图"))
        self.menu_5.setTitle(_translate("MainWindow", "外观"))
        self.action_4.setText(_translate("MainWindow", "打开"))
        self.action_4.setToolTip(_translate("MainWindow", "打开 Ctrl+O"))
        self.action_5.setText(_translate("MainWindow", "关闭"))
        self.action_5.setToolTip(_translate("MainWindow", "关闭 Ctrl+W"))
        self.action_6.setText(_translate("MainWindow", "新建"))
        self.action_6.setToolTip(_translate("MainWindow", "新建 Ctrl+N"))
        self.action_7.setText(_translate("MainWindow", "保存"))
        self.action_7.setToolTip(_translate("MainWindow", "保存 Ctrl+S"))
        self.action_8.setText(_translate("MainWindow", "撤销"))
        self.action_8.setToolTip(_translate("MainWindow", "撤销 Ctrl+Z"))
        self.action_9.setText(_translate("MainWindow", "重做"))
        self.action_9.setToolTip(_translate("MainWindow", "重做 Ctrl+Shift+Z"))
        self.action_10.setText(_translate("MainWindow", "命令行"))
        self.action_11.setText(_translate("MainWindow", "运行"))
        self.action_13.setText(_translate("MainWindow", "项目结构"))
        self.action_14.setText(_translate("MainWindow", "状态栏"))
    
    # 1. 设置快捷键
    def setQuickKey(self):
        self.action_4.setShortcut("Ctrl+O")
        self.action_5.setShortcut("Ctrl+W")
        self.action_6.setShortcut("Ctrl+N")
        self.action_7.setShortcut("Ctrl+S")
        self.action_8.setShortcut("Ctrl+Z")
        self.action_9.setShortcut("Ctrl+Shift+Z")

    # 2. 设置 icon, 选做
    def setIconKey(self):
        pass
    
    # 2. 为 Menu 的 Action 绑定 trigger
    def triggerKey(self):
         self.menu.triggered[QtGui.QAction].connect(self.message)
    
    def message(self, m):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self.centralwidget, "提示", "选中: "+m.text(), QMessageBox.StandardButton.Ok)

    # 3. apply
    def apply(self):
        self.setQuickKey()
        self.setIconKey()
        self.triggerKey()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
