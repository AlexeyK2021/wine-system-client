from random import randint

import numpy as np
from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QWidget
from pyqtgraph import QtWidgets, QtGui
import pyqtgraph as pg
from controllers.apiController import get_current_temperature
from pages import resources
from pages.operatorPage import Ui_OperatorWindow
from pages.testform import Ui_Form


class OperatorPage(QMainWindow):
    def __init__(self):
        super(OperatorPage, self).__init__()
        self.ui = Ui_OperatorWindow()
        self.ui.setupUi(self)
        self.ui.input_valve_led.setChecked(True)

        # self.ui.widget = Ui_Form()
        # self.ui.widget.setupUi(self)

    #     self.ui.tank_selector.addItems({"hello": "World", "1234": 5})
    #     self.x = 0
    #     self.y = [get_current_temperature(1)]
    #
    #     pen = pg.mkPen(color=(255, 0, 0))
    #     self.data_line = self.ui.graph.plot(y=self.y, pen="g")
    #     self.ui.graph.showGrid(x=True, y=True)
    #     self.ui.graph.setBackground('w')
    #
    #     # self.ui.graph.setBackground(self.palette().color(QtGui.QPalette.window))
    #     # self.data_line.QPen('b', width=1)
    #     # self.ui.graph.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30, 32, 34, 32, 33, 31, 29, 32, 35, 45])
    #     self.timer = QtCore.QTimer()
    #     self.timer.setInterval(1000)
    #     self.timer.timeout.connect(self.update_plot_data)
    #     self.timer.start()
    #
    # def update_plot_data(self):
    #     # self.x = self.x[1:]  # Remove the first y element.
    #     # self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
    #     #
    #     # self.y = self.y[1:]  # Remove the first
    #     # self.y.append(randint(0, 100))  # Add a new random value.
    #     #
    #     # self.data_line.setData(self.x, self.y)  # Update the data.
    #
    #     self.y[:-1] = self.y[1:]  # shift data in the array one sample left
    #     self.y[-1] = get_current_temperature(1)
    #     self.x += 1
    #     self.data_line.setData(y=self.y)
    #     self.data_line.setPos(self.x, 0)


class FastFermentationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
