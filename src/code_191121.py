#! _*_ coding:utf-8 _*_
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QDialog, QLabel, QToolTip, QVBoxLayout, \
    QHBoxLayout
from PyQt5.QtGui import QPalette


"""
获得宽和高
width()
height()
geometry().width()
geometry().height()
frameGeometry().width()
frameGeometry().height()

获得坐标
x()
y()
geometry().x()
geometry().y()
frameGeometry().x()
frameGeometry().y()

QLabel控件：

setAlignment()：设置文本对齐方式

setIndent()：设置文本缩进

text()：获取文本内容

setBuddy()：设置伙伴关系

setText()：设置文本内容

selectedText()：返回所选择的字符

"""
class FirstWidget(QMainWindow):
    def __init__(self, parent=None):
        super(FirstWidget, self).__init__(parent)
        self.widget = None
        self.dialog = None
        self.create_win()

    def create_win(self):
        self.widget = QWidget()
        self.widget.setGeometry(0, 0, 400, 400)
        self.widget.setWindowTitle(u'获得窗口在屏幕中的坐标！！')
        button = QPushButton(self.widget)  # 新建Button对象，并添加的widget中
        button.setText('获取')
        button.move(50, 50)
        button.clicked.connect(self.on_click)
        self.widget.show()

    def on_click(self):
        height = self.widget.height()
        width = self.widget.width()
        x = self.widget.x()
        y = self.widget.y()
        self.dialog = QDialog()
        self.dialog.setWindowTitle('提示!!')
        self.dialog.setGeometry(50, 50, 200, 100)
        QLabel('窗口的坐标是:\n x=%s y=%s\n width=%s height=%s' % (x, y, width, height), self.dialog)
        self.dialog.show()


"""
QToolTop 的使用演示

"""


class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setGeometry(400, 400, 400, 400)
        self.setToolTip('鼠标光标是在Widget工作区域')
        button = QPushButton('按钮')
        button.move(200, 200)
        layout = QHBoxLayout()
        layout.addWidget(button)
        widget = QWidget()
        widget.setLayout(layout)
        QToolTip.setFont(QFont('SansSerif', 12))
        button.setToolTip('鼠标光标是在Button工作区域！！')
        self.setCentralWidget(widget)


"""
QLabel 的多种使用情况演示
"""


class ThirdWidow(QMainWindow):
    def __init__(self, parent=None):
        super(ThirdWidow, self).__init__(parent)
        self.Init_UI()
        # self.show()

    def Init_UI(self):
        # Main Win 主窗口
        self.setWindowTitle('Label演示')
        self.setGeometry(0, 0, 500, 500)
        # control Win 控制窗口
        widget = QWidget(self)
        widget.setGeometry(0, 0, 500, 500)

        # 文本1
        label = QLabel(widget)
        label2 = QLabel(widget)
        label3 = QLabel(widget)
        label4 = QLabel(widget)

        label.setText("<font color=yellow>这是一个文本控件.</font>")
        label.setAutoFillBackground(True)               # 设置文本背景可填充
        label.setGeometry(0, 0, 500, 30)
        palette = QPalette()                            # 创建填充对象
        palette.setColor(QPalette.Window, Qt.blue)      # 设置填充对象的颜色
        label.setPalette(palette)                       # 将填充对象填充到文字背景上
        label.setAlignment(Qt.AlignCenter)              # 设置文本居于父组件中间

        # 文本2
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")
        label2.linkHovered.connect(self.link_hovered)
        # 文本3
        label3.setToolTip('这是一张图片')
        label3.setPixmap(QPixmap('./images/five_image.jpg'))
        label3.setAlignment(Qt.AlignCenter)


        label4.setText("<a href='http://www.baidu.com/'>单击进入百度首页</a>")
        label4.setOpenExternalLinks(True)                # 设置超链接单击跳转
        label4.setToolTip('这是一个超链接')
        label4.setAlignment(Qt.AlignRight)
        label4.linkActivated.connect(self.link_activied)

        layout = QVBoxLayout()                          # 创建布局对象
        layout.addWidget(label)                         # 将文本控件添加到布局
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        widget.setLayout(layout)                          # 将布局添加到窗口上

    def link_hovered(self):
        print('鼠标光标移动事件信号')

    def link_activied(self):
        print('鼠标光标单击事件信号')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # first = FirstWidget()
    # first.create_win()
    # second = SecondWindow()
    third = ThirdWidow()
    third.show()
    sys.exit(app.exec_())
