#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: dlgEditExe
#*
#*  Descrição: this class takes care of all interaction with the user
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  well     1997/jun/20  version started
#*  mlabru   2009/SET/01  version started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    1997/jun/20  version started
#*  3.01-01  2009/SET/01  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  includes
#*  -----------------------------------------------------------------------------------------------
#*/

#/ Python library
#/ ------------------------------------------------------------------------------------------------
import sys

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ PyQt library
#/ ------------------------------------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.clsExe as clsExe

import model.glbDefs as glbDefs

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.dialog.Qt.dlgEditExe_ui as dlgEditExe_ui

#** -----------------------------------------------------------------------------------------------
#*  defines
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  SiPAR::dlgEditExe
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class dlgEditExe ( QtGui.QDialog, dlgEditExe_ui.Ui_dlgEditExe ):

    #** -------------------------------------------------------------------------------------------
    #*  dlgEditExe::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_oTabExe - DOCUMENT ME!
    #*  @param  f_oExe    - DOCUMENT ME!
    #*  @param  f_Parent  - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_oTabExe=None, f_oExe=None, f_Parent=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "dlgEditExe::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  init super class
        #*/
        super ( dlgEditExe, self ).__init__ ( f_Parent )

        #** ---------------------------------------------------------------------------------------
        #*  monta a dialog
        #*/
        self.setupUi ( self )

        #** ---------------------------------------------------------------------------------------
        #*  salva os parâmetros localmente
        #*/
        self._oExe = f_oExe
        self._oTabExe = f_oTabExe

        #** ---------------------------------------------------------------------------------------
        #*  exercício existe ?
        #*/
        if ( None != f_oExe ):

            #** -----------------------------------------------------------------------------------
            #*/
            self.qleKey.setText ( f_oExe._szKey )
            self.qleDescr.setText ( f_oExe._szDescr )

            self.cbxPAR.addItem ( f_oExe._szPAR )
            self.cbxAnv.addItem ( f_oExe._szAnv )

            #** -----------------------------------------------------------------------------------
            #*/
            #self.cbxCab.setValue ( f_oExe._iCab )
            
            #** -----------------------------------------------------------------------------------
            #*/
            self.qsbVentoVel.setValue ( f_oExe._fVentoVel )
            self.qsbVentoDir.setValue ( f_oExe._fVentoDir )
            self.qsbGateDist.setValue ( f_oExe._fGateDist )
            self.qsbGateAfst.setValue ( f_oExe._fGateAfst )
            self.qsbGateAlt.setValue ( f_oExe._fGateAlt )

            #** -----------------------------------------------------------------------------------
            #*/
            self.buttonBox.button ( QtGui.QDialogButtonBox.Ok ).setText ( "&Aceita" )
            self.buttonBox.button ( QtGui.QDialogButtonBox.Ok ).setFocus ()

            #** -----------------------------------------------------------------------------------
            #*/
            self.setWindowTitle ( u"SiPAR - Edição de Exercícios" )

        #** ---------------------------------------------------------------------------------------
        #*  senão, posiciona cursor no início do formulário
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            self.qleKey.setFocus ()

        #** ---------------------------------------------------------------------------------------
        #*/
        self.on_qleKey_textEdited ( QtCore.QString ())

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  dlgEditExe::accept
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def accept ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "dlgEditExe::accept"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( None != self._oTabExe )

        #** ---------------------------------------------------------------------------------------
        #*  obtém os dados do exercício
        #*/
        l_szKey = self.qleKey.text ().toUpper ()
        l_szDescr = self.qleDescr.text ().toUpper ()

        l_szPAR = self.cbxPAR.currentText ().toUpper ()
        l_szAnv = self.cbxAnv.currentText ().toUpper ()

        #** ---------------------------------------------------------------------------------------
        #*  obtém os valores do exercício
        #*/
        #l_iCab = int ( self.cbxCab.value ())
        l_iCab = 12

        #** ---------------------------------------------------------------------------------------
        #*  obtém os valores do exercício
        #*/
        l_fVentoVel = float ( self.qsbVentoVel.value ())
        l_fVentoDir = float ( self.qsbVentoDir.value ())

        l_fGateDist = float ( self.qsbGateDist.value ())
        l_fGateAfst = float ( self.qsbGateAfst.value ())
        l_fGateAlt  = float ( self.qsbGateAlt.value ())

        #** ---------------------------------------------------------------------------------------
        #*  exercício inexistente ?
        #*/
        if ( None == self._oExe ):

            #** -----------------------------------------------------------------------------------
            #*  cria uma nova exercício
            #*/
            self._oExe = clsExe.clsExe ( [ l_szKey, l_szDescr, l_szPAR, l_iCab,
                                           l_fVentoVel, l_fVentoDir, l_szAnv,
                                           l_fGateDist, l_fGateAfst, l_fGateAlt ] )
            #assert ( self._oExe )

            #** -----------------------------------------------------------------------------------
            #*  cria uma nova entrada na tabela de exercícios com o exercício criado
            #*/
            self._oTabExe.add ( self._oExe, l_szKey )

        #** ---------------------------------------------------------------------------------------
        #*  se existe, atualiza a informação
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  atualiza os dados do exercício
            #*/
            self._oTabExe.updateTabela ( self._oExe, [ l_szKey, l_szDescr, l_szPAR, l_iCab,
                                                       l_fVentoVel, l_fVentoDir, l_szAnv,
                                                       l_fGateDist, l_fGateAfst, l_fGateAlt ] )

        #** ---------------------------------------------------------------------------------------
        #*  faz o "accept"
        #*/
        QtGui.QDialog.accept ( self )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  dlgEditExe::on_qleKey_textEdited
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_szTxt - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    @QtCore.pyqtSignature("QString")
    def on_qleKey_textEdited ( self, f_szTxt ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "dlgEditExe::on_qleKey_textEdited"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        self.buttonBox.button ( QtGui.QDialogButtonBox.Ok ).setEnabled ( not self.qleKey.text ().isEmpty ())

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )






    def findStyles ( self ):

        fontDatabase = QtGui.QFontDatabase()
        currentItem = self.styleCombo.currentText()
        self.styleCombo.clear()
                                    
        for style in fontDatabase.styles(self.fontCombo.currentText()):
            self.styleCombo.addItem(style)
                                                                
        index = self.styleCombo.findText(currentItem)
        if index == -1:
            self.styleCombo.setCurrentIndex(0)
        else:
            self.styleCombo.setCurrentIndex(index)
                                                                                                                                     
        self.characterWidget.updateStyle(self.styleCombo.currentText())

#** -----------------------------------------------------------------------------------------------
#*  defines
#*  -----------------------------------------------------------------------------------------------
#*/
if ( "__main__" == __name__ ):

    #** -------------------------------------------------------------------------------------------
    #*/
    l_App = QtGui.QApplication ( sys.argv )
    #assert ( l_App )

    #** -------------------------------------------------------------------------------------------
    #*/
    l_Dlg = dlgEditExe ( 0 )
    #assert ( l_Dlg )

    #** -------------------------------------------------------------------------------------------
    #*/
    l_Dlg.show ()

    #** -------------------------------------------------------------------------------------------
    #*/
    l_App.exec_ ()

#** ----------------------------------------------------------------------------------------------- *#
