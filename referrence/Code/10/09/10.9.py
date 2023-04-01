# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/8  19:39 
# 文件名称   ：10.9.py
# 开发工具   ：PyCharm

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtGui,QtCore

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI() # 初始化窗口

    def initUI(self):
        self.setWindowTitle("使用表格显示数据库中的数据")
        self.resize(400,180) # 设置窗口大小
        vhayout=QHBoxLayout() # 创建水平布局
        table=QTableWidget() # 创建表格
        import pymysql
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "root", "mrsoft",charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        cursor.execute("select * from books") # 执行SQL语句
        result=cursor.fetchall() # 获取所有记录
        row = cursor.rowcount  # 取得记录个数，用于设置表格的行数
        vol = len(result[0])  # 取得字段数，用于设置表格的列数
        cursor.close() # 关闭游标
        db.close() # 关闭连接
        table.setRowCount(row) # 设置表格行数
        table.setColumnCount(vol) # 设置表格列数
        # 设置表格的标题名称
        table.setHorizontalHeaderLabels(['ID','图书名称','图书分类','图书价格','出版时间'])
        for i in range(row): # 遍历行
            for j in range(vol): # 遍历列

                # if j==4: # 如果是第4列，则显示图片
                #     data = QTableWidgetItem(QtGui.QIcon("date.png"),str(result[i][j]))  # 同时插入文字和图片
                # else:
                #     data = QTableWidgetItem(str(result[i][j]))  # 直接插入文字

                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                table.setItem(i, j, data)
                # data.setForeground(QtGui.QBrush(QtGui.QColor("green"))) # 设置单元格文本颜色
                # data.setBackground(QtGui.QBrush(QtGui.QColor("yellow"))) # 设置单元格背景颜色

                # # 将第2列设置为ComboBox下拉列表
                # if j==2: # 判断是否为第2列
                #     comobox = QComboBox() # 创建一个下拉列表对象
                #     # 为下拉列表设置数据源
                #     comobox.addItems(['Python', 'Java', 'C语言', '.NET'])
                #     comobox.setCurrentIndex(0) # 默认选中第一项
                #     table.setCellWidget(i,2,comobox) # 将创建的下拉列表显示在表格中
                # else:
                #     data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                #     table.setItem(i, j, data)

                # # 合并第3列的第1——5行
                # # （0表示第1行，2表示第3列，5表示跨越5行<1、2、3、4、5行>，1表示跨越1列）
                # table.setSpan(0, 2, 5, 1)
                # # 合并第4列的第3——5行
                # # （2表示第3行，3表示第4列，3表示跨越3行<3、4、5行>，1表示跨越1列）
                # table.setSpan(2, 3, 3, 1)
                # # 合并第5列的第3——5行
                # # （2表示第3行，4表示第5列，3表示跨越3行<3、4、5行>，1表示跨越1列）
                # table.setSpan(2, 4, 3, 1)

        table.resizeColumnsToContents() # 使列宽跟随内容改变
        table.resizeRowsToContents() # 使行高度跟随内容改变
        table.setAlternatingRowColors(True)  # 使表格颜色交错显示
        vhayout.addWidget(table) # 将表格添加到水平布局中

        # table.horizontalHeader().setStretchLastSection(True) # 设置最后一列自动填充容器
        # table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # 设置表格的自动伸缩模式
        # table.verticalHeader().setVisible(False) # 隐藏垂直标题
        # table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # 禁止编辑单元格
        # table.sortItems(4,QtCore.Qt.DescendingOrder) # 设置降序排序

        self.setLayout(vhayout) # 设置当前窗口的布局方式

if __name__=='__main__':
    import sys
    app=QApplication(sys.argv) # 创建窗口程序
    demo=Demo() # 创建窗口类对象
    demo.show() # 显示窗口
    sys.exit(app.exec_())