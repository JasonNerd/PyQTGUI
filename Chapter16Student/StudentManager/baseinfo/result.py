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
        self.bindCboxes()   # 设置下拉列表
        self.editLimit()
        self.comboBox_2.currentTextChanged.connect(self.bindClass)      # 变换 年级 时需要调整 班级列表
        self.comboBox_2.currentTextChanged.connect(self.bindSubject)    # 变换 年级 时需要调整 科目列表
        self.comboBox_2.currentTextChanged.connect(self.bindStudent)    # 变换 年级 时需要调整 学生列表
        self.comboBox_3.currentTextChanged.connect(self.bindStudent)    # 变换 班级 时需要调整 学生列表
        self.query()
        self.pushButton.clicked.connect(self.addItem)       # 按钮信号槽
        self.pushButton_2.clicked.connect(self.updItem)
        self.pushButton_3.clicked.connect(self.delItem)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.query)
        self.tableWidget.itemClicked.connect(self.onTableItemClicked)

    def modifyStyle(self):
        self.setWindowFlags(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setStyleSheet("background-color: #ceabc7; color: #393562;")
        self.pushButton.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_2.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_3.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_4.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_5.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSortingEnabled(True) # 可排序
        self.tableWidget.verticalHeader().setVisible(False) # 隐藏竖排标题
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)   #设置选择整行
    def editLimit(self):
        # 接受两位数以内的整数或小数，若为小数，只接受 xx.5
        # 以0开头 或者 以 1-9后接一个数字 开头, 后面可选接上 .5
        regResult = QtCore.QRegularExpression("^(0|([1-9]\d{1}))(\.5)?$") 
        self.lineEdit.setValidator(QtGui.QRegularExpressionValidator(regResult))      # 分数
        self.lineEdit.setPlaceholderText("例如: 59.5")

    def bindCboxes(self):
        self.bindCbox(self.comboBox, "select kindName from tb_examkinds")      # 考试类别: 独立
        self.bindCbox(self.comboBox_2, "select gradeName from tb_grade")       # 所在年级: 独立
        self.bindClass()      # 班级: 附属于年级, comboBox_3
        self.bindSubject()    # 学科: 附属于年级, comboBox_5
        self.bindStudent()    # 姓名: 附属于年级和班级, comboBox_4
    def bindClass(self):
        gradeName = self.comboBox_2.currentText()
        gradeID = self.getGradeID(gradeName)
        if gradeID is not None:
            self.bindCbox(self.comboBox_3, f"select className from tb_class where gradeID='{gradeID}'")
        else:
            self.bindCbox(self.comboBox_3, "select className from tb_class")
    def bindSubject(self):
        gradeName = self.comboBox_2.currentText()
        if gradeName != "" and gradeName != "全部":
            self.bindCbox(self.comboBox_5, f"select subName from tb_subject where gradeName='{gradeName}'")
        else:
            self.bindCbox(self.comboBox_5, "select subName from tb_subject")
    def bindStudent(self):
        gradeName = self.comboBox_2.currentText()
        className = self.comboBox_3.currentText()
        gradeID = self.getGradeID(gradeName)
        classID = self.getClassID(className)
        if gradeID is None: 
            self.bindCbox(self.comboBox_4, "select stuName from tb_student") # 全部年级的学生
        elif classID is None:
            self.bindCbox(self.comboBox_4, f"select stuName from tb_student where gradeID='{gradeID}'")
        else:
            self.bindCbox(self.comboBox_4, f"select stuName from tb_student where gradeID='{gradeID}' and classID='{classID}'")
    def bindCbox(self, cbox, sqlstr):
        cbox.clear()
        cbox.addItem("全部")
        result = dboperation.query(sqlstr)
        cbox.addItems([r[0] for r in result])
        cbox.setCurrentIndex(0)
    def getGradeID(self, gradeName):
        if gradeName != "" and gradeName != "全部":
            gradeID = dboperation.query("select gradeID from tb_grade where gradeName=%s", gradeName)
            return gradeID[0][0]
        return None
    def getClassID(self, className):
        if className != "" and className != "全部":
            classID = dboperation.query("select classID from tb_class where className=%s", className)
            return classID[0][0]
        return None
    def getStuID(self, stuName):
        if stuName != "" and stuName != "全部":
            stuID = dboperation.query("select stuID from tb_student where stuName=%s", stuName)
            return stuID[0][0]
        return None
    def getKindID(self, kindName):
        if kindName != "" and kindName != "全部":
            kindID = dboperation.query("select kindID from tb_examkinds where kindName=%s", kindName)
            return kindID[0][0]
        return None
    def getSubID(self, subName):
        if subName != "" and subName != "全部":
            subID = dboperation.query("select subID from tb_subject where subName=%s", subName)
            return subID[0][0]
        return None
    
    
    def query(self):
        self.tableWidget.setRowCount(0) # 清空
        # 注意这里需要依据 三个下拉列表 进行条件查询
        ## 1. 获取三个下拉列表值
        kindName = self.comboBox.currentText()
        gradeName = self.comboBox_2.currentText()
        className = self.comboBox_3.currentText()
        ## 2. 条件查询
        baseSql = "select ID, stuID, stuName, CONCAT(gradeName, className), subName, kindName, result from v_resultinfo "
        if kindName == "全部":
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
        else:
            if gradeName == "全部":
                if className == "全部":
                    result = dboperation.query(baseSql+"where kindName=%s", kindName)
                else:
                    result = dboperation.query(baseSql+"where className=%s and kindName=%s", className, kindName)
            else:
                if className == "全部":
                    result = dboperation.query(baseSql+"where gradeName=%s and kindName=%s", gradeName, kindName)
                else:
                    result = dboperation.query(baseSql+"where className=%s and gradeName=%s and kindName=%s", className, gradeName, kindName)
        # 3. 展示查询结果
        row = len(result)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["编号", "学生编号", "学生姓名", "班级", "科目", "考试类型", "成绩"])
        for i in range(row):
            for j in range(7):
                data = QtWidgets.QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i, j, data)
    
    def ifExistRes(self, stuID, kindID, subID):
        res = dboperation.query("select * from tb_result where stuID=%s and kindID=%s and subID=%s", stuID, kindID, subID)
        return len(res) > 0
    def addItem(self):
        stuName = self.comboBox_4.currentText()
        stuID = self.getStuID(stuName)
        kindName = self.comboBox.currentText()
        kindID = self.getKindID(kindName)
        subName = self.comboBox_5.currentText()
        subID = self.getSubID(subName)
        result = self.lineEdit.text()
        if stuID is None:
            QMessageBox.information(self, "提示", "请选择学生")
        elif kindID is None:
            QMessageBox.information(self, "提示", "请选择考试类型")
        elif subID is None:
            QMessageBox.information(self, "提示", "请选择科目")
        elif result == "":
            QMessageBox.information(self, "提示", "请输入成绩")
        elif self.ifExistRes(stuID, kindID, subID):
            QMessageBox.information(self, "提示", "条目重复")
        else:
            sqlstr = "insert into tb_result(stuID, kindID, subID, result) values(%s, %s, %s, %s)"
            res = dboperation.exec(sqlstr, (stuID, kindID, subID, result))
            if res > 0:
                self.query()
    
    def onTableItemClicked(self, item):
        self.r = item.row()
        self.itemID = self.tableWidget.item(self.r, 0).text()
        self.stuID = self.tableWidget.item(self.r, 1).text()
        self.gradeName = dboperation.query("select gradeName from v_studentinfo where stuID=%s", self.stuID)[0][0]
        self.className = dboperation.query("select className from v_studentinfo where stuID=%s", self.stuID)[0][0]
        self.stuName = self.tableWidget.item(self.r, 2).text()
        self.subName = self.tableWidget.item(self.r, 4).text()
        self.kindName = self.tableWidget.item(self.r, 5).text()
        self.result = self.tableWidget.item(self.r, 6).text()
        self.comboBox.setCurrentText(self.kindName)
        self.comboBox_2.setCurrentText(self.gradeName)
        self.comboBox_3.setCurrentText(self.className)
        self.comboBox_4.setCurrentText(self.stuName)
        self.comboBox_5.setCurrentText(self.subName)
        self.lineEdit.setText(self.result)

    def updItem(self):
        try:
            stuName = self.comboBox_4.currentText()
            stuID = self.getStuID(stuName)
            kindName = self.comboBox.currentText()
            kindID = self.getKindID(kindName)
            subName = self.comboBox_5.currentText()
            subID = self.getSubID(subName)
            result = self.lineEdit.text()
            sqlstr = "update tb_result set stuID=%s, kindID=%s, subID=%s, result=%s"
            res = dboperation.exec(sqlstr, (stuID, kindID, subID, result))
            if res > 0:
                self.query()
        except:
            QMessageBox.information(self, "提示", "请选择表格的一行")

    def delItem(self):
        try:
            sqlstr = "delete from tb_result where ID=%s"
            res = dboperation.exec(sqlstr, (self.itemID))
        except:
            QMessageBox.information(self, "提示", "请选择表格的一行")

    def modifyStyle(self):
        self.setWindowFlags(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setStyleSheet("background-color: #ceabc7; color: #393562;")
        self.pushButton.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_2.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_3.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_4.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.pushButton_5.setStyleSheet("background-color: #f6f2ff; color: #510279;")
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)   #设置选择整行
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 60, 32))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 32, 100, 28))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 60, 32))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 32, 100, 28))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 30, 60, 32))
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(500, 32, 100, 28))
        self.comboBox_3.setObjectName("comboBox_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 80, 550, 320))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 410, 60, 28))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 410, 60, 28))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 80, 84, 44))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 149, 84, 44))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 218, 84, 44))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 287, 84, 44))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 410, 60, 28))
        self.label_9.setObjectName("label_9")
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(90, 410, 100, 28))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(250, 410, 191, 28))
        self.comboBox_5.setObjectName("comboBox_5")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 410, 100, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 356, 84, 44))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "考试类别："))
        self.label_2.setText(_translate("MainWindow", "所在年级："))
        self.label_3.setText(_translate("MainWindow", "所在班级："))
        self.label_4.setText(_translate("MainWindow", "姓名："))
        self.label_6.setText(_translate("MainWindow", "科目："))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.pushButton_4.setText(_translate("MainWindow", "退出"))
        self.label_9.setText(_translate("MainWindow", "分数："))
        self.pushButton_5.setText(_translate("MainWindow", "更新"))
