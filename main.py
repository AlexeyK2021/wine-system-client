import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QMainWindow

from controllers.loginController import LoginPage
from pages.loginPage import Ui_LoginWindow
from pages.loginPageDialog import Ui_ErrorLoginDialog

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = LoginPage()
    win.show()
    sys.exit(app.exec())
