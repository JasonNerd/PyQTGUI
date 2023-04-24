from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LogReg(object):
    def setupUi(self, LogReg):
        LogReg.setObjectName("LogReg")
        LogReg.resize(600, 400)
        LogReg.setStyleSheet("background-color: rgb(228, 232, 255);\n"
"color: rgb(71, 4, 93);")
        self.centralwidget = QtWidgets.QWidget(parent=LogReg)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 90, 200, 30))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(246, 242, 255);\n"
"font: 14pt \"Calibri\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 90, 80, 30))
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 140, 200, 30))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color: rgb(246, 242, 255);\n"
"font: 14pt \"Calibri\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 140, 80, 30))
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label_2.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 250, 90, 42))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(81, 2, 121);\n"
"color: rgb(246, 242, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 250, 90, 42))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(81, 2, 121);\n"
"font: 14pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(246, 242, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        LogReg.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=LogReg)
        self.statusbar.setObjectName("statusbar")
        LogReg.setStatusBar(self.statusbar)

        self.retranslateUi(LogReg)
        QtCore.QMetaObject.connectSlotsByName(LogReg)

    def retranslateUi(self, LogReg):
        _translate = QtCore.QCoreApplication.translate
        LogReg.setWindowTitle(_translate("LogReg", "MainWindow"))
        self.label.setText(_translate("LogReg", "账 号："))
        self.label_2.setText(_translate("LogReg", "密 码："))
        self.pushButton.setText(_translate("LogReg", "注 册"))
        self.pushButton_2.setText(_translate("LogReg", "登 录"))
    
    # 以下位自己编写的代码
    def modifyZhhao(self):
        # 限制账号名为 不超过4位的中文
        regCh24 = QtCore.QRegularExpression("[\u4e00-\u9fa5]{1,4}$")
        self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(regCh24))
        self.lineEdit.setPlaceholderText("不超过4位的中文")
        self.lineEdit.editingFinished.connect(self.transL12) # 自动聚焦密码行
    
    def modifyPsw(self):
        # 限制密码是 8至12位的数字和大写字母 的组合
        regApN812 = QtCore.QRegularExpression("[0-9a-zA-Z]{8,12}")
        self.lineEdit_2.setValidator(QtGui.QRegularExpressionValidator(regApN812))
        self.lineEdit_2.setPlaceholderText("8至12位数字字母组合")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    
    def modifyLoggin(self):
        self.pushButton_2.clicked.connect(self.message)
    
    def transL12(self):
        self.lineEdit_2.setFocus()
    
    def message(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(MainWindow, "登录信息", "用户名: "+self.lineEdit.text()+", 密码: "+self.lineEdit_2.text(),
                                QMessageBox.StandardButton.Ok)

    def applyModify(self):
        self.modifyZhhao()
        self.modifyPsw()
        self.modifyLoggin()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LogReg()
    ui.setupUi(MainWindow)
    ui.applyModify()
    MainWindow.show()
    sys.exit(app.exec())