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
        result = dboperation.query("select gradeName from tb_grade")
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
        result = dboperation.query("select * from tb_subject")
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
        regN412 = QtCore.QRegularExpression("^[A-Z]{2}[0-9]{2}")
        self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(regN412))
        self.lineEdit_2.setValidator(QtGui.QRegularExpressionValidator(regCh24))
        self.lineEdit.setPlaceholderText("例如: QR02")
        self.lineEdit_2.setPlaceholderText("例如: 希尔伯格政法学")
    
    # 添加班级信息
    def add(self):
        # 1. 判断输入是否为空
        subID = self.lineEdit.text()
        subName = self.lineEdit_2.text()
        gradeName = self.comboBox.currentText()
        if subName != "" and subName != "":
            # 2. 判断是否年级信息已存在
            if not self.ifExistGradeInfo(subID, subName):
                res = dboperation.exec("insert into tb_subject values(%s, %s, %s)", (subID, gradeName, subName))
                if res > 0: # 3. 刷新表格
                    self.query()
            else:
                QMessageBox.information(self, "提示", "已添加该条目, 请勿重复输入")
        
    def ifExistGradeInfo(self, subID, subName):
        resid = dboperation.query(f"select * from tb_subject where subID = '{subID}'")
        resna = dboperation.query(f"select * from tb_subject where subName = '{subName}'")
        return len(resid)>0 or len(resna)>0
    
    def getItem(self, item):
        # 获取选中的表格行, 并显示在 line_edit 中
        r = item.row()
        self.subID = self.tableWidget.item(r, 0).text()
        self.gradeName = self.tableWidget.item(r, 1).text()
        self.subName = self.tableWidget.item(r, 2).text()
        self.lineEdit.setText(self.subID)
        self.comboBox.setCurrentText(self.gradeName)
        self.lineEdit_2.setText(self.subName)

    def delitem(self):
        # 依据 id 删除, 注意同时要删除年级下对应的班级信息
        try:
            isok = dboperation.exec("delete from tb_subject where subID= %s", (self.subID,))
            if isok > 0:
                self.query()
        except:
            QMessageBox.information(self, "提示", "请先选择表格的一行")
        
    def upditem(self):
        try:
            subID = self.lineEdit.text()
            subName = self.lineEdit_2.text()
            gradeName = self.comboBox.currentText()
            if self.subID == subID:
                isok = dboperation.exec("update tb_subject set subName=%s, gradeName=%s where subID=%s", (subName, gradeName, self.subID))
                if isok > 0:
                    self.query()
            else:
                QMessageBox.information(self, "提示", "科目编号不可修改")
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
        item.setText(_translate("MainWindow", "科目编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "年级名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "科目名称"))
        self.label.setText(_translate("MainWindow", "科目编号"))
        self.label_2.setText(_translate("MainWindow", "科目名称"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "删除"))
        self.pushButton_3.setText(_translate("MainWindow", "修改"))
        self.label_3.setText(_translate("MainWindow", "年级名称"))
