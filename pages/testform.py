# Form implementation generated from reading ui file 'designs/ff_widget.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(720, 450)
		self.he_pump_led = QtWidgets.QRadioButton(parent=Form)
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
		self.input_valve_led = QtWidgets.QRadioButton(parent=Form)
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
		self.output_valve_led = QtWidgets.QRadioButton(parent=Form)
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
		self.mnemoscheme = QtWidgets.QLabel(parent=Form)
		self.mnemoscheme.setGeometry(QtCore.QRect(0, 0, 720, 450))
		self.mnemoscheme.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Russian, QtCore.QLocale.Country.Russia))
		self.mnemoscheme.setText("")
		self.mnemoscheme.setMargin(50)
		self.mnemoscheme.setTextFormat(QtCore.Qt.TextFormat.RichText)
		self.mnemoscheme.setPixmap(QtGui.QPixmap("designs\\mnemo/бб.svg"))
		self.mnemoscheme.setScaledContents(True)
		self.mnemoscheme.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.mnemoscheme.setWordWrap(False)
		self.mnemoscheme.setObjectName("mnemoscheme")
		self.output_led = QtWidgets.QRadioButton(parent=Form)
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
		self.high_level_led = QtWidgets.QRadioButton(parent=Form)
		self.high_level_led.setGeometry(QtCore.QRect(270, 226, 16, 16))
		self.high_level_led.setStyleSheet("QRadioButton\n"
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
		self.high_level_led.setText("")
		self.high_level_led.setIconSize(QtCore.QSize(50, 50))
		self.high_level_led.setCheckable(False)
		self.high_level_led.setChecked(False)
		self.high_level_led.setObjectName("high_level_led")
		self.low_level_led = QtWidgets.QRadioButton(parent=Form)
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
		self.temp_lcd = QtWidgets.QLCDNumber(parent=Form)
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
		self.he_input_led = QtWidgets.QRadioButton(parent=Form)
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
		self.pres_lcd = QtWidgets.QLCDNumber(parent=Form)
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
		self.he_output_led = QtWidgets.QRadioButton(parent=Form)
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
		self.co2_valve_led = QtWidgets.QRadioButton(parent=Form)
		self.co2_valve_led.setGeometry(QtCore.QRect(401, 116, 16, 16))
		self.co2_valve_led.setStyleSheet("QRadioButton\n"
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
		self.co2_valve_led.setIconSize(QtCore.QSize(50, 50))
		self.co2_valve_led.setCheckable(True)
		self.co2_valve_led.setChecked(False)
		self.co2_valve_led.setObjectName("co2_valve_led")
		self.he_pump_led.raise_()
		self.input_valve_led.raise_()
		self.output_valve_led.raise_()
		self.output_led.raise_()
		self.high_level_led.raise_()
		self.low_level_led.raise_()
		self.temp_lcd.raise_()
		self.he_input_led.raise_()
		self.pres_lcd.raise_()
		self.he_output_led.raise_()
		self.co2_valve_led.raise_()
		self.mnemoscheme.raise_()

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
