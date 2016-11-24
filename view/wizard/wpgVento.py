#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wpgVento
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
#import os
#import sys

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ PyQt
#/ ------------------------------------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.locData as locData

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.wizard.acmeWizardPage as acmeWizardPage

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
#*  wpgVento::wpgVento
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wpgVento ( acmeWizardPage.acmeWizardPage ):

    #** -------------------------------------------------------------------------------------------
    #*  wpgVento::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_wizard - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_wizard=None ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgVento::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  init super class
        #*/
        acmeWizardPage.acmeWizardPage.__init__ ( self, f_wizard )

        #** ---------------------------------------------------------------------------------------
        #*  locale
        #*/
        self.setLocale ( QtCore.QLocale ( QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil ))

        #** ---------------------------------------------------------------------------------------
        #*  imagem
        #*/
        l_image = QtGui.QLabel ( self )
        #assert ( l_image )

        l_image.setGeometry ( QtCore.QRect ( 20, 30, 256, 290 ))
        l_image.setBackgroundRole ( QtGui.QPalette.Base )
        l_image.setSizePolicy ( QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored )
        l_image.setScaledContents ( True )

        l_image.setPixmap ( QtGui.QPixmap.fromImage ( QtGui.QImage ( "data/images/wpgVento.gif" )))

        #** ---------------------------------------------------------------------------------------
        #*  fonte do título
        #*/
        l_font = QtGui.QFont ()
        #assert ( l_font )

        l_font.setFamily ( "Sans Serif" )
        l_font.setPointSize ( 14 )

        #** ---------------------------------------------------------------------------------------
        #*  título
        #*/
        l_lblTitle = QtGui.QLabel ( self )
        #assert ( l_lblTitle )

        l_lblTitle.setGeometry ( QtCore.QRect ( 300, 30, 400, 20 ))
        l_lblTitle.setFont ( l_font )
        l_lblTitle.setText ( self.tr ( "<center><b>"
                                       "Dados do vento"
                                       "</b></center>" ))

        #** ---------------------------------------------------------------------------------------
        #*  grid
        #*/
        l_gridLayoutWidget = QtGui.QWidget ( self )
        #assert ( l_gridLayoutWidget )

        l_gridLayoutWidget.setGeometry ( QtCore.QRect ( 350, 100, 300, 150 ))

        #** ---------------------------------------------------------------------------------------
        #*  fonte
        #*/
        l_font = QtGui.QFont ()
        #assert ( l_font )

        l_font.setPointSize ( 12 )

        #** ---------------------------------------------------------------------------------------
        #*  intensidade do vento
        #*/
        l_lblInt = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( l_lblInt )

        l_lblInt.setFont ( l_font )
        l_lblInt.setText ( self.tr ( "&Intensidade:" ))

        self._qsbVel = QtGui.QDoubleSpinBox ( l_gridLayoutWidget )
        #assert ( self._qsbVel )

        self._qsbVel.setAlignment ( QtCore.Qt.AlignRight )
        self._qsbVel.setRange ( 0., 100. )
        self._qsbVel.setSingleStep ( 5. )
        self._qsbVel.setSuffix ( self.tr ( " kts" ))
        self._qsbVel.setDecimals ( 1 )
        self._qsbVel.setSpecialValueText ( self.tr ( "sem vento" ))

        l_lblInt.setBuddy ( self._qsbVel )

        self.setFocusProxy ( self._qsbVel )

        #** ---------------------------------------------------------------------------------------
        #*  direção do vento
        #*/
        l_lblDir = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( l_lblDir )

        l_lblDir.setFont ( l_font )
        l_lblDir.setText ( self.tr ( u"&Direção:" ))

        self._qsbDir = QtGui.QDoubleSpinBox ( l_gridLayoutWidget )
        #assert ( self._qsbDir )

        self._qsbDir.setAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter )
        self._qsbDir.setRange ( 0., 359.9 )
        self._qsbDir.setSingleStep ( 1. )
        self._qsbDir.setSuffix ( self.tr ( " gr" ))
        self._qsbDir.setDecimals ( 1 )
        self._qsbDir.setSpecialValueText ( self.tr ( "sem vento" ))

        l_lblDir.setBuddy ( self._qsbDir )

        #** ---------------------------------------------------------------------------------------
        #*  layout
        #*/
        l_lay = QtGui.QGridLayout ( l_gridLayoutWidget )
        #assert ( l_lay )

        l_lay.setMargin ( 10 )
        l_lay.setSpacing ( 10 )

        l_lay.addWidget ( l_lblInt,     1, 0 )
        l_lay.addWidget ( self._qsbVel, 1, 1 )
        l_lay.addWidget ( l_lblDir,     2, 0 )
        l_lay.addWidget ( self._qsbDir, 2, 1 )

        #** ---------------------------------------------------------------------------------------
        #*/
        self.connect ( self._qsbVel, QtCore.SIGNAL ( "valueChanged(QString)" ),
                       self,         QtCore.SIGNAL ( "completeStateChanged()" ))
        self.connect ( self._qsbDir, QtCore.SIGNAL ( "valueChanged(QString)" ),
                       self,         QtCore.SIGNAL ( "completeStateChanged()" ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgVento::isComplete
    #*  -------------------------------------------------------------------------------------------
    #*  verifica se a form está aceitável
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def isComplete ( self ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgVento::isComplete"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return (( not self._qsbVel.cleanText ().isEmpty ()) and
                ( not self._qsbDir.cleanText ().isEmpty ()))

    #** -------------------------------------------------------------------------------------------
    #*  wpgVento::nextPage
    #*  -------------------------------------------------------------------------------------------
    #*  próxima página na seqüência do wizard
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def nextPage ( self ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgVento::nextPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( locData.g_oExe )

        #** ---------------------------------------------------------------------------------------
        #*  salva os valores no exercício
        #*/
        locData.g_oExe._fVentoDir = self._qsbDir.value ()
        locData.g_oExe._fVentoVel = self._qsbVel.value ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( self._oWizard._pagCanal )

    #** -------------------------------------------------------------------------------------------
    #*  wpgVento::resetPage
    #*  -------------------------------------------------------------------------------------------
    #*  reseta os campos da form
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def resetPage ( self ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgVento::resetPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  reseta os campos da form
        #*/
        self._qsbDir.setValue ( 61. )
        self._qsbVel.setValue ( 10. )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "wpgVento" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** -----------------------------------------------------------------------------------------------
#*  this is the bootstrap process
#*/
if ( '__main__' == __name__ ):

    #** -------------------------------------------------------------------------------------------
    #*  m.poirot logger
    #*/
    logging.basicConfig ()

    #** -------------------------------------------------------------------------------------------
    #*
    l_wpg = wpgVento ()
    #assert ( l_wpg )

#** ----------------------------------------------------------------------------------------------- *#
