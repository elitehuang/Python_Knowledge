#! _*_ coding:utf-8 _*_

import sys

from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QFormLayout, QLineEdit, QInputDialog, QLabel, QFontDialog, QColorDialog, QTextEdit, QFileDialog

"""
对话框:QDialog

QMessageBox 
QColorDialog
QFileDialog
QFontDialog
QInputDialog

"""


class MessageBox(QMainWindow):
    def __init__(self, parent=None):
        super(MessageBox, self).__init__(parent)
        self.button_first = QPushButton('Show 对话框')
        self.button_second = QPushButton('显示消息对话框')
        self.button_third = QPushButton('显示警告对话框')
        self.button_fourth = QPushButton('显示错误对话框')
        self.button_five = QPushButton('显示提问对话框')
        self.button_six = QPushButton('显示关于对话框')
        self.widget = QWidget(self)
        self.init_ui()
        self.flag = 0

    def init_ui(self):
        self.setWindowTitle('Dialog Function Test')
        self.move(0, 0)
        self.setFixedSize(850, 400)

        self.widget.setGeometry(0, 0, 850, 400)
        layout = QHBoxLayout()
        self.widget.setLayout(layout)

        layout.addStretch(1)
        layout.addWidget(self.button_first)

        layout.addStretch(1)
        layout.addWidget(self.button_second)

        layout.addStretch(1)
        layout.addWidget(self.button_third)

        layout.addStretch(1)
        layout.addWidget(self.button_fourth)

        layout.addStretch(1)
        layout.addWidget(self.button_five)

        layout.addStretch(1)
        layout.addWidget(self.button_six)

        self.button_first.clicked.connect(self.show_dialog)
        self.button_second.clicked.connect(self.show_message_box)
        self.button_third.clicked.connect(self.show_message_box)
        self.button_fourth.clicked.connect(self.show_message_box)
        self.button_five.clicked.connect(self.show_message_box)
        self.button_six.clicked.connect(self.show_message_box)

        self.show()

    def show_dialog(self):
        self.flag = 1
        dialog = QDialog()
        dialog.setWindowTitle('QDialog Test')
        dialog.setGeometry(250, 150, 350, 200)
        button = QPushButton('确定', dialog)
        button.move(50, 50)
        button.clicked.connect(dialog.close)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()
        pass

    def show_message_box(self):
        text = self.sender().text()
        if text == '显示消息对话框':
            # reply 是按键的id
            reply = QMessageBox.information(self, '消息',  '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply)
            pass
        elif text == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            pass
        elif text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            pass
        elif text == '显示提问对话框':
            QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            pass
        elif text == '显示关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')


"""
QInputDialog的静态函数
1、getText()
QInputDialog的getText()函数弹出标准字符串输入对话框，getText()函数原型如下：
QString getText( QWidget * parent, #标准输入对话框的父窗口
const QString & title, #输入对话框的标题名
const QString & label,#标准输入对话框的标签提示
const QString & text = QString(), #标准字符串输入对话框弹出时QLineEdit控件中默认出现的文字
bool * ok = 0, #用于指示标准输入对话框的哪个按钮被触发，若ok为true，则表示用户单击了OK（确定）按钮，若ok为false，则表示用户单击了Cancel（取消）按钮
Qt::WindowFlags flags = 0, #知名标准输入对话框的窗体标识
Qt::InputMethodHints inputMethodHints = Qt::ImhNone ); [static]
2、getItem()
QInputDialog的getItem()函数弹出标准条目选择对话框，getItem()函数原型如下：
QString getItem( QWidget * parent, 标准输入对话框的父窗口
const QString & title, 标准输入对话框的标题名
const QString & label, 标准输入对话框的标签提示
const QStringList & list, 指定标准输入对话框中QComboBox控件显示的可选条目，为一个QStringList对象
int current = 0, 指定标准输入对话框中QComboBox控件显示的可选条目，为一个QStringList对象
bool editable = true, 指定QComboBox控件中显示的文字是否可编辑；
bool * ok = 0, 用于指定标准输入对话框的哪个那妞被触发，若ok为false，则表示用户单击了Cancel（取消）按钮；
Qt::WindowFlags f = 0 ) ; [static]用于指定标准输入对话框的哪个那妞被触发，若ok为false，则表示用户单击了Cancel（取消）按钮；
3、getInteger()
QInputDialog的getInteger()函数弹出标准int类型输入对话框，getInteger()函数原型如下：
int getInteger( QWidget * parent, 父窗口
const QString & title,标题名
const QString & label, 标签提示
int value = 0, 指定标准输入对话框中QSpinBox控件默认显示值
int minValue = -2147483647,
int maxValue = 2147483647, 指定QSpinBoxBox控件的数值范围，最小和最大值
int step = 1, step指定QSpinBox控件的步进值（即步长）
bool * ok = 0,
Qt::WindowFlags f = 0 ) ;

4、getDouble()
QInputDialog的getDouble()函数弹出标准double类型输入对话框，getDouble()函数原型如下：
double getDouble( QWidget * parent,
const QString & title,
const QString & label,标签提示
double value = 0, 指定标准输入对话框中QSpinBox控件默认显示值
double minValue = -2147483647,
double maxValue 2147483647,
int decimals = 1, 指定QSpinBox控件的浮动数的小数点位数
bool * ok = 0,
Qt::WindowFlags f = 0 ) ;
————————————————
版权声明：本文为CSDN博主「忍耐恒_至拙胜至巧」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/panrenlong/article/details/79948261
"""


