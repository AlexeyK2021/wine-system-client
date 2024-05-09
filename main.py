import sys
import threading

import websocket
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget

from config import API_IP, API_PORT
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
    websocket.enableTrace(True)
    operator_page.ws = websocket.create_connection(f"ws://{API_IP}:{API_PORT}/api/tanks/ws")
    threading.Thread(target=operator_page.get_data).start()


if __name__ == '__main__':
    login_page.on_operator_enter = on_login
    win.addWidget(login_page)
    win.addWidget(operator_page)

    win.resize(800, 600)
    win.show()
    sys.exit(app.exec())
