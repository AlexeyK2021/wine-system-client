import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget

from controllers.adminController import AdminPage
from controllers.loginController import LoginPage
from controllers.sandboxController import SandBoxPage

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = QStackedWidget()

    login_page = LoginPage()
    admin_page = AdminPage()
    sandbox = SandBoxPage()
    login_page.on_admin_enter = lambda: win.setCurrentIndex(1)
    login_page.on_sandbox = lambda: win.setCurrentIndex(2)

    win.addWidget(login_page)
    win.addWidget(admin_page)
    win.addWidget(sandbox)

    win.resize(800, 600)
    win.show()
    sys.exit(app.exec())
