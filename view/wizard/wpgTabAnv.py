#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wpgTabAnv
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
import model.clsTabelaAnv as clsTabelaAnv
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
#*  wpgTabAnv::wpgTabAnv
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wpgTabAnv ( acmeWizardPage.acmeWizardPage ):

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabAnv::__init__
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
        l_szMetodo = "wpgTabAnv::__init__"


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
                                              u"Seleção da aeronave"
                                               "</b></font></center>" ))
        #assert ( l_lblTitle )

        #** ---------------------------------------------------------------------------------------
        #*  cria a tabela de aeronaves
        #*/
        locData.g_oTabAnv = clsTabelaAnv.clsTabelaAnv ()
        #assert ( None != locData.g_oTabAnv )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw = QtGui.QTableWidget ( f_wizard )
        #assert ( self._qtw )

        #** ---------------------------------------------------------------------------------------
        #*/
        self.setFocusProxy ( self._qtw )

        #** ---------------------------------------------------------------------------------------
        #*/
        #l_lblMsg = QtGui.QLabel ( self.tr ( "Escolha uma aeronave da lista." ))
        ##assert ( l_lblMsg )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_glo = QtGui.QGridLayout ()
        #assert ( l_glo )

        l_glo.addWidget ( l_lblTitle, 0, 0, 1, 2 )
        l_glo.setRowMinimumHeight ( 1, 10 )

        l_glo.addWidget ( self._qtw, 3, 0)
        l_glo.setRowMinimumHeight ( 4, 10 )

        #l_glo.addWidget ( l_lblMsg, 6, 0, 1, 2 )
        #l_glo.setRowStretch ( 6, 1 )

        self.setLayout ( l_glo )

        #** ---------------------------------------------------------------------------------------
        #*  conecta click a seleção da linha
        #*/
        self.connect ( self._qtw, QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self.selectAnv )

        self.connect ( self._qtw, QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self,      QtCore.SIGNAL ( "completeStateChanged()" ))

        #** ---------------------------------------------------------------------------------------
        #*  carrega a tabela de aeronaves
        #*/
        self.loadInitialFile ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabAnv::isComplete
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def isComplete ( self ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgTabAnv::isComplete"


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
        return ( None != locData.g_oExe._oAnv )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabAnv::loadInitialFile
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
        l_szMetodo = "wpgTabAnv::loadInitialFile"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  recupera a última tabela de aeronaves utilizada
        #*/
        l_szFName = QtCore.QString ( "data/tabAnv.DAT" )

        #** ---------------------------------------------------------------------------------------
        #*  tabela existe ?
        #*/
        if (( l_szFName ) and ( QtCore.QFile.exists ( l_szFName ))):

            #** -----------------------------------------------------------------------------------
            #*  carrega a tabela
            #*/
            l_bOk, l_szMsg = locData.g_oTabAnv.load ( l_szFName )

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
    #*  wpgTabAnv::nextPage
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def nextPage ( self ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgTabAnv::nextPage"


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
        return ( self._oWizard._pagGate )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabAnv::resetPage
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def resetPage ( self ):

        #/ nome do metodo (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgTabAnv::resetPage"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        #self._qtw.clear ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabAnv::selectAnv
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_parent - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def selectAnv ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgTabAnv::selectAnv"


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
        #assert ( locData.g_oTabAnv )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o número da linha selecionada da tabela
        #*/
        l_iRow = self._qtw.currentRow ()
        #l_log.debug ( "l_iRow: " + str ( l_iRow ))

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
            #l_log.debug ( "l_ID: " + str ( l_ID ))

            #l_log.debug ( "locData.g_oExe._oAnv: " + str ( locData.g_oExe._oAnv ))
            #** -----------------------------------------------------------------------------------
            #*  obtém a aeronave selecionada da tabela pelo id
            #*/
            locData.g_oExe._oAnv = locData.g_oTabAnv.itemFromId ( l_ID )
            #assert ( locData.g_oExe._oAnv )

            #l_log.debug ( "locData.g_oExe._oAnv: " + str ( locData.g_oExe._oAnv ))

            #** -----------------------------------------------------------------------------------
            #*  obtém a chave da aeronave selecionada
            #*/
            locData.g_oExe._szAnv = locData.g_oExe._oAnv._szKey

            #l_log.debug ( "locData.g_oExe._szAnv: " + str ( locData.g_oExe._szAnv ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabAnv::updateTable
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_oAnvCur - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateTable ( self, f_oAnvCur=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "wpgTabAnv::updateTable"

        #/ linha selecionada (objeto aeronave)
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
        self._qtw.setRowCount ( len ( locData.g_oTabAnv ))
        self._qtw.setColumnCount ( 7 )

        #** ---------------------------------------------------------------------------------------
        #*  configura o cabeçalho da tabela
        #*/
        self._qtw.setHorizontalHeaderLabels ( [ "Sigla", u"Descrição", "VelApx\n(kt)",
                                                "RazMaxSub\n(ft/min)", "RazMaxDesc\n(ft/min)",
                                                "RazMaxCurv\n(gr/seg)", "TetoServ\n(ft)" ] )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setAlternatingRowColors ( True )
        self._qtw.setEditTriggers ( QtGui.QTableWidget.NoEditTriggers )
        self._qtw.setSelectionBehavior ( QtGui.QTableWidget.SelectRows )
        self._qtw.setSelectionMode ( QtGui.QTableWidget.SingleSelection )

        #** ---------------------------------------------------------------------------------------
        #*  carrega a tabela na widget
        #*/
        for l_iRow, l_oAnv in enumerate ( locData.g_oTabAnv ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oAnv._szKey )

            #** -----------------------------------------------------------------------------------
            #*/
            if (( f_oAnvCur is not None ) and ( f_oAnvCur == id ( l_oAnv ))):

                #** -------------------------------------------------------------------------------
                #*/
                l_oSel = l_oItem

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem.setData ( QtCore.Qt.UserRole, QtCore.QVariant ( long ( id ( l_oAnv ))))

            #** -----------------------------------------------------------------------------------
            #*/
            self._qtw.setItem ( l_iRow, 0, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oAnv._szDescr )

            #** -----------------------------------------------------------------------------------
            #*/
            self._qtw.setItem ( l_iRow, 1, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a velocidade de aproximação
            #*/
            l_dVal = l_oAnv._fVelApx

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 2, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a razão máxima de subida
            #*/
            l_dVal = l_oAnv._fRazMaxSub

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 3, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a razão máxima de descida
            #*/
            l_dVal = l_oAnv._fRazMaxDesc

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 4, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a razão máxima de curva
            #*/
            l_dVal = l_oAnv._fRazMaxCurv

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 5, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém o teto de serviço
            #*/
            l_dVal = l_oAnv._fTetoServ

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )
            self._qtw.setItem ( l_iRow, 6, l_oItem )

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
logger = logging.getLogger ( "wpgTabAnv" )

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
    l_wpg = wpgTabAnv ()
    #assert ( l_wpg )

#** ----------------------------------------------------------------------------------------------- *#