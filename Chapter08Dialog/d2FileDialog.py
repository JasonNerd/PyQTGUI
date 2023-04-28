
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(180, 70, 491, 351))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(188, 179, 184);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QFileDialog"))
        self.pushButton.setText(_translate("MainWindow", "Select Image"))

    def bindList(self):
        imgDialog = QtWidgets.QFileDialog(self.centralwidget)
        imgDialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)  # 单个文件
        imgDialog.setNameFilter("图片文件(*.jpg *.png *.jpeg *.bmp")
        if imgDialog.exec():    # 选择了文件
            self.setBorder(imgDialog.selectedFiles()[0])
    
    def setBorder(self, img):
        self.centralwidget.setStyleSheet(f"#listWidget{{border-image:url({img})}}")
    
    def apply(self):
        self.pushButton.clicked.connect(self.bindList)

# 在py代码文件中, 定义一个 bindList() 槽函数, 用来使用 QFieDialog 类创建一个文件对话框, 
# 在该文件对话框中可以设置选择单个文件, 并且只能显示图片文件, 选择完之后, 会将选择的文件显示到ListWidget列表中;
# 最后将自定义的 bindList() 槽函数绑定到 PushButton 控件的clicked 信号上。
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
