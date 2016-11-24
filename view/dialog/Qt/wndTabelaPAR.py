#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: wndTabelaPAR
#*
#*  Descrição: this class takes care of all interaction with the user
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  well     1997/fev/12  version started
#*  mlabru   2009/set/01  version started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    1997/fev/12  version started
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
import model.clsTabelaPAR as clsTabelaPAR
import model.locData as locData
import model.qrcResources as qrcResources

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.dialog.Qt.dlgEditPAR as dlgEditPAR
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
#*  wndTabelaPAR::wndTabelaPAR
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class wndTabelaPAR ( wndTabelaModel.wndTabelaModel ):

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaPAR::__init__
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
        #l_szMetodo = "wndTabelaPAR::__init__"


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
        self.setWindowTitle ( u"Tabela de Sítios PAR" )

        #** ---------------------------------------------------------------------------------------
        #*  conecta click a seleção da linha
        #*/
        self.connect ( self._qtw,
                       QtCore.SIGNAL ( "itemSelectionChanged()" ),
                       self.selectPAR )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaPAR::configTexts
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
        #l_szMetodo = "wndTabelaPAR::configTexts"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._txtSettings = "wndTabelaPAR"

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

        self._txtExportTit = "SiPAR - Exporta Tabela de Sítios PAR"
        self._txtExportMsg = "Arquivos XML do SiPAR (*.xml)"

        self._txtOpenTit = "SiPAR - Abre Tabela de Sítios PAR"
        self._txtOpenMsg = "Tabela de Sítios PAR ({0})"

        self._txtRemoveTit = "SiPAR - Apaga sítio PAR"
        self._txtRemoveMsg = "Apaga sítio PAR {0} ?"

        self._txtSaveAsTit = "SiPAR - Salva Tabela de Sítios PAR"
        self._txtSaveAsMsg = "Tabela de Sítios PAR ({0})"

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaPAR::editAdd
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
        #l_szMetodo = "wndTabelaPAR::editAdd"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  cria a dialog de edição de sítios
        #*/
        l_Dlg = dlgEditPAR.dlgEditPAR ( self._oTab, None, self)
        #assert ( l_Dlg )

        #** ---------------------------------------------------------------------------------------
        #*  processa a dialog de edição da sítio (modal)
        #*/
        if ( l_Dlg.exec_ ()):

            #** -----------------------------------------------------------------------------------
            #*  atualiza a tabela de sítios
            #*/
            self.updateTable ( id ( l_Dlg._oPAR ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaPAR::editEdit
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
        #l_szMetodo = "wndTabelaPAR::editEdit"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a sítio atual
        #*/
        l_oPAR = self.getCurrentLine ()

        if ( l_oPAR is not None ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_Dlg = dlgEditPAR.dlgEditPAR ( self._oTab, l_oPAR, self )
            #assert ( l_Dlg )

            #** -----------------------------------------------------------------------------------
            #*/
            if ( l_Dlg.exec_ ()):

                #** -------------------------------------------------------------------------------
                #*/
                self.updateTable ( id ( l_oPAR ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaPAR::loadInitialFile
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def loadInitialFile ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "wndTabelaPAR::loadInitialFile"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  a tabela de PAR's existe ?
        #*/
        if ( None == self._oTab ):

            #** -----------------------------------------------------------------------------------
            #*  cria a tabela de PAR's
            #*/
            self._oTab = clsTabelaPAR.clsTabelaPAR ()
            #assert ( None != self._oTab )

            #** -----------------------------------------------------------------------------------
            #*  tenta carregar a tabela padrão
            #*/
            self.loadTabela ( "data/tabPAR.DAT", self._oTab )
                                                
        #** ---------------------------------------------------------------------------------------
        #*/
        self.updateTable ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaPAR::selectPAR
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
        #l_szMetodo = "wndTabelaPAR::selectPAR"


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
        #*  obtém o sítio PAR selecionado
        #*/
        l_oPAR = self.getCurrentLine ()

        if ( l_oPAR is not None ):

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
            #*  salva o sítio PAR selecionada
            #*/
            locData.g_oExe._oPAR = l_oPAR
            #assert ( locData.g_oExe._oPAR )

            #l_log.debug ( "locData.g_oExe._oPAR: " + str ( locData.g_oExe._oPAR ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  wndTabelaPAR::updateTable
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
        #l_szMetodo = "wndTabelaPAR::updateTable"

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
        #*/
        self._qtw.clear ()

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setRowCount ( len ( self._oTab ))

        #** ---------------------------------------------------------------------------------------
        #*/
        self._qtw.setColumnCount ( 11 )

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
        #*/
        for l_iRow, l_oPAR in enumerate ( self._oTab ):

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

#** ----------------------------------------------------------------------------------------------- *#
