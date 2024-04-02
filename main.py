import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QStackedWidget

from controllers.adminController import AdminPage
from controllers.loginController import LoginPage

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = QStackedWidget()

    login_page = LoginPage()
    login_page.on_admin_enter = lambda: win.setCurrentIndex(1)

    admin_page = AdminPage()

    win.addWidget(login_page)
    win.addWidget(admin_page)

    win.resize(800, 600)
    win.show()
    sys.exit(app.exec())
