import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget

from controllers.loginController import LoginPage
from controllers.operatorController import OperatorPage

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = QStackedWidget()

    login_page = LoginPage()
    operator_page = OperatorPage()
    login_page.on_operator_enter = lambda: win.setCurrentIndex(1)

    win.addWidget(login_page)
    win.addWidget(operator_page)

    win.resize(800, 600)
    win.show()
    app.exec()
    sys.exit()
