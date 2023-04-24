
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LCDNumber(object):
    def setupUi(self, SpinBox):
        SpinBox.setObjectName("SpinBox")
        SpinBox.resize(600, 400)
        SpinBox.setStyleSheet("background-color: rgb(228, 232, 255);\n""color: rgb(71, 4, 93);")
        self.centralwidget = QtWidgets.QWidget(parent=SpinBox)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(140, 180, 321, 111))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 140, 161, 30))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(246, 242, 255);\n""font: 14pt \"Calibri\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 140, 111, 30))
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label.setStyleSheet("font: 14pt \"Microsoft YaHei UI\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        SpinBox.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=SpinBox)
        self.statusbar.setObjectName("statusbar")
        SpinBox.setStatusBar(self.statusbar)

        self.retranslateUi(SpinBox)
        QtCore.QMetaObject.connectSlotsByName(SpinBox)

    def retranslateUi(self, SpinBox):
        _translate = QtCore.QCoreApplication.translate
        SpinBox.setWindowTitle(_translate("SpinBox", "MainWindow"))
        self.lineEdit.setText(_translate("SpinBox", "2323"))
        self.label.setText(_translate("SpinBox", "请输入数字："))
    
    def modifyLCD(self):
        self.lcdNumber.setDigitCount(5) # 最多显示5位数字
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Mode.Dec) # 十进制
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)  # 样式: Flat平滑样式
    
    def modifyLineEdit(self):
        reg = QtCore.QRegularExpression("[0-9]{1,5}") # 5位以内的数字
        self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(reg))
        self.lineEdit.setPlaceholderText("5位以内的数字")
        self.lineEdit.editingFinished.connect(self.setLCDN) # line edit 连接到 LCD
    
    def setLCDN(self):
        self.lcdNumber.setProperty("value", self.lineEdit.text())
    
    def applyModify(self):
        self.modifyLCD()
        self.modifyLineEdit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LCDNumber()
    ui.setupUi(MainWindow)
    ui.applyModify()
    MainWindow.show()
    sys.exit(app.exec())