
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 90, 201, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 160, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 320, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 270, 75, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 230, 75, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QMessageBox的五种类型"))
        self.pushButton.setText(_translate("MainWindow", "Error"))
        self.pushButton_2.setText(_translate("MainWindow", "Question"))
        self.pushButton_3.setText(_translate("MainWindow", "Infomation"))
        self.pushButton_4.setText(_translate("MainWindow", "Warnings"))
        self.pushButton_5.setText(_translate("MainWindow", "About"))
    
    # 五种类型的 对话框
    def info(self):
        sel = QMessageBox.information(self.centralwidget, "消息", "a information box", 
                                      QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        if sel == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self.centralwidget, "消息", "同意")
        else:
            QMessageBox.information(self.centralwidget, "消息", "拒绝")
    
    def warn(self):
        QMessageBox.warning(self.centralwidget, "警告", "a warning box", QMessageBox.StandardButton.Ok)
    
    def erro(self):
        QMessageBox.critical(self.centralwidget, "异常", "a errono box", QMessageBox.StandardButton.Ok)

    def prob(self):
        QMessageBox.question(self.centralwidget, "确认？", "a qusetionary box", QMessageBox.StandardButton.Ok)

    def abot(self):
        QMessageBox.about(self.centralwidget, "关于", "what's this")
    
    def apply(self):
        self.pushButton.clicked.connect(self.erro)
        self.pushButton_4.clicked.connect(self.warn)
        self.pushButton_3.clicked.connect(self.info)
        self.pushButton_5.clicked.connect(self.abot)
        self.pushButton_2.clicked.connect(self.prob)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
