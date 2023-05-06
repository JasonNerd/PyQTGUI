import sys
from PyQt6 import QtWidgets
from login import login

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.run()
    MainWindow.show()
    sys.exit(app.exec())

# 千月木
# 2P02Y3Q502T
# setStyleSheet("background-color: #ceabc7; color: #393562;")   # 背景肉粉紫色, 前景深黛墨紫色
# setStyleSheet("background-color: #510279; color: #f6f2ff;")   # 背景纯墨紫色, 前景淡白粉紫色

# A001
# 本科二年级