# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/10  8:45 
# 文件名称   ：11.1.py
# 开发工具   ：PyCharm

file = open('message.txt','w',encoding='utf-8') # 创建或打开文件
# 写入一条信息
file.write("我不是一个伟大的程序员，我只是一个具有良好习惯的优秀程序员。\n")
file.close() # 关闭文件对象

# file = open('message.txt','a',encoding='utf-8') # 以追加方式打开文件
# # 写入一条信息
# file.write("靠代码行数来衡量开发进度，就像是凭重量来衡量飞机制造的进度。\n")
# file.close() # 关闭文件对象
