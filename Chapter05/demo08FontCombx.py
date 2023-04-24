from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 384)
        MainWindow.setStyleSheet("color: rgb(81, 2, 121);background-color: rgb(246, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 50, 191, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fontComboBox = QtWidgets.QFontComboBox(parent=self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(130, 90, 241, 31))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 210, 261, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FontComboBox"))
        self.label.setText(_translate("MainWindow", "FontComboBox: 字体选择"))
        self.label_2.setText(_translate("MainWindow", "若知是梦何须醒，不比真如一相会"))

    def setft(self):
        fly = self.fontComboBox.currentText()
        font = self.label_2.font()
        font.setFamily(fly)
        self.label_2.setFont(font)
    
    def modify(self):
        self.fontComboBox.setFontFilters(QtWidgets.QFontComboBox.FontFilter.AllFonts)
        self.fontComboBox.currentIndexChanged.connect(self.setft)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.modify()
    MainWindow.show()
    sys.exit(app.exec())