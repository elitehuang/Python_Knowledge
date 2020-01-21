# _*_ coding:utf-8 _*_

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPainter
from PyQt5.QtWidgets import QApplication, QWidget


class FillRect(QWidget):
    def __init___(self, parent=None):
        super(FillRect, self).__init__(parent)

    def paintEvent(self, event):
        self.setWindowTitle('QBrush Function Test')
        self.move(0, 0)
        self.setFixedSize(860, 480)
        paint = QPainter()
        paint.begin(self)
        brush = QBrush(Qt.SolidPattern)
        paint.setBrush(brush)
        paint.drawRect(10, 15, 90, 60)

        brush = QBrush(Qt.Dense1Pattern)
        paint.setBrush(brush)
        paint.drawRect(135, 15, 90, 60)

        brush = QBrush(Qt.Dense2Pattern)
        paint.setBrush(brush)
        paint.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.Dense3Pattern)
        paint.setBrush(brush)
        paint.drawRect(375, 15, 90, 60)

        brush = QBrush(Qt.Dense4Pattern)
        paint.setBrush(brush)
        paint.drawRect(500, 15, 90, 60)

        brush = QBrush(Qt.Dense5Pattern)
        paint.setBrush(brush)
        paint.drawRect(625, 15, 90, 60)

        brush = QBrush(Qt.Dense6Pattern)
        paint.setBrush(brush)
        paint.drawRect(10, 115, 90, 60)

        brush = QBrush(Qt.Dense7Pattern)
        paint.setBrush(brush)
        paint.drawRect(135, 115, 90, 60)

        brush = QBrush(Qt.BDiagPattern)
        paint.setBrush(brush)
        paint.drawRect(250, 115, 90, 60)

        brush = QBrush(Qt.CrossPattern)
        paint.setBrush(brush)
        paint.drawRect(375, 115, 90, 60)

        brush = QBrush(Qt.DiagCrossPattern)
        paint.setBrush(brush)
        paint.drawRect(500, 115, 90, 60)

        brush = QBrush(Qt.ConicalGradientPattern)
        paint.setBrush(brush)
        paint.drawRect(625, 115, 90, 60)

        brush = QBrush(Qt.FDiagPattern)
        paint.setBrush(brush)
        paint.drawRect(10, 205, 90, 60)

        brush = QBrush(Qt.HorPattern)
        paint.setBrush(brush)
        paint.drawRect(135, 205, 90, 60)

        brush = QBrush(Qt.LinearGradientPattern)
        paint.setBrush(brush)
        paint.drawRect(250, 205, 90, 60)

        brush = QBrush(Qt.RadialGradientPattern)
        paint.setBrush(brush)
        paint.drawRect(375, 205, 90, 60)

        brush = QBrush(Qt.TexturePattern)
        paint.setBrush(brush)
        paint.drawRect(500, 205, 90, 60)

        brush = QBrush(Qt.VerPattern)
        paint.setBrush(brush)
        paint.drawRect(625, 205, 90, 60)

        paint.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = FillRect()
    win.show()
    sys.exit(app.exec_())
