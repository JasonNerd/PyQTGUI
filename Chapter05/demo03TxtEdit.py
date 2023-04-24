from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TextEdit(object):
    def setupUi(self, TextEdit):
        TextEdit.setObjectName("TextEdit")
        TextEdit.resize(600, 400)
        TextEdit.setStyleSheet("background-color: rgb(228, 232, 255);\n"
"color: rgb(71, 4, 93);")
        self.centralwidget = QtWidgets.QWidget(parent=TextEdit)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 110, 180, 120))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(390, 110, 180, 120))
        self.textEdit_2.setAutoFillBackground(True)
        self.textEdit_2.setAcceptRichText(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 90, 54, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        TextEdit.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=TextEdit)
        self.statusbar.setObjectName("statusbar")
        TextEdit.setStatusBar(self.statusbar)

        self.retranslateUi(TextEdit)
        QtCore.QMetaObject.connectSlotsByName(TextEdit)

    def retranslateUi(self, TextEdit):
        _translate = QtCore.QCoreApplication.translate
        TextEdit.setWindowTitle(_translate("TextEdit", "MainWindow"))
        self.textEdit.setPlainText(_translate("TextEdit", "身为社奉行神里家的女儿，绫华常提防着贵胄门庭之间的权力争斗。"))
        self.textEdit_2.setHtml(_translate("TextEdit", "身为<b>社奉行</b>神里家的女儿，"
                                           "<span style=\" font-family:\'fangsong\'; font-size:20pt; color:#8c8cff;\">"
                                           "绫华</span>常提防着贵胄门庭之间的权力争斗。"))
        self.label.setText(_translate("TextEdit", "纯文本："))
        self.label_2.setText(_translate("TextEdit", "HTML文本: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TextEdit()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())