# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/10  13:07 
# 文件名称   ：11.2.py
# 开发工具   ：PyCharm

with open('message.txt','r',encoding='utf-8') as file: # 以读取模式打开文件
    print("===========读取前5个字符===============")

    # # 从指定位置读取指定个数的字符
    # file.seek(9)  # 移动文件指针到新的位置
    # string = file.read(5)  # 读取5个字符

    print(file.read(5))  # 读取前5个字符
    print("\n===========读取第一行数据===============")
    print(file.readline())  # 输出第一行数据
    print("\n===========读取所有数据===============")
    print(file.readlines())# 读取全部数据