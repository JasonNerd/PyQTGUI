

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 300)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: #ceabc7")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 19, 23);\n"
"color: rgb(255, 255, 171);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 19, 23);\n"
"color: rgb(255, 255, 171);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 30, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 19, 23);\n"
"color: rgb(255, 255, 171);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 30, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 19, 23);\n"
"color: rgb(255, 255, 171);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 30, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 19, 23);\n"
"color: rgb(255, 255, 171);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 30, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 80, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 171);\n"
"background-color: rgb(85, 85, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 80, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 140, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(246, 242, 255); color: rgb(81, 2, 121);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 210, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(246, 242, 255); color: rgb(81, 2, 121);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "00"))
        self.label_2.setText(_translate("MainWindow", "00"))
        self.label_3.setText(_translate("MainWindow", "00"))
        self.label_4.setText(_translate("MainWindow", "00"))
        self.label_5.setText(_translate("MainWindow", "00"))
        self.label_6.setText(_translate("MainWindow", "红球"))
        self.label_7.setText(_translate("MainWindow", "00"))
        self.label_8.setText(_translate("MainWindow", "蓝球"))
        self.pushButton.setText(_translate("MainWindow", "start"))
        self.pushButton_2.setText(_translate("MainWindow", "stop"))
    
    # 以下为 自定义代码
    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.start()
        self.timer.timeout.connect(self.getnum)
    
    def getnum(self):
        import random
        self.label.setText("{0:02d}".format(random.randint(1, 33)))
        self.label_2.setText("{0:02d}".format(random.randint(1, 33)))
        self.label_3.setText("{0:02d}".format(random.randint(1, 33)))
        self.label_4.setText("{0:02d}".format(random.randint(1, 33)))
        self.label_5.setText("{0:02d}".format(random.randint(1, 33)))
        self.label_7.setText("{0:02d}".format(random.randint(1, 33)))
    
    def stop(self):
        self.timer.stop()
    
    def apply(self):
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
