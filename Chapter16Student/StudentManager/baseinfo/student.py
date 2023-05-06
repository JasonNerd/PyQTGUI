import sys
sys.path.append("../")
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QAbstractItemView, QMessageBox
from tools import dboperation

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        self.modifyStyle()  # 调整样式
        self.editLimit()
        self.bindGrade()
        self.bindClass()
        self.query()
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.update)
        self.pushButton_3.clicked.connect(self.delitem)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.query)
        self.comboBox_2.currentIndexChanged.connect(self.bindClass)
        self.tableWidget.itemClicked.connect(self.onItemClicked)
    
    def onItemClicked(self, item):
        self.r = item.row()
        self.stuID = self.tableWidget.item(self.r, 0).text()
        self.lineEdit_2.setText(self.stuID)
        self.stuName = self.tableWidget.item(self.r, 1).text()
        self.lineEdit.setText(self.stuName)
        classID = dboperation.query("select classID from tb_student where stuID=%s", self.stuID)[0][0]
        className = dboperation.query("select className from tb_class where classID=%s", classID)[0][0]
        gradeID = dboperation.query("select gradeID from tb_student where stuID=%s", self.stuID)[0][0]
        gradeName = dboperation.query("select gradeName from tb_grade where gradeID=%s", gradeID)[0][0]
        self.comboBox_2.setCurrentText(gradeName)
        self.comboBox_3.setCurrentText(className)
        age = self.tableWidget.item(self.r, 3).text()
        self.lineEdit_3.setText(age)
        sex = self.tableWidget.item(self.r, 4).text()
        self.comboBox.setCurrentText(sex)
        phone = self.tableWidget.item(self.r, 5).text()
        self.lineEdit_4.setText(phone)
        address = self.tableWidget.item(self.r, 6).text()
        self.lineEdit_5.setText(address)

    def update(self):
        stuID = self.lineEdit_2.text()
        stuName = self.lineEdit.text()
        try:
            if self.stuID == stuID and self.stuName == stuName:
                classID = self.getClassID()
                gradeID = self.getGradeID()
                age = self.lineEdit_3.text()
                sex = self.comboBox.currentText()
                phone = self.lineEdit_4.text()
                address = self.lineEdit_5.text()
                sqlstr = "update tb_student set classID=%s, gradeID=%s, age=%s, sex=%s, phone=%s, address=%s where stuID=%s"
                res = dboperation.exec(sqlstr, (classID, gradeID, age, sex, phone, address, stuID))
                if res > 0:
                    self.query()
            else:
                QMessageBox.information(self, "提示", "学号和姓名无法被更改")
        except:
            QMessageBox.information(self, "提示", "请先选择表格的一行")

    def delitem(self):
        try:
            stuID = self.tableWidget.item(self.r, 0).text()
            res = dboperation.exec("delete from tb_student where stuID=%s", (stuID))
            if res > 0:
                self.query()
        except:
            QMessageBox.information(self, "提示", "请先选择表格的一行")
    
    def query(self):
        self.tableWidget.setRowCount(0) # 清空
        # 注意这里需要依据 年级和班级 进行条件查询
        ## 1. 获取选择的 年级 和 班级
        gradeName = self.comboBox_2.currentText()
        className = self.comboBox_3.currentText()
        ## 2. 条件查询
        baseSql = "select stuID, stuName, CONCAT(gradeName, className), age, sex, phone, address from v_studentinfo "
        if gradeName == "全部":
            if className == "全部":
                result = dboperation.query(baseSql)
            else:
                result = dboperation.query(baseSql+"where className=%s", className)
        else:
            if className == "全部":
                result = dboperation.query(baseSql+"where gradeName=%s", gradeName)
            else:
                result = dboperation.query(baseSql+"where className=%s and gradeName=%s", className, gradeName)
        # 3. 展示查询结果
        row = len(result)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["学号", "姓名", "班级", "年龄", "性别", "电话", "住址"])
        for i in range(row):
            for j in range(7):
                data = QtWidgets.QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, data)
    
    def add(self):
        stuID = self.lineEdit_2.text()
        stuName = self.lineEdit.text()
        classID = self.getClassID()
        gradeID = self.getGradeID()
        age = self.lineEdit_3.text()
        sex = self.comboBox.currentText()
        phone = self.lineEdit_4.text()
        address = self.lineEdit_5.text()
        print(stuID, stuName, classID, gradeID, age, sex, phone, address)
        if classID is None or gradeID is None:
            QMessageBox.information(self, "提示", "请选择年级和班级")
        elif stuID == "" or stuName == "":
            QMessageBox.information(self, "提示", "请输入姓名和学号")
        elif age == "":
            QMessageBox.information(self, "提示", "年龄不可以为空")
        elif phone == "" or address == "":
            QMessageBox.information(self, "提示", "电话或住址不可以为空")
        else:
            sqlstr = "insert into tb_student values(%s, %s, %s, %s, %s, %s, %s, %s)"
            res = dboperation.exec(sqlstr, (stuID, stuName, classID, gradeID, age, sex, phone, address))
            if res > 0:
                self.query()
    
    def getClassID(self):
        className = self.comboBox_3.currentText()
        if className != "" and className != "全部":
            classID = dboperation.query("select classID from tb_class where className=%s", className)
            return classID[0][0]
        return None

    def getGradeID(self):
        gradeName = self.comboBox_2.currentText()
        if gradeName != "" and gradeName != "全部":
            gradeID = dboperation.query("select gradeID from tb_grade where gradeName=%s", gradeName)
            return gradeID[0][0]
        return None

    def modifyStyle(self):
        self.setWindowFlags(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setStyleSheet("background-color: #ceabc7; color: #393562;")
        self.pushButton.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_2.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_3.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_4.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_5.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)   #设置选择整行
        self.tableWidget.setSortingEnabled(True) # 可排序
        self.tableWidget.verticalHeader().setVisible(False) # 隐藏竖排标题

    # 限制输入框
    def editLimit(self):
        regStuID = QtCore.QRegularExpression("^[1-3][0-9]{7}")
        regPhone = QtCore.QRegularExpression("^1[35678]\d{9}$") # ^1[35678]\d{9}$
        regName = QtCore.QRegularExpression("[\u4e00-\u9fa5]{2,6}$")
        regAge = QtCore.QRegularExpression("\d{1,2}")
        self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(regName))      # 姓名
        self.lineEdit_2.setValidator(QtGui.QRegularExpressionValidator(regStuID))   # 学号
        self.lineEdit_3.setValidator(QtGui.QRegularExpressionValidator(regAge))     # 年龄
        self.lineEdit_4.setValidator(QtGui.QRegularExpressionValidator(regPhone))   # 电话
        self.lineEdit.setPlaceholderText("例如: 克拉拉")
        self.lineEdit_2.setPlaceholderText("例如: 22221234")
        self.lineEdit_3.setPlaceholderText("例如: 32")
        self.lineEdit_4.setPlaceholderText("例如: 15131452117")
        self.lineEdit_5.setPlaceholderText("例如: 雅利洛六号母星布诺尼亚市上城区")
        self.comboBox.addItems(["男", "女"])
    
    def bindGrade(self):
        self.comboBox_2.addItem("全部")
        result = dboperation.query("select gradeName from tb_grade")
        self.comboBox_2.addItems([r[0] for r in result])
    
    def bindClass(self):
        gradeID = self.getGradeID()
        self.comboBox_3.clear() 
        self.comboBox_3.addItem("全部")
        if gradeID is not None:
            result = dboperation.query("select className from tb_class where gradeID=%s", gradeID)
        else:
            result = dboperation.query("select className from tb_class")
        self.comboBox_3.addItems([r[0] for r in result])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 8, 60, 32))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 10, 100, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 8, 60, 32))
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(410, 10, 100, 28))
        self.comboBox_3.setObjectName("comboBox_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 50, 550, 320))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 376, 41, 28))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 70, 60, 36))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 120, 60, 36))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 170, 60, 36))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 220, 60, 36))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 376, 100, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 270, 60, 36))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 410, 100, 28))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 410, 41, 28))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 376, 41, 28))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 376, 100, 28))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 410, 41, 28))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 410, 131, 28))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 410, 161, 28))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(390, 410, 41, 28))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 380, 41, 28))
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(430, 380, 68, 28))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "所在年级："))
        self.label_3.setText(_translate("MainWindow", "所在班级："))
        self.label_4.setText(_translate("MainWindow", "姓名："))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.pushButton_4.setText(_translate("MainWindow", "退出"))
        self.pushButton_5.setText(_translate("MainWindow", "刷新"))
        self.label_5.setText(_translate("MainWindow", "学号："))
        self.label_6.setText(_translate("MainWindow", "年龄："))
        self.label_7.setText(_translate("MainWindow", "电话："))
        self.label_8.setText(_translate("MainWindow", "住址："))
        self.label_9.setText(_translate("MainWindow", "性别："))
