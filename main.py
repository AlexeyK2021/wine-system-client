import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtCore import QDir
from PyQt6.QtWidgets import QStackedWidget

from controllers.loginController import LoginPage
from controllers.operatorController import OperatorPage
from controllers.sandboxController import SandBoxPage

if __name__ == '__main__':
    root = os.path.dirname(os.path.abspath(__file__))
    QDir.addSearchPath('icons', os.path.join(root, '/designs/icons/'))

    app = QtWidgets.QApplication(sys.argv)
    win = QStackedWidget()

    login_page = LoginPage()
    # admin_page = AdminPage()
    operator_page = OperatorPage()
    sandbox = SandBoxPage()
    # login_page.on_admin_enter = lambda: win.setCurrentIndex(1)
    login_page.on_operator_enter = lambda: win.setCurrentIndex(1)
    # login_page.on_sandbox = lambda: win.setCurrentIndex(3)

    win.addWidget(login_page)
    # win.addWidget(admin_page)
    win.addWidget(operator_page)
    # win.addWidget(sandbox)

    win.resize(800, 600)
    win.show()
    sys.exit(app.exec())
