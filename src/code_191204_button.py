#! _*_ coding:utf-8 _*_

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QRadioButton, QHBoxLayout, \
    QCheckBox, QComboBox, QLabel, QFormLayout

"""
QT中Button的种类：
QPushButton
QAbstractButton
QToolButton
QRadioButton
QCheckBox
"""


class PushButtonTest(QMainWindow):
    def __init__(self, parent=None):
        super(PushButtonTest, self).__init__(parent)
        self.init_ui()
        self.flag = 0

    def init_ui(self):
        self.setWindowTitle('PushButton Function Test')
        self.move(0, 0)
        self.setFixedSize(845, 400)
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        first_button = QPushButton('FirstButton')
        first_button.setCheckable(True)                                 # True:按下有被选中的效果
        first_button.toggle()

        second_button = QPushButton('SecondButton')
        second_button.setIcon(QIcon(QPixmap('./images/color')))         # 在按键前面加图标

        third_button = QPushButton('ThirdButton')
        third_button.setEnabled(False)                                  # 设置按钮不可用

        fourth_button = QPushButton('&FourthButton')                    # 添加热键，Alt + F 表示按下效果
        fourth_button.setDefault(True)                                  # 设置默认的按键, 按回车时直接单击默认按键

        layout.addWidget(first_button)
        layout.addWidget(second_button)
        layout.addWidget(third_button)
        layout.addWidget(fourth_button)

        first_button.clicked.connect(lambda: self.click_button(first_button))
        first_button.clicked.connect(lambda: self.button_status(first_button))
        second_button.clicked.connect(lambda: self.click_button(second_button))
        fourth_button.clicked.connect(lambda: self.click_button(fourth_button))

    def click_button(self, button):                                             # 按键已经被单击
        self.flag = 1
        print('单击的按钮是' + button.text())

    def button_status(self, button):                                            # 检查按键是否被按下
        self.flag = 1
        if button.isChecked():
            print(button.text() + '被选中。。。')
        else:
            print(button.text() + '没有被选中。。。')


"""
单选按钮控件:QRadioButton
"""


