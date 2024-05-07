import sys
import threading
import ast

import websocket
from PyQt6.QtWidgets import QMainWindow, QWidget

from controllers.apiController import get_tanks, get_tank_info_ws
from pages.ff_widget import Ui_FF_Widget
from pages.operatorPage import Ui_OperatorWindow
from pages.sf_widget import Ui_SF_Widget
import pages.resources
import rel


class OperatorPage(QMainWindow):
    def __init__(self):
        super(OperatorPage, self).__init__()
        self.ui = Ui_OperatorWindow()
        self.ui.setupUi(self)
        self.ui.input_valve_led.setChecked(True)
        self.tanks = get_tanks()
        for t in self.tanks:
            if t.type_id == 1:
                self.ui.tabWidget.addTab(FastFermentationWidget(), t.name)
            elif t.type_id == 2:
                self.ui.tabWidget.addTab(SlowFermentationWidget(), t.name)

        # self.ui.tabWidget.currentChanged.connect(self.indexChanged)

        websocket.enableTrace(True)
        self.ws = websocket.create_connection(f"ws://127.0.0.1:5000/api/tanks/ws")
        threading.Thread(target=self.get_data).start()

        # self.indexChanged(0)

    #     self.ui.widget = Ui_Form()
    #     self.ui.widget.setupUi(self)
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

    def get_data(self):
        while True:
            index = self.ui.tabWidget.currentIndex()
            try:
                self.ws.send(f"{self.tanks[index].id}")
                data = self.ws.recv()
                print(data)
            except:
                sys.exit()

    # def indexChanged(self, index):
    #     print(f"Tab{index}")
    # self.ws.send_text(f"{self.tanks[index].id}")

    # asyncio.run(self.update_data(self.tanks[index].id))

    # async def update_data(self, tankId):
    # async with websockets.connect(f"ws://localhost:5000/api/tank/{tankId}/ws") as ws:
    #     while True:
    #         msg = ws.recv()
    #         print(msg)

    # def on_message(self, ws, message):
    #     print(message)
    #
    # def on_error(self, ws, error):
    #     print(error)
    #
    # def on_close(self, ws, close_status_code, close_msg):
    #     print("### closed ###")
    #
    # def on_open(self, ws):
    #     print("Opened connection")


class FastFermentationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FF_Widget()
        self.ui.setupUi(self)


class SlowFermentationWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SF_Widget()
        self.ui.setupUi(self)
