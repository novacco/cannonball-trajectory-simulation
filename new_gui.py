# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cannon_plot = cannon_plot(self.centralwidget)
        self.cannon_plot.setGeometry(QtCore.QRect(680, 20, 391, 251))
        self.cannon_plot.setObjectName("cannon_plot")
        self.x_plot = x_plot(self.centralwidget)
        self.x_plot.setGeometry(QtCore.QRect(270, 290, 391, 251))
        self.x_plot.setObjectName("x_plot")
        self.y_plot = y_plot(self.centralwidget)
        self.y_plot.setGeometry(QtCore.QRect(680, 290, 391, 251))
        self.y_plot.setObjectName("y_plot")
        self.run_sim = QtWidgets.QPushButton(self.centralwidget)
        self.run_sim.setGeometry(QtCore.QRect(50, 160, 181, 41))
        self.run_sim.setObjectName("run_sim")
        self.find_angle = QtWidgets.QPushButton(self.centralwidget)
        self.find_angle.setGeometry(QtCore.QRect(50, 210, 181, 41))
        self.find_angle.setObjectName("find_angle")
        self.angle = QtWidgets.QLineEdit(self.centralwidget)
        self.angle.setGeometry(QtCore.QRect(50, 30, 113, 22))
        self.angle.setObjectName("angle")
        self.initial_velocity = QtWidgets.QLineEdit(self.centralwidget)
        self.initial_velocity.setGeometry(QtCore.QRect(50, 60, 113, 22))
        self.initial_velocity.setObjectName("initial_velocity")
        self.mass = QtWidgets.QLineEdit(self.centralwidget)
        self.mass.setGeometry(QtCore.QRect(50, 90, 113, 22))
        self.mass.setObjectName("mass")
        self.air_resistance = QtWidgets.QLineEdit(self.centralwidget)
        self.air_resistance.setGeometry(QtCore.QRect(50, 120, 113, 22))
        self.air_resistance.setObjectName("air_resistance")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 30, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 141, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 90, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 120, 181, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 270, 141, 31))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.run_sim.setText(_translate("MainWindow", "Run"))
        self.find_angle.setText(_translate("MainWindow", "Optimize angle"))
        self.angle.setText(_translate("MainWindow", ""))
        self.initial_velocity.setText(_translate("MainWindow", ""))
        self.mass.setText(_translate("MainWindow", ""))
        self.air_resistance.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "Angle phi"))
        self.label_2.setText(_translate("MainWindow", "Initial velocity"))
        self.label_3.setText(_translate("MainWindow", "Mass "))
        self.label_4.setText(_translate("MainWindow", "Air resistance coefficient"))
        self.label_5.setText(_translate("MainWindow", "Optimal angle: "))


from cannon_plot import cannon_plot
from x_plot import x_plot
from y_plot import y_plot


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())