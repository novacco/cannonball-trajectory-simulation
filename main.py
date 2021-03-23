from new_gui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
from simulation import simulation, find_optimal_angle, max_values


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.run_sim.clicked.connect(self.on_sim_click)
        self.ui.find_angle.clicked.connect(self.on_angle_click)
        self.listX = []
        self.listY = []
        self.listT = []

    def on_sim_click(self):
        angle = float(self.ui.angle.text())
        air_resistance = float(self.ui.air_resistance.text())
        initial_velocity = float(self.ui.initial_velocity.text())
        mass = float(self.ui.mass.text())

        sim = simulation(angle, mass, air_resistance, initial_velocity)
        self.listX = sim[0]
        self.listY = sim[1]
        self.listT = sim[2]
        self.update_graph()

        maxes = max_values(angle, mass, air_resistance, initial_velocity)
        self.ui.label_6.setText(f"Flight Time: {round(maxes[2],2)}s")
        self.ui.label_7.setText(f"Max Range: {round(maxes[3],2)}m")
        self.ui.label_8.setText(f"Max Height: {round(maxes[0],2)}m in {round(maxes[1],2)}s")

    def on_angle_click(self):
        air_resistance = float(self.ui.air_resistance.text())
        initial_velocity = float(self.ui.initial_velocity.text())
        mass = float(self.ui.mass.text())

        angle = find_optimal_angle(mass, air_resistance, initial_velocity)
        self.ui.label_5.setText(f"Optimal angle: {angle}")

    def update_graph(self):
        self.ui.cannon_plot.canvas.axes.clear()
        self.ui.cannon_plot.canvas.axes.plot(self.listX, self.listY)
        self.ui.cannon_plot.canvas.axes.legend("H", loc='upper right')
        self.ui.cannon_plot.canvas.axes.set_title('Ball flight trajectory')
        self.ui.cannon_plot.canvas.draw()

        self.ui.x_plot.canvas.axes.clear()
        self.ui.x_plot.canvas.axes.plot(self.listT, self.listX)
        self.ui.x_plot.canvas.axes.legend("R", loc='upper right')
        self.ui.x_plot.canvas.axes.set_title('Range in time')
        self.ui.x_plot.canvas.draw()

        self.ui.y_plot.canvas.axes.clear()
        self.ui.y_plot.canvas.axes.plot(self.listT, self.listY)
        self.ui.y_plot.canvas.axes.legend("H", loc='upper right')
        self.ui.y_plot.canvas.axes.set_title('Height in time')
        self.ui.y_plot.canvas.draw()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
