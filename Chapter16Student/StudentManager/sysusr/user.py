import sys
sys.path.append("../")
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # 只显示最小化和关闭按钮按键
        self.setWindowFlags(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)