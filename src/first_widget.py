#! _*_ coding:utf-8 _*_

"""
QWidget:
设置窗口的大小：resize()
设置窗口的位置：move(x,y)
获得窗口左上角坐标：pos()
获得窗口的大小：size()
获得窗口的高/宽度：height(),width()
单独设置窗口的高/宽度: setFixedWidth(height)，setFixedWidth(width)
使宽高固定，即窗口大小固定不可变：，setFixedSize(w,h)/，setFixedWidth(size)
同时设置窗口的位置和大小：setGeometry(x,y,w,h)
获得窗口的大小和位置：frameGeometry()
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建应用的实例
    w = QWidget()                   # 创建一个窗口
    w.resize(400, 400)              # 设置一个窗口的尺寸
    w.move(0, 0)                    # 窗口位置
    w.setWindowTitle('第一个基于PyQt5的桌面程序')     # 设置窗口标题
    w.show()                        # 显示窗口
    sys.exit(app.exec_())           # 进入程序主循环， 维持窗口的持续显示
