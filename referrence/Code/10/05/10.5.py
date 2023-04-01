# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/8  16:31 
# 文件名称   ：10.5.py
# 开发工具   ：PyCharm

import sqlite3
# 连接到SQLite数据库,数据库文件是mrsoft.db
conn = sqlite3.connect('mrsoft.db')
# 创建一个Cursor
cursor = conn.cursor()
# 删除ID为1的用户
cursor.execute('delete from user where id = ?',(1,))
# 获取所有用户信息
cursor.execute('select * from user')
# 记录查询结果
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 提交事务
conn.commit()
# 关闭Connection:
conn.close()