import sys
from PyQt6 import QtWidgets
from controllers.loginController import LoginPage

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = LoginPage()
    win.show()
    sys.exit(app.exec())

