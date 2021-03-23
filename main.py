from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import math
from new_gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.run_sim.clicked.connect(self.on_sim_click)
        self.ui.find_angle.clicked.connect(self.on_angle_click)

    def on_sim_click(self):
        pass

    def on_angle_click(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
