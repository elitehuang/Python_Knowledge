#! _*_ coding:utf-8 _*_

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSpinBox, QLabel, QVBoxLayout, QHBoxLayout, QFormLayout, \
    QSlider

"""
计数器控件：QSpinBox
"""


class SpinBox(QWidget):
    def __init__(self, parent=None):
        super(SpinBox, self).__init__(parent)
        self.label = QLabel('当前值: 0')

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('SpinBox Function Test')
        self.move(0, 0)
        self.setFixedSize(400, 200)
        self.label.setAlignment(Qt.AlignCenter)

        spin_box = QSpinBox()

        spin_box1 = QSpinBox()
        spin_box1.setValue(10)                              # 设置初始值为10
        spin_box1.setSingleStep(10)                         # 设置每次+或- 10

        layout = QFormLayout()
        self.setLayout(layout)

        layout.addRow(self.label)
        layout.addRow(spin_box)
        layout.addRow(spin_box1)

        spin_box.valueChanged.connect(lambda: self.change_value(spin_box))
        spin_box1.valueChanged.connect(lambda: self.change_value(spin_box1))

    def change_value(self, spin_box):
        value = spin_box.value()
        self.label.setText('当前值: ' + str(value))


"""
滑块控件: QSlider
"""


class Slider(QWidget):
    def __init__(self, parent=None):
        super(Slider, self).__init__(parent)
        self.label = QLabel('当前刻度为: 10')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Slider Function Test')
        self.move(0, 0)
        self.setFixedSize(400, 200)
        self.label.setAlignment(Qt.AlignCenter)

        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(10)                                   # 设置最小值
        slider.setMaximum(100)                                  # 设置最大值
        slider.setSingleStep(2)                                 # 设置步长
        slider.setTickPosition(QSlider.TicksBelow)              # 设置刻度的方向
        slider.setTickInterval(5)                               # 设置刻度间隔

        layout = QFormLayout()
        self.setLayout(layout)
        layout.addRow(self.label)
        layout.addRow(slider)

        slider.valueChanged.connect(lambda: self.value_change(slider))

    def value_change(self, slider):
        value = slider.value()
        self.label.setText('当前刻度为:' + str(value))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Slider()
    widget.show()
    sys.exit(app.exec_())
