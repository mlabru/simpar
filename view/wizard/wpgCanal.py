#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wpgCanal
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

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ PyQt
#/ ------------------------------------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.glbData as glbData

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.wizard.acmeWizardPage as acmeWizardPage

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  wpgCanal::wpgCanal
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wpgCanal ( acmeWizardPage.acmeWizardPage ):

    #** -------------------------------------------------------------------------------------------
    #*  wpgCanal::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_wizard - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_wizard=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgCanal::__init__"


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

        l_image.setPixmap ( QtGui.QPixmap.fromImage ( QtGui.QImage ( "data/images/wpgCanal.png" )))

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
        l_lblTitle.setText ( self.tr (  "<center><b>"
                                       u"Canal de comunicação"
                                        "</b></center>" ))

        #** ---------------------------------------------------------------------------------------
        #*  grid
        #*/
        l_gridLayoutWidget = QtGui.QWidget ( self )
        #assert ( l_gridLayoutWidget )

        l_gridLayoutWidget.setGeometry ( QtCore.QRect ( 350, 100, 300, 150 ))

        #** ---------------------------------------------------------------------------------------
        #*/
        l_font = QtGui.QFont ()
        #assert ( l_font )

        l_font.setPointSize ( 12 )

        #** ---------------------------------------------------------------------------------------
        #*  canal de comunicação
        #*/
        l_lblCanal = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( l_lblCanal )

        l_lblCanal.setFont ( l_font )
        l_lblCanal.setText ( self.tr ( "&Canal:" ))

        self._qsbCanal = QtGui.QSpinBox ( l_gridLayoutWidget )
        #assert ( self._qsbCanal )

        self._qsbCanal.setAlignment ( QtCore.Qt.AlignRight )
        self._qsbCanal.setRange ( 3, 27 )
        self._qsbCanal.setSingleStep ( 1 )

        l_lblCanal.setBuddy ( self._qsbCanal )

        self.setFocusProxy ( self._qsbCanal )

        #** ---------------------------------------------------------------------------------------
        #*  layout
        #*/
        l_lay = QtGui.QGridLayout ( l_gridLayoutWidget )
        #assert ( l_lay )

        l_lay.setMargin ( 10 )
        l_lay.setSpacing ( 10 )

        l_lay.addWidget ( l_lblCanal,     0, 0 )
        l_lay.addWidget ( self._qsbCanal, 0, 1 )

        #** ---------------------------------------------------------------------------------------
        #*/
        self.connect ( self._qsbCanal, QtCore.SIGNAL ( "valueChanged(QString)" ),
                       self,           QtCore.SIGNAL ( "completeStateChanged()" ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgCanal::isComplete
    #*  -------------------------------------------------------------------------------------------
    #*  verifica se a form está aceitável
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def isComplete ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgCanal::isComplete"


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
        return ( not self._qsbCanal.cleanText ().isEmpty ())

    #** -------------------------------------------------------------------------------------------
    #*  wpgCanal::nextPage
    #*  -------------------------------------------------------------------------------------------
    #*  próxima página na seqüência do wizard
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def nextPage ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgCanal::nextPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  salva os valores
        #*/
        glbData.g_iCanal = self._qsbCanal.value ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( self._oWizard._pagTermina )

    #** -------------------------------------------------------------------------------------------
    #*  wpgCanal::resetPage
    #*  -------------------------------------------------------------------------------------------
    #*  reseta os campos da form
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def resetPage ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgCanal::resetPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  reseta os campos da form
        #*/
        self._qsbCanal.setValue ( glbData.g_iCanal )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "wpgCanal" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
