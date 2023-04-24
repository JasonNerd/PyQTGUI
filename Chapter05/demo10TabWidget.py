
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/img/tx3.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(81, 2, 121);\n"
"background-color: rgb(246, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 481))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 520, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 520, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ListWidget属性"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
    
    def addtab(self):
        self.tab = QtWidgets.QWidget()
        name = "tab_"+str(self.tabWidget.count()+1)
        self.tab.setObjectName(name)
        self.tabWidget.addTab(self.tab, name)
    
    def deltab(self):
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
    
    def gettab(self, currentIndex):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self.centralwidget, "提示", 
                                self.tabWidget.tabText(currentIndex)+", 其编号为: "+str(self.tabWidget.currentIndex()),
                                QMessageBox.StandardButton.Ok)
    
    def modify(self):
        self.pushButton.clicked.connect(self.addtab)
        self.pushButton_2.clicked.connect(self.deltab)
        self.tabWidget.currentChanged.connect(self.gettab)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.modify()
    MainWindow.show()
    sys.exit(app.exec())