class RadioButtonTest(QMainWindow):
    def __init__(self, parent=None):
        super(RadioButtonTest, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('RadioButton Function Test')
        self.move(0, 0)
        self.setFixedSize(845, 400)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        widget.setLayout(layout)

        first_button = QRadioButton('FirstButton')
        first_button.setChecked(True)
        first_button.toggled.connect(self.toggled_button)
        second_button = QRadioButton('SecondButton')
        second_button.toggled.connect(self.toggled_button)

        layout.addWidget(first_button)
        layout.addWidget(second_button)

    def toggled_button(self):
        button = self.sender()
        if button.isChecked():
            print(button.text() + '被选中')
        else:
            print(button.text() + '取消选中')
    """
    # This function is equal to function toggled_button
    def button_status(self):
        button = self.sender()
        if button.text() == 'FirstButton':
            if button.isChecked():
                print(button.text() + '被选中')
            else:
                print(button.text() + '取消选中')
        elif button.text() == 'SecondButton':
            if button.isChecked():
                print(button.text() + '被选中')
            else:
                print(button.text() + '取消选中')
    """


"""
复选框控件: QCheckBox
"""


class CheckBoxButton(QWidget):
    def __init__(self, parent=None):
        super(CheckBoxButton, self).__init__(parent)
        self.second_button = QCheckBox('SecondCheckBox')
        self.first_button = QCheckBox('FirstCheckBox')
        self.third_button = QCheckBox('ThirdCheckBox')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('CheckBox Button Function Test')
        self.move(0, 0)
        self.setFixedSize(840, 400)
        layout = QHBoxLayout()
        self.setLayout(layout)
        self.first_button.setChecked(True)
        self.first_button.toggled.connect(lambda: self.toggled_button(self.first_button))

        self.second_button.setChecked(False)
        self.second_button.toggled.connect(lambda: self.toggled_button(self.second_button))

        self.third_button.setTristate(True)                         # 设置控件有半选属性
        self.third_button.setCheckState(Qt.PartiallyChecked)        # 设置控件状态为半选状态
        self.third_button.toggled.connect(lambda: self.toggled_button(self.third_button))

        layout.addWidget(self.first_button)
        layout.addWidget(self.second_button)
        layout.addWidget(self.third_button)

    def toggled_button(self, check_button):
        first_status = self.first_button.text() + '的状态是：' + str(self.first_button.isChecked())
        second_status = self.second_button.text() + '的状态是：' + str(self.second_button.isChecked())
        # 0.1.2:空.半选.全选
        third_status = self.third_button.text() + '的状态是：' + str(self.third_button.checkState())
        change_status = check_button.text() + '的状态改变为：' + str(check_button.isChecked())
        print(first_status + '\n' + second_status + '\n' + third_status + '\n' + change_status)


"""
下拉列表控件：QComboBox
"""
fruits = ['西瓜', '葡萄', '冬枣', '橙子', '雪梨']
sooner = ['刘德华', '张学友', '黎明', '郭富城', '张杰', '邓紫棋', '韩雪', '张含韵', '黎姿', '卖麻批']
code_language = ['C', 'C++', 'JAVA', 'Android', 'Object-C', 'Python']
girls = ['黄蓉', '余伟燕', '丁宁', '王晓娟', '朱晓花', '丁秀萍', '邵晨曦', '陶颖', '宋沁园']


class ComBoBox(QWidget):
    def __init__(self, parent=None):
        super(ComBoBox, self).__init__(parent)
        self.label_text = QLabel('显示选择的下拉框内容')
        self.first_button = QComboBox()
        self.second_button = QComboBox()
        self.third_button = QComboBox()
        self.fourth_button = QComboBox()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QComBoBox Function Test')
        self.move(0, 0)
        self.setFixedSize(250, 100)

        layout = QFormLayout()
        layout.addRow(self.label_text)
        self.label_text.setAlignment(Qt.AlignCenter)
        layout.addRow(self.first_button, self.second_button)
        layout.addRow(self.third_button, self.fourth_button)

        self.first_button.addItems(fruits)
        self.first_button.addItem('哈密瓜')
        self.second_button.addItems(sooner)
        self.third_button.addItems(code_language)
        self.fourth_button.addItems(girls)

        # self.first_button.currentIndexChanged.connect(lambda: self.index_change(self.first_button))
        # self.second_button.currentIndexChanged.connect(lambda: self.index_change(self.second_button))
        # self.third_button.currentIndexChanged.connect(lambda: self.index_change(self.third_button))

        # self.first_button.currentIndexChanged.connect(lambda: self.show_change(self.first_button))
        # self.second_button.currentIndexChanged.connect(lambda: self.show_change(self.second_button))
        # self.third_button.currentIndexChanged.connect(lambda: self.show_change(self.third_button))
        # self.fourth_button.currentIndexChanged.connect(lambda: self.show_change(self.fourth_button))

        self.first_button.currentIndexChanged.connect(lambda: self.show_all_count(self.first_button))
        self.second_button.currentIndexChanged.connect(lambda: self.show_all_count(self.second_button))
        self.third_button.currentIndexChanged.connect(lambda: self.show_all_count(self.third_button))
        self.fourth_button.currentIndexChanged.connect(lambda: self.show_all_count(self.fourth_button))

        self.setLayout(layout)

    # def index_change(self, button):
    #     print('选中的下拉选项为：' + button.itemText(button.currentIndex()))

    def show_change(self, change):
        text = change.itemText(change.currentIndex())
        print('选中的下拉选项为：' + text)
        self.label_text.setText(text)
        self.label_text.adjustSize()

    def show_all_count(self, combobox):

        count = combobox.count()
        current_text = combobox.currentText()
        self.label_text.setText(current_text)
        self.label_text.adjustSize()
        for index in range(count):
            text = combobox.itemText(index)
            print('Item' + str(index) + '=' + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PushButtonTest()
    window.show()
    sys.exit(app.exec_())

