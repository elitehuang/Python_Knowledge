#! _*_ coding:utf-8 _*_

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QFormLayout, QLabel, QLineEdit

"""
让控件支持拖拽动作A--》B：

B.setAcceptDrops(True)

B的两个动作：
1.dragEnterEvent(A 拖拽到B区域时触发) 
2.dropEvent(A 在B区域放下触发)


"""


class ComboBoxDrop(QComboBox):
    def __init__(self, parent=None):
        super(ComboBoxDrop, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        print(event)
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.addItem(event.mimeData().text())


class DragDropDemo(QWidget):
    def __init__(self, parent=None):
        super(DragDropDemo, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.move(0, 0)
        self.setWindowTitle('Drag Function Test')
        self.setFixedSize(860, 480)

        layout = QFormLayout()
        self.setLayout(layout)

        label = QLabel('将左边编辑框中的文本拖拽到右边')
        layout.addRow(label)
        combo = ComboBoxDrop()
        edit = QLineEdit()
        edit.setDragEnabled(True)                   # 设置编辑框可拖拽
        layout.addRow(edit, combo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DragDropDemo()
    win.show()
    sys.exit(app.exec_())


