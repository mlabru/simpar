# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wndMain.ui'
#
# Created: Wed Sep 22 10:03:12 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_wndMain(object):
    def setupUi(self, wndMain):
        wndMain.setObjectName("wndMain")
        wndMain.resize(520, 469)
        wndMain.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.centralwidget = QtGui.QWidget(wndMain)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(35, 10, 450, 250))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(5, 10, 440, 24))
        self.label.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(5, 50, 440, 24))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(5, 90, 440, 24))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(5, 130, 440, 24))
        self.label_2.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(5, 170, 440, 24))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(5, 210, 440, 24))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.label_6.setObjectName("label_6")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(35, 270, 450, 191))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self._btnPAR = QtGui.QPushButton(self.groupBox)
        self._btnPAR.setGeometry(QtCore.QRect(250, 10, 200, 55))
        self._btnPAR.setObjectName("_btnPAR")
        self._btnAnv = QtGui.QPushButton(self.groupBox)
        self._btnAnv.setGeometry(QtCore.QRect(0, 10, 200, 55))
        self._btnAnv.setObjectName("_btnAnv")
        self._btnJoy = QtGui.QPushButton(self.groupBox)
        self._btnJoy.setEnabled(False)
        self._btnJoy.setGeometry(QtCore.QRect(250, 70, 200, 55))
        self._btnJoy.setObjectName("_btnJoy")
        self._btnPil = QtGui.QPushButton(self.groupBox)
        self._btnPil.setEnabled(True)
        self._btnPil.setGeometry(QtCore.QRect(0, 130, 200, 55))
        self._btnPil.setDefault(True)
        self._btnPil.setObjectName("_btnPil")
        self._btnFim = QtGui.QPushButton(self.groupBox)
        self._btnFim.setGeometry(QtCore.QRect(250, 130, 200, 55))
        self._btnFim.setObjectName("_btnFim")
        self._btnExe = QtGui.QPushButton(self.groupBox)
        self._btnExe.setGeometry(QtCore.QRect(0, 70, 200, 55))
        self._btnExe.setObjectName("_btnExe")
        wndMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(wndMain)
        QtCore.QMetaObject.connectSlotsByName(wndMain)

    def retranslateUi(self, wndMain):
        wndMain.setWindowTitle(QtGui.QApplication.translate("wndMain", "SiPAR 3.01 [Piloto]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("wndMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">SIMULADOR RADAR</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("wndMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\"> DE BAIXO CUSTO PARA</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("wndMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">TREINAMENTO DE CONTROLADORES</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("wndMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">EM RADAR DE APROXIMAÇÃO</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("wndMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">DE PRECISÃO (PAR)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("wndMain", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">(C) 2010  ITA - ICEA </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self._btnPAR.setText(QtGui.QApplication.translate("wndMain", "Tabela de Sítios PAR", None, QtGui.QApplication.UnicodeUTF8))
        self._btnAnv.setText(QtGui.QApplication.translate("wndMain", "Tabela de Aeronaves", None, QtGui.QApplication.UnicodeUTF8))
        self._btnJoy.setText(QtGui.QApplication.translate("wndMain", "Ajustar Joystick", None, QtGui.QApplication.UnicodeUTF8))
        self._btnPil.setText(QtGui.QApplication.translate("wndMain", "Configurar Simulação", None, QtGui.QApplication.UnicodeUTF8))
        self._btnFim.setText(QtGui.QApplication.translate("wndMain", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self._btnExe.setText(QtGui.QApplication.translate("wndMain", "Tabela de Exercícios", None, QtGui.QApplication.UnicodeUTF8))

