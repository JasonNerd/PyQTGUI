# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/8  18:31 
# 文件名称   ：10.8.py
# 开发工具   ：PyCharm

import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "mrsoft",charset="utf8")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 数据列表
data = [("零基础学Python",'Python','79.80','2018-5-20'),
        ("Python从入门到项目实践",'Python','99.80','2019-6-18'),
        ("PyQt5从入门到实践",'Python','69.80','2020-5-21'),
        ("OpenCV从入门到实践",'Python','69.80','2020-5-21'),
        ("Python算法从入门到实践",'Python','69.80','2020-5-21'),
       ]
try:
    # 执行sql语句，插入多条数据
    cursor.executemany("insert into books(name, category, price, publish_time) values (%s,%s,%s,%s)", data)
    # 提交数据
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()
