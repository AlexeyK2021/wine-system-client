from PyQt6 import QtWidgets
import sys

from design import Ui_MainWindow


class login(QtWidgets.QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.log_in_button.clicked.connect(lambda _: self.login(self.ui.login.text(), self.ui.passwd.text()))

    def login(self, login, passwd):
        self.ui.label.adjustSize()
        print(f"LOGIN: {login}, {passwd}")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = login()
    win.show()
    sys.exit(app.exec())
