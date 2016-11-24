#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wpgTabPAR
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
import model.clsTabelaPAR as clsTabelaPAR
import model.locData as locData
import model.glbDefs as glbDefs

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
#*  wpgTabPAR::wpgTabPAR
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wpgTabPAR ( acmeWizardPage.acmeWizardPage ):

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabPAR::__init__
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
        #l_szMetodo = "wpgTabPAR::__init__"


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
        #*  título da página
        #*/
        l_lblTitle = QtGui.QLabel ( self.tr (  "<center><font size=\"5\"><b>"
                                              u"Seleção do sítio PAR"
                                               "</b></font></center>" ))
        #assert ( l_lblTitle )

        #** ---------------------------------------------------------------------------------------
        #*  cria a tabela de sítios PAR
        #*/
        locData.g_oTabPAR = clsTabelaPAR.clsTabelaPAR ()
        #assert ( None != locData.g_oTabPAR )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw = QtGui.QTableWidget ( f_wizard )
        #assert ( self._qtw )

        #** ---------------------------------------------------------------------------------------
        #*/
        self.setFocusProxy ( self._qtw )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_glo = QtGui.QGridLayout ()
        #assert ( l_glo )

        l_glo.addWidget ( l_lblTitle, 0, 0, 1, 2 )
        l_glo.setRowMinimumHeight ( 1, 10 )

        l_glo.addWidget ( self._qtw, 3, 0 )
        l_glo.setRowMinimumHeight ( 4, 10 )

        self.setLayout ( l_glo )

        #** ---------------------------------------------------------------------------------------
        #*  conecta click a seleção da linha
        #*/
        self.connect ( self._qtw, QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self.selectPAR )

        self.connect ( self._qtw, QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self,      QtCore.SIGNAL ( "completeStateChanged()" ))

        #** ---------------------------------------------------------------------------------------
        #*  carrega a tabela de sítios PAR
        #*/
        self.loadInitialFile ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabPAR::isComplete
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def isComplete ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabPAR::isComplete"


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
        return ( None != locData.g_oExe._oPAR )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabPAR::loadInitialFile
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_parent - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def loadInitialFile ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabPAR::loadInitialFile"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  recupera a última tabela de sítios PAR utilizada
        #*/
        l_szFName = QtCore.QString ( "data/tabPAR.DAT" )

        #** ---------------------------------------------------------------------------------------
        #*  tabela existe ?
        #*/
        if (( l_szFName ) and ( QtCore.QFile.exists ( l_szFName ))):

            #** -----------------------------------------------------------------------------------
            #*  carrega a tabela
            #*/
            l_bOk, l_szMsg = locData.g_oTabPAR.load ( l_szFName )

            #** -----------------------------------------------------------------------------------
            #*/
            if ( l_bOk ):

                #** -------------------------------------------------------------------------------
                #*  carrega a tabela
                #*/
                self.updateTable ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabPAR::nextPage
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def nextPage ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabPAR::nextPage"


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
        return ( self._oWizard._pagCab )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabPAR::resetPage
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def resetPage ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabPAR::resetPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        #self._qtw.clear ()
        pass

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabPAR::selectPAR
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_parent - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def selectPAR ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabPAR::selectPAR"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._qtw )
        #assert ( locData.g_oExe )
        #assert ( locData.g_oTabPAR )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o número da linha selecionada da tabela
        #*/
        l_iRow = self._qtw.currentRow ()
        #l_log.info ( "l_iRow: " + str ( l_iRow ))

        #** ---------------------------------------------------------------------------------------
        #*  existe uma linha selecionada ?
        #*/
        if ( l_iRow > -1 ):

            #** -----------------------------------------------------------------------------------
            #*  obtém a linha selecionada da tabela
            #*/
            l_oItem = self._qtw.item ( l_iRow, 0 )
            #assert ( l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém o id da linha
            #*/
            l_ID = l_oItem.data ( QtCore.Qt.UserRole ).toLongLong () [ 0 ]
            #l_log.info ( "l_ID: " + str ( l_ID ))

            #l_log.info ( "locData.g_oExe._oPAR: " + str ( locData.g_oExe._oPAR ))
            #** -----------------------------------------------------------------------------------
            #*  obtém o PAR selecionado da tabela pelo id
            #*/
            locData.g_oExe._oPAR = locData.g_oTabPAR.itemFromId ( l_ID )
            #assert ( locData.g_oExe._oPAR )

            #l_log.info ( "locData.g_oExe._oPAR: " + str ( locData.g_oExe._oPAR ))

            #** -----------------------------------------------------------------------------------
            #*  obtém a chave do PAR selecionado
            #*/
            locData.g_oExe._szPAR = str ( locData.g_oExe._oPAR._szKey )

            #l_log.info ( "locData.g_oExe._szPAR: " + str ( locData.g_oExe._szPAR ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabPAR::updateTable
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_oPARCur - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateTable ( self, f_oPARCur=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabPAR::updateTable"

        #/ linha selecionada (objeto sítio)
        #/ ----------------------------------------------------------------------------------------
        l_oSel = None


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  limpa a widget
        #*/
        self._qtw.clear ()

        #** ---------------------------------------------------------------------------------------
        #*  configura número de linhas e colunas da tabela
        #*/
        self._qtw.setRowCount ( len ( locData.g_oTabPAR ))
        self._qtw.setColumnCount ( 11 )

        #** ---------------------------------------------------------------------------------------
        #*  configura o cabeçalho da tabela
        #*/
        self._qtw.setHorizontalHeaderLabels ( [ "Sigla", u"Descrição", "Cabeceira\nprincipal",
                                                "Alt Ant\nPTP (m)", "Alt Ant\nPTS (m)", "Dst Ant\nEixo (m)",
                                                "Dst Ant\nPTP (m)", "Dst Ant\nPTS (m)",
                                                "Ang Rampa\n(gr)", "Retardo\n(s)", "Decl.\n(gr)" ] )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setAlternatingRowColors ( True )
        self._qtw.setEditTriggers ( QtGui.QTableWidget.NoEditTriggers )
        self._qtw.setSelectionBehavior ( QtGui.QTableWidget.SelectRows )
        self._qtw.setSelectionMode ( QtGui.QTableWidget.SingleSelection )

        #** ---------------------------------------------------------------------------------------
        #*  carrega a tabela na widget
        #*/
        for l_iRow, l_oPAR in enumerate ( locData.g_oTabPAR ):

            #** -----------------------------------------------------------------------------------
            #*  chave do sítio
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oPAR._szKey )

            #** -----------------------------------------------------------------------------------
            #*/
            if (( f_oPARCur is not None ) and ( f_oPARCur == id ( l_oPAR ))):

                #** -------------------------------------------------------------------------------
                #*/
                l_oSel = l_oItem

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem.setData ( QtCore.Qt.UserRole, QtCore.QVariant ( long ( id ( l_oPAR ))))

            #** -----------------------------------------------------------------------------------
            #*/
            self._qtw.setItem ( l_iRow, 0, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  descrição do sítio
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oPAR._szDescr )

            #** -----------------------------------------------------------------------------------
            #*/
            self._qtw.setItem ( l_iRow, 1, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a cabeceira principal
            #*/
            l_fVal = l_oPAR._iCab0

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 2, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a altura da antena relativo ao ponto toque principal
            #*/
            l_fVal = l_oPAR._fHAnt0

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 3, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a altura da antena relativo ao ponto toque secundário
            #*/
            l_fVal = l_oPAR._fHAnt1

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 4, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a distância da antena ao eixo da pista
            #*/
            l_fVal = l_oPAR._fDstAntEixo

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 5, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a distância da antena ao ponto toque principal
            #*/
            l_fVal = l_oPAR._fDstAntPT0

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 6, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a distância da antena ao ponto toque secundário
            #*/
            l_fVal = l_oPAR._fDstAntPT1

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 7, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém o ângulo da rampa de aproximação
            #*/
            l_fVal = l_oPAR._fAngRampa

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 8, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém o retardo da antena
            #*/
            l_fVal = l_oPAR._aiRetardo [ 0 ]

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 9, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a declinação magnética
            #*/
            l_fVal = l_oPAR._iDecl

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 10, l_oItem )

        #** ---------------------------------------------------------------------------------------
        #*  ajusta o tamanho das colunas pelo conteúdo
        #*/
        self._qtw.resizeColumnsToContents ()

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( l_oSel is not None ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_oSel.setSelected ( True )

            #** -----------------------------------------------------------------------------------
            #*/
            self._qtw.setCurrentItem ( l_oSel )

            #** -----------------------------------------------------------------------------------
            #*/
            self._qtw.scrollToItem ( l_oSel )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "wpgTabPAR" )

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
    l_wpg = wpgTabPAR ()
    #assert ( l_wpg )

#** ----------------------------------------------------------------------------------------------- *#
