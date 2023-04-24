import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPixmap, QBrush, QPalette, QPainter, QIcon, QFont
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("TextLabel")
        MainWindow.resize(720, 400)
        self.bgimg = "../resource/img/SeaBlue.jpg"
        # text label
        self.textLabel = QLabel(parent=MainWindow)
        self.setTextLabel()
        # image label
        self.imgLabel = QLabel(parent=MainWindow)
        self.setImgLabel()
        # link label
        self.lkLabel = QLabel(parent=MainWindow)
        self.setLkLabel()

    def setLkLabel(self):
        self.lkLabel.setGeometry(250, 200, 180, 32)
        self.lkLabel.setText("<a href='https://www.miyoushe.com/ys/'>神里服艺@绫华-店铺动态</a>")
        self.lkLabel.setOpenExternalLinks(True)

    def setImgLabel(self):
        self.imgLabel.setGeometry(200, 200, 32, 32)
        self.imgLabel.setPixmap(QPixmap(self.bgimg))  # 此时 label 就是一张图片

    
    def setTextLabel(self):
        self.textLabel.setObjectName("demoLabel")
        self.textLabel.setGeometry(QtCore.QRect(2, 2, 120, 40))
        # self.textLabel.setGeometry(QtCore.QRect(300, 140, 120, 40))
        self.textLabel.setText("神里服艺@绫华")
        self.textLabel.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        font = QFont()
        font.setFamily("宋体")
        font.setBold(True)
        font.setPointSize(12)
        self.textLabel.setFont(font)
        self.textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) # 设置水平垂直居中
        self.textLabel.setWordWrap(True)    # 文本可换行显示
        # 将标签设置为图片
        # 注意 StyleSheet 只设置一次, 所有的样式放到一个字符串
        # self.textLabel.setStyleSheet("background-color: #9370DB;\n"
        self.textLabel.setStyleSheet(f"border-image: url({self.bgimg});\n"
                                     "color: #FFFAFA;")
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())