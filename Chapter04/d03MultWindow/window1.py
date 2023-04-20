import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow
        self.mainWindow.setObjectName("MainWindow")
        self.mainWindow.resize(800, 600)
        self.retranslateUi()
        self.setBackground()
        self.setTipsBtn()
        self.tipsBtn.clicked.connect(self.openOthers)   # 点击按钮 打开其他窗口
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setTipsBtn(self):
        self.tipsBtn = QtWidgets.QPushButton(parent=self.mainWindow)
        self.tipsBtn.setGeometry(QtCore.QRect(600, 400, 100, 48))
        self.tipsBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tipsBtn.setText("打开窗口")
        self.tipsBtn.setObjectName("tipsBtn")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.mainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def setBackground(self):
        self.mainWindow.setStyleSheet("#LingHua{background-color: rgb(222, 127, 64)}")
        self.mainWindow.setStyleSheet("#tipsBtn{background-color: rgb(0, 205, 205)}")

    def openOthers(self):
        import window2, window3, window4
        self.second = window2.Ui_MainWindow()
        self.second.show()
        self.third = window3.Ui_MainWindow()
        self.third.show()
        self.fourth = window4.Ui_MainWindow()
        self.fourth.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
