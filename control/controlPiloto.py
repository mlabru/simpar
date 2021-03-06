#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: controlPiloto
#*
#*  Descrição: DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração       
#*  -----------------------------------------------------------------------------------------------
#*  well     1997/jun/20  versão 1.0 started
#*  mlabru   2009/set/01  versão 3.0 started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    1997/jun/20  versão inicial (DOS/Modula-2)
#*  3.01-01  2009/set/01  versão para Linux
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  includes
#*  -----------------------------------------------------------------------------------------------
#*/

#/ Python library
#/ ------------------------------------------------------------------------------------------------
import os
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
import control.flightPiloto as flightPiloto
import control.netManager as netManager

import control.simStats as simStats
import control.simTime as simTime

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.glbData as glbData
import model.glbDefs as glbDefs

import model.modelPiloto as modelPiloto

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.dialog.Tk.dlgConfirm as dlgConfirm

import view.viewPiloto as viewPiloto

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  controlPiloto::controlPiloto
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class controlPiloto ( controlManager.controlManager ):

    #** -------------------------------------------------------------------------------------------
    #*  controlPiloto::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes controller
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlPiloto::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  inicia a super classe
        #*/
        controlManager.controlManager.__init__ ( self, "SiPAR.cfg" )

        #** ---------------------------------------------------------------------------------------
        #*  checa se o arquivo de configuração existe
        #*/
        if ( os.path.exists ( "data/cfgExe.DAT" )):

            #** -----------------------------------------------------------------------------------
            #*  instancia o modelo
            #*
            self._mm = modelPiloto.modelPiloto ()
            #assert ( self._mm )

            #** -----------------------------------------------------------------------------------
            #*  carrega os arquivos na memória
            #*/
            if ( self._mm.iniciaBaseDados ( "data/cfgExe.DAT" )):

                #** -------------------------------------------------------------------------------
                #*  flag de teclas 
                #*/
                self._bKeyUp    = False
                self._bKeyDown  = False
                self._bKeyLeft  = False
                self._bKeyRight = False

                #** -------------------------------------------------------------------------------
                #*  posição do joystick
                #*/
                self._iJoyX = 0
                self._iJoyY = 0

                #** -------------------------------------------------------------------------------
                #*  create simulation time engine
                #*/
                self._st = simTime.simTime ()
                #assert ( self._st )

                #** -------------------------------------------------------------------------------
                #*  cria o socket de envio
                #*/
                self._ns = netManager.netSender ( self._mm.getCanal ())
                #assert ( self._ns )

                #** -------------------------------------------------------------------------------
                #*  cria o pier de comunicação
                #*/
                #self._voip.addPier ( self._mm.getCanal ())

                #** -------------------------------------------------------------------------------
                #*  create flight control task
                #*/
                self._fc = flightPiloto.flightPiloto ( self )
                #assert ( self._fc )

                #** -------------------------------------------------------------------------------
                #*  create view manager task
                #*
                self._vm = viewPiloto.viewPiloto ( self )
                #assert ( self._vm )

                #** -------------------------------------------------------------------------------
                #*  create simulation statistics control
                #*/
                self._ss = simStats.simStats ()
                #assert ( self._ss )

            #** -----------------------------------------------------------------------------------
            #*  não consegui carregar os arquivos na memória
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*  reset view manager
                #*/
                self._vm = None

        #** ---------------------------------------------------------------------------------------
        #*  há algo errado no paraíso...
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  reset model manager
            #*/
            self._mm = None

            #** -----------------------------------------------------------------------------------
            #*  reset view manager
            #*/
            self._vm = None

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  controlPiloto::run
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
        #l_szMetodo = "controlPiloto::run"


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
            #*  termina a aplicação
            #*/
            self.cbkTermina ()

        #** ---------------------------------------------------------------------------------------
        #*  ativa o relógio da simulação
        #*/
        self.startTime ()

        #** ---------------------------------------------------------------------------------------
        #*  keep things running
        #*/
        glbData.g_bKeepRun = True

        #** ---------------------------------------------------------------------------------------
        #*  starts flight control
        #*/
        self._fc.start ()

        #** ---------------------------------------------------------------------------------------
        #*  starts view manager (user interface)
        #*/
        self._vm.start ()

        #** ---------------------------------------------------------------------------------------
        #*  obtem o controle do menu
        #*/
        #l_guiApp = self._vm.getGuiApp ()
        ##assert ( l_guiApp )

        #** ---------------------------------------------------------------------------------------
        #*  no flight under control
        #*/
        #l_stAtvCntrl = None

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
                #*/
                #l_log.info ( "event: " + str ( l_evt ))

                #** -------------------------------------------------------------------------------
                #*  check if user quits
                #*/
                if ( QUIT == l_evt.type ):

                    #** ---------------------------------------------------------------------------
                    #*  termina a aplicação
                    #*/
                    self.cbkTermina ( True )

                #** -------------------------------------------------------------------------------
                #*  this is the keyboard control structure
                #*/
                elif ( KEYDOWN == l_evt.type ):

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to terminate application
                    #*/
                    if ( K_ESCAPE == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  termina a aplicação
                        #*/
                        self.cbkTermina ( True )

                    #** ---------------------------------------------------------------------------
                    #*  down arrow key ?
                    #*/
                    elif ( K_KP2 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  down arrow
                        #*/
                        self._bKeyDown = True

                    #** ---------------------------------------------------------------------------
                    #*  left arrow key ?
                    #*/
                    elif ( K_KP4 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  left arrow
                        #*/
                        self._bKeyLeft = True

                    #** ---------------------------------------------------------------------------
                    #*  right arrow key ?
                    #*/
                    elif ( K_KP6 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  right arrow
                        #*/
                        self._bKeyRight = True

                    #** ---------------------------------------------------------------------------
                    #*  up arrow key ?
                    #*/
                    elif ( K_KP8 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  up arrow
                        #*/
                        self._bKeyUp = True

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to desaccelerate simulation
                    #*/
                    elif ( K_KP_DIVIDE == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*/
                        if ( glbDefs.xTIM_Accel > 1 ):

                            #** -------------------------------------------------------------------
                            #*/
                            #assert ( self._ns )
                            #assert ( self._st )

                            #** -------------------------------------------------------------------
                            #*  ajusta a hora da simulação
                            #*/
                            self._st.ajustaHora ( self._st.obtemHoraSim ())

                            #** -------------------------------------------------------------------
                            #*  desacelera a simulação
                            #*/
                            glbDefs.xTIM_Accel -= 1
                            #l_log.info ( "xTIM_Accel: " + str ( glbDefs.xTIM_Accel ))

                            #** -------------------------------------------------------------------
                            #*  envia o aviso de desaceleração
                            #*/
                            self._ns.sendCnfg ( str ( glbDefs.xMSG_Vrs ) + glbDefs.xMSG_Sep +
                                                str ( glbDefs.xMSG_Acc ) + glbDefs.xMSG_Sep +
                                                str ( glbDefs.xTIM_Accel ))
                            
                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to accelerate simulation
                    #*/
                    elif ( K_KP_MULTIPLY == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*/
                        #assert ( self._ns )
                        #assert ( self._st )

                        #** -----------------------------------------------------------------------
                        #*  ajusta a hora da simulação
                        #*/
                        self._st.ajustaHora ( self._st.obtemHoraSim ())

                        #** -----------------------------------------------------------------------
                        #*  acelera a simulação
                        #*/
                        glbDefs.xTIM_Accel += 1
                        #l_log.info ( "xTIM_Accel: " + str ( glbDefs.xTIM_Accel ))

                        #** -----------------------------------------------------------------------
                        #*  envia o aviso de aceleração
                        #*/
                        self._ns.sendCnfg ( str ( glbDefs.xMSG_Vrs ) + glbDefs.xMSG_Sep +
                                            str ( glbDefs.xMSG_Acc ) + glbDefs.xMSG_Sep +
                                            str ( glbDefs.xTIM_Accel ))
                        
                    #** ---------------------------------------------------------------------------
                    #*  check if user wants to toggle voip communication
                    #*/
                    #elif ( K_SPACE == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  toggle voip communication
                        #*/
                        #self._voip.toggleTalk ()

                    #** ---------------------------------------------------------------------------
                    #*  check if user wants <C>ongelar
                    #*/
                    elif ( K_c == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  freeze application
                        #*/
                        self.cbkCongela ()

                #** -------------------------------------------------------------------------------
                #*  this is the keyboard control structure
                #*/
                elif ( KEYUP == l_evt.type ):

                    #** ---------------------------------------------------------------------------
                    #*  down arrow key ?
                    #*/
                    if ( K_KP2 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  down arrow
                        #*/
                        self._bKeyDown = False

                    #** ---------------------------------------------------------------------------
                    #*  left arrow key ?
                    #*/
                    elif ( K_KP4 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  left arrow
                        #*/
                        self._bKeyLeft = False

                    #** ---------------------------------------------------------------------------
                    #*  center point key ?
                    #*/
                    elif ( K_KP5 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  reset keys
                        #*/
                        self._bKeyDown  = False
                        self._bKeyLeft  = False
                        self._bKeyRight = False
                        self._bKeyUp    = False

                        #** -----------------------------------------------------------------------
                        #*  reset position
                        #*/
                        self._iJoyX = 0
                        self._iJoyY = 0

                    #** ---------------------------------------------------------------------------
                    #*  right arrow key ?
                    #*/
                    elif ( K_KP6 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  right arrow
                        #*/
                        self._bKeyRight = False

                    #** ---------------------------------------------------------------------------
                    #*  up arrow key ?
                    #*/
                    elif ( K_KP8 == l_evt.key ):

                        #** -----------------------------------------------------------------------
                        #*  up arrow
                        #*/
                        self._bKeyUp = False

                #** -------------------------------------------------------------------------------
                #*  this is the mouse control structure
                #*/
                #elif ( MOUSEBUTTONDOWN == l_evt.type ):

                    #** ---------------------------------------------------------------------------
                    #*  user pressed right button ?
                    #*/
                    #if ( 1 == l_evt.button ):

                        ##l_log.info ( "l_evt(A): " + str ( l_evt ))
                        
                        #** -----------------------------------------------------------------------
                        #*  check if mouse position matches any flight positions
                        #*/
                        #l_stAtvCntrl = self._vm.cbkSelectFlight ( l_evt.pos, True )

                        ##l_log.info ( "l_evt(M): " + str ( l_evt ))

                        #** -----------------------------------------------------------------------
                        #*  none flight selected ?
                        #*/
                        #if ( None == l_stAtvCntrl ):

                            #** -------------------------------------------------------------------
                            #*  check if mouse position matches VoIP control
                            #*/
                            #self._vm.cbkCheckVoIP ( l_evt.pos )

                        ##l_log.info ( "l_evt(D): " + str ( l_evt ))

                    #** ---------------------------------------------------------------------------
                    #*  user pressed left button ?
                    #*/
                    #elif ( 3 == l_evt.button ):

                        #** -----------------------------------------------------------------------
                        #*  check if mouse position matches any flight positions
                        #*/
                        #l_stAtvCntrl = self._vm.cbkSelectFlight ( l_evt.pos, False )

            #** -----------------------------------------------------------------------------------
            #*  trata teclado
            #*/
            self.countKeys ()

            #** -----------------------------------------------------------------------------------
            #*  trata os eventos de menu
            #*/
            #l_guiApp.run ( l_events )

            #** -----------------------------------------------------------------------------------
            #*  obtém o tempo final em segundos e calcula o tempo decorrido
            #*/
            l_lDif = time.time () - l_lNow

            #l_log.info ( "l_lDif....(E): " + str ( l_lDif ))        
            #l_log.info ( "xTIM_Evnt.(E): " + str ( glbDefs.xTIM_Evnt ))
            #l_log.info ( "Wait/Sleep(E): " + str ( glbDefs.xTIM_Evnt - l_lDif ))

            #** -----------------------------------------------------------------------------------
            #*  está adiantado ?
            #*/
            if ( glbDefs.xTIM_Evnt > l_lDif ):
                                                
                #l_log.info ( "Adiantado em: " + str ( glbDefs.xTIM_Evnt - l_lDif ))

                #** -------------------------------------------------------------------------------
                #*  permite o scheduler (1/10th)
                #*/
                time.sleep ( glbDefs.xTIM_Evnt - l_lDif )

        #** ---------------------------------------------------------------------------------------
        #*/
        #self._ss.noProcFlights = fe.flightsProcessed

        #** ---------------------------------------------------------------------------------------
        #*/
        #self._ss.printScore ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  controlPiloto::cbkCongela
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkCongela ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlPiloto::cbkCongela"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._ns )
        #assert ( self._st )
        #assert ( self._vm )

        #** ---------------------------------------------------------------------------------------
        #*  envia o aviso de congelamento
        #*/
        self._ns.sendCnfg ( str ( glbDefs.xMSG_Vrs ) + glbDefs.xMSG_Sep +
                            str ( glbDefs.xMSG_Frz ))
        
        #** ---------------------------------------------------------------------------------------
        #*  obtem a hora atual
        #*/
        self._st.cbkCongela ()

        #** ---------------------------------------------------------------------------------------
        #*  pause application
        #*/
        self._vm.cbkCongela ()

        #** ---------------------------------------------------------------------------------------
        #*  pause the app
        #*/
        while ( glbData.g_bKeepRun ):

            #** -----------------------------------------------------------------------------------
            #*  obtém um único evento da fila
            #*/
            l_event = pygame.event.wait ()
            #l_log.info ( "event(2): " + str ( l_event ))

            #** -----------------------------------------------------------------------------------
            #*  tecla pressionada ?
            #*/
            if ( KEYDOWN == l_event.type ):

                #** -------------------------------------------------------------------------------
                #*  <D>escongela ?
                #*/
                if ( K_d == l_event.key ):

                    #** ---------------------------------------------------------------------------
                    #*  cai fora...
                    #*/
                    break

        #** ---------------------------------------------------------------------------------------
        #*  envia o aviso de descongelamento
        #*/
        self._ns.sendCnfg ( str ( glbDefs.xMSG_Vrs ) + glbDefs.xMSG_Sep +
                            str ( glbDefs.xMSG_Ufz ))
        
        #** ---------------------------------------------------------------------------------------
        #*  continue application
        #*/
        self._vm.cbkDescongela ()

        #** ---------------------------------------------------------------------------------------
        #*  restaura a hora
        #*/
        self._st.cbkDescongela ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  controlPiloto::countKeys
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def countKeys ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlPiloto::countKeys"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  manche à frente (desce)
        #*/
        if ( self._bKeyUp ):
        
            self._iJoyY -= 1
        
        #** ---------------------------------------------------------------------------------------
        #*  manche à trás (sobe)
        #*/
        if ( self._bKeyDown ):
        
            self._iJoyY += 1
        
        #** ---------------------------------------------------------------------------------------
        #*  manche à esquerda (curva para esquerda)
        #*/
        if ( self._bKeyLeft ):
        
            self._iJoyX -= 1
        
        #** ---------------------------------------------------------------------------------------
        #*  manche à direita (curva para direita)
        #*/
        if ( self._bKeyRight ):
        
            self._iJoyX += 1
        
        #** ---------------------------------------------------------------------------------------
        #*  normaliza X (range em X [-16, 16])
        #*/
        if ( self._iJoyX > 16 ):

            self._iJoyX = 16

        elif ( self._iJoyX < -16 ):

            self._iJoyX = -16
        
        #** ---------------------------------------------------------------------------------------
        #*  normaliza Y (range em Y [-20, 20])
        #*/
        if ( self._iJoyY > 20 ):

            self._iJoyY = 20

        elif ( self._iJoyY < -20 ):

            self._iJoyY = -20
        
        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  controlPiloto::startTime
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def startTime ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlPiloto::startTime"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._mm )
        #assert ( self._st )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o exercício
        #*/
        l_stExe = self._mm.getExercicio ()
        #assert ( l_stExe )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a hora de início do exercício
        #*/
        l_tHora = l_stExe.getHora ()
        #l_log.info ( "l_tHora: " + str ( l_tHora ))

        #** ---------------------------------------------------------------------------------------
        #*  inicia o relógio da simulação
        #*/
        self._st.setaHora ( l_tHora )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** ===========================================================================================
    #*  acesso a área de dados do objeto
    #** ===========================================================================================

    #** -------------------------------------------------------------------------------------------
    #*  controlPiloto::getJoyX
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getJoyX ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlPiloto::getJoyX"


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
        #*  returns the application view
        #*/
        return ( self._iJoyX )

    #** -------------------------------------------------------------------------------------------
    #*  controlPiloto::getJoyY
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getJoyY ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "controlPiloto::getJoyY"


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
        #*  returns the application view
        #*/
        return ( self._iJoyY )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "controlPiloto" )

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
    l_cm = controlPiloto ()
    #assert ( l_cm )

#** ----------------------------------------------------------------------------------------------- *#
