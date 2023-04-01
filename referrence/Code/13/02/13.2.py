# -*- coding: utf-8 -*-
# 开发团队   ：明日科技
# 开发人员   ：小科
# 开发时间   ：2020/4/15  10:53 
# 文件名称   ：13.2.py
# 开发工具   ：PyCharm

from PyQt5.QtCore import QThread # 导入线程模块

class Thread(QThread): # 创建线程类
    def __init__(self):
        super(Thread,self).__init__()
    # 重写run()方法
    def run(self):
        num=0 # 定义一个变量，用来叠加输出
        while True: # 定义无限循环
            num=num+1 # 变量叠加
            print(num) # 输出变量
            Thread.sleep(1) # 使线程休眠1秒
            if num==10: # 如果数字到10
                Thread.quit() # 退出线程

# 添加主方法
if  __name__=="__main__":
    # 导入模块
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv) # 创建应用对象
    thread =Thread() # 创建线程对象
    thread.start() # 启动线程
    sys.exit(app.exec_()) # 关闭时退出程序
