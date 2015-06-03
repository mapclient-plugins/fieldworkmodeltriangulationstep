# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Wed Jun  3 21:49:49 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(482, 246)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(Dialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtGui.QLabel(self.configGroupBox)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.idLineEdit)
        self.discLabel = QtGui.QLabel(self.configGroupBox)
        self.discLabel.setObjectName("discLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.discLabel)
        self.discLineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.discLineEdit.setObjectName("discLineEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.discLineEdit)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.idLineEdit, self.discLineEdit)
        Dialog.setTabOrder(self.discLineEdit, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configure Fieldwork Model Triangulation Step", None, QtGui.QApplication.UnicodeUTF8))
        self.idLabel.setText(QtGui.QApplication.translate("Dialog", "Identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.discLabel.setText(QtGui.QApplication.translate("Dialog", "Discretisation:", None, QtGui.QApplication.UnicodeUTF8))

