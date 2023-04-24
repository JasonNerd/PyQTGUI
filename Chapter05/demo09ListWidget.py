from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\../../resource/img/tx3.jpg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(81, 2, 121);\n"
"background-color: rgb(246, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 75, 600, 450))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        self.listWidget.setFont(font)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("background-color: rgb(188, 179, 184);\n"
"color: rgb(165, 153, 223);")
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ListWidget属性"))

    
    def modify(self):
        from collections import OrderedDict
        data = OrderedDict({
            "第1名": "战狼2, 2017年上映, 票房56.83亿",
            "第2名": "哪之魔童降世, 2019年上映, 票房50.12亿",
            "第3名": "流浪地球, 2019年上映, 票房46.86亿",
            "第4名": "复仇者联盟-终局之战, 2019年上映, 票房42.50亿",
            '第5名': '红海行动, 2018年上映,票房36.51亿',
            '第6名': '唐人街探案2, 2018年上映, 票房33.98亿',
            '第7名': '美人鱼, 2016年上映,票房33.86亿',
            "第8名": "我和我的祖国, 2019年上映, 票房31.71亿",
            "第9名": "我不是药神, 2018年上映, 票房31.00亿",
            "第10名": "中国机长, 2019年上映, 票房29.13亿"
        })
        for k, v in data.items():
            self.item = QtWidgets.QListWidgetItem(self.listWidget)
            self.item.setText(k+": "+v)
            self.item.setToolTip(v)
            self.listWidget.addItem(self.item)
        # 设置 点击信号, 除此之外 还有个 currentItemChanged 信号
        self.listWidget.itemClicked.connect(self.message)
    
    def message(self, item):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self.centralwidget, "提示", item.text(), QMessageBox.StandardButton.Ok)
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.modify()
    MainWindow.show()
    sys.exit(app.exec())