# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dlgEditAnv.ui'
#
# Created: Wed Sep 22 10:03:11 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgEditAnv(object):
    def setupUi(self, dlgEditAnv):
        dlgEditAnv.setObjectName("dlgEditAnv")
        dlgEditAnv.resize(701, 204)
        dlgEditAnv.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        dlgEditAnv.setSizeGripEnabled(True)
        dlgEditAnv.setModal(True)
        self.gridlayout = QtGui.QGridLayout(dlgEditAnv)
        self.gridlayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridlayout.setMargin(5)
        self.gridlayout.setSpacing(5)
        self.gridlayout.setObjectName("gridlayout")
        self.buttonBox = QtGui.QDialogButtonBox(dlgEditAnv)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridlayout.addWidget(self.buttonBox, 11, 4, 1, 2)
        self.lblKey = QtGui.QLabel(dlgEditAnv)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblKey.sizePolicy().hasHeightForWidth())
        self.lblKey.setSizePolicy(sizePolicy)
        self.lblKey.setObjectName("lblKey")
        self.gridlayout.addWidget(self.lblKey, 0, 0, 1, 1)
        self.qsbRazMaxDesc = QtGui.QSpinBox(dlgEditAnv)
        self.qsbRazMaxDesc.setAlignment(QtCore.Qt.AlignRight)
        self.qsbRazMaxDesc.setMinimum(1000)
        self.qsbRazMaxDesc.setMaximum(10000)
        self.qsbRazMaxDesc.setSingleStep(100)
        self.qsbRazMaxDesc.setProperty("value", 3000)
        self.qsbRazMaxDesc.setObjectName("qsbRazMaxDesc")
        self.gridlayout.addWidget(self.qsbRazMaxDesc, 9, 2, 1, 1)
        self.lblRazMaxSub = QtGui.QLabel(dlgEditAnv)
        self.lblRazMaxSub.setObjectName("lblRazMaxSub")
        self.gridlayout.addWidget(self.lblRazMaxSub, 6, 3, 1, 1)
        self.qsbVelApx = QtGui.QSpinBox(dlgEditAnv)
        self.qsbVelApx.setAlignment(QtCore.Qt.AlignRight)
        self.qsbVelApx.setMinimum(50)
        self.qsbVelApx.setMaximum(200)
        self.qsbVelApx.setSingleStep(10)
        self.qsbVelApx.setProperty("value", 130)
        self.qsbVelApx.setObjectName("qsbVelApx")
        self.gridlayout.addWidget(self.qsbVelApx, 6, 2, 1, 1)
        self.lblVelApx = QtGui.QLabel(dlgEditAnv)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVelApx.sizePolicy().hasHeightForWidth())
        self.lblVelApx.setSizePolicy(sizePolicy)
        self.lblVelApx.setObjectName("lblVelApx")
        self.gridlayout.addWidget(self.lblVelApx, 6, 0, 1, 1)
        self.lblRazMaxDesc = QtGui.QLabel(dlgEditAnv)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRazMaxDesc.sizePolicy().hasHeightForWidth())
        self.lblRazMaxDesc.setSizePolicy(sizePolicy)
        self.lblRazMaxDesc.setObjectName("lblRazMaxDesc")
        self.gridlayout.addWidget(self.lblRazMaxDesc, 9, 0, 1, 1)
        self.lblDescr = QtGui.QLabel(dlgEditAnv)
        self.lblDescr.setObjectName("lblDescr")
        self.gridlayout.addWidget(self.lblDescr, 0, 3, 1, 1)
        self.qleDescr = QtGui.QLineEdit(dlgEditAnv)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qleDescr.sizePolicy().hasHeightForWidth())
        self.qleDescr.setSizePolicy(sizePolicy)
        self.qleDescr.setObjectName("qleDescr")
        self.gridlayout.addWidget(self.qleDescr, 0, 4, 1, 1)
        self.qleKey = QtGui.QLineEdit(dlgEditAnv)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qleKey.sizePolicy().hasHeightForWidth())
        self.qleKey.setSizePolicy(sizePolicy)
        self.qleKey.setObjectName("qleKey")
        self.gridlayout.addWidget(self.qleKey, 0, 2, 1, 1)
        self.qsbRazMaxSub = QtGui.QSpinBox(dlgEditAnv)
        self.qsbRazMaxSub.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbRazMaxSub.setMinimum(500)
        self.qsbRazMaxSub.setMaximum(2800)
        self.qsbRazMaxSub.setSingleStep(100)
        self.qsbRazMaxSub.setProperty("value", 2000)
        self.qsbRazMaxSub.setObjectName("qsbRazMaxSub")
        self.gridlayout.addWidget(self.qsbRazMaxSub, 6, 4, 1, 1)
        self.lblRazMaxCurv = QtGui.QLabel(dlgEditAnv)
        self.lblRazMaxCurv.setObjectName("lblRazMaxCurv")
        self.gridlayout.addWidget(self.lblRazMaxCurv, 9, 3, 1, 1)
        self.qsbRazMaxCurv = QtGui.QSpinBox(dlgEditAnv)
        self.qsbRazMaxCurv.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbRazMaxCurv.setMinimum(3)
        self.qsbRazMaxCurv.setMaximum(8)
        self.qsbRazMaxCurv.setProperty("value", 5)
        self.qsbRazMaxCurv.setObjectName("qsbRazMaxCurv")
        self.gridlayout.addWidget(self.qsbRazMaxCurv, 9, 4, 1, 1)
        self.lblTetoServ = QtGui.QLabel(dlgEditAnv)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTetoServ.sizePolicy().hasHeightForWidth())
        self.lblTetoServ.setSizePolicy(sizePolicy)
        self.lblTetoServ.setObjectName("lblTetoServ")
        self.gridlayout.addWidget(self.lblTetoServ, 11, 0, 1, 1)
        self.qsbTetoServ = QtGui.QSpinBox(dlgEditAnv)
        self.qsbTetoServ.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.qsbTetoServ.setMinimum(15000)
        self.qsbTetoServ.setMaximum(90000)
        self.qsbTetoServ.setSingleStep(1000)
        self.qsbTetoServ.setProperty("value", 40000)
        self.qsbTetoServ.setObjectName("qsbTetoServ")
        self.gridlayout.addWidget(self.qsbTetoServ, 11, 2, 1, 1)
        self.lblKey.setBuddy(self.qleKey)
        self.lblRazMaxSub.setBuddy(self.qsbRazMaxSub)
        self.lblVelApx.setBuddy(self.qsbVelApx)
        self.lblRazMaxDesc.setBuddy(self.qsbRazMaxDesc)
        self.lblDescr.setBuddy(self.qleDescr)
        self.lblRazMaxCurv.setBuddy(self.qsbRazMaxCurv)
        self.lblTetoServ.setBuddy(self.qsbTetoServ)

        self.retranslateUi(dlgEditAnv)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlgEditAnv.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlgEditAnv.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgEditAnv)
        dlgEditAnv.setTabOrder(self.qleKey, self.qleDescr)
        dlgEditAnv.setTabOrder(self.qleDescr, self.qsbVelApx)
        dlgEditAnv.setTabOrder(self.qsbVelApx, self.qsbRazMaxSub)
        dlgEditAnv.setTabOrder(self.qsbRazMaxSub, self.qsbRazMaxDesc)
        dlgEditAnv.setTabOrder(self.qsbRazMaxDesc, self.qsbRazMaxCurv)
        dlgEditAnv.setTabOrder(self.qsbRazMaxCurv, self.qsbTetoServ)
        dlgEditAnv.setTabOrder(self.qsbTetoServ, self.buttonBox)

    def retranslateUi(self, dlgEditAnv):
        dlgEditAnv.setWindowTitle(QtGui.QApplication.translate("dlgEditAnv", "SiPAR - Edição de Aeronaves", None, QtGui.QApplication.UnicodeUTF8))
        self.lblKey.setText(QtGui.QApplication.translate("dlgEditAnv", "Sigla:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbRazMaxDesc.setSpecialValueText(QtGui.QApplication.translate("dlgEditAnv", "Unknown", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbRazMaxDesc.setSuffix(QtGui.QApplication.translate("dlgEditAnv", " ft/min", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRazMaxSub.setText(QtGui.QApplication.translate("dlgEditAnv", "Razão Máxima de Subida:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbVelApx.setSpecialValueText(QtGui.QApplication.translate("dlgEditAnv", "Unknown", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbVelApx.setSuffix(QtGui.QApplication.translate("dlgEditAnv", " kt", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVelApx.setText(QtGui.QApplication.translate("dlgEditAnv", "Velocidade de Aproximação:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRazMaxDesc.setText(QtGui.QApplication.translate("dlgEditAnv", "Razão Máxima de Descida:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDescr.setText(QtGui.QApplication.translate("dlgEditAnv", "Descrição:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbRazMaxSub.setSuffix(QtGui.QApplication.translate("dlgEditAnv", " ft/min", None, QtGui.QApplication.UnicodeUTF8))
        self.lblRazMaxCurv.setText(QtGui.QApplication.translate("dlgEditAnv", "Razão Máxima de Curva:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbRazMaxCurv.setSuffix(QtGui.QApplication.translate("dlgEditAnv", " gr/seg", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTetoServ.setText(QtGui.QApplication.translate("dlgEditAnv", "Teto de Serviço:", None, QtGui.QApplication.UnicodeUTF8))
        self.qsbTetoServ.setSuffix(QtGui.QApplication.translate("dlgEditAnv", " ft", None, QtGui.QApplication.UnicodeUTF8))
