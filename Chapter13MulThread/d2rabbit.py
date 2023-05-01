from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QThread, pyqtSignal

class Rabbit(QThread):
    sinOut = pyqtSignal(str)
    def __init__(self):
        super(Rabbit, self).__init__()
    # 重写 run 方法
    def run(self):
        for i in range(1, 11):
            QThread.msleep(100)
            self.sinOut.emit(f"\n Rabbit have run {i*10} meters.")
            if i == 9:
                self.sinOut.emit("\n Rabbit is sleepping!")
                QThread.sleep(5)
            if i == 10:
                self.sinOut.emit("\n Rabbit get to the terminal.")
            
class Turtle(QThread):
    sinOut = pyqtSignal(str)
    def __init__(self):
        super(Turtle, self).__init__()
    # 重写 run 方法
    def run(self):
        for i in range(1, 11):
            QThread.msleep(500)
            self.sinOut.emit(f"\n Turtle have run {i*10} meters.")
            if i == 10:
                self.sinOut.emit("\n Turtle get to the terminal.")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 608)
        MainWindow.setStyleSheet("background-color: rgb(246, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 40, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(246, 242, 255);\n"
"background-color: rgb(57, 53, 98);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 40, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(246, 242, 255);\n"
"background-color: rgb(57, 53, 98);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 90, 221, 351))
        self.textEdit.setStyleSheet("color: rgb(57, 53, 98);\n"
"background-color: rgb(206, 171, 199);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(360, 90, 241, 351))
        self.textEdit_2.setStyleSheet("color: rgb(57, 53, 98);\n"
"background-color: rgb(206, 171, 199);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 500, 75, 24))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Rabbit"))
        self.label_2.setText(_translate("MainWindow", "Turtle"))
        self.pushButton.setText(_translate("MainWindow", "Start"))

    # 以下为自定义代码
    def apply(self):
        self.pushButton.clicked.connect(self.contest) # 比赛开始
    
    def contest(self):
        self.r = Rabbit()
        self.t = Turtle()
        self.r.sinOut.connect(self.rslot)
        self.t.sinOut.connect(self.tslot)
        self.r.start()
        self.t.start()
    
    def rslot(self, txt):
        self.textEdit.setPlainText(self.textEdit.toPlainText()+txt)
    def tslot(self, txt):
        self.textEdit_2.setPlainText(self.textEdit_2.toPlainText()+txt)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
