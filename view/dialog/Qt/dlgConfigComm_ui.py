# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgConfigComm.ui'
#
# Created: Wed Sep 22 10:03:11 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgConfigComm(object):
    def setupUi(self, dlgConfigComm):
        dlgConfigComm.setObjectName("dlgConfigComm")
        dlgConfigComm.resize(326, 135)
        dlgConfigComm.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        dlgConfigComm.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(dlgConfigComm)
        self.buttonBox.setGeometry(QtCore.QRect(120, 90, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lblCanal = QtGui.QLabel(dlgConfigComm)
        self.lblCanal.setGeometry(QtCore.QRect(91, 30, 70, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCanal.sizePolicy().hasHeightForWidth())
        self.lblCanal.setSizePolicy(sizePolicy)
        self.lblCanal.setMinimumSize(QtCore.QSize(61, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblCanal.setFont(font)
        self.lblCanal.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.lblCanal.setObjectName("lblCanal")
        self.qsbCanal = QtGui.QSpinBox(dlgConfigComm)
        self.qsbCanal.setGeometry(QtCore.QRect(170, 30, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qsbCanal.setFont(font)
        self.qsbCanal.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.qsbCanal.setMinimum(3)
        self.qsbCanal.setMaximum(27)
        self.qsbCanal.setObjectName("qsbCanal")
        self.lblCanal.setBuddy(self.qsbCanal)

        self.retranslateUi(dlgConfigComm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlgConfigComm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlgConfigComm.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgConfigComm)

    def retranslateUi(self, dlgConfigComm):
        dlgConfigComm.setWindowTitle(QtGui.QApplication.translate("dlgConfigComm", "SiPAR - Configura Comunicação", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCanal.setText(QtGui.QApplication.translate("dlgConfigComm", "Canal:", None, QtGui.QApplication.UnicodeUTF8))

