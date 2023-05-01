
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 310)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # two label
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setObjectName("label")
        # two line-edit
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setObjectName("lineEdit_2")
        # two push-btn
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setObjectName("pushButton_2")
        # grid layout
        grid = QtWidgets.QGridLayout(parent=self.centralwidget)
        grid.addWidget(self.label, 0, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.lineEdit, 0, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.label_2, 1, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.lineEdit_2, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.pushButton, 2, 0, QtCore.Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.pushButton_2, 2, 1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.centralwidget.setLayout(grid)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Login"))
        self.label.setText(_translate("MainWindow", "User Name"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
