#! _*_ coding:utf-8 _*_
import sys
from ui_src.first_qt import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    mainWin = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(mainApp.exec_())           # 进入程序主循环， 维持窗口的持续显示
