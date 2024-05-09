import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget

from controllers.loginController import LoginPage
from controllers.operatorController import OperatorPage

app = QtWidgets.QApplication(sys.argv)
win = QStackedWidget()
login_page = LoginPage()
operator_page = OperatorPage()


def on_login(login):
    global win
    print(login)
    operator_page.user_login = login
    win.setCurrentIndex(1)


if __name__ == '__main__':
    login_page.on_operator_enter = on_login
    win.addWidget(login_page)
    win.addWidget(operator_page)

    win.resize(800, 600)
    win.show()
    sys.exit(app.exec())
