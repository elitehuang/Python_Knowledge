#! _*_ coding:utf-8 _*_
import os
import sys

# from PyQt5.QtCore import QFileInfo, QFile
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QWidget, QHBoxLayout
from PyQt5.QtGui import QIcon

"""
一、笔记
1、主窗口类型：QMainWindow,QWidget,QDialog

不确定窗口的用途使用Qwidget
对话窗口的基类，没有菜单栏、工具栏、状态栏：QDialog
包含菜单栏、工具栏状态栏：QMianWindow

获得当前文件绝对路径的方法：
1.QT方法
    QFileInfo(__file__).absolutePath()：D:/workspace/PyQT_Test/src 不适用于Windows系统 
    QFile.exists(path)判断路径或文件是否存在
2.
    os.path.abspath(os.path.dirname(__file__)): windows下获得当前句对路径"D:\workspace\PyQT_Test\src\images\color.png
    os.path.exists(file_path) 判断路径或文件是否存在

    # QFileInfo(__file__).absolutePath() + 'images/bitbug_favicon_2.ico' 适用于Mac系统
    # path = os.path.abspath(os.path.dirname(__file__)) + "\\images\\bitbug_favicon_2.ico"
    # print(path, QFile.exists(path))

"""


"""
FirstWindow:实现窗口移动到屏幕中心的操作
"""


class FirstWindow(QMainWindow):
    def __init__(self, parpent=None):
        super(FirstWindow, self).__init__(parpent)
        # 设置主窗口的标题
        self.setWindowTitle('第一个MainWindow程序')

        # self.resize(400, 400)                 # 设置窗口的宽和高
        self.setGeometry(0, 0, 400, 400)        # 设置窗口的初始位置、宽和高
        self.status = self.statusBar()
        self.status.showMessage('只显示10秒时间', 10000)
        pass

    def center(self):           # 使得窗口的位置居于屏幕中心
        screen = QDesktopWidget().screenGeometry()  # 获得屏幕坐标
        size = self.geometry()                      # 获得窗口坐标
        x = (screen.width()-size.width()) / 2
        y = (screen.height()-size.height()) / 2
        time.sleep(3)
        self.move(x, y)


"""
SecondWindow:实现单击按钮窗口关闭
"""


class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setGeometry(0, 0, 600, 600)
        self.setWindowTitle('退出应用程序')
        self.app = None
        # 建议由小往大慢慢的构建整个应用GUI：如下所示，新建Button控件-->
        # 新建布局-->往布局加Button-->新建窗口-->往窗口添加布局
        self.button1 = QPushButton('退出')
        self.button1.clicked.connect(self.click_button)

        layout = QHBoxLayout()          # 新建布局
        layout.addWidget(self.button1)          # 往布局中加按钮控件

        main_frame = QWidget()                   # 新建窗口
        main_frame.setLayout(layout)             # 设置窗口的布局

        self.setCentralWidget(main_frame)        # 设置窗口为应用的中心窗口

    def click_button(self):
        sender = self.sender()  # 获得button对象
        print(sender.text() + '按钮被按下')
        self.app.quit()              # 退出应用程序

    def get_app(self, application):      # 获取App的对象
        self.app = application


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/color.png"))
    # FirstWindow()
    mainWin = SecondWindow()
    mainWin.get_app(app)
    mainWin.show()

    sys.exit(app.exec_())

