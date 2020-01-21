#! _*_ coding:utf-8 _*_

import sys
from ui_src.main_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class Deal_MainUI(Ui_MainWindow):
    def __init__(self, parent):
        self.ui = Ui_MainWindow.__init__(parent)
    pass

    def get_all_control(self):

        pass

    def deal_button_event(self, event):

        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Deal_MainUI(None)
    ui.setupUi(window)

    window.show()

    sys.exit(app.exec_())

