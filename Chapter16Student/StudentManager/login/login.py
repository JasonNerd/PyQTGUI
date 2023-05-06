import sys
sys.path.append("../")
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from tools import dboperation
from primary import main

class Ui_MainWindow(object):
    def setupUi(self, Login):
        self.MainWindow = Login
        Login.setObjectName("Login")
        Login.resize(720, 480)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        Login.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 108, 96, 48))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 200, 96, 48))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 106, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 200, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 310, 260, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(81, 2, 121); color: rgb(246, 242, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 380, 260, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(81, 2, 121); color: rgb(246, 242, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "管理员登录"))
        self.label.setText(_translate("Login", "用户名："))
        self.label_2.setText(_translate("Login", "密  码："))
        self.pushButton.setText(_translate("Login", "登 录"))
        self.pushButton_2.setText(_translate("Login", "退 出"))
    
    ## 以下为自己编写的代码
    def setIcon(self, img):
        icon = QIcon()
        icon.addPixmap(QPixmap(img), QIcon.Mode.Normal, QIcon.State.Off)
        self.MainWindow.setWindowIcon(icon)
    
    # 对输入做限制
    def editLimit(self):
        regCh24 = QtCore.QRegularExpression("[\u4e00-\u9fa5]{2,4}$")
        regApN812 = QtCore.QRegularExpression("[0-9A-Z]{8,12}")
        self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(regCh24))
        self.lineEdit_2.setValidator(QtGui.QRegularExpressionValidator(regApN812))
        self.lineEdit.setPlaceholderText("昵称(2到4位的中文)")
        self.lineEdit_2.setPlaceholderText("密码(8至12位数字大写字母组合)")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    
    # 提交并检查信息
    usr = dboperation.query("select * from tb_user")[0]
    def checkSysUsrInfo(self):
        account = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        if account == "" or password == "":
            QMessageBox.warning(self.centralwidget, "警告", "账号密码均为必填字段", QMessageBox.StandardButton.Ok)
        else: # 确保得到有效输入后进行检查
            if(self.checkAcc(account)):
                if(self.checkPas(password)):
                    self.m = main.Ui_MainWindow() # 跳转到主窗口
                    self.m.show()
                    self.MainWindow.hide()

    def checkAcc(self, account):
        if self.usr[0] != account:
            QMessageBox.warning(self.centralwidget, "警告", "不存在该账号!", QMessageBox.StandardButton.Ok)
            return False
        else:
            return True
    
    def checkPas(self, password):
        if self.usr[1] != password:
            QMessageBox.warning(self.centralwidget, "警告", "密码错误!", QMessageBox.StandardButton.Ok)
            return False
        else:
            return True

    def run(self):
        self.setIcon("src/nilu.png")
        self.MainWindow.setStyleSheet("background-color: #ceabc7; color: #393562;")
        self.editLimit()
        self.lineEdit.setText("千月木")
        self.lineEdit_2.setText("2P02Y3Q502T")
        self.pushButton.clicked.connect(self.checkSysUsrInfo)
        self.pushButton_2.clicked.connect(self.MainWindow.close)
