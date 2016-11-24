#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wpgGate
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
import model.locData as locData

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
#*  wpgGate::wpgGate
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wpgGate ( acmeWizardPage.acmeWizardPage ):

    #** -------------------------------------------------------------------------------------------
    #*  wpgGate::__init__
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
        #l_szMetodo = "wpgGate::__init__"


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
        #assert ( l_image is not None )

        l_image.setGeometry ( QtCore.QRect ( 20, 30, 256, 290 ))
        l_image.setBackgroundRole ( QtGui.QPalette.Base )
        l_image.setSizePolicy ( QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored )
        l_image.setScaledContents ( True )

        l_image.setPixmap ( QtGui.QPixmap.fromImage ( QtGui.QImage ( "data/images/wpgGate.jpg" )))

        #** ---------------------------------------------------------------------------------------
        #*  fonte do título
        #*/
        l_font = QtGui.QFont ()
        #assert ( l_font is not None )

        l_font.setFamily ( "Sans Serif" )
        l_font.setPointSize ( 14 )

        #** ---------------------------------------------------------------------------------------
        #*  título
        #*/
        self._lblTitle = QtGui.QLabel ( self )
        #assert ( self._lblTitle is not None )

        self._lblTitle.setGeometry ( QtCore.QRect ( 300, 30, 400, 20 ))
        self._lblTitle.setFont ( l_font )
        self._lblTitle.setText ( self.tr ( u"<center><b>"
                                           u"Posição da aeronave"
                                           u"</b></center>" ))

        #** ---------------------------------------------------------------------------------------
        #*  grid
        #*/
        l_gridLayoutWidget = QtGui.QWidget ( self )
        #assert ( l_gridLayoutWidget is not None )

        l_gridLayoutWidget.setGeometry ( QtCore.QRect ( 350, 100, 300, 150 ))

        #** ---------------------------------------------------------------------------------------
        #*/
        l_font = QtGui.QFont ()
        #assert ( l_font is not None )

        l_font.setPointSize ( 12 )

        #** ---------------------------------------------------------------------------------------
        #*  distância
        #*/
        l_lblDst = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( l_lblDst is not None )

        l_lblDst.setFont ( l_font )
        l_lblDst.setText ( self.tr ( u"&Distância:" ))

        self._qsbDst = QtGui.QDoubleSpinBox ( l_gridLayoutWidget )
        #assert ( self._qsbDst is not None )

        self._qsbDst.setAlignment ( QtCore.Qt.AlignRight )
        self._qsbDst.setRange ( 0., 50. )
        self._qsbDst.setSingleStep ( 1. )
        self._qsbDst.setSuffix ( self.tr ( " NM" ))
        self._qsbDst.setDecimals ( 1 )

        l_lblDst.setBuddy ( self._qsbDst )

        self.setFocusProxy ( self._qsbDst )

        #** ---------------------------------------------------------------------------------------
        #*  altura
        #*/
        l_lblAlt = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( l_lblAlt is not None )

        l_lblAlt.setFont ( l_font )
        l_lblAlt.setText ( self.tr ( "&Altura:" ))

        self._qsbAlt = QtGui.QDoubleSpinBox ( l_gridLayoutWidget )
        #assert ( self._qsbAlt is not None )

        self._qsbAlt.setAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter )
        self._qsbAlt.setRange ( 1000., 20000. )
        self._qsbAlt.setSingleStep ( 100. )
        self._qsbAlt.setSuffix ( self.tr ( " ft" ))
        self._qsbAlt.setDecimals ( 1 )

        l_lblAlt.setBuddy ( self._qsbAlt )

        #** ---------------------------------------------------------------------------------------
        #*  afastamento
        #*/
        l_lblAft = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( l_lblAft is not None )

        l_lblAft.setFont ( l_font )
        l_lblAft.setText ( self.tr ( "&Afastamento do eixo:" ))

        self._qsbAft = QtGui.QDoubleSpinBox ( l_gridLayoutWidget )
        #assert ( self._qsbAft is not None )

        self._qsbAft.setAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter )
        self._qsbAft.setRange ( 5., 200. )
        self._qsbAft.setSingleStep ( 5. )
        self._qsbAft.setSuffix ( self.tr ( " m" ))
        self._qsbAft.setDecimals ( 1 )

        l_lblAft.setBuddy ( self._qsbAft )

        #** ---------------------------------------------------------------------------------------
        #*  layout
        #*/
        l_lay = QtGui.QGridLayout ( l_gridLayoutWidget )
        #assert ( l_lay is not None )

        l_lay.setMargin ( 10 )
        l_lay.setSpacing ( 10 )

        l_lay.addWidget ( l_lblDst,     1, 0 )
        l_lay.addWidget ( self._qsbDst, 1, 1 )
        l_lay.addWidget ( l_lblAlt,     2, 0 )
        l_lay.addWidget ( self._qsbAlt, 2, 1 )
        l_lay.addWidget ( l_lblAft,     3, 0 )
        l_lay.addWidget ( self._qsbAft, 3, 1 )

        #** ---------------------------------------------------------------------------------------
        #*/
        self.connect ( self._qsbDst, QtCore.SIGNAL ( "valueChanged(QString)" ),
                       self,         QtCore.SIGNAL ( "completeStateChanged()" ))
        self.connect ( self._qsbAft, QtCore.SIGNAL ( "valueChanged(QString)" ),
                       self,         QtCore.SIGNAL ( "completeStateChanged()" ))
        self.connect ( self._qsbAlt, QtCore.SIGNAL ( "valueChanged(QString)" ),
                       self,         QtCore.SIGNAL ( "completeStateChanged()" ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgGate::isComplete
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
        #l_szMetodo = "wpgGate::isComplete"


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
        return (( not self._qsbDst.cleanText ().isEmpty ()) and
                ( not self._qsbAft.cleanText ().isEmpty ()) and
                ( not self._qsbAlt.cleanText ().isEmpty ()))

    #** -------------------------------------------------------------------------------------------
    #*  wpgGate::nextPage
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
        #l_szMetodo = "wpgGate::nextPage"


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
        locData.g_oExe._fGateAfst = self._qsbAft.value ()
        locData.g_oExe._fGateAlt  = self._qsbAlt.value ()
        locData.g_oExe._fGateDist = self._qsbDst.value ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( self._oWizard._pagVento )

    #** -------------------------------------------------------------------------------------------
    #*  wpgGate::resetPage
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
        #l_szMetodo = "wpgGate::resetPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  reseta os campos da form
        #*/
        self._qsbAft.setValue ( 20. )
        self._qsbAlt.setValue ( 3000. )
        self._qsbDst.setValue ( 5. )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "wpgGate" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
