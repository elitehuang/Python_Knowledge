#! _*_ coding:utf-8 _*_

import sys

from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QGridLayout


class ClipBoard(QDialog):
    def __init__(self, parent=None):
        super(ClipBoard, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ClipBoard Function Test')
        self.move(0, 0)
        self.setFixedSize(400, 800)
        text_copy = QPushButton('复制文本')
        text_paste = QPushButton('粘贴文本')

        html_copy = QPushButton('复制HTML')
        html_paste = QPushButton('粘贴HTML')

        img_copy = QPushButton('复制图片')
        img_paste = QPushButton('粘贴图片')

        self.text_label = QLabel('默认文本')
        self.img_label = QLabel()
        self.img_label.setPixmap(QPixmap('./images/color.png'))

        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(text_copy, 0, 0)
        layout.addWidget(img_copy, 0, 1)
        layout.addWidget(html_copy, 0, 2)

        layout.addWidget(text_paste, 1, 0)
        layout.addWidget(img_paste, 1, 1)
        layout.addWidget(html_paste, 1, 2)

        layout.addWidget(self.text_label, 2, 0, 1, 1)
        layout.addWidget(self.img_label, 2, 2)

        text_copy.clicked.connect(self.copy_text)
        text_paste.clicked.connect(self.paste_text)
        img_copy.clicked.connect(self.copy_img)
        img_paste.clicked.connect(self.paste_img)
        html_copy.clicked.connect(self.copy_html)
        html_paste.clicked.connect(self.paste_html)

    def copy_text(self):
        print(self.text_label)
        clipboard = QApplication.clipboard()
        clipboard.setText('Hello ClipBoard!!')

    def paste_text(self):
        clipboard = QApplication.clipboard()
        self.text_label.setText(clipboard.text())

    def copy_img(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('./images/color.png'))

    def paste_img(self):
        clipboard = QApplication.clipboard()
        self.img_label.setPixmap(clipboard.pixmap())
        pass

    def copy_html(self):
        print(self)
        mime_data = QMimeData()
        mime_data.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setHtml(mime_data)
        pass

    def paste_html(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        if mime_data.hasHeml():
            self.text_label.setText(mime_data.html())
        else:
            print('Have no html address')

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ClipBoard()
    dialog.show()
    sys.exit(app.exec_())

