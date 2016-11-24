#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wndTabelaExe
#*
#*  Descrição: this class takes care of all interaction with the user
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  well     1997/jun/20  version started
#*  mlabru   2009/set/01  version started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    1997/jun/20  version started
#*  3.01-01  2009/set/01  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  includes
#*  -----------------------------------------------------------------------------------------------
#*/
from __future__ import unicode_literals

#/ Python library
#/ ------------------------------------------------------------------------------------------------
import platform
import sys

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ PyQt library
#/ ------------------------------------------------------------------------------------------------
from PyQt4 import QtCore, QtGui

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.clsTabelaExe as clsTabelaExe
import model.locData as locData
import model.glbDefs as glbDefs
import model.qrcResources as qrcResources

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.dialog.Qt.dlgEditExe as dlgEditExe
import view.dialog.Qt.wndTabelaModel as wndTabelaModel

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  wndTabelaExe::wndTabelaExe
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wndTabelaExe ( wndTabelaModel.wndTabelaModel ):

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaExe::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the main menu
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_parent - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_oTab, f_parent=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wndTabelaExe::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  init super class
        #*/
        wndTabelaModel.wndTabelaModel.__init__ ( self, f_oTab, f_parent )

        #** ---------------------------------------------------------------------------------------
        #*  restaura as configurações da janela
        #*/
        self.configTexts ()

        #** ---------------------------------------------------------------------------------------
        #*  restaura as configurações da janela
        #*/
        self.restoreSettings ()

        #** ---------------------------------------------------------------------------------------
        #*  título da janela
        #*/
        self.setWindowTitle ( u"Tabela de Exercícios" )

        #** ---------------------------------------------------------------------------------------
        #*  conecta click a seleção da linha
        #*/
        self.connect ( self._qtw,
                       QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self.selectExe )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaExe::configTexts
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def configTexts ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wndTabelaExe::configTexts"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._txtSettings = "wndTabelaExe"

        #** ---------------------------------------------------------------------------------------
        #*/
        self._txtAboutTit = "SiPAR - Sobre"
        self._txtAboutMsg = """<b>SiPAR</b> v. {0}
                               <p>Copyright &copy; 1997-2010 ICEA.
                               <p>Simulador Radar de Baixo Custo
                                  para Treinamento de Controladores em
                                  Radar de Aproximação de Precisão (PAR).
                               <p>Python {1} - Qt {2} - PyQt {3} on {4}"""

        self._txtContinueTit = u"SiPAR - Alterações pendentes"
        self._txtContinueMsg = u"Salva alterações pendentes ?"

        self._txtExportTit = "SiPAR - Exporta Tabela de Exercícios"
        self._txtExportMsg = "Arquivos XML do SiPAR (*.xml)"

        self._txtOpenTit = "SiPAR - Abre Tabela de Exercícios"
        self._txtOpenMsg = "Tabela de Exercícios ({0})"

        self._txtRemoveTit = "SiPAR - Apaga exercício"
        self._txtRemoveMsg = "Apaga exercício {0} ?"

        self._txtSaveAsTit = "SiPAR - Salva Tabela de Exercícios"
        self._txtSaveAsMsg = "Tabela de Exercícios ({0})"

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaExe::editAdd
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def editAdd ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wndTabelaExe::editAdd"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  cria a dialog de edição de exercícios
        #*/
        l_Dlg = dlgEditExe.dlgEditExe ( self._oTab, None, self )
        #assert ( l_Dlg )

        #** ---------------------------------------------------------------------------------------
        #*  processa a dialog de edição de exercício (modal)
        #*/
        if ( l_Dlg.exec_ ()):

            #** -----------------------------------------------------------------------------------
            #*  se ok, atualiza a tabela de exercícios
            #*/
            self.updateTable ( id ( l_Dlg._oExe ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaExe::editEdit
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def editEdit ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wndTabelaExe::editEdit"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o exercício atual
        #*/
        l_oExe = self.getCurrentLine ()

        if ( l_oExe is not None ):

            #** -----------------------------------------------------------------------------------
            #*  cria a dialog de edição de exercício
            #*/
            l_Dlg = dlgEditExe.dlgEditExe ( self._oTab, l_oExe, self )
            #assert ( l_Dlg )

            #** -----------------------------------------------------------------------------------
            #*  processa a dialog de edição de exercício (modal)
            #*/
            if ( l_Dlg.exec_ ()):

                #** -------------------------------------------------------------------------------
                #*  se ok, atualiza a tabela de exercícios
                #*/
                self.updateTable ( id ( l_oExe ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaExe::loadInitialFile
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
        #l_szMetodo = "wndTabelaExe::loadInitialFile"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  a tabela de exercícios existe ?
        #*/
        if ( None == self._oTab ):

            #** -----------------------------------------------------------------------------------
            #*  cria a tabela de exercícios
            #*/
            self._oTab = clsTabelaExe.clsTabelaExe ()
            #assert ( None != self._oTab )

            #** -----------------------------------------------------------------------------------
            #*  tenta carregar a tabela padrão
            #*/
            self.loadTabela ( "data/tabExe.DAT", self._oTab )
                                                
        #** ---------------------------------------------------------------------------------------
        #*/
        self.updateTable ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaExe::selectExe
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
        #l_szMetodo = "wndTabelaExe::selectExe"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o exercício selecionado
        #*/
        l_oExe = self.getCurrentLine ()

        if ( l_oExe is not None ):

            #** -----------------------------------------------------------------------------------
            #*  salva o exercício selecionado
            #*/
            locData.g_oExe = l_oExe
            #assert ( locData.g_oExe )

            #l_log.debug ( "locData.g_oExe: " + str ( locData.g_oExe ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaExe::updateTable
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
        #l_szMetodo = "wndTabelaExe::updateTable"

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
        #*/
        self._qtw.clear ()

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setRowCount ( len ( self._oTab ))

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setColumnCount ( 10 )
        self._qtw.setHorizontalHeaderLabels ( [ "Sigla", u"Descrição", u"Sítio PAR", "Cabec.",
                                                "Int Vento\n(kt)", "Dir Vento\n(gr)", "Aeronave",
                                                "Dist\n(NM)", "Afst Eixo\n(m)", "Altura\n(ft)" ] )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setAlternatingRowColors ( True )
        self._qtw.setEditTriggers ( QtGui.QTableWidget.NoEditTriggers )
        self._qtw.setSelectionBehavior ( QtGui.QTableWidget.SelectRows )
        self._qtw.setSelectionMode ( QtGui.QTableWidget.SingleSelection )

        #** ---------------------------------------------------------------------------------------
        #*/
        for l_iRow, l_oExe in enumerate ( self._oTab ):

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
            l_iVal = l_oExe._iCab

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_iVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 3, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  velocidade do vento
            #*/
            l_fVal = l_oExe._fVentoVel

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 4, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  direção do vento
            #*/
            l_fVal = l_oExe._fVentoDir

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
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
            l_fVal = l_oExe._fGateDist

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 7, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  afastamento do eixo da pista
            #*/
            l_fVal = l_oExe._fGateAfst

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 8, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  altura
            #*/
            l_fVal = l_oExe._fGateAlt

            #** -----------------------------------------------------------------------------------
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_fVal ))
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

#** ----------------------------------------------------------------------------------------------- *#
