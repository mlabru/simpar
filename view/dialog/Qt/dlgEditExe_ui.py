# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgEditExe.ui'
#
# Created: Wed Sep 22 10:03:11 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgEditExe(object):
    def setupUi(self, dlgEditExe):
        dlgEditExe.setObjectName("dlgEditExe")
        dlgEditExe.resize(600, 250)
        dlgEditExe.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        dlgEditExe.setSizeGripEnabled(True)
        dlgEditExe.setModal(True)
        self.lblKey = QtGui.QLabel(dlgEditExe)
        self.lblKey.setGeometry(QtCore.QRect(10, 12, 36, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblKey.sizePolicy().hasHeightForWidth())
        self.lblKey.setSizePolicy(sizePolicy)
        self.lblKey.setObjectName("lblKey")
        self.qleKey = QtGui.QLineEdit(dlgEditExe)
        self.qleKey.setGeometry(QtCore.QRect(80, 10, 101, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qleKey.sizePolicy().hasHeightForWidth())
        self.qleKey.setSizePolicy(sizePolicy)
        self.qleKey.setObjectName("qleKey")
        self.lblDescr = QtGui.QLabel(dlgEditExe)
        self.lblDescr.setGeometry(QtCore.QRect(190, 12, 68, 17))
        self.lblDescr.setObjectName("lblDescr")
        self.qleDescr = QtGui.QLineEdit(dlgEditExe)
        self.qleDescr.setGeometry(QtCore.QRect(275, 10, 311, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qleDescr.sizePolicy().hasHeightForWidth())
        self.qleDescr.setSizePolicy(sizePolicy)
        self.qleDescr.setObjectName("qleDescr")
        self.lblPAR = QtGui.QLabel(dlgEditExe)
        self.lblPAR.setGeometry(QtCore.QRect(10, 50, 62, 17))
        self.lblPAR.setObjectName("lblPAR")
        self.lblAnv = QtGui.QLabel(dlgEditExe)
        self.lblAnv.setGeometry(QtCore.QRect(355, 50, 66, 17))
        self.lblAnv.setObjectName("lblAnv")
        self.gbxVento = QtGui.QGroupBox(dlgEditExe)
        self.gbxVento.setGeometry(QtCore.QRect(310, 90, 270, 120))
        self.gbxVento.setObjectName("gbxVento")
        self.lblVentoVel = QtGui.QLabel(self.gbxVento)
        self.lblVentoVel.setGeometry(QtCore.QRect(10, 40, 80, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVentoVel.sizePolicy().hasHeightForWidth())
        self.lblVentoVel.setSizePolicy(sizePolicy)
        self.lblVentoVel.setObjectName("lblVentoVel")
        self.qsbVentoVel = QtGui.QSpinBox(self.gbxVento)
        self.qsbVentoVel.setGeometry(QtCore.QRect(160, 40, 84, 27))
        self.qsbVentoVel.setAlignment(QtCore.Qt.AlignRight)
        self.qsbVentoVel.setMinimum(0)
        self.qsbVentoVel.setMaximum(100)
        self.qsbVentoVel.setSingleStep(5)
        self.qsbVentoVel.setProperty("value", 10)
        self.qsbVentoVel.setObjectName("qsbVentoVel")
        self.lblVentoDir = QtGui.QLabel(self.gbxVento)
        self.lblVentoDir.setGeometry(QtCore.QRect(10, 80, 54, 17))
        self.lblVentoDir.setObjectName("lblVentoDir")
        self.qsbVentoDir = QtGui.QSpinBox(self.gbxVento)
        self.qsbVentoDir.setGeometry(QtCore.QRect(140, 80, 102, 27))
        self.qsbVentoDir.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbVentoDir.setMinimum(0)
        self.qsbVentoDir.setMaximum(360)
        self.qsbVentoDir.setSingleStep(1)
        self.qsbVentoDir.setProperty("value", 61)
        self.qsbVentoDir.setObjectName("qsbVentoDir")
        self.buttonBox = QtGui.QDialogButtonBox(dlgEditExe)
        self.buttonBox.setGeometry(QtCore.QRect(420, 210, 176, 27))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gbxGate = QtGui.QGroupBox(dlgEditExe)
        self.gbxGate.setGeometry(QtCore.QRect(10, 90, 270, 120))
        self.gbxGate.setObjectName("gbxGate")
        self.lblGateDist = QtGui.QLabel(self.gbxGate)
        self.lblGateDist.setGeometry(QtCore.QRect(10, 40, 65, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblGateDist.sizePolicy().hasHeightForWidth())
        self.lblGateDist.setSizePolicy(sizePolicy)
        self.lblGateDist.setObjectName("lblGateDist")
        self.qsbGateDist = QtGui.QSpinBox(self.gbxGate)
        self.qsbGateDist.setGeometry(QtCore.QRect(160, 30, 110, 27))
        self.qsbGateDist.setAlignment(QtCore.Qt.AlignRight)
        self.qsbGateDist.setMinimum(0)
        self.qsbGateDist.setMaximum(50)
        self.qsbGateDist.setSingleStep(1)
        self.qsbGateDist.setProperty("value", 5)
        self.qsbGateDist.setObjectName("qsbGateDist")
        self.lblGateAfst = QtGui.QLabel(self.gbxGate)
        self.lblGateAfst.setGeometry(QtCore.QRect(10, 100, 140, 17))
        self.lblGateAfst.setObjectName("lblGateAfst")
        self.qsbGateAfst = QtGui.QSpinBox(self.gbxGate)
        self.qsbGateAfst.setGeometry(QtCore.QRect(190, 90, 81, 27))
        self.qsbGateAfst.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbGateAfst.setMinimum(5)
        self.qsbGateAfst.setMaximum(200)
        self.qsbGateAfst.setSingleStep(5)
        self.qsbGateAfst.setProperty("value", 20)
        self.qsbGateAfst.setObjectName("qsbGateAfst")
        self.lblGateAlt = QtGui.QLabel(self.gbxGate)
        self.lblGateAlt.setGeometry(QtCore.QRect(10, 70, 43, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblGateAlt.sizePolicy().hasHeightForWidth())
        self.lblGateAlt.setSizePolicy(sizePolicy)
        self.lblGateAlt.setObjectName("lblGateAlt")
        self.qsbGateAlt = QtGui.QSpinBox(self.gbxGate)
        self.qsbGateAlt.setGeometry(QtCore.QRect(190, 60, 81, 27))
        self.qsbGateAlt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbGateAlt.setMinimum(1000)
        self.qsbGateAlt.setMaximum(20000)
        self.qsbGateAlt.setSingleStep(100)
        self.qsbGateAlt.setProperty("value", 3000)
        self.qsbGateAlt.setObjectName("qsbGateAlt")
        self.cbxPAR = QtGui.QComboBox(dlgEditExe)
        self.cbxPAR.setGeometry(QtCore.QRect(80, 45, 81, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbxPAR.sizePolicy().hasHeightForWidth())
        self.cbxPAR.setSizePolicy(sizePolicy)
        self.cbxPAR.setObjectName("cbxPAR")
        self.cbxAnv = QtGui.QComboBox(dlgEditExe)
        self.cbxAnv.setGeometry(QtCore.QRect(442, 45, 141, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbxAnv.sizePolicy().hasHeightForWidth())
        self.cbxAnv.setSizePolicy(sizePolicy)
        self.cbxAnv.setObjectName("cbxAnv")
        self.lblCab = QtGui.QLabel(dlgEditExe)
        self.lblCab.setGeometry(QtCore.QRect(180, 50, 71, 17))
        self.lblCab.setObjectName("lblCab")
        self.cbxCab = QtGui.QComboBox(dlgEditExe)
        self.cbxCab.setEnabled(False)
        self.cbxCab.setGeometry(QtCore.QRect(275, 45, 60, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbxCab.sizePolicy().hasHeightForWidth())
        self.cbxCab.setSizePolicy(sizePolicy)
        self.cbxCab.setObjectName("cbxCab")
        self.lblKey.setBuddy(self.qleKey)
        self.lblDescr.setBuddy(self.qleDescr)
        self.lblPAR.setBuddy(self.cbxPAR)
        self.lblAnv.setBuddy(self.cbxAnv)
        self.lblVentoVel.setBuddy(self.qsbVentoVel)
        self.lblVentoDir.setBuddy(self.qsbVentoDir)
        self.lblGateDist.setBuddy(self.qsbGateDist)
        self.lblGateAfst.setBuddy(self.qsbGateAfst)
        self.lblGateAlt.setBuddy(self.qsbGateAlt)
        self.lblCab.setBuddy(self.cbxCab)

        self.retranslateUi(dlgEditExe)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlgEditExe.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlgEditExe.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgEditExe)
        dlgEditExe.setTabOrder(self.qleKey, self.qleDescr)
        dlgEditExe.setTabOrder(self.qleDescr, self.cbxPAR)
        dlgEditExe.setTabOrder(self.cbxPAR, self.cbxCab)
        dlgEditExe.setTabOrder(self.cbxCab, self.cbxAnv)
        dlgEditExe.setTabOrder(self.cbxAnv, self.qsbGateDist)
        dlgEditExe.setTabOrder(self.qsbGateDist, self.qsbGateAlt)
        dlgEditExe.setTabOrder(self.qsbGateAlt, self.qsbGateAfst)
        dlgEditExe.setTabOrder(self.qsbGateAfst, self.qsbVentoVel)
        dlgEditExe.setTabOrder(self.qsbVentoVel, self.qsbVentoDir)
        dlgEditExe.setTabOrder(self.qsbVentoDir, self.buttonBox)

    def retranslateUi(self, dlgEditExe):
        dlgEditExe.setWindowTitle(QtGui.QApplication.translate("dlgEditExe", "SiPAR - Edição de Exercícios", None, QtGui.QApplication.UnicodeUTF8))
        self.lblKey.setText(QtGui.QApplication.translate("dlgEditExe", "Sigla:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDescr.setText(QtGui.QApplication.translate("dlgEditExe", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPAR.setText(QtGui.QApplication.translate("dlgEditExe", "Sítio PAR:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAnv.setText(QtGui.QApplication.translate("dlgEditExe", "Aeronave:", None, QtGui.QApplication.UnicodeUTF8))
        self.gbxVento.setTitle(QtGui.QApplication.translate("dlgEditExe", "Vento", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVentoVel.setText(QtGui.QApplication.translate("dlgEditExe", "Intensidade:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbVentoVel.setSpecialValueText(QtGui.QApplication.translate("dlgEditExe", "Unknown", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbVentoVel.setSuffix(QtGui.QApplication.translate("dlgEditExe", " kt", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVentoDir.setText(QtGui.QApplication.translate("dlgEditExe", "Direção:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbVentoDir.setSuffix(QtGui.QApplication.translate("dlgEditExe", " gr", None, QtGui.QApplication.UnicodeUTF8))
        self.gbxGate.setTitle(QtGui.QApplication.translate("dlgEditExe", "Gate", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGateDist.setText(QtGui.QApplication.translate("dlgEditExe", "Distância:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbGateDist.setSpecialValueText(QtGui.QApplication.translate("dlgEditExe", "Unknown", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbGateDist.setSuffix(QtGui.QApplication.translate("dlgEditExe", " NM", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGateAfst.setText(QtGui.QApplication.translate("dlgEditExe", "Afastamento do eixo:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbGateAfst.setSuffix(QtGui.QApplication.translate("dlgEditExe", " m", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGateAlt.setText(QtGui.QApplication.translate("dlgEditExe", "Altura:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbGateAlt.setSuffix(QtGui.QApplication.translate("dlgEditExe", " ft", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCab.setText(QtGui.QApplication.translate("dlgEditExe", "Cabeceira:", None, QtGui.QApplication.UnicodeUTF8))
