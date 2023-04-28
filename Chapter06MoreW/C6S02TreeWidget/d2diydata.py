# 自定义数据模型
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 374)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 0, 512, 376))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def apply(self):
        # 准备数据
        labels = ["年级", "班级", "姓名", "分数"]
        n = 10
        names = ['马云', '马化腾', '李彦宏', '王兴', '刘强东', '董明珠', '张一鸣', '任正非', '丁磊', '程维']
        scores = [65, 89, 45, 68, 90, 100, 99, 76, 85, 73]
        # 设定数据模型
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(labels)
        # 为数据模型填充数据
        import random
        # 一级、二级列表数量
        num_f = random.randrange(3, 8)
        for i in range(num_f):
            grade = QtGui.QStandardItem(f"年级{i+1}")
            model.appendRow(grade)
            num_s = random.randrange(5, 10)
            for j in range(num_s):
                itemEmpty = QtGui.QStandardItem("")
                itemClass = QtGui.QStandardItem(f"班级{j+1}")
                itemName = QtGui.QStandardItem(names[random.randint(0, n-1)])
                itemScore = QtGui.QStandardItem(str(scores[random.randint(0, n-1)]))
                grade.appendRow([itemEmpty, itemClass, itemName, itemScore])
        self.treeView.setModel(model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.apply()
    MainWindow.show()
    sys.exit(app.exec())
