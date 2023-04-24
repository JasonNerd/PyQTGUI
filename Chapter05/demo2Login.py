import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPixmap, QBrush, QPalette, QPainter, QIcon
from PyQt6.QtWidgets import QMessageBox, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(400, 300)
        login.setStyleSheet("background-color: rgb(228, 232, 255);\ncolor: rgb(71, 4, 93);")

        self.centralwidget = QtWidgets.QWidget(parent=login)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 60, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(228, 229, 255);\ncolor: rgb(71, 4, 93);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 60, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(228, 229, 255);\ncolor: rgb(71, 4, 93);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 180, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 90, 180, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 210, 75, 24))
        self.pushButton.setObjectName("pushButton")
        login.setCentralWidget(self.centralwidget)
        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    # 在这里写逻辑代码
    def txtLimit(self):
        # 限制账号名为 2到4位的中文
        # 限制密码是 8至12位的数字和大写字母 的组合
        regCh24 = QtCore.QRegularExpression("[\u4e00-\u9fa5]{2,4}$")
        regApN812 = QtCore.QRegularExpression("[0-9A-Z]{8,12}")
        self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(regCh24))
        self.lineEdit_2.setValidator(QtGui.QRegularExpressionValidator(regApN812))
        self.lineEdit.setPlaceholderText("2到4位的中文")
        self.lineEdit_2.setPlaceholderText("8至12位数字大写字母组合")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        # self.lineEdit_2.setValidator(QtGui.QIntValidator(10000000, 99999999))


    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "MainWindow"))
        self.label.setText(_translate("login", "账 号："))
        self.label_2.setText(_translate("login", "密 码："))
        self.pushButton.setText(_translate("login", "登录服艺"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.txtLimit()
    MainWindow.show()
    sys.exit(app.exec())