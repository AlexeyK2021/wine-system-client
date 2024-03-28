from PyQt6 import QtWidgets
import sys

from design import Ui_MainWindow


class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.ui.label.setText("Hello world!!")
        self.ui.label.adjustSize()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = main_window()
    win.show()
    sys.exit(app.exec())
