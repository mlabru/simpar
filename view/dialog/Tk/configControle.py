#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: configControle
#*
#*  Descrição: DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração       
#*  -----------------------------------------------------------------------------------------------
#*  well     1997/fev/12  versão 1.0 started
#*  mlabru   2009/set/01  versão 3.0 started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    1997/fev/12  versão inicial (DOS/Modula-2)
#*  3.01-01  2009/set/01  versão para Linux
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  for standalone bootstrap process
#*  -----------------------------------------------------------------------------------------------
#*/
if ( '__main__' == __name__ ):

    #/ Python Library
    #/ --------------------------------------------------------------------------------------------
    import sys

    sys.path.insert ( 0, ".." )

#** -----------------------------------------------------------------------------------------------
#*  includes
#*  -----------------------------------------------------------------------------------------------
#*/

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ Tkinter (gui library)
#/ ------------------------------------------------------------------------------------------------
import Tkinter

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.locDefs as locDefs

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.dialog.Tk.dlgConfig as dlgConfig
import view.dialog.Tk.tkUtils as tkUtils

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  configControle::configControle
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class configControle ( dlgConfig.dlgConfig ): 

    #** -------------------------------------------------------------------------------------------
    #*  configControle::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self ):

        #/ nome do método (logger)
        #/ -----------------------------------------------------------------------------------------
        #l_szMetodo = "configControle::__init__"


        #** ----------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ----------------------------------------------------------------------------------------
        #*  inicia a superclass
        #*/
        dlgConfig.dlgConfig.__init__ ( self )

        #** ----------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  configControle::criaWinCfg
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_tkRoot - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def criaWinCfg ( self, f_tkRoot ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "configControle::criaWinCfg"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  widgets initialization
        #*/
        self._frmM = Tkinter.Frame ( f_tkRoot, bg = "blue" )
        self._frmM.pack ()

        #** ---------------------------------------------------------------------------------------
        #*  labels
        #*/
        l_lbl1 = Tkinter.Label ( self._frmM, background = "#0000ff",
                                             font = "{MS Sans Serif} 20",
                                             foreground = "#ffff00",
                                             text = locDefs.xTXT_Tit )
        l_lbl1.grid ( row = 1, column = 0, columnspan = 4 )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_lbl2 = Tkinter.Label ( self._frmM, background = "#0000ff",
                                             font = "{MS Sans Serif} 16",
                                             foreground = "#ffff00",
                                             text = u"Simulador para Treinamento de" )
        l_lbl2.grid ( row = 2, column = 0, columnspan = 4 )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_lbl3 = Tkinter.Label ( self._frmM, background = "#0000ff",
                                             font = "{MS Sans Serif} 16",
                                             foreground = "#ffff00",
                                             text = u"Controladores em Radar de" )
        l_lbl3.grid ( row = 3, column = 0, columnspan = 4 )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_lbl4 = Tkinter.Label ( self._frmM, background = "#0000ff",
                                             font = "{MS Sans Serif} 16",
                                             foreground = "#ffff00",
                                             text = u"Aproximação de Precisão" )
        l_lbl4.grid ( row = 4, column = 0, columnspan = 4 )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_lbl6 = Tkinter.Label ( self._frmM, background = "#0000ff",
                                             font = "{MS Sans Serif} 14",
                                             foreground = "#ffff00",
                                             text = "(C) ITA - ICEA 2010" )
        l_lbl6.grid ( row = 6, column = 0, columnspan = 4 )

        #** ---------------------------------------------------------------------------------------
        #*  frame canal
        #*/
        l_frmChannel = Tkinter.Frame ( self._frmM, bd = 2, relief = Tkinter.RAISED )
        l_frmChannel.pack ()
        l_frmChannel.grid ( column = 0, row = 9, columnspan = 4, sticky = "news" )

        #** ---------------------------------------------------------------------------------------
        #*  label canal
        #*/
        #l_lbl7 = Tkinter.Label ( l_frmChannel, width = 16, text = "Canal" )
        #l_lbl7.pack ( side = Tkinter.LEFT, padx = 5 )

        #** ---------------------------------------------------------------------------------------
        #*  button (Canal) (Tkinter.DISABLED)
        #*/
        l_lbl7 = Tkinter.Button ( l_frmChannel, width = 16, text = "Canal", state = Tkinter.NORMAL )
        l_lbl7.pack ( side = Tkinter.LEFT, padx = 5 )

        #** ---------------------------------------------------------------------------------------
        #*  listbox canal
        #*/
        self._lbxCanal = Tkinter.Listbox ( l_frmChannel, height = 2, width = 16 )
        self._lbxCanal.pack ( side = Tkinter.RIGHT, fill = Tkinter.Y, padx = 5 )

        #** ---------------------------------------------------------------------------------------
        #*  listbox populate
        #*/
        for l_iI in xrange ( 3, 93 ): 

            self._lbxCanal.insert ( Tkinter.END, l_iI )

        #** ---------------------------------------------------------------------------------------
        #*  scrollbar canal
        #*/
        l_scl = Tkinter.Scrollbar ( l_frmChannel, command = self._lbxCanal.yview )
        l_scl.pack ( side = Tkinter.RIGHT, fill = Tkinter.Y, padx = 5 )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._lbxCanal.configure ( yscrollcommand = l_scl.set )
        self._lbxCanal.selection_set ( 0 )

        #** ---------------------------------------------------------------------------------------
        #*  frame buttons
        #*/
        l_frmButtons = Tkinter.Frame ( self._frmM, bd = 2, relief = Tkinter.RAISED )
        l_frmButtons.pack ()
        l_frmButtons.grid ( column = 0, row = 10, columnspan = 4, sticky = "news" )

        #** ---------------------------------------------------------------------------------------
        #*  button (Ok)
        #*/
        self._btnOk = Tkinter.Button ( l_frmButtons, width = 16, text = "Ok", command = self.doOk )
        self._btnOk.pack ( side = Tkinter.LEFT, padx = 5, pady = 3 )

        #** ---------------------------------------------------------------------------------------
        #*  button (Cancel)
        #*/
        l_btnCancel = Tkinter.Button ( l_frmButtons, width = 16, text = "Cancel", command = self.doCancel )
        l_btnCancel.pack ( side = Tkinter.RIGHT, padx = 5, pady = 3 )

        #** ---------------------------------------------------------------------------------------
        #*  resize behavior (self._frmM)
        #*/
        self._frmM.grid_rowconfigure ( 0, minsize = 20 )
        self._frmM.grid_rowconfigure ( 1, minsize = 40 )
        self._frmM.grid_rowconfigure ( 2, minsize = 40 )
        self._frmM.grid_rowconfigure ( 3, minsize = 40 )
        self._frmM.grid_rowconfigure ( 4, minsize = 40 )
        self._frmM.grid_rowconfigure ( 5, minsize = 20 )
        self._frmM.grid_rowconfigure ( 6, minsize = 40 )
        self._frmM.grid_rowconfigure ( 7, minsize = 20 )

        #** ---------------------------------------------------------------------------------------
        #*/
        f_tkRoot.update ()

        #** ---------------------------------------------------------------------------------------
        #*  center in screen
        #*/
        tkUtils.center_toplevel_in_screen ( f_tkRoot )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  configControle::startConfigPanel
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def startConfigPanel ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "configControle::startConfigPanel"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  load Tkinter
        #*/
        l_tkRoot = Tkinter.Tk ()
        l_tkRoot.configure ( bg = "blue" )

        #** ---------------------------------------------------------------------------------------
        #*  terminal de pilotagem ?
        #*/
        l_tkRoot.title ( locDefs.xTXT_Tit + " [Controle]" )

        #** ---------------------------------------------------------------------------------------
        #*  cria a janela de configuração
        #*/
        self.criaWinCfg ( l_tkRoot )

        #** ---------------------------------------------------------------------------------------
        #*  processa o diálogo
        #*/
        l_tkRoot.mainloop ()

        #** ---------------------------------------------------------------------------------------
        #*  obtém o nome do arquivo de exercício selecionado
        #*/
        l_iCanal = int ( self._lbxCanal.curselection () [ 0 ] ) + 3
        #l_log.info ( "Canal de dados: " + str ( l_iCanal ))

        #** ---------------------------------------------------------------------------------------
        #*  unload Tkinter
        #*/
        l_tkRoot.destroy ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  Ok ?
        #*/
        if ( self._bOk ):

            #** -----------------------------------------------------------------------------------
            #*/
            return ( True, l_iCanal )

        #** ---------------------------------------------------------------------------------------
        #*  senao, usuario cancelou  
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            return ( False, -1 )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "configControle" )

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
    #*/
    x = configControle ()
    y, z = x.startConfigPanel () 
 
    #** -------------------------------------------------------------------------------------------
    #*/
    print x
    print y, z

#** ----------------------------------------------------------------------------------------------- *#
