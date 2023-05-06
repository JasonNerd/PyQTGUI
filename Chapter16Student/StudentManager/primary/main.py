import sys
sys.path.append("../")
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QWidget
from settings import grade, classes, subject, examkinds
from baseinfo import student, result
from query import resultinfo, studentinfo
from sysusr import user

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # 只显示最小化和关闭按钮按键
        self.setWindowFlags(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        self.run()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        self.menubar.setStyleSheet("background-color: #510279; color: #f6f2ff;")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtGui.QAction(parent=MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtGui.QAction(parent=MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtGui.QAction(parent=MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtGui.QAction(parent=MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtGui.QAction(parent=MainWindow)
        self.action_11.setObjectName("action_11")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.menu_3.addAction(self.action_8)
        self.menu_3.addAction(self.action_9)
        self.menu_4.addAction(self.action_10)
        self.menu_4.addAction(self.action_11)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "基础设置"))
        self.menu_2.setTitle(_translate("MainWindow", "信息管理"))
        self.menu_3.setTitle(_translate("MainWindow", "系统查询"))
        self.menu_4.setTitle(_translate("MainWindow", "用户设置"))
        self.action.setText(_translate("MainWindow", "年级信息"))
        self.action_2.setText(_translate("MainWindow", "班级信息"))
        self.action_3.setText(_translate("MainWindow", "科目类别"))
        self.action_4.setText(_translate("MainWindow", "考试类别"))
        self.action_6.setText(_translate("MainWindow", "学生管理"))
        self.action_7.setText(_translate("MainWindow", "成绩管理"))
        self.action_8.setText(_translate("MainWindow", "学生信息查询"))
        self.action_9.setText(_translate("MainWindow", "学生成绩查询"))
        self.action_10.setText(_translate("MainWindow", "用户维护"))
        self.action_11.setText(_translate("MainWindow", "退出"))

    # 以下为自编写代码
    def run(self):
        self.modifyStyle()
        self.menu.triggered[QtGui.QAction].connect(self.openMenu1)
        self.menu_2.triggered[QtGui.QAction].connect(self.openMenu2)
        self.menu_3.triggered[QtGui.QAction].connect(self.openMenu3)
        self.menu_4.triggered[QtGui.QAction].connect(self.openMenu4)
    
    # 调整样式
    def modifyStyle(self):
        self.setStyleSheet("background-color: #ceabc7; color: #393562;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/nilu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
    
    def openMenu1(self, act):
        if act.text() == "年级信息":
            self.m = grade.Ui_MainWindow()
            self.setCentralWidget(self.m)
        elif act.text() == "班级信息":
            self.m = classes.Ui_MainWindow()
            self.setCentralWidget(self.m)
        elif act.text() == "科目类别":
            self.m = subject.Ui_MainWindow()
            self.setCentralWidget(self.m)
        elif act.text() == "考试类别":
            self.m = examkinds.Ui_MainWindow()
            self.setCentralWidget(self.m)
    
    def openMenu2(self, act):
        if act.text() == "学生管理":
            self.m = student.Ui_MainWindow()
            self.setCentralWidget(self.m)
        elif act.text() == "成绩管理":
            self.m = result.Ui_MainWindow()
            self.setCentralWidget(self.m)
    
    def openMenu3(self, act):
        if act.text() == "学生信息查询":
            self.m = studentinfo.Ui_MainWindow()
            self.m.show()
        elif act.text() == "学生成绩查询":
            self.m = resultinfo.Ui_MainWindow()
            self.m.show()
    
    def openMenu4(self, act):
        if act.text() == "用户维护":
            self.m = user.Ui_MainWindow()
            self.m.show()
