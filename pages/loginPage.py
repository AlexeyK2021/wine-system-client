# Form implementation generated from reading ui file 'designs/loginPage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
	def setupUi(self, LoginWindow):
		LoginWindow.setObjectName("LoginWindow")
		LoginWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
		self.formLayoutWidget.setGeometry(QtCore.QRect(230, 210, 271, 137))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
		self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setHorizontalSpacing(5)
		self.formLayout.setVerticalSpacing(15)
		self.formLayout.setObjectName("formLayout")
		self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
		self.label.setObjectName("label")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
		self.login = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
		self.login.setText("")
		self.login.setObjectName("login")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.login)
		self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
		self.label_2.setObjectName("label_2")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
		self.passwd = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
		self.passwd.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDate|QtCore.Qt.InputMethodHint.ImhHiddenText|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase|QtCore.Qt.InputMethodHint.ImhNoPredictiveText|QtCore.Qt.InputMethodHint.ImhPreferLowercase|QtCore.Qt.InputMethodHint.ImhSensitiveData|QtCore.Qt.InputMethodHint.ImhUppercaseOnly)
		self.passwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
		self.passwd.setObjectName("passwd")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passwd)
		self.clear_button = QtWidgets.QPushButton(parent=self.formLayoutWidget)
		self.clear_button.setObjectName("clear_button")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.clear_button)
		self.log_in_button = QtWidgets.QPushButton(parent=self.formLayoutWidget)
		self.log_in_button.setObjectName("log_in_button")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.log_in_button)
		LoginWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(parent=LoginWindow)
		self.statusbar.setObjectName("statusbar")
		LoginWindow.setStatusBar(self.statusbar)

		self.retranslateUi(LoginWindow)
		self.passwd.returnPressed.connect(self.log_in_button.click) # type: ignore
		QtCore.QMetaObject.connectSlotsByName(LoginWindow)

	def retranslateUi(self, LoginWindow):
		_translate = QtCore.QCoreApplication.translate
		LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
		self.label.setText(_translate("LoginWindow", "Логин"))
		self.label_2.setText(_translate("LoginWindow", "Пароль"))
		self.clear_button.setText(_translate("LoginWindow", "Очистить"))
		self.log_in_button.setText(_translate("LoginWindow", "Войти"))