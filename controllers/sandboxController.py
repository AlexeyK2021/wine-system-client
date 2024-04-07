from PyQt6.QtWidgets import QMainWindow, QPushButton

from pages.sandbox import Ui_SandBoxWindow


class SandBoxPage(QMainWindow):
    def __init__(self):
        super(SandBoxPage, self).__init__()
        self.ui = Ui_SandBoxWindow()
        self.ui.setupUi(self)

        names = ["hello", "world"]

        for i in names:
            temp_btn = QPushButton(i)
            temp_btn.clicked.connect(lambda: temp_btn.text())
            self.ui.verticalLayout.addWidget(temp_btn)
