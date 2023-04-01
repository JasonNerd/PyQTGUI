# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/8  16:09 
# 文件名称   ：10.1.py
# 开发工具   ：PyCharm

import sqlite3
# 连接到SQLite数据库
# 数据库文件是mrsoft.db，如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mrsoft.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
cursor.execute('create  table  user (id int(10)  primary key, name varchar(20))')
# 关闭游标
cursor.close()
# 关闭Connection
conn.close()
