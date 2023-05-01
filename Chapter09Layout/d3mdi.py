
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mdiArea = QtWidgets.QMdiArea(parent=self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 601, 361))
        self.mdiArea.setObjectName("mdiArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(parent=self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menuBar.addAction(self.menu.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    ## -----------------------------------------------------
    ## 以下为自定义区域
    count = 0
    def apply(self):
        self.menu.triggered[QtGui.QAction].connect(self.subwindow)

    def subwindow(self, act):
        if act.text() == "新建":
            sub = QtWidgets.QMdiSubWindow()
            self.count += 1
            sub.setWindowTitle("子窗口"+str(self.count))
            sub.setWidget(QtWidgets.QLabel(f"这是第({self.count})个窗口"))
            self.mdiArea.addSubWindow(sub)
            sub.show()
        elif act.text() == "平铺显示":
            self.mdiArea.tileSubWindows()
        elif act.text() == "级联显示":
            self.mdiArea.cascadeSubWindows()
    ## 以上为自定义区域
    ## -----------------------------------------------------
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "子窗体操作"))
        self.action.setText(_translate("MainWindow", "新建"))
        self.action_2.setText(_translate("MainWindow", "平铺显示"))
        self.action_3.setText(_translate("MainWindow", "级联显示"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
