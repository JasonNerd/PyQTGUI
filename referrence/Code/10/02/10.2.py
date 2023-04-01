# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/8  16:13 
# 文件名称   ：10.2.py
# 开发工具   ：PyCharm

import sqlite3
# 连接到SQLite数据库，数据库文件是mrsoft.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('mrsoft.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条SQL语句，插入一条记录
cursor.execute('insert into user (id, name) values ("1", "MRSOFT")')
cursor.execute('insert into user (id, name) values ("2", "Andy")')
cursor.execute('insert into user (id, name) values ("3", "明日科技小助手")')
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection
conn.close()
