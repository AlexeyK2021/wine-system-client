from PyQt6 import QtWebSockets, QtNetwork
from PyQt6.QtWidgets import QDialog, QMainWindow

from ApiController import auth, check_admin, API_URL
from pages.loginPage import Ui_LoginWindow
from pages.loginPageDialog import Ui_ErrorLoginDialog

import asyncio
import websockets
import hashlib


def hash_text(text):
    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


class LoginPage(QMainWindow):
    on_admin_enter = None
    on_sandbox = None

    def __init__(self):
        super(LoginPage, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.log_in_button.clicked.connect(
            lambda: self.login(self.ui.login.text(), self.ui.passwd.text()))
        self.ui.clear_button.clicked.connect(lambda: self.clear_creds())

        self.ui.pushButton.clicked.connect(lambda: self.on_sandbox())

    def login(self, login, passwd):
        self.ui.label.adjustSize()
        if auth(login, hash_text(passwd)):
            if check_admin(login):
                self.on_admin_enter()
            else:
                pass  # user page
        else:
            dlg = LoginPageDialog()
            dlg.exec()

    def clear_creds(self):
        self.ui.login.setText("")
        self.ui.passwd.setText("")


class LoginPageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_ErrorLoginDialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
