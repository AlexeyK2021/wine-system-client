from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QDialog, QPushButton

from pages.addTankDialog import Ui_AddTankDialog
from pages.adminPage import Ui_AdminWindow
from pages.editTankDialog import Ui_EditTankDialog


class AdminPage(QMainWindow):
    def __init__(self):
        super(AdminPage, self).__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)

        # self.ui.add_tank.triggered.connect(self.new_tank)
        # self.ui.add_sensor.triggered.connect(self.new_sensor)
        # self.ui.add_actuator.triggered.connect(self.new_actuator)
        # self.ui.add_param.triggered.connect(self.new_param)
        # self.ui.add_user.triggered.connect(self.new_user)
        # self.ebb1 = QtGui.QAction(parent=self)
        # self.ebb1.setText("ЕББ1")
        # self.ebb1.setObjectName("ebb1")
        #
        # self.ui.tanks.addAction(self.ebb1)

        # for name in tanks:
        #     self.ui.
        self.tanks = list()
        self.tanks.append("Hello")
        self.tanks.append("World")
        self.ui.tanks_list.addItems(self.tanks)

        self.ui.add_tank.clicked.connect(
            lambda: self.add_tank_dialog(
                lambda name, mqtt: self.add_tank(name, mqtt)
            )
        )
        self.ui.del_tank.clicked.connect(
            lambda: self.del_tank(
                self.ui.tanks_list.selectedIndexes()[0].row()
            )
        )
        self.ui.edit_tank.clicked.connect(
            lambda: self.edit_tank_dialog(
                self.tanks[self.ui.tanks_list.selectedIndexes()[0].row()], "MQTT NA",
                lambda old_name, new_name, new_mqtt: self.edit_tank(old_name, new_name, new_mqtt)
            )
        )

    def add_tank(self, name, mqtt):
        self.tanks.append(str(name))
        self.update_list()

    def del_tank(self, id):
        self.tanks.pop(id)
        self.update_list()

    def edit_tank(self, old_name, new_name, new_mqtt):
        self.tanks[self.tanks.index(str(old_name))] = str(new_name)
        self.update_list()

    def add_tank_dialog(self, on_save):
        dlg = AddTankDialog()
        dlg.ui.buttonBox.accepted.connect(lambda: on_save(dlg.ui.tank_name.text(), dlg.ui.mqtt_topic.text()))
        dlg.exec()

    def edit_tank_dialog(self, name, mqtt, on_save):
        dlg = EditTankDialog()
        dlg.ui.tank_name.setText(name)
        dlg.ui.mqtt_topic.setText(mqtt)
        dlg.ui.buttonBox.accepted.connect(
            lambda: on_save(
                name,
                dlg.ui.tank_name.text(),
                dlg.ui.mqtt_topic.text()
            )
        )
        dlg.exec()

    def update_list(self):
        self.ui.tanks_list.clear()
        self.ui.tanks_list.addItems(self.tanks)


def new_sensor(self):
    print("add sensor")
    pass


def new_actuator(self):
    print("add actuator")
    pass


def new_param(self):
    print("add param")
    pass


def new_user(self):
    print("add user")
    pass


class AddTankDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_AddTankDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)


class EditTankDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_EditTankDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
