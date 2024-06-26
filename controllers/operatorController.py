import json
import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow, QWidget, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton
from websocket import WebSocketConnectionClosedException

from controllers.apiController import get_tanks, activate_tank, emergency_stop
from pages.ff_widget import Ui_FF_Widget
from pages.operatorPage import Ui_OperatorWindow
from pages.sf_widget import Ui_SF_Widget
import pages.resources


class OperatorPage(QMainWindow):
    user_login = None
    ws = None

    def __init__(self):
        super(OperatorPage, self).__init__()
        self.ui = Ui_OperatorWindow()
        self.ui.setupUi(self)

        self.ui.stop.clicked.connect(
            # lambda: emergency_stop(
            #     self.tanks[self.ui.tabWidget.currentIndex()]['id'],
            #     self.user_login
            # )
            lambda: ApproveAction(
                "Подтвердите остановку",
                lambda: emergency_stop(
                    self.tanks[self.ui.tabWidget.currentIndex()]['id'],
                    self.user_login
                )
            ).exec()
        )
        self.ui.activate.clicked.connect(
            lambda: ApproveAction(
                "Подтвердите инициализацию",
                lambda: activate_tank(
                    self.tanks[self.ui.tabWidget.currentIndex()]['id'],
                    self.user_login
                )
            ).exec()
        )

    def get_data(self):
        while True:
            index = self.ui.tabWidget.currentIndex()
            tank_id = self.tanks[index]['id']
            try:
                self.ws.send(f"{tank_id}")
                text = self.ws.recv()
                data = json.loads(text)
                if data["tank_id"] == tank_id:
                    self.update_ui(data)
            except WebSocketConnectionClosedException:
                print("Error websocket connection")
                sys.exit()

    def update_ui(self, data):
        self.ui.activate.setEnabled(data["process_id"] == 9)

        self.ui.curr_process.setText(data["process_name"])
        ui = self.tabs[self.ui.tabWidget.currentIndex()].ui

        ui.temp_lcd.display(data["params"]["Temperature"])
        ui.pres_lcd.display(data["params"]["Pressure"])
        self.set_lamp(ui.high_level_led, data["params"]["High_Level_Sensor"])
        self.set_lamp(ui.low_level_led, data["params"]["Low_Level_Sensor"])

        self.set_lamp(ui.input_valve_led, data["actuators"]["Input_Valve"])
        self.set_lamp(ui.he_input_led, data["actuators"]["HE_Input_Valve"])
        self.set_lamp(ui.he_output_led, data["actuators"]["HE_Output_Valve"])
        self.set_lamp(ui.he_pump_led, data["actuators"]["HE_Pump"])
        self.set_lamp(ui.co2_valve_led, data["actuators"]["CO2_Valve"])
        self.set_lamp(ui.output_pump_led, data["actuators"]["Output_Pump"])
        self.set_lamp(ui.output_valve_led, data["actuators"]["Output_Valve"])

    def set_lamp(self, lamp, value):
        if value == 1:
            lamp.setPixmap(QtGui.QPixmap(":/Mnemoscheme/icons/greenlamp.svg"))
        elif value == 0:
            lamp.setPixmap(QtGui.QPixmap(":/Mnemoscheme/icons/redlamp.svg"))

    def on_enter(self):
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


class ApproveAction(QDialog):
    def __init__(self, text, approve, parent=None):
        super().__init__(parent)
        self.approve = approve
        self.setWindowTitle("Подтверждение действия")

        self.layout = QVBoxLayout()
        message = QLabel(text)

        approve_btn = QPushButton()
        approve_btn.setText("Подтверждаю")
        approve_btn.clicked.connect(self.accepted)

        self.layout.addWidget(message)
        self.layout.addWidget(approve_btn)
        self.setLayout(self.layout)

    def accepted(self):
        self.approve()
        self.close()
