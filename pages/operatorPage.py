# Form implementation generated from reading ui file 'designs/operatorPage.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_OperatorWindow(object):
	def setupUi(self, OperatorWindow):
		OperatorWindow.setObjectName("OperatorWindow")
		OperatorWindow.resize(800, 600)
		OperatorWindow.setMinimumSize(QtCore.QSize(800, 600))
		OperatorWindow.setMaximumSize(QtCore.QSize(800, 600))
		OperatorWindow.setAcceptDrops(True)
		self.centralwidget = QtWidgets.QWidget(parent=OperatorWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 231, 80))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
		self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
		self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.curr_process = QtWidgets.QLabel(parent=self.gridLayoutWidget)
		self.curr_process.setText("")
		self.curr_process.setObjectName("curr_process")
		self.gridLayout.addWidget(self.curr_process, 1, 1, 1, 1)
		self.next_process = QtWidgets.QLabel(parent=self.gridLayoutWidget)
		self.next_process.setText("")
		self.next_process.setObjectName("next_process")
		self.gridLayout.addWidget(self.next_process, 2, 1, 1, 1)
		self.tank_selector = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
		self.tank_selector.setObjectName("tank_selector")
		self.gridLayout.addWidget(self.tank_selector, 0, 1, 1, 1)
		self.co2_output_lcd = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.co2_output_lcd.setGeometry(QtCore.QRect(403, 116, 16, 16))
		self.co2_output_lcd.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"")
		self.co2_output_lcd.setText("")
		self.co2_output_lcd.setIconSize(QtCore.QSize(50, 50))
		self.co2_output_lcd.setCheckable(False)
		self.co2_output_lcd.setChecked(False)
		self.co2_output_lcd.setObjectName("co2_output_lcd")
		self.output_led = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.output_led.setGeometry(QtCore.QRect(565, 320, 16, 16))
		self.output_led.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.output_led.setText("")
		self.output_led.setIconSize(QtCore.QSize(50, 50))
		self.output_led.setCheckable(False)
		self.output_led.setChecked(False)
		self.output_led.setObjectName("output_led")
		self.mnemoscheme = QtWidgets.QLabel(parent=self.centralwidget)
		self.mnemoscheme.setGeometry(QtCore.QRect(0, 0, 720, 450))
		self.mnemoscheme.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Russian, QtCore.QLocale.Country.Russia))
		self.mnemoscheme.setText("")
		self.mnemoscheme.setTextFormat(QtCore.Qt.TextFormat.RichText)
		self.mnemoscheme.setPixmap(QtGui.QPixmap("designs\\mnemo/бб.svg"))
		self.mnemoscheme.setScaledContents(True)
		self.mnemoscheme.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.mnemoscheme.setWordWrap(False)
		self.mnemoscheme.setObjectName("mnemoscheme")
		self.pres_lcd = QtWidgets.QLCDNumber(parent=self.centralwidget)
		self.pres_lcd.setGeometry(QtCore.QRect(528, 248, 81, 30))
		self.pres_lcd.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
		self.pres_lcd.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.pres_lcd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
		self.pres_lcd.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.pres_lcd.setSmallDecimalPoint(True)
		self.pres_lcd.setDigitCount(3)
		self.pres_lcd.setMode(QtWidgets.QLCDNumber.Mode.Dec)
		self.pres_lcd.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
		self.pres_lcd.setProperty("value", 123.0)
		self.pres_lcd.setProperty("intValue", 123)
		self.pres_lcd.setObjectName("pres_lcd")
		self.low_level_led = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.low_level_led.setGeometry(QtCore.QRect(270, 339, 16, 16))
		self.low_level_led.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.low_level_led.setText("")
		self.low_level_led.setIconSize(QtCore.QSize(50, 50))
		self.low_level_led.setCheckable(False)
		self.low_level_led.setChecked(False)
		self.low_level_led.setObjectName("low_level_led")
		self.he_pump_led = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.he_pump_led.setGeometry(QtCore.QRect(196, 280, 16, 16))
		self.he_pump_led.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.he_pump_led.setText("")
		self.he_pump_led.setIconSize(QtCore.QSize(50, 50))
		self.he_pump_led.setCheckable(False)
		self.he_pump_led.setChecked(False)
		self.he_pump_led.setObjectName("he_pump_led")
		self.input_valve_led = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.input_valve_led.setGeometry(QtCore.QRect(267, 178, 16, 16))
		self.input_valve_led.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.input_valve_led.setIconSize(QtCore.QSize(50, 50))
		self.input_valve_led.setCheckable(True)
		self.input_valve_led.setChecked(False)
		self.input_valve_led.setObjectName("input_valve_led")
		self.temp_lcd = QtWidgets.QLCDNumber(parent=self.centralwidget)
		self.temp_lcd.setGeometry(QtCore.QRect(450, 247, 81, 30))
		self.temp_lcd.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
		self.temp_lcd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
		self.temp_lcd.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.temp_lcd.setSmallDecimalPoint(False)
		self.temp_lcd.setDigitCount(3)
		self.temp_lcd.setMode(QtWidgets.QLCDNumber.Mode.Dec)
		self.temp_lcd.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
		self.temp_lcd.setProperty("value", 123.0)
		self.temp_lcd.setProperty("intValue", 123)
		self.temp_lcd.setObjectName("temp_lcd")
		self.he_output_led = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.he_output_led.setGeometry(QtCore.QRect(270, 280, 16, 16))
		self.he_output_led.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.he_output_led.setText("")
		self.he_output_led.setIconSize(QtCore.QSize(50, 50))
		self.he_output_led.setCheckable(False)
		self.he_output_led.setChecked(False)
		self.he_output_led.setObjectName("he_output_led")
		self.he_input_led = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.he_input_led.setGeometry(QtCore.QRect(239, 235, 16, 16))
		self.he_input_led.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.he_input_led.setText("")
		self.he_input_led.setIconSize(QtCore.QSize(50, 50))
		self.he_input_led.setCheckable(False)
		self.he_input_led.setChecked(False)
		self.he_input_led.setObjectName("he_input_led")
		self.output_valve_led = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.output_valve_led.setGeometry(QtCore.QRect(503, 321, 16, 16))
		self.output_valve_led.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.output_valve_led.setText("")
		self.output_valve_led.setIconSize(QtCore.QSize(50, 50))
		self.output_valve_led.setCheckable(False)
		self.output_valve_led.setChecked(False)
		self.output_valve_led.setObjectName("output_valve_led")
		self.high_level_led_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
		self.high_level_led_2.setGeometry(QtCore.QRect(270, 226, 16, 16))
		self.high_level_led_2.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/icons/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}")
		self.high_level_led_2.setText("")
		self.high_level_led_2.setIconSize(QtCore.QSize(50, 50))
		self.high_level_led_2.setCheckable(False)
		self.high_level_led_2.setChecked(False)
		self.high_level_led_2.setObjectName("high_level_led_2")
		self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(0, 550, 800, 51))
		self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"	background-color: red;\n"
