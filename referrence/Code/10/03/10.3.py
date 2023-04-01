# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/8  16:17 
# 文件名称   ：10.3.py
# 开发工具   ：PyCharm

import sqlite3
# 连接到SQLite数据库,数据库文件是mrsoft.db
conn = sqlite3.connect('mrsoft.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行查询语句
cursor.execute('select * from user')

# 获取查询结果
result1 = cursor.fetchone()
print(result1)

# result2 = cursor.fetchmany(2) # 使用fetchmany方法查询多条数据
# print(result2)

# result3 = cursor.fetchall() # 使用fetchmany方法查询多条数据
# print(result3)

# cursor.execute('select * from user where id > ?',(1,))
# result3 = cursor.fetchall()
# print(result3)

# 关闭游标
cursor.close()
# 关闭Connection
conn.close()
