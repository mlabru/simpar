#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wpgTabExe
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
import math

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ PyQt
#/ ------------------------------------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.clsTabelaExe as clsTabelaExe
import model.locData as locData
import model.glbDefs as glbDefs

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
#*  wpgTabExe::wpgTabExe
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wpgTabExe ( acmeWizardPage.acmeWizardPage ):

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabExe::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_wizard - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_wizard=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabExe::__init__"


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
                                              u"Seleção do exercício"
                                               "</b></font></center>" ))
        #assert ( l_lblTitle )

        #** ---------------------------------------------------------------------------------------
        #*  cria a tabela de exercícios
        #*/
        locData.g_oTabExe = clsTabelaExe.clsTabelaExe ()
        #assert ( None != locData.g_oTabExe )

        #** ---------------------------------------------------------------------------------------
        #*  cabeceiras
        #*/
        self._aiCab = [ 'P', 'S' ]

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw = QtGui.QTableWidget ( f_wizard )
        #assert ( self._qtw )

        #** ---------------------------------------------------------------------------------------
        #*/
        self.setFocusProxy ( self._qtw )

        #** ---------------------------------------------------------------------------------------
        #*/
        #l_lblMsg = QtGui.QLabel ( self.tr ( u"Escolha um exercício da lista." ))
        ##assert ( l_lblMsg )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_lay = QtGui.QGridLayout ()
        #assert ( l_lay )

        l_lay.addWidget ( l_lblTitle, 0, 0, 1, 2 )
        l_lay.setRowMinimumHeight ( 1, 10 )

        l_lay.addWidget ( self._qtw, 3, 0)
        l_lay.setRowMinimumHeight ( 4, 10 )

        #l_lay.addWidget ( l_lblMsg, 6, 0, 1, 2 )
        #l_lay.setRowStretch ( 6, 1 )

        self.setLayout ( l_lay )

        #** ---------------------------------------------------------------------------------------
        #*  conecta click a seleção da linha
        #*/
        self.connect ( self._qtw, QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self.selectExe )

        self.connect ( self._qtw, QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self,      QtCore.SIGNAL ( "completeStateChanged()" ))

        #** ---------------------------------------------------------------------------------------
        #*  carrega a tabela de exercícios
        #*/
        self.loadInitialFile ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabExe::isComplete
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def isComplete ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabExe::isComplete"

        #/ ok flag
        #/ ----------------------------------------------------------------------------------------
        l_bOk = False


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  existe uma linha selecionada e um exercício carregado ?
        #*/
        if (( self._qtw.currentRow () > -1 ) and ( None != locData.g_oExe )):

            #** -----------------------------------------------------------------------------------
            #*  verifica se as tabelas de aeronaves e PAR's estão carregadas
            #*/
            #assert ( locData.g_oTabPAR )
            #assert ( locData.g_oTabAnv )

            #** -----------------------------------------------------------------------------------
            #*  tudo certo... 
            #*/
            l_bOk = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( l_bOk )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabExe::loadInitialFile
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
        #l_szMetodo = "wpgTabExe::loadInitialFile"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  recupera a última tabela de exercícios utilizada
        #*/
        l_szFName = QtCore.QString ( "data/tabExe.DAT" )

        #** ---------------------------------------------------------------------------------------
        #*  tabela existe ?
        #*/
        if (( l_szFName ) and ( QtCore.QFile.exists ( l_szFName ))):

            #** -----------------------------------------------------------------------------------
            #*  carrega a tabela
            #*/
            l_bOk, l_szMsg = locData.g_oTabExe.load ( l_szFName )

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
    #*  wpgTabExe::nextPage
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def nextPage ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabExe::nextPage"


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
        return ( self._oWizard._pagCanal )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabExe::selectExe
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def selectExe ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabExe::selectExe"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

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

            #l_log.debug ( "locData.g_oExe: " + str ( locData.g_oExe ))
            #** -----------------------------------------------------------------------------------
            #*  obtém o exercício selecionado da tabela pelo id
            #*/
            locData.g_oExe = locData.g_oTabExe.itemFromId ( l_ID )
            #assert ( locData.g_oExe )

            #l_log.debug ( "locData.g_oExe: " + str ( locData.g_oExe ))

            #** -----------------------------------------------------------------------------------
            #*  obtém a aeronave do exercício selecionado
            #*/
            locData.g_oExe._oAnv = locData.g_oTabAnv.itemFromKey ( locData.g_oExe._szAnv )
            #assert ( locData.g_oExe._oAnv )

            #l_log.debug ( "locData.g_oExe._oAnv: " + str ( locData.g_oExe._oAnv ))

            #** -----------------------------------------------------------------------------------
            #*  obtém o PAR do exercício selecionado
            #*/
            locData.g_oExe._oPAR = locData.g_oTabPAR.itemFromKey ( locData.g_oExe._szPAR )
            #assert ( locData.g_oExe._oPAR )

            #l_log.debug ( "locData.g_oExe._oPAR: " + str ( locData.g_oExe._oPAR ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wpgTabExe::updateTable
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_oExeCur - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateTable ( self, f_oExeCur=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wpgTabExe::updateTable"

        #/ linha selecionada (objeto exercício)
        #/ ----------------------------------------------------------------------------------------
        l_oSel = None


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
        #assert ( locData.g_oTabExe )

        #** ---------------------------------------------------------------------------------------
        #*  limpa a widget
        #*/
        self._qtw.clear ()

        #** ---------------------------------------------------------------------------------------
        #*  configura número de linhas e colunas da tabela
        #*/
        self._qtw.setGeometry ( QtCore.QRect ( 0, 0, 600, 440 ))

        self._qtw.setRowCount ( len ( locData.g_oTabExe ))
        self._qtw.setColumnCount ( 10 )

        #** ---------------------------------------------------------------------------------------
        #*  configura o cabeçalho da tabela
        #*/
        self._qtw.setHorizontalHeaderLabels ( [ "Sigla", u"Descrição", u"Sítio PAR", "Cabec.\nem uso",
                                                "Int Vento\n(kt)", "Dir Vento\n(gr)", "Aeronave",
                                                "Dist\n(NM)", "Afst Eixo\n(m)", "Altura\n(ft)" ] )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setAlternatingRowColors ( True )
        self._qtw.setEditTriggers ( QtGui.QTableWidget.NoEditTriggers )
        self._qtw.setSelectionBehavior ( QtGui.QTableWidget.SelectRows )
        self._qtw.setSelectionMode ( QtGui.QTableWidget.SingleSelection )

        #** ---------------------------------------------------------------------------------------
        #*  carrega a tabela na widget
        #*/
        for l_iRow, l_oExe in enumerate ( locData.g_oTabExe ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oExe._szKey )

            #** -----------------------------------------------------------------------------------
            #*/
            if (( f_oExeCur is not None ) and ( f_oExeCur == id ( l_oExe ))):

                #** -------------------------------------------------------------------------------
                #*/
                l_oSel = l_oItem

            #** -----------------------------------------------------------------------------------
            #*  chave
            #*/
            l_oItem.setData ( QtCore.Qt.UserRole, QtCore.QVariant ( long ( id ( l_oExe ))))

            self._qtw.setItem ( l_iRow, 0, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  descrição
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oExe._szDescr )

            self._qtw.setItem ( l_iRow, 1, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  sítio PAR
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oExe._szPAR )
            l_oItem.setTextAlignment ( QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 2, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  cabeceira em uso
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( self._aiCab [ l_oExe._iCab ] ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 3, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  velocidade do vento
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_oExe._fVentoVel ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 4, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  direção do vento
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_oExe._fVentoDir ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 5, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  aeronave
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oExe._szAnv )
            l_oItem.setTextAlignment ( QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 6, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  distância
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_oExe._fGateDist ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 7, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  afastamento do eixo da pista
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_oExe._fGateAfst ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 8, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  altura
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_oExe._fGateAlt ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 9, l_oItem )

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
logger = logging.getLogger ( "wpgTabExe" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
