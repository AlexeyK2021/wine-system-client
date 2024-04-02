from PyQt6.QtWidgets import QDialog, QMainWindow

from ApiController import auth, check_admin
from pages.loginPage import Ui_LoginWindow
from pages.loginPageDialog import Ui_ErrorLoginDialog


class LoginPage(QMainWindow):
    on_admin_enter = None

    def __init__(self):
        super(LoginPage, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.log_in_button.clicked.connect(
            lambda: self.login(self.ui.login.text(), self.ui.passwd.text()))
        self.ui.clear_button.clicked.connect(lambda: self.clear_creds())

    def login(self, login, passwd):
        self.ui.label.adjustSize()
        if auth(login, passwd):
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
