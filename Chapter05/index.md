---
title: "Chapter05 PyQT常用控件-文本控件"
date: 2023-04-20T17:16:59+08:00
draft: false
tags: ["PyQT"]
categories: ["学习笔记"]
twemoji: true
lightgallery: true
---

![](./image/2023-04-20-17-18-50.png)
![](./image/2023-04-20-17-19-02.png)
![](./image/2023-04-20-17-22-41.png)

## 文本控件
### Label
```py
self.TextLabel = QtWidgets.QLabel(parent=self.centralwidget)
font = QtGui.QFont()
font.setFamily("华文仿宋")
font.setPointSize(12)
self.TextLabel.setFont(font)
self.TextLabel.setStyleSheet("background-color: rgb(120, 24, 255);")
self.TextLabel.setWordWrap(True)
```
### LineEdit
![](./image/2023-04-21-11-38-52.png)
![](./image/2023-04-21-11-39-05.png)

### TextEdit
![](./image/2023-04-21-14-55-01.png)

### SpinBox
![](./image/2023-04-21-15-23-57.png)
![](./image/2023-04-21-15-24-32.png)
![](./image/2023-04-21-15-24-43.png)

### LCDNumber
![](./image/2023-04-21-15-25-07.png)
![](./image/2023-04-21-15-25-18.png)

## Buttons
### PushButton
![](./image/2023-04-21-15-25-59.png)
![](./image/2023-04-21-15-26-14.png)

### ToolButton
![](./image/2023-04-24-09-36-34.png)

### CommandLinkButton
![](./image/2023-04-24-09-44-26.png)
![](./image/2023-04-24-09-44-39.png)

### Radio Button
![](./image/2023-04-24-09-47-05.png)

### ComboBox, FontComboBox, ListWidget
![](./image/2023-04-24-15-52-53.png)
![](./image/2023-04-24-15-53-29.png)
![](./image/2023-04-24-15-53-50.png)

### TabWidget
![](./image/2023-04-24-16-59-49.png)
![](./image/2023-04-24-17-00-04.png)
![](./image/2023-04-24-17-00-56.png)

