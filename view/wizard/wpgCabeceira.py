#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wpgCabeceira
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
import model.clsPAR as clsPAR

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
#*  wpgCabeceira::wpgCabeceira
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wpgCabeceira ( acmeWizardPage.acmeWizardPage ):

    #** -------------------------------------------------------------------------------------------
    #*  wpgCabeceira::__init__
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
        #l_szMetodo = "wpgCabeceira::__init__"


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
        ##assert ( l_image is not None )

        l_image.setGeometry ( QtCore.QRect ( 20, 30, 256, 290 ))
        l_image.setBackgroundRole ( QtGui.QPalette.Base )
        l_image.setSizePolicy ( QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored )
        l_image.setScaledContents ( True )

        l_image.setPixmap ( QtGui.QPixmap.fromImage ( QtGui.QImage ( "data/images/wpgCabeceira.jpg" )))

        #** ---------------------------------------------------------------------------------------
        #*  fonte do título
        #*/
        l_font = QtGui.QFont ()
        ##assert ( l_font is not None )

        l_font.setFamily ( "Sans Serif" )
        l_font.setPointSize ( 14 )

        #** ---------------------------------------------------------------------------------------
        #*  título da página
        #*/
        l_lblTitle = QtGui.QLabel ( self )
        ##assert ( l_lblTitle is not None )

        l_lblTitle.setGeometry ( QtCore.QRect ( 300, 30, 400, 32 ))
        l_lblTitle.setFont ( l_font )
        l_lblTitle.setText ( self.tr (  "<center><b>"
                                       u"Seleção da cabeceira em uso"
                                        "</b></center>" ))

        #** ---------------------------------------------------------------------------------------
        #*  grid
        #*/
        l_gridLayoutWidget = QtGui.QWidget ( self )
        ##assert ( l_gridLayoutWidget is not None )

        l_gridLayoutWidget.setGeometry ( QtCore.QRect ( 350, 100, 300, 150 ))

        #** ---------------------------------------------------------------------------------------
        #*  fonte dos ítens
        #*/
        l_font = QtGui.QFont ()
        ##assert ( l_font is not None )

        l_font.setPointSize ( 12 )

        #** ---------------------------------------------------------------------------------------
        #*  cabeceira principal
        #*/
        self._rbtC0 = QtGui.QRadioButton ( l_gridLayoutWidget )
        ##assert ( self._rbtC0 is not None )

        self._rbtC0.setFont ( l_font )
        self._rbtC0.setText ( self.tr ( u"Cabeceira &principal..." ))

        self.setFocusProxy ( self._rbtC0 )

        #** ---------------------------------------------------------------------------------------
        #*  cabeceira secundária
        #*/
        self._rbtC1 = QtGui.QRadioButton ( l_gridLayoutWidget )
        ##assert ( self._rbtC1 is not None )

        self._rbtC1.setFont ( l_font )
        self._rbtC1.setText ( self.tr ( u"Cabeceira &secundária..." ))

        #** ---------------------------------------------------------------------------------------
        #*  layout
        #*/
        l_lay = QtGui.QGridLayout ( l_gridLayoutWidget )
        ##assert ( l_lay is not None )

        l_lay.setMargin ( 10 )
        l_lay.setSpacing ( 10 )

        l_lay.addWidget ( self._rbtC0, 0, 0 )
        l_lay.addWidget ( self._rbtC1, 1, 0 )

        #** ---------------------------------------------------------------------------------------
        #*  cabeceiras
        #*/
        self._aiCab = None

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgCabeceira::nextPage
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
        #l_szMetodo = "wpgCabeceira::nextPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        ##assert ( locData.g_oExe )
                                        
        #** ---------------------------------------------------------------------------------------
        #*  selecionou cabeceira principal ?
        #*/
        if ( self._rbtC0.isChecked ()):

            #** -----------------------------------------------------------------------------------
            #*  salva o valor no exercício
            #*/
            locData.g_oExe._iCab = 0

        #** ---------------------------------------------------------------------------------------
        #*  senão, selecionou cabeceira secundária
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  salva o valor no exercício
            #*/
            locData.g_oExe._iCab = 1

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( self._oWizard._pagTabAnv )

    #** -------------------------------------------------------------------------------------------
    #*  wpgCabeceira::resetPage
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
        #l_szMetodo = "wpgCabeceira::resetPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        ##assert ( locData.g_oExe )
        ##assert ( locData.g_oExe._oPAR )
        ##assert ( isinstance ( locData.g_oExe._oPAR, clsPAR.clsPAR ))

        #** ---------------------------------------------------------------------------------------
        #*  obtém as cabeceiras de pista
        #*/
        self._aiCab = locData.g_oExe._oPAR.getCabeceiras ()
        ##assert ( self._aiCab )

        #** ---------------------------------------------------------------------------------------
        #*  monta label com as cabeceiras
        #*/
        self._rbtC0.setText ( self.tr ( u"Cabeceira &principal (%d)" % self._aiCab [ 0 ] ))
        self._rbtC1.setText ( self.tr ( u"Cabeceira &secundária (%d)" % self._aiCab [ 1 ] ))

        #** ---------------------------------------------------------------------------------------
        #*  seleciona botão cabeceira principal
        #*/
        self._rbtC0.setChecked ( True )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "wpgCabeceira" )

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
    l_wpg = wpgCabeceira ()
    ##assert ( l_wpg )

#** ----------------------------------------------------------------------------------------------- *#
