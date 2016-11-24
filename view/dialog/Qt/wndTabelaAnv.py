#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wndTabelaAnv
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
import model.clsExe as clsExe
import model.clsTabelaAnv as clsTabelaAnv
import model.locData as locData
import model.qrcResources as qrcResources

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.dialog.Qt.dlgEditAnv as dlgEditAnv
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
#*  wndTabelaAnv::wndTabelaAnv
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wndTabelaAnv ( wndTabelaModel.wndTabelaModel ):

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaAnv::__init__
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
        #l_szMetodo = "wndTabelaAnv::__init__"


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
        self.setWindowTitle ( "Tabela de Aeronaves" )

        #** ---------------------------------------------------------------------------------------
        #*  conecta click a seleção da linha
        #*/
        self.connect ( self._qtw,
                       QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self.selectAnv )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaAnv::configTexts
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
        #l_szMetodo = "wndTabelaAnv::configTexts"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._txtSettings = "wndTabelaAnv"

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

        self._txtExportTit = "SiPAR - Exporta Tabela de Aeronaves"
        self._txtExportMsg = "Arquivos XML do SiPAR (*.xml)"

        self._txtOpenTit = "SiPAR - Abre Tabela de Aeronaves"
        self._txtOpenMsg = "Tabela de Aeronaves ({0})"

        self._txtRemoveTit = "SiPAR - Apaga aeronave"
        self._txtRemoveMsg = "Apaga aeronave {0} ?"

        self._txtSaveAsTit = "SiPAR - Salva Tabela de Aeronaves"
        self._txtSaveAsMsg = "Tabela de Aeronaves ({0})"

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaAnv::editAdd
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_parent - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def editAdd ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wndTabelaAnv::editAdd"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  cria a dialog de edição de aeronaves
        #*/
        l_Dlg = dlgEditAnv.dlgEditAnv ( self._oTab, None, self)
        #assert ( l_Dlg )

        #** ---------------------------------------------------------------------------------------
        #*  processa a dialog de edição da aeronave (modal)
        #*/
        if ( l_Dlg.exec_ ()):

            #** -----------------------------------------------------------------------------------
            #*  atualiza a tabela de aeronaves
            #*/
            self.updateTable ( id ( l_Dlg._oAnv ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaAnv::editEdit
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_parent - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def editEdit ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wndTabelaAnv::editEdit"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a aeronave selecionada
        #*/
        l_oAnv = self.getCurrentLine ()

        if ( l_oAnv is not None ):

            #** -----------------------------------------------------------------------------------
            #*  cria a dialog de edição de aeronave
            #*/
            l_Dlg = dlgEditAnv.dlgEditAnv ( self._oTab, l_oAnv, self )
            #assert ( l_Dlg )

            #** -----------------------------------------------------------------------------------
            #*  edição ok ?
            #*/
            if ( l_Dlg.exec_ ()):

                #** -------------------------------------------------------------------------------
                #*  atualiza a tabela de aeronaves
                #*/
                self.updateTable ( id ( l_oAnv ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaAnv::loadInitialFile
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
        #l_szMetodo = "wndTabelaAnv::loadInitialFile"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  a tabela de aeronaves existe ?
        #*/
        if ( None == self._oTab ):

            #** -----------------------------------------------------------------------------------
            #*  cria a tabela de aeronaves
            #*/
            self._oTab = clsTabelaAnv.clsTabelaAnv ()
            #assert ( None != self._oTab )

            #** -----------------------------------------------------------------------------------
            #*  tenta carregar a tabela padrão
            #*/
            self.loadTabela ( "data/tabAnv.DAT", self._oTab )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza a tabela
        #*/
        self.updateTable ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaAnv::selectAnv
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
        #l_szMetodo = "wndTabelaAnv::selectAnv"


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
        #*  obtém a aeronave selecionada
        #*/
        l_oAnv = self.getCurrentLine ()

        if ( l_oAnv is not None ):

            #** ---------------------------------------------------------------------------------------
            #*  o exercício não existe ?
            #*/
            if ( None == locData.g_oExe ):

                #** -----------------------------------------------------------------------------------
                #*  cria um exercício
                #*/
                locData.g_oExe = clsExe.clsExe ()
                #assert ( locData.g_oExe )

            #** -----------------------------------------------------------------------------------
            #*  salva a aeronave selecionada
            #*/
            locData.g_oExe._oAnv = l_oAnv
            #assert ( locData.g_oExe._oAnv )

            #l_log.debug ( "locData.g_oExe._oAnv: " + str ( locData.g_oExe._oAnv ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaAnv::updateTable
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_iCurId - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateTable ( self, f_iCurId=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wndTabelaAnv::updateTable"

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
        #*/
        self._qtw.clear ()

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setRowCount ( len ( self._oTab ))

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setColumnCount ( 7 )

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
        #*  percorre a tabela de aeronaves...
        #*/
        for l_iRow, l_oAnv in enumerate ( self._oTab ):

            #** -----------------------------------------------------------------------------------
            #*  obtém o item correspondente a chave atual
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oAnv._szKey )

            #** -----------------------------------------------------------------------------------
            #*  o item selecionado é a aeronave atual ?
            #*/
            if (( f_iCurId is not None ) and ( id ( l_oAnv ) == f_iCurId )):

                #** -------------------------------------------------------------------------------
                #*  salva o item selecionado
                #*/
                l_oSel = l_oItem

            #** -----------------------------------------------------------------------------------
            #*  configura a chave da aeronave (sigla)
            #*/
            l_oItem.setData ( QtCore.Qt.UserRole, QtCore.QVariant ( long ( id ( l_oAnv ))))

            self._qtw.setItem ( l_iRow, 0, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  configura a descrição
            #*/
            l_oItem = QtGui.QTableWidgetItem ( l_oAnv._szDescr )

            self._qtw.setItem ( l_iRow, 1, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a velocidade de aproximação
            #*/
            l_dVal = l_oAnv._fVelApx

            #** -----------------------------------------------------------------------------------
            #*  configura a velocidade de aproximação
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 2, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a razão máxima de subida
            #*/
            l_dVal = l_oAnv._fRazMaxSub

            #** -----------------------------------------------------------------------------------
            #*  configura a razão máxima de subida
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 3, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a razão máxima de descida
            #*/
            l_dVal = l_oAnv._fRazMaxDesc

            #** -----------------------------------------------------------------------------------
            #*  configura a razão máxima de descida
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 4, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém a razão máxima de curva
            #*/
            l_dVal = l_oAnv._fRazMaxCurv

            #** -----------------------------------------------------------------------------------
            #*  configura a razão máxima de curva
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 5, l_oItem )

            #** -----------------------------------------------------------------------------------
            #*  obtém o teto de serviço
            #*/
            l_dVal = l_oAnv._fTetoServ

            #** -----------------------------------------------------------------------------------
            #*  configura o teto de serviço
            #*/
            l_oItem = QtGui.QTableWidgetItem ( "{0}".format ( l_dVal ))
            l_oItem.setTextAlignment ( QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter )

            self._qtw.setItem ( l_iRow, 6, l_oItem )

        #** ---------------------------------------------------------------------------------------
        #*  ajusta o tamanho das colunas pelo conteúdo
        #*/
        self._qtw.resizeColumnsToContents ()

        #** ---------------------------------------------------------------------------------------
        #*  havia uma linha selecionada ?
        #*/
        if ( l_oSel is not None ):

            #** -----------------------------------------------------------------------------------
            #*  seta flag de seleção
            #*/
            l_oSel.setSelected ( True )

            #** -----------------------------------------------------------------------------------
            #*  seta a linha atual
            #*/
            self._qtw.setCurrentItem ( l_oSel )

            #** -----------------------------------------------------------------------------------
            #*  posiciona na linha selecionada
            #*/
            self._qtw.scrollToItem ( l_oSel )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** ----------------------------------------------------------------------------------------------- *#
