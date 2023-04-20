import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPixmap, QBrush, QPalette, QPainter, QIcon
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow
        self.setInfo()          # 窗口大小, 背景, 标题, 图标
        self.setCloseButton()   # 1个按钮 -- 关闭窗口
        self.setTipsBtn()       # 1个按钮 -- 弹出一个提示窗
        self.closeBtn.clicked.connect(MainWindow.close)  # 关闭窗口
        self.tipsBtn.clicked.connect(self.showMessage)

    def showMessage(self):
        QMessageBox.information(self.mainWindow, "白鹭霜华", "欢迎进入PyQT6!",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                QMessageBox.StandardButton.No)

    def setTipsBtn(self):
        self.tipsBtn = QtWidgets.QPushButton(parent=self.mainWindow)
        self.tipsBtn.setGeometry(QtCore.QRect(600, 400, 100, 48))
        self.tipsBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.tipsBtn.setText("欢迎进入")
        self.tipsBtn.setObjectName("tipsBtn")

    def setCloseButton(self):
        self.closeBtn = QtWidgets.QPushButton(parent=self.mainWindow)
        self.closeBtn.setGeometry(QtCore.QRect(300, 200, 100, 48))
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.closeBtn.setText("关闭窗口")
        self.closeBtn.setObjectName("closeBtn")

    def setInfo(self):
        self.mainWindow.setObjectName("LingHua")  # 对象名, 独一无二
        self.mainWindow.resize(800, 600)  # 窗口大小
        self.mainWindow.setWindowTitle("绫化服艺@神里")  # 窗口标题
        self.mainWindow.setWindowOpacity(0.98)  # 窗口透明度
        self.setIcon("../resource/img/paimeng1.png")
        self.setBackground("../resource/img/bachsz.jpg")

    def setIcon(self, img):
        icon = QIcon()
        icon.addPixmap(QPixmap(img), QIcon.Mode.Normal, QIcon.State.Off)
        self.mainWindow.setWindowIcon(icon)

    def setBackground(self, img):
        self.mainWindow.setStyleSheet("#LingHua{background-color: rgb(222, 127, 64)}")
        self.mainWindow.setStyleSheet("#tipsBtn{background-color: rgb(0, 205, 205)}")
        self.mainWindow.setStyleSheet("#closeBtn{background-color: rgb(255, 31, 31)}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

