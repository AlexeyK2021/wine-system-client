import json
import threading
import websocket

from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow, QWidget
from websocket import WebSocketConnectionClosedException
from config import API_IP, API_PORT
from controllers.apiController import get_tanks
from pages.ff_widget import Ui_FF_Widget
from pages.operatorPage import Ui_OperatorWindow
from pages.sf_widget import Ui_SF_Widget


class OperatorPage(QMainWindow):
    def __init__(self):
        super(OperatorPage, self).__init__()
        self.ui = Ui_OperatorWindow()
        self.ui.setupUi(self)
        self.tanks = get_tanks()
        self.tabs = []
        for t in self.tanks:
            if t["type_id"] == 1:
                ff = FastFermentationWidget()
                self.ui.tabWidget.addTab(ff, t["name"])
                self.tabs.append(ff)
            elif t["type_id"] == 2:
                sf = SlowFermentationWidget()
                self.ui.tabWidget.addTab(sf, t["name"])
                self.tabs.append(sf)

        # self.ui.tabWidget.currentChanged.connect(self.indexChanged)

        websocket.enableTrace(True)
        self.ws = websocket.create_connection(f"ws://{API_IP}:{API_PORT}/api/tanks/ws")
        threading.Thread(target=self.get_data).start()

    def get_data(self):
        while True:
            index = self.ui.tabWidget.currentIndex()
            try:
                self.ws.send(f"{self.tanks[index]['id']}")
                text = self.ws.recv()
                data = json.loads(text)
                print(data)
                self.update_ui(data)
            except WebSocketConnectionClosedException:
                print("Error websocket connection")

    def update_ui(self, data):
        ui = self.tabs[self.ui.tabWidget.currentIndex()].ui

        ui.temp_lcd.display(data["params"]["Temperature"])
        ui.pres_lcd.display(data["params"]["Pressure"])

        self.set_lamp(ui.input_valve_led, data["actuators"]["Input_Valve"])
        self.set_lamp(ui.he_input_led, data["actuators"]["HE_Input_Valve"])
        self.set_lamp(ui.he_output_led, data["actuators"]["HE_Output_Valve"])
        self.set_lamp(ui.he_pump_led, data["actuators"]["HE_Pump"])
        self.set_lamp(ui.co2_valve_led, data["actuators"]["CO2_Valve"])
        self.set_lamp(ui.output_pump_led, data["actuators"]["Output_Pump"])
        self.set_lamp(ui.output_valve_led, data["actuators"]["Output_Valve"])
        pass

    def set_lamp(self, lamp, value):
        if value:
            lamp.setPixmap(QtGui.QPixmap(":/Mnemoscheme/icons/greenlamp.svg"))
        else:
            lamp.setPixmap(QtGui.QPixmap(":/Mnemoscheme/icons/redlamp.svg"))


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
