#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: dlgConfigComm
#*
#*  Descricao: this class takes care of all interaction with the user
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  well     1997/???/??  versão 1.0 started
#*  mlabru   2009/SET/01  versão 3.0 started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    1997/???/??  versão inicial
#*  3.01-01  2009/SET/01  versão para Linux
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
from PyQt4 import QtGui

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.glbData as glbData

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.dialog.Qt.dlgConfigComm_ui as dlgConfigComm_ui

#** -----------------------------------------------------------------------------------------------
#*  defines
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  variaveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  SiPAR::dlgConfigComm
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class dlgConfigComm ( QtGui.QDialog, dlgConfigComm_ui.Ui_dlgConfigComm ):

    #** -------------------------------------------------------------------------------------------
    #*  dlgConfigComm::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_iCanal  - DOCUMENT ME!
    #*  @param  f_Parent  - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_iCanal=None, f_Parent=None ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "dlgConfigComm::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  init super class
        #*/
        super ( dlgConfigComm, self ).__init__ ( f_Parent )

        #** ---------------------------------------------------------------------------------------
        #*  inicia a dialog
        #*/
        self.setupUi ( self )

        #** ---------------------------------------------------------------------------------------
        #*  salva o canal atual localmente
        #*/
        self._iCanal = f_iCanal

        #** ---------------------------------------------------------------------------------------
        #*  canal existe ?
        #*/
        if ( None != f_iCanal ):

            #** -----------------------------------------------------------------------------------
            #*/
            self.qsbCanal.setValue ( f_iCanal )

            #** -----------------------------------------------------------------------------------
            #*/
            self.buttonBox.button ( QtGui.QDialogButtonBox.Ok ).setText ( "&Aceita" )
            self.buttonBox.button ( QtGui.QDialogButtonBox.Ok ).setFocus ()

            #** -----------------------------------------------------------------------------------
            #*/
            self.setWindowTitle ( u"SiPAR - Configura Comunicação" )

        #** ---------------------------------------------------------------------------------------
        #*  senão, posiciona cursor no início do formulário
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            self.qsbCanal.setFocus ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  dlgConfigComm::accept
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def accept ( self ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "dlgConfigComm::accept"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  obtem o valor do canal de comunicação
        #*/
        glbData.g_iCanal = int ( self.qsbCanal.value ())

        #** ---------------------------------------------------------------------------------------
        #*  faz o "accept"
        #*/
        QtGui.QDialog.accept ( self )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*  bootstrap process
#*  -----------------------------------------------------------------------------------------------
#*/
if ( "__main__" == __name__ ):

    #** -------------------------------------------------------------------------------------------
    #*/
    l_App = QtGui.QApplication ( sys.argv )
    #assert ( l_App )

    #** -------------------------------------------------------------------------------------------
    #*/
    l_Dlg = dlgConfigComm ( 0 )
    #assert ( l_Dlg )

    #** -------------------------------------------------------------------------------------------
    #*/
    l_Dlg.show ()

    #** -------------------------------------------------------------------------------------------
    #*/
    l_App.exec_ ()

#** ----------------------------------------------------------------------------------------------- *#