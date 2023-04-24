from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SpinBox(object):
    def setupUi(self, SpinBox):
        SpinBox.setObjectName("SpinBox")
        SpinBox.resize(600, 400)
        SpinBox.setStyleSheet("background-color: rgb(228, 232, 255);\n"
"color: rgb(71, 4, 93);")
        self.centralwidget = QtWidgets.QWidget(parent=SpinBox)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(170, 130, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(380, 130, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 100, 54, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 100, 101, 16))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(130, 160, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        SpinBox.setCentralWidget(self.centralwidget)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 180, 300, 16))
        self.label_3.setObjectName("label_3")
        self.retranslateUi(SpinBox)
        QtCore.QMetaObject.connectSlotsByName(SpinBox)

    def retranslateUi(self, SpinBox):
        _translate = QtCore.QCoreApplication.translate
        SpinBox.setWindowTitle(_translate("SpinBox", "MainWindow"))
        self.label.setText(_translate("SpinBox", "SpinBox"))
        self.label_2.setText(_translate("SpinBox", "DoubleSpinBox"))

    # 对于生成的就原封不动, 要改就单写函数
    def modifySB(self):
        # 选择 2到30以内的数
        self.spinBox.setValue(2)
        self.spinBox.setRange(2, 30)
        self.spinBox.setSingleStep(2)
        self.spinBox.valueChanged.connect(self.getValue)

    def modifyDSB(self):
        # 选择 0到1以内的两位小数
        self.doubleSpinBox.setValue(0.2)
        self.doubleSpinBox.setRange(0, 1)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setDecimals(2) # 保留2位小数
        self.doubleSpinBox.valueChanged.connect(self.getValue)
    
    # 获取控件值, 显示在 一个label中
    def getValue(self):
        val1 = self.spinBox.value()
        val2 = self.doubleSpinBox.value()
        self.label_3.setText("SpinBox: "+str(val1)+"\tDoubleSpinBox: "+str(val2))

    def applyModify(self):
        self.modifySB()
        self.modifyDSB()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SpinBox()
    ui.setupUi(MainWindow)
    ui.applyModify()
    MainWindow.show()
    sys.exit(app.exec())