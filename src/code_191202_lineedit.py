#! _*_ coding:utf-8 _*_

from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFormLayout, QLineEdit, QPushButton, \
    QVBoxLayout, QTextEdit
import sys


"""
QLineEdit:

基本功能:输入单行的文本

class LineEdit
模式1：回显模式(EchoMode)
包含：Normal、NoEcho、Password、PasswordEchoOnEdit
==============================================================================
class LineEdit2
QLineEdit输入校验器：如限制只能输入整数、浮点数或满足一定条件的字符串

===============================================================================
"""


class LineEdit(QMainWindow):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QLineEdit Function Test')
        self.setGeometry(0, 0, 600, 600)
        widget = QWidget(self)
        widget.setGeometry(0, 0, 600, 300)
        layout = QFormLayout()
        widget.setLayout(layout)
        normal = QLineEdit()
        no_echo = QLineEdit()
        password = QLineEdit()
        password_echo_on_edit = QLineEdit()

        layout.addRow('Normal', normal)
        layout.addRow('NoEcho', no_echo)
        layout.addRow('Password', password)
        layout.addRow('PasswordEchoOnEdit', password_echo_on_edit)

        # setPlacehcolderText()
        normal.setPlaceholderText('Normal')                                     # 设置初始字符串为Normal
        no_echo.setPlaceholderText('NoEcho')
        password.setPlaceholderText('Password')
        password_echo_on_edit.setPlaceholderText('PasswordEchoOnEdit')          # 设置初始字符串为PasswordEchoOnEdit

        normal.setEchoMode(QLineEdit.Normal)
        no_echo.setEchoMode(QLineEdit.NoEcho)
        password.setEchoMode(QLineEdit.Password)                                # 设置显示模式为Password
        password_echo_on_edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


class LineEdit2(QMainWindow):
    def __init__(self, parent=None):
        super(LineEdit2, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QLineEdit Function Test2')
        self.move(0, 0)                             # 设置起始位置
        # self.setGeometry(0, 0, 600, 200)          # 设置窗口起始位置和窗口大小
        self.setFixedSize(600, 200)                 # 设置窗口大小不可变
        widget = QWidget(self)
        widget.setGeometry(0, 0, 600, 200)
        layout = QFormLayout()
        widget.setLayout(layout)

        int_number = QLineEdit()
        float_number = QLineEdit()
        regex_number = QLineEdit()

        layout.addRow('IntNumber', int_number)
        layout.addRow('FloatNumber', float_number)
        layout.addRow('RegexNumber', regex_number)

        int_number.setPlaceholderText('整数')                         # 整数
        float_number.setPlaceholderText('浮点数')
        regex_number.setPlaceholderText('正则限定输入字母和数字')

        # 设置整数校验器对象
        int_var = QIntValidator(widget)
        int_var.setRange(1, 99)

        # 设置浮点数校验器对象
        float_var = QDoubleValidator(widget)
        float_var.setRange(-360, 360)
        float_var.setNotation(QDoubleValidator.StandardNotation)
        float_var.setDecimals(2)                                    # 设置精度为2

        # 设置正则校验器对象
        regex_var = QRegExpValidator(widget)
        regex = QRegExp('[a-zA-Z0-9]+$')
        regex_var.setRegExp(regex)

        # 将QLineEdit 对象绑定校验器对象
        int_number.setValidator(int_var)
        float_number.setValidator(float_var)
        regex_number.setValidator(regex_var)


class LineEdit3(QMainWindow):
    def __init__(self, parent=None):
        super(LineEdit3, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QLineEdit Function Test3')
        self.setFixedSize(600, 300)
        self.move(0, 0)
        widget = QWidget(self)
        widget.setGeometry(0, 0, 600, 300)

        layout = QFormLayout()
        widget.setLayout(layout)

        ip_edit = QLineEdit()
        mac_edit = QLineEdit()
        date_edit = QLineEdit()
        license_edit = QLineEdit()

        ip_edit.setInputMask('000.000.000.000;_')
        mac_edit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        date_edit.setInputMask('0000-00-00')
        license_edit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        layout.addRow('数字掩码', ip_edit)
        layout.addRow('Mac掩码', mac_edit)
        layout.addRow('日期', date_edit)
        layout.addRow('许可证掩码', license_edit)


class LineEdit4(QMainWindow):
    def __init__(self, parent=None):
        super(LineEdit4, self).__init__(parent)
        self.edit = None
        self.text_button = None
        self.html_button = None
        self.text_to_button = None
        self.html_to_button = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QLineEdit Function Test4')
        self.move(0, 0)
        self.setFixedSize(850, 400)

        widget = QWidget(self)
        widget.setGeometry(0, 0, 850, 400)

        layout = QVBoxLayout()
        widget.setLayout(layout)
        self.edit = QTextEdit()
        self.text_button = QPushButton('文本按钮')
        self.html_button = QPushButton('HTML按钮')
        self.text_to_button = QPushButton('获取文本按钮')
        self.html_to_button = QPushButton('获取HTML按钮')

        layout.addWidget(self.edit)
        layout.addWidget(self.text_button)
        layout.addWidget(self.html_button)
        layout.addWidget(self.text_to_button)
        layout.addWidget(self.html_to_button)

        self.text_button.clicked.connect(self.clicked_button_text)
        self.html_button.clicked.connect(self.clicked_button_html)
        self.html_to_button.clicked.connect(self.clicked_button_to_html)
        self.text_to_button.clicked.connect(self.clicked_button_to_text)

    def clicked_button_text(self):
        self.edit.setPlainText('Hello World!!, Python 世界你好吗')
        pass

    def clicked_button_html(self):
        self.edit.setHtml("<font color='blue' size='5'>Hello World!!!</font>")

    def clicked_button_to_html(self):
        print(self.edit.toHtml())

    def clicked_button_to_text(self):
        print(self.edit.toPlainText())


class QLineEditDemo(QMainWindow):
    def __init__(self, parent=None):
        super(QLineEditDemo, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QLineEdit Function Demo')
        self.move(0, 0)
        self.setFixedSize(800, 450)

        widget = QWidget(self)
        widget.setGeometry(0, 0, 800, 450)

        layout = QFormLayout()
        widget.setLayout(layout)

        edit1 = QLineEdit()
        edit2 = QLineEdit()
        edit3 = QLineEdit()
        edit4 = QLineEdit()
        edit6 = QLineEdit('PyQt5 Only Read Text')
        edit5 = QLineEdit()
        validate = QIntValidator()
        edit1.setValidator(validate)
        # validate.setRange(1, 4800)                    # [1,4800]
        edit1.setMaxLength(6)                           # 不超过999999
        edit1.setAlignment(Qt.AlignRight)               # 设置控件靠右边
        edit1.setFont(QFont('Arial', 20))               # 设置字体大小为20

        edit2.setValidator(QDoubleValidator(0.99, 99.99, 5))
        edit3.setInputMask('99_9999_999999;#')
        edit4.textChanged.connect(self.text_changed)
        edit5.setEchoMode(QLineEdit.Password)
        edit6.setReadOnly(True)
        layout.addRow('整数校验', edit1)
        layout.addRow('浮点数校验', edit2)
        layout.addRow('Input校验', edit3)
        layout.addRow('文本变化', edit4)
        layout.addRow('密码', edit5)
        layout.addRow('只读', edit6)

    def text_changed(self, text):
        self.height()
        print('输入文本内容'+text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LineEdit4()
    window.show()
    sys.exit(app.exec_())
    pass
