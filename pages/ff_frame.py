# Form implementation generated from reading ui file 'designs/ff_frame.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
	def setupUi(self, Frame):
		Frame.setObjectName("Frame")
		Frame.resize(720, 450)
		self.he_output_lcd_2 = QtWidgets.QRadioButton(parent=Frame)
		self.he_output_lcd_2.setGeometry(QtCore.QRect(565, 320, 16, 16))
		self.he_output_lcd_2.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"")
		self.he_output_lcd_2.setText("")
		self.he_output_lcd_2.setIconSize(QtCore.QSize(50, 50))
		self.he_output_lcd_2.setCheckable(False)
		self.he_output_lcd_2.setChecked(False)
		self.he_output_lcd_2.setObjectName("he_output_lcd_2")
		self.he_output_lcd = QtWidgets.QRadioButton(parent=Frame)
		self.he_output_lcd.setGeometry(QtCore.QRect(270, 280, 16, 16))
		self.he_output_lcd.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"")
		self.he_output_lcd.setText("")
		self.he_output_lcd.setIconSize(QtCore.QSize(50, 50))
		self.he_output_lcd.setCheckable(False)
		self.he_output_lcd.setChecked(False)
		self.he_output_lcd.setObjectName("he_output_lcd")
		self.pres_lcd = QtWidgets.QLCDNumber(parent=Frame)
		self.pres_lcd.setGeometry(QtCore.QRect(528, 248, 81, 30))
		self.pres_lcd.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
		self.pres_lcd.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
		self.pres_lcd.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
		self.pres_lcd.setSmallDecimalPoint(True)
		self.pres_lcd.setDigitCount(3)
		self.pres_lcd.setMode(QtWidgets.QLCDNumber.Mode.Dec)
		self.pres_lcd.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Flat)
		self.pres_lcd.setProperty("value", 123.0)
		self.pres_lcd.setProperty("intValue", 123)
		self.pres_lcd.setObjectName("pres_lcd")
		self.co2_output_lcd = QtWidgets.QRadioButton(parent=Frame)
		self.co2_output_lcd.setGeometry(QtCore.QRect(410, 120, 16, 16))
		self.co2_output_lcd.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"")
		self.co2_output_lcd.setText("")
		self.co2_output_lcd.setIconSize(QtCore.QSize(50, 50))
		self.co2_output_lcd.setCheckable(False)
		self.co2_output_lcd.setChecked(False)
		self.co2_output_lcd.setObjectName("co2_output_lcd")
		self.input_valve_led = QtWidgets.QRadioButton(parent=Frame)
		self.input_valve_led.setGeometry(QtCore.QRect(267, 178, 16, 16))
		self.input_valve_led.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"")
		self.input_valve_led.setText("")
		self.input_valve_led.setIconSize(QtCore.QSize(50, 50))
		self.input_valve_led.setCheckable(False)
		self.input_valve_led.setChecked(False)
		self.input_valve_led.setObjectName("input_valve_led")
		self.temp_lcd = QtWidgets.QLCDNumber(parent=Frame)
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
		self.he_pump_lcd = QtWidgets.QRadioButton(parent=Frame)
		self.he_pump_lcd.setGeometry(QtCore.QRect(196, 280, 16, 16))
		self.he_pump_lcd.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"")
		self.he_pump_lcd.setText("")
		self.he_pump_lcd.setIconSize(QtCore.QSize(50, 50))
		self.he_pump_lcd.setCheckable(False)
		self.he_pump_lcd.setChecked(False)
		self.he_pump_lcd.setObjectName("he_pump_lcd")
		self.he_input_lcd = QtWidgets.QRadioButton(parent=Frame)
		self.he_input_lcd.setGeometry(QtCore.QRect(239, 235, 16, 16))
		self.he_input_lcd.setStyleSheet("QRadioButton\n"
"{\n"
"	color: red;\n"
"}\n"
"QRadioButton:indicator:checked\n"
"{\n"
"	image: url(:/Mnemoscheme/greenlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton:indicator:unchecked\n"
"{\n"
"	image: url(:/Mnemoscheme/redlamp.svg);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"")
		self.he_input_lcd.setText("")
		self.he_input_lcd.setIconSize(QtCore.QSize(50, 50))
		self.he_input_lcd.setCheckable(False)
		self.he_input_lcd.setChecked(False)
		self.he_input_lcd.setObjectName("he_input_lcd")
		self.mnemoscheme = QtWidgets.QLabel(parent=Frame)
		self.mnemoscheme.setGeometry(QtCore.QRect(0, 0, 720, 450))
		self.mnemoscheme.setText("")
		self.mnemoscheme.setTextFormat(QtCore.Qt.TextFormat.RichText)
		self.mnemoscheme.setPixmap(QtGui.QPixmap(":/Mnemoscheme/бб.svg"))
		self.mnemoscheme.setScaledContents(True)
		self.mnemoscheme.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.mnemoscheme.setWordWrap(False)
		self.mnemoscheme.setObjectName("mnemoscheme")

		self.retranslateUi(Frame)
		QtCore.QMetaObject.connectSlotsByName(Frame)

	def retranslateUi(self, Frame):
		_translate = QtCore.QCoreApplication.translate
		Frame.setWindowTitle(_translate("Frame", "Frame"))