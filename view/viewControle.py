#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: viewControle
#*
#*  Descrição: this class takes care of all interaction with the user. It has been designed so that
#*             it can be directly linked to an AI.
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

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.glbData as glbData
import model.glbDefs as glbDefs
import model.locDefs as locDefs

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.guiIMet as guiIMet
import view.guiInfo as guiInfo
import view.guiMessage as guiMessage
import view.guiSliders as guiSliders
import view.guiScopeControle as guiScopeControle
import view.guiVoIP as guiVoIP

import view.stripControle as stripControle

import view.viewManager as viewManager
import view.viewUtils as viewUtils
import view.viewVideoBruto as viewVideoBruto

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  viewControle::viewControle
#*  -----------------------------------------------------------------------------------------------
#*  handles all interaction with user. This class is the interface to SiPAR. It is based on pygame
#*  and SDL packages. It draws the scope on the screen and handles all mouse input.
#*  -----------------------------------------------------------------------------------------------
#*/
class viewControle ( viewManager.viewManager ):

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the display
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_cm - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_cm ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert ( f_cm )

        #** ---------------------------------------------------------------------------------------
        #*  initialize super classe
        #*/
        viewManager.viewManager.__init__ ( self, f_cm )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o PAR
        #*/
        self._oPAR = self._oExe.getPAR ()
        #assert ( self._oPAR )
                                        
        #** ---------------------------------------------------------------------------------------
        #*  define o título da janela
        #*/
        pygame.display.set_caption ( locDefs.xTXT_Tit + " [Controle/" + self._oExe.getKey () + "]" )


        #** ---------------------------------------------------------------------------------------
        #*  initialize info area
        #*/
        self._infoBox = guiInfo.guiInfo ( f_cm, self._screen,
                                          glbDefs.xSCR_POS [ glbDefs.xSCR_Info ][ 0 ],
                                          glbDefs.xSCR_POS [ glbDefs.xSCR_Info ][ 1 ] )
        #assert ( self._infoBox )

        #** ---------------------------------------------------------------------------------------
        #*  initialize strip list
        #*/
        self._stripList = stripControle.stripControle ( f_cm, self._screen, 
                                                        glbDefs.xSCR_CTR [ glbDefs.xSCR_Strip ][ 0 ],
                                                        glbDefs.xSCR_CTR [ glbDefs.xSCR_Strip ][ 1 ] )
        #assert ( self._stripList )

        #** ---------------------------------------------------------------------------------------
        #*  initialize sliders box
        #*/
        self._sldrBox = guiSliders.guiSliders ( f_cm, self._screen,
                                                glbDefs.xSCR_CTR [ glbDefs.xSCR_Sliders ][ 0 ],
                                                glbDefs.xSCR_CTR [ glbDefs.xSCR_Sliders ][ 1 ] )
        #assert ( self._sldrBox )

        #** ---------------------------------------------------------------------------------------
        #*  initialize VoIP box
        #*/
        self._voipBox = guiVoIP.guiVoIP ( f_cm, self._screen,
                                          glbDefs.xSCR_CTR [ glbDefs.xSCR_VoIP ][ 0 ],
                                          glbDefs.xSCR_CTR [ glbDefs.xSCR_VoIP ][ 1 ] )
        #assert ( self._voipBox )

        #** ---------------------------------------------------------------------------------------
        #*  initialize info met area
        #*/
        self._imetBox = guiIMet.guiIMet ( f_cm, self._screen,
                                          glbDefs.xSCR_CTR [ glbDefs.xSCR_IMet ][ 0 ],
                                          glbDefs.xSCR_CTR [ glbDefs.xSCR_IMet ][ 1 ] )
        #assert ( self._imetBox )

        #** ---------------------------------------------------------------------------------------
        #*  initialize message box
        #*/
        self._msgBox = guiMessage.guiMessage ( f_cm, self._screen,
                                               glbDefs.xSCR_CTR [ glbDefs.xSCR_Msg ][ 0 ],
                                               glbDefs.xSCR_CTR [ glbDefs.xSCR_Msg ][ 1 ] )
        #assert ( self._msgBox )

        #** ---------------------------------------------------------------------------------------
        #*  inicia scope do controle
        #*/
        self._scope = guiScopeControle.guiScopeControle ( f_cm, self._screen,
                                                          glbDefs.xSCR_POS [ glbDefs.xSCR_Scope ][ 0 ],
                                                          glbDefs.xSCR_POS [ glbDefs.xSCR_Scope ][ 1 ] )
        #assert ( self._scope )
        
        #** ---------------------------------------------------------------------------------------
        #*  flight call sign
        #*/
        self._bCallSign = False

        #** ---------------------------------------------------------------------------------------
        #*  inicia área de mensagens de erro e de alerta
        #*/
        self._msgBox.addTxt ( locDefs.xTXT_Tit + " (C) ICEA 2009-10", locDefs.xCOR_Messages )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza a tela
        #*/
        self.dispFlip ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::cbkElimina
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_stAtv - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkElimina ( self, f_stAtv ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::cbkElimina"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert ( f_stAtv )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._fc )

        #** ---------------------------------------------------------------------------------------
        #*  obtem o flight engine da aeronave
        #*/
        l_fe = f_stAtv.getFE ()
        #assert ( l_fe )

        #** ---------------------------------------------------------------------------------------
        #*  retira a aeronave da lista de aeronaves ativas
        #*/
        self._fc.cbkElimina ( l_fe )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::cbkExeEscala
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkExeEscala ( self, f_iEsc ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::cbkExeEscala"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert ( f_iEsc in locDefs.xSET_EscalasValidas )
        
        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._oExe )
        
        #** ---------------------------------------------------------------------------------------
        #*  verifica se mudou a escala
        #*/
        if ( self._oExe.getEscala () != f_iEsc ):

            #** -----------------------------------------------------------------------------------
            #*  configura a nova escala
            #*/
            self._oExe.setEscala ( f_iEsc )

            #** -----------------------------------------------------------------------------------
            #*  avisa que houve mudança de escala
            #*/
            self._oExe.setMudouEscala ( True )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::cbkExeToggleCab
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkExeToggleCab ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::cbkExeToggleCab"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._oExe )
        
        #** ---------------------------------------------------------------------------------------
        #*  verifica se mudou a escala
        #*/
        self._oExe.toggleCab ()

        #** ---------------------------------------------------------------------------------------
        #*  avisa que houve mudança de cabeceira
        #*/
        self._oExe.setMudouCab ( True )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::cbkAlidAzim
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkAlidAzim ( self, f_iVal ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::cbkAlidAzim"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  calcula o novo valor
        #*/
        if ( f_iVal > 0 ):
        
            self._oPAR.incAlidAzim ()

        else:

            self._oPAR.decAlidAzim ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::cbkAlidElev
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkAlidElev ( self, f_iVal ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::cbkAlidElev"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._oExe )
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a cabeceira atual
        #*/
        l_iCab = self._oExe.getCabAtu ()
        #assert ( l_iCab in locDefs.xSET_CabsValidas )
                                        
        #** ---------------------------------------------------------------------------------------
        #*  cabeceira secundária ?
        #*/
        if ( 1 == l_iCab ):
        
            #** -----------------------------------------------------------------------------------
            #*  inverte o sinal
            #*/
            f_iVal *= -1

        #** ---------------------------------------------------------------------------------------
        #*  calcula o novo valor
        #*/
        if ( f_iVal > 0 ):
        
            self._oPAR.incAlidElev ()

        else:

            self._oPAR.decAlidElev ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::cbkHRefLine
    #*  -------------------------------------------------------------------------------------------
    #*  drive application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkHRefLine ( self, f_iVal ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::cbkHRefLine"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._oExe )
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a escala atual
        #*/
        l_iEsc = self._oExe.getEscala ()
        #assert ( l_iEsc in locDefs.xSET_EscalasValidas )
                                        
        l_iEsc -= 1
                                                
        #** ---------------------------------------------------------------------------------------
        #*  calcula o novo valor
        #*/
        f_iVal += self._oPAR.getHRefLine ()

        #** ---------------------------------------------------------------------------------------
        #*  valor válido para a escala ?
        #*/
        if ( 0 <= f_iVal <= self._oPAR.getMaxHRefLine ( l_iEsc )):
        
            #** -----------------------------------------------------------------------------------
            #*  atualiza e salva o valor da HRefLine
            #*/
            self._oPAR.setHRefLine ( f_iVal )                                        
            #l_log.info ( "self._oPAR.setHRefLine: " + str ( f_iVal ))

            #** -----------------------------------------------------------------------------------
            #*  avisa que houve mudança nas alidades
            #*/
            self._oPAR.setMudouAlidades ( True )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::dispFlip
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def dispFlip ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::dispFlip"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._screenLock )

        #** ---------------------------------------------------------------------------------------
        #*  acquire lock
        #*/
        self._screenLock.acquire ()

        #** ---------------------------------------------------------------------------------------
        #*  update display
        #*/
        pygame.display.flip ()

        #** ---------------------------------------------------------------------------------------
        #*  release lock
        #*/
        self._screenLock.release ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::run
    #*  -------------------------------------------------------------------------------------------
    #*  routine that runs the application
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def run ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::run"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._st )
        
        #** ---------------------------------------------------------------------------------------
        #*  enquanto nao inicia...
        #*/
        while ( not glbData.g_bKeepRun ):

            #** -----------------------------------------------------------------------------------
            #*  aguarda 1 seg
            #*/
            time.sleep ( 1 )

        #** ---------------------------------------------------------------------------------------
        #*  inicia hora da simulação
        #*/
        self._dHoraSim = self._st.obtemHoraSim ()

        #** ---------------------------------------------------------------------------------------
        #*  eternal loop
        #*/
        while ( glbData.g_bKeepRun ):

            #** -----------------------------------------------------------------------------------
            #*  verifica condições de execução
            #*/
            #assert ( self._infoBox )
            #assert ( self._imetBox )
            #assert ( self._msgBox )
            #assert ( self._sldrBox )
            #assert ( self._voipBox )
            #assert ( self._oExe )
            #assert ( self._scope )
            #assert ( self._screen )
            
            #** -----------------------------------------------------------------------------------
            #*  obtem o tempo inicial em segundos
            #*/
            #l_lNow = time.time ()
            #l_log.info ( "l_lNow: " + str ( l_lNow ))

            #** -----------------------------------------------------------------------------------
            #*  mudou a escala ou a cabeceira ?
            #*/
            if ( self._oExe.getMudouEscala () or self._oExe.getMudouCab ()):

                #** -------------------------------------------------------------------------------
                #*  atualiza o scope (VA e VS)
                #*/
                self._scope.doRedraw ()

                #** -------------------------------------------------------------------------------
                #*  reseta o flag de mudança de alidades
                #*/
                self._oPAR.setMudouAlidades ( False )

                #** -------------------------------------------------------------------------------
                #*  reseta o flag de mudança de cabeceira
                #*/
                self._oExe.setMudouCab ( False )

                #** -------------------------------------------------------------------------------
                #*  reseta o flag de mudança de escala
                #*/
                self._oExe.setMudouEscala ( False )

            #** -----------------------------------------------------------------------------------
            #*  mudou as alidades ?
            #*/
            elif ( self._oPAR.getMudouAlidades ()):

                #** -------------------------------------------------------------------------------
                #*  atualiza o scope (VA)
                #*/
                self._scope.doRedrawVA ()

                #** -------------------------------------------------------------------------------
                #*  reseta o flag de mudança de alidades
                #*/
                self._oPAR.setMudouAlidades ( False )

            #** -----------------------------------------------------------------------------------
            #*  enquanto estiver congelado...
            #*/
            while (( glbData.g_bKeepRun ) and ( self._bPause )):

                #l_log.info ( "pausado !!" )

                #** -------------------------------------------------------------------------------
                #*  permite o scheduler (1/10th)
                #*/
                time.sleep ( glbDefs.xTIM_Wait )

            #** ---------------------------------------------------------------------------------------
            #*  exibe relógio e versão
            #*/
            self._infoBox.doDraw ( self._screen )

            #** -----------------------------------------------------------------------------------
            #*  atualiza os vôos
            #*/
            self.updateFlights ()

            #** ---------------------------------------------------------------------------------------
            #*  exibe parâmetros de PAR
            #*/
            self._sldrBox.doDraw ( self._screen )

            #** ---------------------------------------------------------------------------------------
            #*  exibe parâmetros de comunicação
            #*/
            self._voipBox.doDraw ( self._screen )

            #** ---------------------------------------------------------------------------------------
            #*  exibe mensagens de alertas e erros
            #*/
            self._msgBox.doDraw ( self._screen )

            #** ---------------------------------------------------------------------------------------
            #*  exibe informações meteorológicas
            #*/
            self._imetBox.doDraw ( self._screen )

            #** -----------------------------------------------------------------------------------
            #*  atualiza a tela
            #*/
            self.dispFlip ()

            #** -----------------------------------------------------------------------------------
            #*  obtem o tempo final em segundos e calcula o tempo decorrido
            #*/
            #l_lDif = time.time () - l_lNow

            #l_log.info ( "l_lDif......(V): " + str ( l_lDif ))
            #l_log.info ( "xTIM_Refresh(V): " + str ( glbDefs.xTIM_Refresh ))
            #l_log.info ( "Wait/Sleep..(V): " + str ( glbDefs.xTIM_Refresh - l_lDif ))

            #** -----------------------------------------------------------------------------------
            #*  está atrasado ?
            #*/
            #if ( glbDefs.xTIM_Refresh > l_lDif ):

                #** -------------------------------------------------------------------------------
                #*  permite o scheduler (1/10th)
                #*/
                #time.sleep ( glbDefs.xTIM_Refresh - l_lDif )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::updateAnv
    #*  -------------------------------------------------------------------------------------------
    #*  updates the display from the flights in the flightlist
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_oFlt - DOCUMENT ME!
    #*  @param  f_iI   - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateAnv ( self, f_oFlt, f_iI ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::updateAnv"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert ( f_oFlt )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._scope )
        #assert ( self._screen )
        #assert ( self._stripList )
        
        #** ---------------------------------------------------------------------------------------
        #*  atualiza a strip da aeronave
        #*/
        self._stripList.doUpdate ( self._screen, f_iI, f_oFlt )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza o scope
        #*/
        self._scope.doDraw ( self._screen, f_oFlt )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewControle::updateFlights
    #*  -------------------------------------------------------------------------------------------
    #*  updates the display from the flights in the flightlist
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateFlights ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewControle::updateFlights"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._fc )

        #** ---------------------------------------------------------------------------------------
        #*  trava a lista de vôos
        #*/
        glbData.g_lckFlight.acquire ()

        #** ---------------------------------------------------------------------------------------
        #*  atualização das aeronaves na lista de vôos ativos
        #*/
        try:

            #** -----------------------------------------------------------------------------------
            #*  inicia o contador de strips
            #*/
            l_iI = 0

            #** -----------------------------------------------------------------------------------
            #*  obtém a lista de vôos
            #*/
            l_lstFlight = self._fc.getListFlight ()

            #** -----------------------------------------------------------------------------------
            #*  percorre a lista de vôos ativos
            #*/
            for l_key, l_oFlt in l_lstFlight.iteritems ():

                #** -------------------------------------------------------------------------------
                #*  atualiza a posição da aeronave
                #*/
                self.updateAnv ( l_oFlt, l_iI )

                #** -------------------------------------------------------------------------------
                #*  incrementa o contador de strips
                #*/
                l_iI += 1

        #** ---------------------------------------------------------------------------------------
        #*/
        finally:

            #** -----------------------------------------------------------------------------------
            #*  libera a lista de vôos
            #*/
            glbData.g_lckFlight.release ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "viewControle" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
