#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: controlControle
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
#*  includes
#*  -----------------------------------------------------------------------------------------------
#*/

#/ Python library
#/ ------------------------------------------------------------------------------------------------
import sys
import time

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ pyGame (biblioteca gráfica)
#/ ------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *

#/ SiPAR / control
#/ ------------------------------------------------------------------------------------------------
import control.controlManager as controlManager
import control.flightControle as flightControle
import control.netManager as netManager

import control.simStats as simStats
import control.simTime as simTime

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.glbData as glbData
import model.glbDefs as glbDefs

import model.modelControle as modelControle

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.dialog.Tk.configControle as configControle
import view.dialog.Tk.dlgConfirm as dlgConfirm

import view.viewControle as viewControle

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  controlControle::controlControle
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class controlControle ( controlManager.controlManager ):

    #** -------------------------------------------------------------------------------------------
    #*  controlControle::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the display
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlControle::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  inicia a superclass
        #*/
        controlManager.controlManager.__init__ ( self, "SiPAR.cfg" )

        #** ---------------------------------------------------------------------------------------
        #*  cria a janela de configuração
        #*/
        l_ce = configControle.configControle ()
        #assert ( l_ce )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o canal de comunicação
        #*/
        l_bOk, l_iCanal = l_ce.startConfigPanel ()

        #** ---------------------------------------------------------------------------------------
        #*  checa se está tudo bem até agora...
        #*/
        if ( l_bOk ):

            #** -----------------------------------------------------------------------------------
            #*  cria o socket de recebimento de configuração (config listener)
            #*/
            self._cl = netManager.netListener ( l_iCanal, True )
            #assert ( self._cl )

            #** -----------------------------------------------------------------------------------
            #*  aguarda receber os dados do exercício
            #*/
            l_lstExe = self._cl.getExe ()
            #assert ( l_lstExe )

            #l_log.info ( "l_lstExe: " + str ( l_lstExe ))

            #** -----------------------------------------------------------------------------------
            #*  instancia o modelo
            #*
            self._mm = modelControle.modelControle ()
            #assert ( self._mm )

            #** -----------------------------------------------------------------------------------
            #*  carregou os arquivos na memória ?
            #*/
            if ( self._mm.iniciaBaseDados ( l_lstExe )):

                #** -------------------------------------------------------------------------------
                #*  cria o socket de recebimento de dados
                #*/
                self._dl = netManager.netListener ( l_iCanal )
                #assert ( self._dl )

                #** -------------------------------------------------------------------------------
                #*  cria o pier de comunicação
                #*/
                #self._voip.addPier ( l_iCanal )

                #** -------------------------------------------------------------------------------
                #*  create simulation time engine
                #*/
                self._st = simTime.simTime ()
                #assert ( self._st )

                #** -------------------------------------------------------------------------------
                #*  create flight control task
                #*/
                self._fc = flightControle.flightControle ( self )
                #assert ( self._fc )

                #** -------------------------------------------------------------------------------
                #*  create view manager task
                #*
                self._vm = viewControle.viewControle ( self )
                #assert ( self._vm )

                #** -------------------------------------------------------------------------------
                #*  create simulation statistics control
                #*/
                self._ss = simStats.simStats ()
                #assert ( self._ss )

            #** -----------------------------------------------------------------------------------
            #*  senão, não conseguiu carregar os arquivos na memória...
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*/
                self._vm = None

        #** ---------------------------------------------------------------------------------------
        #*  senão, algo errado no paraíso...
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            self._mm = None

            #** -----------------------------------------------------------------------------------
            #*/
            self._vm = None

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  controlControle::run
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def run ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlControle::run"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução (I)
        #*/
        if (( None == self._mm ) or ( None == self._vm )):

            #** -----------------------------------------------------------------------------------
            #*  m.poirot logger
            #*/
            #l_log.debug ( "<< " )

            #** -----------------------------------------------------------------------------------
            #*  termina a aplicação sem confirmação e sem envio de fim
            #*/
            self.cbkTermina ( False, False )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução (II)
        #*/
        #assert ( self._cl )
        #assert ( self._fc )
        #assert ( self._mm )
        #assert ( self._vm )

        #** ---------------------------------------------------------------------------------------
        #*  keep things running
        #*/
        glbData.g_bKeepRun = True

        #** ---------------------------------------------------------------------------------------
        #*  inicia o recebimento de mensagens de configuração
        #*/
        self._cl.start ()

        #** ---------------------------------------------------------------------------------------
        #*  starts flight control
        #*/
        self._fc.start ()

        #** ---------------------------------------------------------------------------------------
        #*  starts view manager (user interface)
        #*/
        self._vm.start ()

        #** ---------------------------------------------------------------------------------------
        #*  application loop
        #*/
        while ( glbData.g_bKeepRun ):

            #** -----------------------------------------------------------------------------------
            #*  obtém o tempo inicial em segundos
            #*/
            l_lNow = time.time ()
            #l_log.info ( "l_lNow: " + str ( l_lNow ))

            #** -----------------------------------------------------------------------------------
            #*  get all events
            #*/
            l_events = pygame.event.get ()

            #** -----------------------------------------------------------------------------------
            #*  trata cada um dos eventos
            #*/
            for l_evt in l_events:

                #** -------------------------------------------------------------------------------
                #*  check if user quits
                #*/
                if ( QUIT == l_evt.type ):

                    #** ---------------------------------------------------------------------------
                    #*  termina a aplicação sem confirmação e sem envio de fim
                    #*/
                    self.cbkTermina ( False, False )

                #** -------------------------------------------------------------------------------
                #*  this is the keyboard control structure
                #*/
                elif ( KEYDOWN == l_evt.type ):

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to decrease angle alidad azimuth
                    #*/
                    if ( K_DOWN == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  decrease angle alidad azimuth
                        #*/
                        self._vm.cbkAlidAzim ( -1 )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to terminate application
                    #*/
                    elif ( K_ESCAPE == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  termina a aplicação sem confirmação e sem envio de fim
                        #*/
                        self.cbkTermina ( False, False )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to decrease reference line
                    #*/
                    elif ( K_KP_MINUS == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  decrease reference line
                        #*/
                        self._vm.cbkHRefLine ( -100 )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to increase reference line
                    #*/
                    elif ( K_KP_PLUS == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  increase reference line
                        #*/
                        self._vm.cbkHRefLine ( 100 )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to decrease angle alidad elevation
                    #*/
                    elif ( K_LEFT == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  decrease angle alidad elevation
                        #*/
                        self._vm.cbkAlidElev ( -1 )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to change cabeceira
                    #*/
                    elif ( K_p == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  muda a cabeceira em uso da aplicação
                        #*/
                        self._vm.cbkExeToggleCab ()

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to increase angle alidad elevation
                    #*/
                    elif ( K_RIGHT == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  increase angle alidad elevation
                        #*/
                        self._vm.cbkAlidElev ( 1 )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to toggle voip communication
                    #*/
                    #elif ( K_SPACE == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  toggle voip communication
                        #*/
                        #self._voip.toggleTalk ()

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to increase angle alidad azimuth
                    #*/
                    elif ( K_UP == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  increase angle alidad azimuth
                        #*/
                        self._vm.cbkAlidAzim ( 1 )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to change scale
                    #*/
                    elif ( K_1 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  muda a escala da aplicação
                        #*/
                        self._vm.cbkExeEscala ( 1 )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to change scale
                    #*/
                    elif ( K_2 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  muda a escala da aplicação
                        #*/
                        self._vm.cbkExeEscala ( 2 )

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to change scale
                    #*/
                    elif ( K_3 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  muda a escala da aplicação
                        #*/
                        self._vm.cbkExeEscala ( 3 )

                #** -------------------------------------------------------------------------------
                #*  this is the mouse control structure
                #*/
                elif ( MOUSEBUTTONDOWN == l_evt.type ):

                    #** ---------------------------------------------------------------------------
                    #*  user pressed right button ?
                    #*/
                    if ( 1 == l_evt.button ):

                        #** -----------------------------------------------------------------------
                        #*  check if mouse position matches VoIP control
                        #*/
                        self._vm.cbkCheckVoIP ( l_evt.pos )

                        #** -----------------------------------------------------------------------
                        #*  check if mouse position matches sliders control
                        #*/
                        self._vm.cbkCheckSliders ( l_evt.pos )

            #** -----------------------------------------------------------------------------------
            #*  obtém um item da queue de entrada
            #*/
            l_lstData = self._cl.getData ()

            #** -----------------------------------------------------------------------------------
            #*  queue tem dados ?
            #*/
            if ( l_lstData ):

                #** -------------------------------------------------------------------------------
                #*  mensagem de aceleração ?
                #*/
                if ( glbDefs.xMSG_Acc == int ( l_lstData [ 0 ] )):

                    #** ---------------------------------------------------------------------------
                    #*  acelera/desacelera a aplicação
                    #*/
                    self.cbkAcelera ( float ( l_lstData [ 1 ] ))

                #** -------------------------------------------------------------------------------
                #*  mensagem de fim de execução ?
                #*/
                elif ( glbDefs.xMSG_Fim == int ( l_lstData [ 0 ] )):

                    #** ---------------------------------------------------------------------------
                    #*  termina a aplicação sem confirmação e sem envio de fim
                    #*/
                    self.cbkTermina ( False, False )

                #** -------------------------------------------------------------------------------
                #*  mensagem de congelamento ?
                #*/
                elif ( glbDefs.xMSG_Frz == int ( l_lstData [ 0 ] )):

                    #** ---------------------------------------------------------------------------
                    #*  freeze application
                    #*/
                    self._vm.cbkFreeze ( False )

                #** -------------------------------------------------------------------------------
                #*  mensagem de hora ?
                #*/
                elif ( glbDefs.xMSG_Tim == int ( l_lstData [ 0 ] )):

                    #** ---------------------------------------------------------------------------
                    #*  coloca a mensagem na queue
                    #*/
                    l_tHora = tuple ( int ( s ) for s in l_lstData [ 1 ][ 1 : -1 ].split ( ',' ))

                    #** ---------------------------------------------------------------------------
                    #*  coloca a mensagem na queue
                    #*/
                    self._st.setaHora ( l_tHora )

                #** -------------------------------------------------------------------------------
                #*  mensagem de descongelamento ?
                #*/
                elif ( glbDefs.xMSG_Ufz == int ( l_lstData [ 0 ] )):

                    #** ---------------------------------------------------------------------------
                    #*  defreeze application
                    #*/
                    self._vm.cbkDefreeze ( False )

                #** -------------------------------------------------------------------------------
                #*  senão, mensagem não reconhecida ou não tratada
                #*/
                else:

                    #** ---------------------------------------------------------------------------
                    #*  próxima mensagem
                    #*/
                    pass

            #** -----------------------------------------------------------------------------------
            #*  senão, aguarda um instante...
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*  obtém o tempo final em segundos e calcula o tempo decorrido
                #*/
                l_lDif = time.time () - l_lNow

                #** -------------------------------------------------------------------------------
                #*  está adiantado ?
                #*/
                if ( glbDefs.xTIM_Evnt > l_lDif ):

                    #** ---------------------------------------------------------------------------
                    #*  permite o scheduler (1/10th)
                    #*/
                    time.sleep ( glbDefs.xTIM_Evnt - l_lDif )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** ===========================================================================================
    #*  acesso a area de dados do objeto
    #*/ ===========================================================================================

    #** -------------------------------------------------------------------------------------------
    #*  controlManager::getCL
    #*  -------------------------------------------------------------------------------------------
    #*  returns the configuration listener
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getCL ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlManager::getCL"


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
        return ( self._cl )

    #** -------------------------------------------------------------------------------------------
    #*  controlManager::getDL
    #*  -------------------------------------------------------------------------------------------
    #*  returns the data listener
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getDL ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlManager::getDL"


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
        return ( self._dl )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "controlControle" )

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
    l_cc = controlControle ()
    #assert ( l_cc )

#** ----------------------------------------------------------------------------------------------- *#
