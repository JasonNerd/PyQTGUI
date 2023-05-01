from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import *

class FormLogin(QWidget):
    def __init__(self, parent=None):
        super(FormLogin, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        form = QFormLayout()
        # two label
        self.label = QtWidgets.QLabel()
        self.label.setText("账号")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setText("密码")
        # two line-edit
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit_2 = QtWidgets.QLineEdit()
        # two push-btn
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setText("登录")
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setText("取消")

        form.addRow(self.label, self.lineEdit)
        form.addRow(self.label_2, self.lineEdit_2)
        form.addRow(self.pushButton, self.pushButton_2)
        self.setLayout(form)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    fl = FormLogin()
    fl.show()
    sys.exit(app.exec())

