

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 420)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 61, 16))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 190, 61, 16))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 230, 61, 16))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 110, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 150, 311, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 190, 311, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 230, 311, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "姓 名："))
        self.label_2.setText(_translate("MainWindow", "年 龄："))
        self.label_3.setText(_translate("MainWindow", "班 级："))
        self.label_4.setText(_translate("MainWindow", "分 数："))
    
    # 设置 input dialog
    def getName(self):
        name, ok = QtWidgets.QInputDialog.getText(self.centralwidget, "姓名", "请输入姓名", QtWidgets.QLineEdit.EchoMode.Normal, "绫华服艺")
        if ok:
            self.lineEdit.setText(name)
    
    def getAge(self):
        age, ok = QtWidgets.QInputDialog.getInt(self.centralwidget, "年龄", "请输入年龄", 20, 1, 100, 1)
        if ok:
            self.lineEdit_2.setText(str(age))
    
    def getGrade(self):
        grade, ok = QtWidgets.QInputDialog.getItem(self.centralwidget, "班级", "请输入班级", ['三年A班', '三年B班', '三年1班', '三年2班'], 0, False)
        if ok:
            self.lineEdit_3.setText(grade)
    
    def getScore(self):
        score, ok = QtWidgets.QInputDialog.getDouble(self.centralwidget, "分数", "请输入分数", 59.0, 0.0, 100, 2)
        if ok:
            self.lineEdit_4.setText(str(score))
    
    # 设置 触发函数
    def apply(self):
        self.lineEdit.returnPressed.connect(self.getName)
        self.lineEdit_2.returnPressed.connect(self.getAge)
        self.lineEdit_3.returnPressed.connect(self.getGrade)
        self.lineEdit_4.returnPressed.connect(self.getScore)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
