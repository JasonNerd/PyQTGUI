# PyQTGUI
基于《Pyhton GUI设计: PyQT5从入门到实践》程序+笔记
该书由明日科技开发，电子版在购买纸质版后在指定阅读器方可阅读
https://www.mingrisoft.com/ebook/595.html

## 安装
```
pip install pyqt6
pip install pyqt6-tools
pyqt6-tools designer
```
```


import sys
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
# C:\Users\mrrai\Desktop\background

```

## Ui 转 Py
```bat
python -m PyQt6.uic.pyuic xxx.ui -o xxx.py
```