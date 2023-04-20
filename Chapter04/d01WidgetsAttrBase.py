import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QBrush, QColor
from PyQt6.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainWindow = MainWindow
        self.setInfo()
        self.setIcon("../resource/img/paimeng1.png")
        self.setBackground("../resource/img/bachsz.jpg")
    
    def setInfo(self):
        self.mainWindow.setObjectName("LingHua")        # 对象名, 独一无二
        self.mainWindow.resize(800, 600)                # 窗口大小
        self.mainWindow.setWindowTitle("绫化服艺@神里")    # 窗口标题
        self.mainWindow.setWindowOpacity(0.7)           # 窗口透明度

    def setIcon(self, img):
        icon = QIcon()
        icon.addPixmap(QPixmap(img), QIcon.Mode.Normal, QIcon.State.Off)
        self.mainWindow.setWindowIcon(icon)

    def setBackground(self, img):
        # 使用 stylesheet 设置 背景图片
        self.mainWindow.setStyleSheet(f"#LingHua{{border-image:url({img})}}")
        # "background-color: rgb(220, 149, 255);"

    def setPalette(self, img):
        palette = QPalette()
        # 设置背景颜色 (扮演角色, 内容)
        # palette.setColor(QPalette.ColorRole.Window, QColor(127, 63, 31, 127))
        # 设置背景图片
        # palette.setBrush(QPalette.ColorRole.Window, QBrush(QPixmap(img)))
        # 使适合窗口大小 ???
        # palette.setBrush(QPalette.ColorRole.Window,
        #                  QBrush(QPixmap(img).scaled(
        #                      self.mainWindow.size(),
        #                      aspectRatioMode=Qt.AspectRatioMode.IgnoreAspectRatio,
        #                      transformMode=Qt.TransformationMode.FastTransformation
        #                  )))
        self.mainWindow.setPalette(palette)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
