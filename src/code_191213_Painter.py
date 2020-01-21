#! _*_ coding:utf-8 _*_
import math
import sys

from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QPolygon, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

"""
painter = QPainter()
painter.begin(self)
painter.DrawTest()
printer.end()

必须在printEvent()方法中绘制各种元素

"""


class PainterText(QWidget):
    def __init__(self, parent=None):
        super(PainterText, self).__init__(parent)
        self.text = '第一个Painter Demo'
        self.setWindowTitle('PainterText Function Test')
        self.setGeometry(0, 0, 400, 180)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QColor(150, 43, 5))
        painter.setFont(QFont('SimSun', 25))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)

        painter.end()


class PaintSinLine(QWidget):
    def __init__(self, parent=None):
        super(PaintSinLine, self).__init__(parent)
        self.setWindowTitle('PaintSinLine Function Test')
        self.setGeometry(0, 0, 480, 180)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()
        for i in range(100000):
            x = 100*(-1 + 2*i/100000) + size.width()/2.0
            y = -50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2
            p = 120*(-1 + 2*i/100000) + size.width()/2.0
            q = 60*(-1 + 2*i/100000) + size.height()/2.0
            painter.drawPoint(x, y)
            painter.drawPoint(p, size.height()/2.0)
            painter.drawPoint(size.width()/2.0, q)

        painter.end()


class PaintLine(QWidget):
    def __init__(self, parent=None):
        super(PaintLine, self).__init__(parent)
        self.setWindowTitle('PaintLine Function Test')
        self.setGeometry(0, 0, 480, 180)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        pen = QPen(Qt.blue, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 100, 250, 100)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 10, 5, 8])
        painter.setPen(pen)
        painter.drawLine(20, 140, 250, 140)

        painter.end()


class PaintGraphical(QWidget):
    def __init__(self, parent=None):
        super(PaintGraphical, self).__init__(parent)
        self.setWindowTitle('PaintGraphical Function Test')
        self.setGeometry(0, 0, 900, 800)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        painter.setPen(Qt.blue)
        # 绘制弧：参数表示 x、y坐标和宽高
        rect = QRect(0, 10, 200, 200)
        # 单位alen:等于1/16度
        painter.drawArc(rect, 0, 50*16)

        # 通过弧长绘制圆
        painter.setPen(Qt.red)
        painter.drawArc(220, 10, 100, 100, 0, 360 * 16)

        # 绘制带弦的弧
        painter.drawChord(10, 120, 100, 100, 13, 130*16)

        # 绘制扇形
        painter.drawPie(10, 240, 100, 100, 13, 130 * 16)

        # 绘制五边形
        point1 = QPoint(140, 380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)

        painter.drawPolygon(QPolygon([point1, point2, point3, point4, point5]))

        # 绘制图形
        image = QImage('./images/color.png')
        painter.drawImage(QRect(400, 400, image.width(), image.height()), image)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PaintGraphical()

    window.show()
    sys.exit(app.exec_())