"	font: 700 16pt \"Segoe UI\";\n"
"}\n"
"\n"
"")
		self.pushButton.setCheckable(False)
		self.pushButton.setObjectName("pushButton")
		self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
		self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
		self.tabWidget.setObjectName("tabWidget")
		self.mnemoscheme.raise_()
		self.gridLayoutWidget.raise_()
		self.co2_output_lcd.raise_()
		self.output_led.raise_()
		self.pres_lcd.raise_()
		self.low_level_led.raise_()
		self.he_pump_led.raise_()
		self.input_valve_led.raise_()
		self.temp_lcd.raise_()
		self.he_output_led.raise_()
		self.he_input_led.raise_()
		self.output_valve_led.raise_()
		self.high_level_led_2.raise_()
		self.pushButton.raise_()
		self.tabWidget.raise_()
		OperatorWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(OperatorWindow)
		QtCore.QMetaObject.connectSlotsByName(OperatorWindow)

	def retranslateUi(self, OperatorWindow):
		_translate = QtCore.QCoreApplication.translate
		OperatorWindow.setWindowTitle(_translate("OperatorWindow", "MainWindow"))
		self.label_3.setText(_translate("OperatorWindow", "Следующий процесс"))
		self.label_2.setText(_translate("OperatorWindow", "Текущий процесс"))
		self.label.setText(_translate("OperatorWindow", "Ёмкость"))
		self.pushButton.setText(_translate("OperatorWindow", "Экстренная остановка"))
