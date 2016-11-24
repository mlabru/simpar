#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wizardPAR
#*
#*  Descrição: interface principal do programa
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  mlabru   2010/AGO/29  versão 1.0 started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    2010/AGO/29  versão inicial
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

#/ PyQt
#/ ------------------------------------------------------------------------------------------------
from PyQt4 import QtGui

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.wizard.wizardModel as wizardModel
import view.wizard.wpgCabeceira as wpgCabeceira
import view.wizard.wpgCanal as wpgCanal
import view.wizard.wpgGate as wpgGate
import view.wizard.wpgStart as wpgStart
import view.wizard.wpgTabAnv as wpgTabAnv
import view.wizard.wpgTabExe as wpgTabExe
import view.wizard.wpgTabPAR as wpgTabPAR
import view.wizard.wpgTermina as wpgTermina
import view.wizard.wpgVento as wpgVento

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  wizardPAR::wizardPAR
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wizardPAR ( wizardModel.wizardModel ):

    #** -------------------------------------------------------------------------------------------
    #*  wizardPAR::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_parent - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_parent=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wizardPAR::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  init super class
        #*/
        wizardModel.wizardModel.__init__ ( self, f_parent )

        #** ---------------------------------------------------------------------------------------
        #*  página da cabeceira
        #*/
        self._pagCab = wpgCabeceira.wpgCabeceira ( self )
        #assert ( self._pagCab )

        #** ---------------------------------------------------------------------------------------
        #*  página do canal de comunicação
        #*/
        self._pagCanal = wpgCanal.wpgCanal ( self )
        #assert ( self._pagCanal )

        #** ---------------------------------------------------------------------------------------
        #*  página do gate da aeronave
        #*/
        self._pagGate = wpgGate.wpgGate ( self )
        #assert ( self._pagGate )

        #** ---------------------------------------------------------------------------------------
        #*  página de início
        #*/
        self._pagStart = wpgStart.wpgStart ( self )
        #assert ( self._pagStart )

        #** ---------------------------------------------------------------------------------------
        #*  página da tabela de aeronaves
        #*/
        self._pagTabAnv = wpgTabAnv.wpgTabAnv ( self )
        #assert ( self._pagTabAnv )

        #** ---------------------------------------------------------------------------------------
        #*  página da tabela de exercícios
        #*/
        self._pagTabExe = wpgTabExe.wpgTabExe ( self )
        #assert ( self._pagTabExe )

        #** ---------------------------------------------------------------------------------------
        #*  página da tabela de sítios PAR
        #*/
        self._pagTabPAR = wpgTabPAR.wpgTabPAR ( self )
        #assert ( self._pagTabPAR )

        #** ---------------------------------------------------------------------------------------
        #*  página de confirmação
        #*/
        self._pagTermina = wpgTermina.wpgTermina ( self )
        #assert ( self._pagTermina )

        #** ---------------------------------------------------------------------------------------
        #*  página do vento
        #*/
        self._pagVento = wpgVento.wpgVento ( self )
        #assert ( self._pagVento )

        #** ---------------------------------------------------------------------------------------
        #*  primeira página (entry-point)
        #*/
        self.setFirstPage ( self._pagStart )

        #** ---------------------------------------------------------------------------------------
        #*  geometria da janela
        #*/
        self.setWindowTitle ( self.tr ( "SiPAR Wizard" ))
        self.resize ( 720, 350 )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "wizardPAR" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** -----------------------------------------------------------------------------------------------
#*  this is the bootstrap process
#*/
if __name__ == "__main__":

    #** -------------------------------------------------------------------------------------------
    #*  m.poirot logger
    #*/
    logging.basicConfig ()

    #** -------------------------------------------------------------------------------------------
    #*
    l_app = QtGui.QApplication ( sys.argv )
    #assert ( l_app )

    #** -------------------------------------------------------------------------------------------
    #*
    l_wzd = wizardPAR ()
    #assert ( l_wzd )

    #** -------------------------------------------------------------------------------------------
    #*
    sys.exit ( l_wzd.exec_ ())

#** ----------------------------------------------------------------------------------------------- *#
                                