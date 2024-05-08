from PyQt6.QtWidgets import QDialog, QMainWindow

from controllers.apiController import auth
from pages.loginPage import Ui_LoginWindow
from pages.loginPageDialog import Ui_ErrorLoginDialog

import hashlib


def hash_text(text):
    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


class LoginPage(QMainWindow):
    on_operator_enter = None

    def __init__(self):
        super(LoginPage, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.log_in_button.clicked.connect(
            lambda: self.login(self.ui.login.text(), self.ui.passwd.text()))
        self.ui.clear_button.clicked.connect(lambda: self.clear_creds())

        # self.ui.pushButton.clicked.connect(lambda: self.on_sandbox())

    def login(self, login, passwd):
        self.ui.label.adjustSize()
        result = auth(login, hash_text(passwd))
        if result == 1:
            self.on_operator_enter()
        elif result == 0:
            dlg = LoginPageDialog()
            dlg.exec()
        else:
            print("Server unavailable")

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
