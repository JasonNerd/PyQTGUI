from exam02chbx import Ui_UsrAccess
from exam02LogRadio import Ui_Login
from PyQt6 import QtCore, QtGui, QtWidgets

# 不超过 4 位的中文
def accountCheck(self):
    reg = QtCore.QRegularExpression("[\u4e00-\u9fa5]{1,4}$")
    self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(reg))
    self.lineEdit.editingFinished.connect(lambda: focusChange(self))

# 8 到  12 位的数字字母组合
def passwdCheck(self):
    reg = QtCore.QRegularExpression("[0-9a-zA-Z]{8,12}")
    self.lineEdit_2.setValidator(QtGui.QRegularExpressionValidator(reg))
    self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

def usrTypeCheck(self):
    if self.radioButton.isChecked():
        return 1    # 管理员
    elif self.radioButton_3.isChecked():
        return 2    # 普通用户
    else:
        return -1

def btnLoginCheck(self):
    usr_dict = {}
    ui = Ui_UsrAccess()
    self.pushButton_3.clicked.connect(lambda: getInfo(self, usr_dict, ui))
    return usr_dict

def focusChange(self):
    self.lineEdit_2.setFocus()

def getInfo(self, usr_dict, ui):
    from PyQt6.QtWidgets import QMessageBox
    usr_dict["account"] = self.lineEdit.text()
    usr_dict["passwd"] = self.lineEdit_2.text()
    usr_dict["acctype"] = usrTypeCheck(self)
    usr_dict["acclist"] = []
    QMessageBox.information(self.centralwidget, "登录信息", str(usr_dict), QMessageBox.StandardButton.Ok)
    ui.show()
    accessCheck(ui=ui)
    self.close()

def applyModify(self):
    accountCheck(self)
    passwdCheck(self)
    return btnLoginCheck(self)


def accessCheck(ui):
    ui.pushButton_3.clicked.connect(lambda: accessClick(ui=ui))    
    
def accessClick(ui):
    from PyQt6.QtWidgets import QMessageBox
    if ui.checkBox.isChecked():
        usr_dict["acclist"].append(ui.checkBox.text())
    if ui.checkBox_2.isChecked():
        usr_dict["acclist"].append(ui.checkBox_2.text())
    if ui.checkBox_3.isChecked():
        usr_dict["acclist"].append(ui.checkBox_3.text())
    if ui.checkBox_4.isChecked():
        usr_dict["acclist"].append(ui.checkBox_4.text())
    if ui.checkBox_5.isChecked():
        usr_dict["acclist"].append(ui.checkBox_5.text())
    QMessageBox.information(ui.centralwidget, "权限选择", str(usr_dict), QMessageBox.StandardButton.Ok)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Login()
    ui.show()
    usr_dict = applyModify(ui)
    sys.exit(app.exec())