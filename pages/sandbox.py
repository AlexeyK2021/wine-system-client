# Form implementation generated from reading ui file 'designs/sandbox.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SandBoxWindow(object):
	def setupUi(self, SandBoxWindow):
		SandBoxWindow.setObjectName("SandBoxWindow")
		SandBoxWindow.resize(800, 600)
		self.centralwidget = QtWidgets.QWidget(parent=SandBoxWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 571))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		SandBoxWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(parent=SandBoxWindow)
		self.statusbar.setObjectName("statusbar")
		SandBoxWindow.setStatusBar(self.statusbar)

		self.retranslateUi(SandBoxWindow)
		QtCore.QMetaObject.connectSlotsByName(SandBoxWindow)

	def retranslateUi(self, SandBoxWindow):
		_translate = QtCore.QCoreApplication.translate
		SandBoxWindow.setWindowTitle(_translate("SandBoxWindow", "MainWindow"))
