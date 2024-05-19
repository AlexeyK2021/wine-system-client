import sys
import threading

import websocket
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget, QMainWindow

from config import API_IP, API_PORT
from controllers.loginController import LoginPage
from controllers.operatorController import OperatorPage

app = QtWidgets.QApplication(sys.argv)
win = QStackedWidget()
login_page = LoginPage()
operator_page = OperatorPage()


def on_login(login):
    global win
    operator_page.user_login = login
    operator_page.on_enter()
    win.setCurrentIndex(1)
    websocket.enableTrace(True)
    operator_page.ws = websocket.create_connection(f"ws://{API_IP}:{API_PORT}/api/tanks/ws")
    threading.Thread(target=operator_page.get_data, daemon=True).start()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        login_page.on_operator_enter = on_login
        win.addWidget(login_page)
        win.addWidget(operator_page)

        win.resize(800, 600)
        win.setWindowTitle("Приложение оператора ИУС брожения виноматериалов")
        win.show()

    def closeEvent(self, a0):
        print("Close")


if __name__ == '__main__':
    main = MainWindow()
    sys.exit(app.exec())
