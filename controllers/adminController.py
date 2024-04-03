from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QDialog

from pages.addTankDialog import Ui_AddTankDialog
from pages.adminPage import Ui_AdminWindow


class AdminPage(QMainWindow):
    def __init__(self):
        super(AdminPage, self).__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)

        self.ui.add_tank.triggered.connect(self.new_tank)
        self.ui.add_sensor.triggered.connect(self.new_sensor)
        self.ui.add_actuator.triggered.connect(self.new_actuator)
        self.ui.add_param.triggered.connect(self.new_param)
        self.ui.add_user.triggered.connect(self.new_user)
        # self.ebb1 = QtGui.QAction(parent=self)
        # self.ebb1.setText("ЕББ1")
        # self.ebb1.setObjectName("ebb1")
        #
        # self.ui.tanks.addAction(self.ebb1)

    def new_tank(self):
        dlg = AddTankDialog()
        dlg.exec()
        print("add tank")
        pass

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
        self.ui.buttonBox.accepted.connect(lambda: print(self.ui.tank_name.text()))
