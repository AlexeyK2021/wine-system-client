# Form implementation generated from reading ui file 'designs/editTankDialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditTankDialog(object):
	def setupUi(self, EditTankDialog):
		EditTankDialog.setObjectName("EditTankDialog")
		EditTankDialog.resize(399, 306)
		self.formLayoutWidget = QtWidgets.QWidget(parent=EditTankDialog)
		self.formLayoutWidget.setGeometry(QtCore.QRect(70, 120, 231, 80))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setObjectName("formLayout")
		self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
		self.label_2.setObjectName("label_2")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
		self.mqtt_topic = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
		self.mqtt_topic.setObjectName("mqtt_topic")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.mqtt_topic)
		self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
		self.label.setObjectName("label")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
		self.tank_name = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
		self.tank_name.setObjectName("tank_name")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tank_name)
		self.buttonBox = QtWidgets.QDialogButtonBox(parent=EditTankDialog)
		self.buttonBox.setGeometry(QtCore.QRect(10, 270, 381, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Save)
		self.buttonBox.setCenterButtons(False)
		self.buttonBox.setObjectName("buttonBox")

		self.retranslateUi(EditTankDialog)
		self.buttonBox.accepted.connect(EditTankDialog.accept) # type: ignore
		self.buttonBox.rejected.connect(EditTankDialog.reject) # type: ignore
		QtCore.QMetaObject.connectSlotsByName(EditTankDialog)

	def retranslateUi(self, EditTankDialog):
		_translate = QtCore.QCoreApplication.translate
		EditTankDialog.setWindowTitle(_translate("EditTankDialog", "Dialog"))
		self.label_2.setText(_translate("EditTankDialog", "Топик MQTT"))
		self.label.setText(_translate("EditTankDialog", "Имя"))
