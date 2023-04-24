from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ComboBox(object):
    def setupUi(self, ComboBox):
        ComboBox.setObjectName("ComboBox")
        ComboBox.resize(512, 384)
        ComboBox.setStyleSheet("color: rgb(81, 2, 121);background-color: rgb(246, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=ComboBox)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 110, 241, 41))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 310, 211, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        ComboBox.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=ComboBox)
        self.statusbar.setObjectName("statusbar")
        ComboBox.setStatusBar(self.statusbar)

        self.retranslateUi(ComboBox)
        QtCore.QMetaObject.connectSlotsByName(ComboBox)

    def retranslateUi(self, ComboBox):
        _translate = QtCore.QCoreApplication.translate
        ComboBox.setWindowTitle(_translate("ComboBox", "下拉组合框示意"))
        self.label.setText(_translate("ComboBox", "ComboBox 下拉组合框示例"))
        self.label_2.setText(_translate("ComboBox", "您选择的职位是："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ComboBox()
    ui.setupUi(MainWindow)
    # 对 ui 进行修改
    selList = ["总经理", "副经理", "财务经理", "人事经理", "职员"]
    ui.comboBox.addItems(selList)
    def info(ui):
         ui.label_2.setText("您选择的职位是："+ui.comboBox.currentText())
    ui.comboBox.setCurrentIndex(0)
    ui.comboBox.currentIndexChanged.connect(lambda: info(ui=ui))
    MainWindow.show()
    sys.exit(app.exec())
