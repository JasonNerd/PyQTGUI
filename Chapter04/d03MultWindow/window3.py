from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Window3")
        MainWindow.resize(400, 255)
        MainWindow.setWindowTitle("Window3")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
