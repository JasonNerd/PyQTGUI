
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # 状态栏
        self.statusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    # 向状态栏添加控件
    def stuffing(self):
        self.statusBar.setStyleSheet("background-color: rgb(246, 242, 255);")
        self.label = QtWidgets.QLabel("@绫华服艺", self.statusBar)
        self.statusBar.addPermanentWidget(self.label)

    # 显示实时时间
    def setTime(self):
        timer = QtCore.QTimer(self.centralwidget)
        timer.timeout.connect(self.showMessage)
        timer.start()

    def showMessage(self):
        dateTime = QtCore.QDateTime.currentDateTime()
        text = dateTime.toString("yyyy-MM-dd HH:mm:ss")
        self.statusBar.showMessage(text, 0)


    def apply(self):
        self.stuffing()
        self.setTime()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
