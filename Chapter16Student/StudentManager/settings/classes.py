import sys
sys.path.append("../")
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QAbstractItemView, QMessageBox
from tools import dboperation

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.modifyStyle()  # 调整样式
        self.editLimit()    # 限制输入框
        self.query()        # 显示班级信息列表
        self.setCombobox()
        self.pushButton.clicked.connect(self.add)
        self.tableWidget.itemClicked.connect(self.getItem)
        self.pushButton_2.clicked.connect(self.delitem)
        self.pushButton_3.clicked.connect(self.upditem)
    
    def setCombobox(self):
        result = dboperation.query("select gradeID from tb_grade")
        self.comboBox.addItems([r[0] for r in result])
        self.comboBox.setCurrentIndex(0)

    def modifyStyle(self):
        self.setWindowFlags(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setStyleSheet("background-color: #ceabc7; color: #393562;")
        self.pushButton.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_2.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_3.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)   #设置选择整行
    
    # 查询所有年级信息并展示
    def query(self):
        self.tableWidget.setRowCount(0) # 清空
        result = dboperation.query("select * from tb_class")
        row = len(result)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(3)
        for i in range(row):
            for j in range(3):
                data = QtWidgets.QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, data)
    # 限制输入框
    def editLimit(self):
        regCh24 = QtCore.QRegularExpression("[\u4e00-\u9fa5]{3,10}$")
        regN412 = QtCore.QRegularExpression("^[a-z][0-9]{3}")
        self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(regN412))
        self.lineEdit_2.setValidator(QtGui.QRegularExpressionValidator(regCh24))
        self.lineEdit.setPlaceholderText("例如: a001")
        self.lineEdit_2.setPlaceholderText("例如: 希儿量子班")
    
    # 添加班级信息
    def add(self):
        # 1. 判断输入是否为空
        classID = self.lineEdit.text()
        className = self.lineEdit_2.text()
        gradeID = self.comboBox.currentText()
        if className != "" and className != "":
            # 2. 判断是否年级信息已存在
            if not self.ifExistGradeInfo(classID, className):
                res = dboperation.exec("insert into tb_class values(%s, %s, %s)", (classID, gradeID, className))
                if res > 0: # 3. 刷新表格
                    self.query()
            else:
                QMessageBox.information(self, "提示", "已添加该条目, 请勿重复输入")
        
    def ifExistGradeInfo(self, classID, className):
        resid = dboperation.query(f"select * from tb_class where classID = '{classID}'")
        resna = dboperation.query(f"select * from tb_class where className = '{className}'")
        return len(resid)>0 and len(resna)>0
    
    def getItem(self, item):
        # 获取选中的表格行, 并显示在 line_edit 中
        r = item.row()
        self.rid = self.tableWidget.item(r, 0).text()
        self.rname = self.tableWidget.item(r, 2).text()
        self.lineEdit.setText(self.rid)
        self.lineEdit_2.setText(self.rname)

    def delitem(self):
        # 依据 id 删除, 注意同时要删除年级下对应的班级信息
        try:
            # self.rid 可能不存在, 也即未选中
            isok = dboperation.exec("delete from tb_class where classID= %s", (self.rid,))
            if isok > 0:
                self.query()
        except:
            QMessageBox.information(self, "提示", "请先选择表格的一行")
        
    def upditem(self):
        # 更新班级信息
        try:
            # self.rid 可能不存在, 也即未选中
            uname = self.lineEdit_2.text()
            ugrade = self.comboBox.currentText()
            if uname == self.rname:
                pass
            else:
                isok = dboperation.exec("update tb_class set className=%s, gradeID=%s where classID=%s", (uname, ugrade, self.rid))
                if isok > 0:
                    self.query()
        except:
            QMessageBox.information(self, "提示", "请先选择表格的一行")
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(19, 10, 672, 311))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.CustomDashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(224)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 330, 54, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 330, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 330, 54, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 330, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 360, 75, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 360, 75, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 360, 75, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(560, 330, 113, 20))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 330, 54, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "班级编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "所在年级编号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "班级名称"))
        self.label.setText(_translate("MainWindow", "班级编号"))
        self.label_2.setText(_translate("MainWindow", "班级名称"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.pushButton_3.setText(_translate("MainWindow", "修改"))
        self.label_3.setText(_translate("MainWindow", "所在年级"))
