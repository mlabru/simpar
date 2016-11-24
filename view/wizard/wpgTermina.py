#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wpgTermina
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
#*  wpgTermina::wpgTermina
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wpgTermina ( acmeWizardPage.acmeWizardPage ):

    #** -------------------------------------------------------------------------------------------
    #*  wpgTermina::__init__
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
        #l_szMetodo = "wpgTermina::__init__"


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
        #*  verifica condições de execução
        #*/
        ##assert ( locData.g_oExe )

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

        l_image.setPixmap ( QtGui.QPixmap.fromImage ( QtGui.QImage ( "data/images/wpgTermina.jpg" )))

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
                                       u"Dados para simulação"
                                        "</b></center>" ))

        #** ---------------------------------------------------------------------------------------
        #*  grid
        #*/
        l_gridLayoutWidget = QtGui.QWidget ( self )
        #assert ( l_gridLayoutWidget )

        l_gridLayoutWidget.setGeometry ( QtCore.QRect ( 350, 60, 300, 220 ))

        #** ---------------------------------------------------------------------------------------
        #*/
        l_font = QtGui.QFont ()
        #assert ( l_font )

        l_font.setPointSize ( 9 )

        #** ---------------------------------------------------------------------------------------
        #*  descrição
        #*/
        self._lblDescr = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( self._lblDescr )

        self._lblDescr.setFont ( l_font )
        self._lblDescr.setWordWrap ( True )

        #** ---------------------------------------------------------------------------------------
        #*  sítio PAR
        #*/
        self._lblPAR = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( self._lblPAR )

        self._lblPAR.setFont ( l_font )

        #** ---------------------------------------------------------------------------------------
        #*  aeronave
        #*/
        self._lblAnv = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( self._lblAnv )

        self._lblAnv.setFont ( l_font )

        #** ---------------------------------------------------------------------------------------
        #*  vento
        #*/
        self._lblVento = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( self._lblVento )

        self._lblVento.setFont ( l_font )

        #** ---------------------------------------------------------------------------------------
        #*  gate
        #*/
        self._lblGate = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( self._lblGate )

        self._lblGate.setFont ( l_font )

        #** ---------------------------------------------------------------------------------------
        #*  canal
        #*/
        self._lblCanal = QtGui.QLabel ( l_gridLayoutWidget )
        #assert ( self._lblCanal )

        self._lblCanal.setFont ( l_font )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_font = QtGui.QFont ()
        #assert ( l_font )

        l_font.setPointSize ( 11 )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._cbxAgree = QtGui.QCheckBox ( l_gridLayoutWidget )
        #assert ( self._cbxAgree )

        self._cbxAgree.setFont ( l_font )
        self._cbxAgree.setText ( self.tr ( u"Dados corretos para simulação." ))

        #** ---------------------------------------------------------------------------------------
        #*/
        self.setFocusProxy ( self._cbxAgree )

        #** ---------------------------------------------------------------------------------------
        #*  layout
        #*/
        l_lay = QtGui.QGridLayout ( l_gridLayoutWidget )
        #assert ( l_lay )

        l_lay.setMargin ( 10 )
        l_lay.setSpacing ( 10 )

        l_lay.addWidget ( self._lblDescr, 0, 0 )
        l_lay.addWidget ( self._lblPAR,   1, 0 )
        l_lay.addWidget ( self._lblAnv,   2, 0 )
        l_lay.addWidget ( self._lblVento, 3, 0 )
        l_lay.addWidget ( self._lblGate,  4, 0 )
        l_lay.addWidget ( self._lblCanal, 5, 0 )
        l_lay.addWidget ( self._cbxAgree, 7, 0 )

        l_lay.setRowMinimumHeight ( 6, 30 )

        #** ---------------------------------------------------------------------------------------
        #*/
        self.connect ( self._cbxAgree, QtCore.SIGNAL ( "toggled(bool)" ),
                       self,           QtCore.SIGNAL ( "completeStateChanged()" ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTermina::isComplete
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
        #l_szMetodo = "wpgTermina::isComplete"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._cbxAgree )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( self._cbxAgree.isChecked ())

    #** -------------------------------------------------------------------------------------------
    #*  wpgTermina::isLastPage
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def isLastPage ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTermina::isLastPage"


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
        return ( True )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTermina::resetPage
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
        #l_szMetodo = "wpgTermina::resetPage"


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
        #*  checa se a descrição existe
        #*/
        if (( locData.g_oExe._szKey is not None ) and
            ( locData.g_oExe._szDescr is not None )):

            #** -----------------------------------------------------------------------------------
            #*  descrição
            #*/
            l_szTxt = self.tr ( u"Descrição: " + str ( locData.g_oExe._szKey ) + " - " +
                                                 str ( locData.g_oExe._szDescr ))

        #** ---------------------------------------------------------------------------------------
        #*  senão, provável exercício recém criado
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  descrição
            #*/
            l_szTxt = self.tr ( u"Exercício criado dinâmicamente." )

        #** ---------------------------------------------------------------------------------------
        #*  descrição
        #*/
        self._lblDescr.setText ( l_szTxt )

        #** ---------------------------------------------------------------------------------------
        #*  sítio PAR
        #*/
        self._lblPAR.setText ( self.tr ( u"Sítio PAR: " + str ( locData.g_oExe._szPAR ) + " - " +
                                                          str ( locData.g_oExe._oPAR._szDescr ) +
                                             " / Cab: " + str ( locData.g_oExe._oPAR._iCab0 )))

        #** ---------------------------------------------------------------------------------------
        #*  aeronave
        #*/
        self._lblAnv.setText ( self.tr ( "Aeronave: " + str ( locData.g_oExe._szAnv ) + " - " +
                                                        str ( locData.g_oExe._oAnv._szDescr )))

        #** ---------------------------------------------------------------------------------------
        #*  vento
        #*/
        self._lblVento.setText ( self.tr ( "Vento: {0} kts / {1} gr".format ( locData.g_oExe._fVentoVel,
                                                                              locData.g_oExe._fVentoDir )))

        #** ---------------------------------------------------------------------------------------
        #*  gate
        #*/
        self._lblGate.setText ( self.tr ( "Gate: {0} NM / {1} ft / {2} m".format ( locData.g_oExe._fGateDist,
                                                                                   locData.g_oExe._fGateAlt,
                                                                                   locData.g_oExe._fGateAfst )))

        #** ---------------------------------------------------------------------------------------
        #*  canal de comunicação
        #*/
        self._lblCanal.setText ( self.tr ( "Canal: " + str ( glbData.g_iCanal )))

        #** ---------------------------------------------------------------------------------------
        #*  check box
        #*/
        self._cbxAgree.setChecked ( False )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "wpgTermina" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