class InputDialog(QMainWindow):
    def __init__(self, parent=None):
        super(InputDialog, self).__init__(parent)
        self.first_button = QPushButton('获取下拉项')
        self.second_button = QPushButton('获取字符串')
        self.third_button = QPushButton('获取整数值')
        self.fourth_button = QPushButton('获取浮点数')
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit3 = QLineEdit()
        self.line_edit4 = QLineEdit()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('InputDialog Function Test')
        self.move(0, 0)
        self.setFixedSize(600, 200)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QFormLayout()
        widget.setLayout(layout)

        # self.line_edit1.setEnabled(False)                 # 设置输入框不可输入
        # self.line_edit2.setEnabled(False)
        # self.line_edit3.setEnabled(False)

        self.line_edit1.setFocusPolicy(Qt.NoFocus)         # 设置输入框无法获取手标焦点
        self.line_edit2.setFocusPolicy(Qt.NoFocus)
        self.line_edit3.setFocusPolicy(Qt.NoFocus)
        self.line_edit4.setFocusPolicy(Qt.NoFocus)
        layout.addRow(self.first_button, self.line_edit1)
        layout.addRow(self.second_button, self.line_edit2)
        layout.addRow(self.third_button, self.line_edit3)
        layout.addRow(self.fourth_button, self.line_edit4)

        self.first_button.clicked.connect(self.get_item)
        self.second_button.clicked.connect(self.get_string)
        self.third_button.clicked.connect(self.get_int)
        self.fourth_button.clicked.connect(self.get_double)

        self.show()

    def get_int(self):
        num, ok = QInputDialog.getInt(self, '整数', '输入整数')
        if ok and num:
            self.line_edit3.setText(str(num))
        pass

    def get_item(self):
        items = ['C', 'C++', 'JAVA', 'Android', 'Object-C', 'Python']
        item, ok = QInputDialog.getItem(self, '编程语言', '语言列表', items)
        if ok and item:
            self.line_edit1.setText(item)
        pass

    def get_string(self):
        string, ok = QInputDialog.getText(self, '字符串', '输入字符串')
        if ok and string:
            self.line_edit2.setText(string)
        pass

    def get_double(self):
        double, ok = QInputDialog.getDouble(self, '浮点数', '输入浮点数')
        if ok and double:
            self.line_edit2.setText(str(double))
        pass


class FontDialog(QMainWindow):
    def __init__(self, parent=None):
        super(FontDialog, self).__init__(parent)
        self.button = QPushButton('配置字体:')
        self.label = QLabel('展示字体属性的变化')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('FontDialog Function Test')
        self.move(0, 0)
        self.setFixedSize(800, 480)
        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QFormLayout()
        widget.setLayout(layout)

        layout.addRow(self.button)
        layout.addRow(self.label)

        self.button.clicked.connect(self.font_show)

        self.show()

    def font_show(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


class ColorDialog(QMainWindow):
    def __init__(self, parent=None):
        super(ColorDialog, self).__init__(parent)
        self.button = QPushButton('改变字体颜色:')
        self.button1 = QPushButton('改变字体背景')
        self.label = QLabel('展示颜色属性的变化')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ColorDialog Function Test')
        self.move(0, 0)
        self.setFixedSize(800, 480)
        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QFormLayout()
        widget.setLayout(layout)

        layout.addRow(self.button)
        layout.addRow(self.button1)
        layout.addRow(self.label)

        self.button.clicked.connect(self.font_show)
        self.button1.clicked.connect(self.font_background_show)
        self.show()

    def font_show(self):
        color = QColorDialog.getColor()
        palette = QPalette()  # 创建填充对象
        palette.setColor(QPalette.WindowText, color)  # 设置填充对象的颜色
        self.label.setPalette(palette)

    def font_background_show(self):
        color = QColorDialog.getColor()
        palette = QPalette()  # 创建填充对象
        palette.setColor(QPalette.Window, color)  # 设置填充对象的颜色
        self.label.setAutoFillBackground(True)
        self.label.setPalette(palette)


class FileDialog(QMainWindow):
    def __init__(self, parent=None):
        super(FileDialog, self).__init__(parent)
        self.button = QPushButton('加载图片')
        self.button1 = QPushButton('加载文本')
        self.image_label = QLabel()
        self.contents = QTextEdit()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ColorDialog Function Test')
        self.move(0, 0)
        self.setFixedSize(800, 480)
        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QVBoxLayout()
        widget.setLayout(layout)

        layout.addWidget(self.button)
        layout.addWidget(self.image_label)
        layout.addWidget(self.button1)
        layout.addWidget(self.contents)

        self.button.clicked.connect(self.load_image)
        self.button1.clicked.connect(self.load_text)
        self.show()

    def load_image(self):
        image, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '(*.jpg *.png)')
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(QPixmap(image))
        pass

    def load_text(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setFilter(QDir.Files)
        if file_dialog.exec():
            file = file_dialog.selectedFiles()
            with open(file[0], 'r', encoding='utf-8') as f:             # 加encoding是为了防止加载中文内容时出错
                self.contents.setText(f.read())
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileDialog()
    sys.exit(app.exec_())
