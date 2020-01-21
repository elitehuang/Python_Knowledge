#! _*_ coding:utf-8 _*_
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtCore import Qt

"""
QLabel 与伙伴控件的搭配演示

1.对于表格布局
layout.addWidget(name_edit, 0, 1, 1, 2)
name_edit：控件对象
0：x坐标
1：y坐标
1：高度
2：宽度
"""


class FirstWidget(QMainWindow):
    def __init__(self, parent=None):
        super(FirstWidget, self).__init__(parent)
        self.InitUI()

    def InitUI(self):
        # 设置主窗口 QMainWindow 基本属性
        self.setGeometry(0, 0, 300, 300)                    # 设置主窗口的初始位置，宽和高
        self.setWindowTitle('FirstWidget')                  # 设置主窗口的标题
        self.setWindowIcon(QIcon('./images/color.png'))     # 设置主窗口的图标

        # 创建并设置控制窗口的基本属性
        widget = QWidget(self)                              # 在主窗口中创建控制窗口
        widget.setGeometry(30, 50, 250, 220)                  # 设置控制窗口的初始位置，宽和高

        # 创建窗口的布局
        layout = QGridLayout(widget)
        widget.setLayout(layout)                            # 将布局设置到控制窗口

        # 创建应用控件

        name_label = QLabel('&Name', widget)                             # 为控制窗口创建一个QLabel应用控件对象
        name_edit = QLineEdit(widget)
        name_edit.setAlignment(Qt.AlignLeft)
        name_label.setBuddy(name_edit)

        pwd_label = QLabel('&Password', widget)  # 为控制窗口创建一个QLabel应用控件对象
        pwd_edit = QLineEdit(widget)
        pwd_edit.setAlignment(Qt.AlignLeft)
        pwd_label.setBuddy(pwd_edit)

        btn_ok = QPushButton('&OK')
        btn_cancel = QPushButton('&Cancel')

        # label1.setAlignment(Qt.AlignCenter)                 # 将文本内容居中

        layout.addWidget(name_label, 0, 0)                            # 将控件label1添加到垂直布局中
        layout.addWidget(name_edit, 0, 1, 1, 2)
        layout.addWidget(pwd_label, 1, 0)
        layout.addWidget(pwd_edit, 1, 1, 1, 2)
        layout.addWidget(btn_ok, 2, 1)
        layout.addWidget(btn_cancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = FirstWidget()
    widget.show()

    sys.exit(app.exec_())
