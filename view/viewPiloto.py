#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: viewPiloto
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

#/ GooeyPy (gui library)
#/ ------------------------------------------------------------------------------------------------
#import gooeypy as gooeypy
#from gooeypy.const import *

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
#import model.cineCalc as cineCalc
import model.glbData as glbData
import model.glbDefs as glbDefs
import model.locDefs as locDefs

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.guiInfo as guiInfo
import view.guiMessage as guiMessage
import view.guiScopePiloto as guiScopePiloto
import view.guiVoIP as guiVoIP

import view.stripPiloto as stripPiloto

import view.guiUtils as guiUtils

import view.viewManager as viewManager
import view.viewUtils as viewUtils

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  viewPiloto::viewPiloto
#*  -----------------------------------------------------------------------------------------------
#*  handles all interaction with user. This class is the interface to SiPAR. It is based on pygame
#*  and SDL packages. It draws the scope on the screen and handles all mouse input.
#*  -----------------------------------------------------------------------------------------------
#*/
class viewPiloto ( viewManager.viewManager ):

    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the display
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_cm ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::__init__"


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
        #*  initialize super class
        #*/
        viewManager.viewManager.__init__ ( self, f_cm )

        #** ---------------------------------------------------------------------------------------
        #*  define o título da janela
        #*/
        pygame.display.set_caption ( locDefs.xTXT_Tit + " [Piloto/" + self._oExe.getKey () + "]" )

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
        self._stripList = stripPiloto.stripPiloto ( f_cm, self._screen, 
                                                    glbDefs.xSCR_PIL [ glbDefs.xSCR_Strip ][ 0 ],
                                                    glbDefs.xSCR_PIL [ glbDefs.xSCR_Strip ][ 1 ] )
        #assert ( self._stripList )

        #** ---------------------------------------------------------------------------------------
        #*  initialize VoIP box
        #*/
        self._voipBox = guiVoIP.guiVoIP ( f_cm, self._screen,
                                          glbDefs.xSCR_PIL [ glbDefs.xSCR_VoIP ][ 0 ],
                                          glbDefs.xSCR_PIL [ glbDefs.xSCR_VoIP ][ 1 ] )
        #assert ( self._voipBox )

        #* ----------------------------------------------------------------------------------------
        #* inicia a gui
        #*
        #gooeypy.init ( myscreen = self._screen )

        #** ---------------------------------------------------------------------------------------
        #*  inicia a app da gui
        #*/
        #self._guiApp = gooeypy.App ( width  = locDefs.xSCR_Size [ 0 ],
        #                             height = locDefs.xSCR_Size [ 1 ],
        #                             theme  = "SiPAR" )
        ##assert ( self._guiApp )

        #** ---------------------------------------------------------------------------------------
        #*  initialize menu list
        #*/
        #self._menuBox = guiMenu.guiMenu ( f_cm, self._screen, self._guiApp,
        #                                  glbDefs.xSCR_PIL [ glbDefs.xSCR_Menu ][ 0 ],
        #                                  glbDefs.xSCR_PIL [ glbDefs.xSCR_Menu ][ 1 ] )
        ##assert ( self._menuBox )

        #** ---------------------------------------------------------------------------------------
        #*  initialize message box
        #*/
        self._msgBox = guiMessage.guiMessage ( f_cm, self._screen,
                                               glbDefs.xSCR_PIL [ glbDefs.xSCR_Msg ][ 0 ],
                                               glbDefs.xSCR_PIL [ glbDefs.xSCR_Msg ][ 1 ] )
        #assert ( self._msgBox )

        #** ---------------------------------------------------------------------------------------
        #*  inicia scope do piloto
        #*/
        self._scope = guiScopePiloto.guiScopePiloto ( f_cm, self._screen,
                                                      glbDefs.xSCR_POS [ glbDefs.xSCR_Scope ][ 0 ],
                                                      glbDefs.xSCR_POS [ glbDefs.xSCR_Scope ][ 1 ] )
        #assert ( self._scope )
        
        #** ---------------------------------------------------------------------------------------
        #*  avisa ao menu sobre a lista de mensagens
        #*/
        #self._menuBox.setMsgBox ( self._msgBox )

        #** ---------------------------------------------------------------------------------------
        #*  inicia área de mensagens de erro e de alerta
        #*/
        self._msgBox.addTxt ( locDefs.xTXT_Tit + " (C) ICEA 2008-10", locDefs.xCOR_Messages )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza a tela
        #*/
        self.dispFlip ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    """
    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::cbkSelectFlight
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkSelectFlight ( self, f_tMouse, f_bNav ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::cbkSelectFlight"

        #/ aeronave selecionada
        #/ ----------------------------------------------------------------------------------------
        l_stAnvSel = None


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #l_log.info ( "f_tMouse: " + str ( f_tMouse ))
        #assert ( f_tMouse )

        #** ---------------------------------------------------------------------------------------
        #*  checks selection via flight strip
        #*/
        if (( f_tMouse [ 0 ] >=   glbDefs.xSCR_PIL [ locDefs.xSCR_Strip ][ 0 ][ 0 ] ) and
            ( f_tMouse [ 0 ] <= ( glbDefs.xSCR_PIL [ locDefs.xSCR_Strip ][ 0 ][ 0 ] +
                                  glbDefs.xSCR_PIL [ locDefs.xSCR_Strip ][ 1 ][ 0 ] ))):

            #l_log.info ( "f_tMouse: " + str ( f_tMouse ))
            #l_log.info ( "glbDefs.xSCR_PIL: " + str ( glbDefs.xSCR_PIL [ locDefs.xSCR_Strip ][ 0 ] ))

            #** -----------------------------------------------------------------------------------
            #*  checks whether mouse position is inside strip flights
            #*/
            l_stAnvSel = self.selectAnvStrip ( f_tMouse, f_bNav )
            
        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  nao achou nenhuma aeronave para seleção
        #*/
        return ( l_stAnvSel )
    """
    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::dispFlip
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def dispFlip ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::dispFlip"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        ##assert ( self._guiApp )
        #assert ( self._screenLock )

        #** ---------------------------------------------------------------------------------------
        #*  acquire lock
        #*/
        self._screenLock.acquire ()

        #** ---------------------------------------------------------------------------------------
        #*  gooeypy iniciado ?
        #*/
        #if ( None != self._guiApp ):

            #** -----------------------------------------------------------------------------------
            #*  atualiza a tela
            #*/
            #self._guiApp.dirty = True
            #self._guiApp.draw ()

        #** ---------------------------------------------------------------------------------------
        #*  atualiza a tela
        #*/
        #gooeypy.update_display ()

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

    """
    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::getSelectedAnv
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getSelectedAnv ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::getSelectedAnv"

        #/ aeronave selecionada
        #/ ----------------------------------------------------------------------------------------
        l_stAtv = None


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
        #*  obtém a lista de vôos ativos
        #*/
        l_lstFlight = self._fc.getListFlight ()

        #assert ( 0 <= len ( l_lstFlight ) < 2 )

        #** ---------------------------------------------------------------------------------------
        #*  percorre a lista de vôos ativos
        #*/
        for l_iI in xrange ( len ( l_lstFlight )):

            #** -----------------------------------------------------------------------------------
            #*  obtém um flight engine
            #*/
            l_fe = l_lstFlight [ l_iI ]
            #assert ( l_fe )

            #** -----------------------------------------------------------------------------------
            #*  obtém a area de dados da aeronave
            #*/
            l_stAtv = l_fe.getAtv ()
            #assert ( l_stAtv )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( l_stAtv )
    """
    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::run
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
        l_szMetodo = "viewPiloto::run"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        ##assert ( self._st )
        
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
        #self._dHoraSim = self._st.obtemHoraSim ()

        #** ---------------------------------------------------------------------------------------
        #*  eternal loop
        #*/
        while ( glbData.g_bKeepRun ):

            #** -----------------------------------------------------------------------------------
            #*  verifica condições de execução
            #*/
            #assert ( self._infoBox )
            ##assert ( self._menuBox )
            #assert ( self._msgBox )
            #assert ( self._oExe )
            #assert ( self._screen )
            #assert ( self._stripList )
            #assert ( self._voipBox )
            
            #** -----------------------------------------------------------------------------------
            #*  obtém o tempo inicial em segundos
            #*/
            #l_lNow = time.time ()
            #l_log.info ( "l_lNow: " + str ( l_lNow ))

            #** -----------------------------------------------------------------------------------
            #*  enquanto estiver congelado...
            #*/
            while (( glbData.g_bKeepRun ) and ( self._bPause )):

                #** -------------------------------------------------------------------------------
                #*  permite o scheduler (2/10th)
                #*/
                time.sleep ( glbDefs.xTIM_Wait )

            #** -----------------------------------------------------------------------------------
            #*  exibe relógio e versão
            #*/
            self._infoBox.doDraw ( self._screen )

            #** -----------------------------------------------------------------------------------
            #*  atualiza os vôos
            #*/
            self.updateFlights ()

            #** -----------------------------------------------------------------------------------
            #*  exibe parâmetros de comunicação
            #*/
            self._voipBox.doDraw ( self._screen )

            #** -----------------------------------------------------------------------------------
            #*  exibe mensagens de alertas e erros
            #*/
            self._msgBox.doDraw ( self._screen )

            #** -----------------------------------------------------------------------------------
            #*  atualiza a tela
            #*/
            self.dispFlip ()

            #** -----------------------------------------------------------------------------------
            #*  obtém o tempo final em segundos e calcula o tempo decorrido
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
    """
    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::showPercurso
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def showPercurso ( self, f_screen, f_stAtv ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::showPercurso"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert ( f_screen )
        #assert ( f_stAtv )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::selectAnvStrip
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def selectAnvStrip ( self, f_tMouse, f_bNav ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::selectAnvStrip"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert ( f_tMouse )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._fc )
        #assert ( self._menuBox )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a lista de vôos ativos
        #*/
        l_lstFlight = self._fc.getListFlight ()

        #** ---------------------------------------------------------------------------------------
        #*  percorre a lista de vôos ativos
        #*/
        for l_iI in xrange ( len ( l_lstFlight )):

            #** -----------------------------------------------------------------------------------
            #*  obtém um flight engine
            #*/
            l_fe = l_lstFlight [ l_iI ]
            #assert ( l_fe )

            #** -----------------------------------------------------------------------------------
            #*  obtém a area de dados da aeronave
            #*/
            l_stAtv = l_fe.getAtv ()
            #assert ( l_stAtv )

            #** -----------------------------------------------------------------------------------
            #*  obtém a posição da strip
            #*/
            l_tPosStrip = l_stAtv.getStrip ()
            #assert ( l_tPosStrip )

            #** -----------------------------------------------------------------------------------
            #*  cria um retangulo
            #*/
            l_rtStrip = pygame.Rect ( l_tPosStrip )
            #assert ( l_rtStrip )

            #** -----------------------------------------------------------------------------------
            #*  'click' dentro da 'strip' ? 
            #*/
            if ( l_rtStrip.collidepoint ( f_tMouse )):

                #** -------------------------------------------------------------------------------
                #*  deseleciona as outras aeronaves
                #*/
                #self._fc.deselectFlights ()

                #** -------------------------------------------------------------------------------
                #*  also update the color of the menu item...
                #*/
                #self._menuBox.deselectFlight ()

                #** -------------------------------------------------------------------------------
                #*  seleciona esta aeronave
                #*/
                l_stAtv.setSelected ( True, f_bNav )

                #** -------------------------------------------------------------------------------
                #*  also update the color of the menu item...
                #*/
                #self._menuBox.selectFlight ( l_stAtv )

                #** -------------------------------------------------------------------------------
                #*  retorna a aeronave selecionada
                #*/
                return ( l_stAtv )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  nao achou nenhuma aeronave para seleção
        #*/
        return ( None )

    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::updateAnv
    #*  -------------------------------------------------------------------------------------------
    #*  updates the display from the flights in the flightlist
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateAnv ( self, f_stAtv, f_iI ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::updateAnv"


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
        #assert ( self._font )
        #assert ( self._stAer )
        #assert ( self._screen )
        #assert ( self._stripList )
        
        #** ---------------------------------------------------------------------------------------
        #*  obtém a posição do vôo
        #*/
        l_tAnvPos = f_stAtv.getPosição ()
        #assert ( l_tAnvPos )
        #l_log.info ( "Posição............: " + str ( l_tAnvPos ))

        #** ---------------------------------------------------------------------------------------
        #*  normaliza
        #*/
        l_tAnvPos = viewUtils.normalizeXY ( l_tAnvPos )
        #assert ( l_tAnvPos )

        #** ---------------------------------------------------------------------------------------
        #*  converte para coordenadas de tela
        #*/
        l_tAnvPos = viewUtils.scale2Device ( l_tAnvPos )
        #assert ( l_tAnvPos )

        #** ---------------------------------------------------------------------------------------
        #*  calculate screen position
        #*/
        l_tScrPos = ( int ( round ( l_tAnvPos [ 0 ] )),
                      int ( round ( l_tAnvPos [ 1 ] )))
        #assert ( l_tScrPos )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a proa
        #*/
        l_dAnvProa = f_stAtv.getNavProa ()
        #l_log.info ( "Proa: " + str ( l_dAnvProa ))

        #** ---------------------------------------------------------------------------------------
        #*  calculate heading transformation
        #*/
        l_dRotate = 360. - l_dAnvProa - self._stAer.getDifDeclinação ()

        #** ---------------------------------------------------------------------------------------
        #*  aeronave selecionada ?
        #*/
        if ( f_stAtv.getSelected ()):

            #** -----------------------------------------------------------------------------------
            #*  user has selected this flight, use green icon
            #*/
            l_icnAtv = pygame.transform.rotate ( self._icnAtvGreen, l_dRotate )
            #assert ( l_icnAtv )

        #** ---------------------------------------------------------------------------------------
        #*  existem alertas para esta aeronave ?
        #*/
        elif ( f_stAtv.getAlert ()):

            #** -----------------------------------------------------------------------------------
            #*  this flight has alerts, use red icons
            #*/
            l_icnAtv = pygame.transform.rotate ( self._icnAtvRed, l_dRotate )
            #assert ( l_icnAtv )

            #** -----------------------------------------------------------------------------------
            #*  existe aviso de alerta
            #*/
            #if ( None != self._sndAlert ):

                #** -------------------------------------------------------------------------------
                #*  calcula o tempo desde o ultimo aviso
                #*/
                #l_dDlt = self._st.obtémHoraSim () - self._dHoraSim

                #** -------------------------------------------------------------------------------
                #*  ja passou mais de 1s ?
                #*/
                #if ( l_dDlt >= 1000. ):

                    #** ---------------------------------------------------------------------------
                    #*  emite o aviso sonoro
                    #*/
                    #self._sndAlert.play ()

                    #** ---------------------------------------------------------------------------
                    #*  salva a hora
                    #*/
                    #self._dHoraSim = self._st.obtémHoraSim ()

        #** ---------------------------------------------------------------------------------------
        #*  senao, normal flight
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  normal flight, use blue icon
            #*/
            l_icnAtv = pygame.transform.rotate ( self._icnAtvBlue, l_dRotate )
            #assert ( l_icnAtv )

        #** ---------------------------------------------------------------------------------------
        #*  calcula a posição do icone na tela
        #*/
        l_icnPos = l_icnAtv.get_rect ()
        #assert ( l_icnPos )

        #** ---------------------------------------------------------------------------------------
        #*  verifica se esta na porção visivel da tela
        #*/
        if ( viewUtils.checkClippingScr ( l_tScrPos, l_icnPos )):

            #** -----------------------------------------------------------------------------------
            #*  obtém a identificação do vôo
            #*/
            l_szTxt = f_stAtv.getIdent () #+ "/" + f_stAtv.getTipo ()
            #assert ( l_szTxt )

            #** -----------------------------------------------------------------------------------
            #*  cria o texto com Id e tipo na cor desejada
            #*/
            l_szTxt = self._font.render ( l_szTxt, 1, locDefs.xCOR_FlightNo )
            #assert ( l_szTxt )

            #** -----------------------------------------------------------------------------------
            #*  make the flight no stand under the icon
            #*/
            l_txtPos = l_szTxt.get_rect ()
            #assert ( l_txtPos )
            
            l_txtPos.center = ( l_tScrPos [ 0 ],
                                l_tScrPos [ 1 ] + 11 + l_txtPos.center [ 1 ] )

            #** -----------------------------------------------------------------------------------
            #*  ajusta o centro do icone
            #*/
            #l_icnPos = l_icnAtv.get_rect ()
            ##assert ( l_icnPos )

            l_icnPos.center = l_tScrPos
            #l_log.info ( "Posição na tela: " + str ( l_icnPos ))

            #** -----------------------------------------------------------------------------------
            #*  put the icon on the screen
            #*/
            #l_srf.set_colorkey ( l_srf.get_at (( 0, 0 )))
            self._screen.blit ( l_icnAtv, l_icnPos )

            #** -----------------------------------------------------------------------------------
            #*  put the flight no. on the screen
            #*/
            #l_srf.set_colorkey ( l_srf.get_at (( 0, 0 )))
            self._screen.blit ( l_szTxt, l_txtPos )

            #** -----------------------------------------------------------------------------------
            #*  should the nav target be displayed ?
            #*/
            if ( f_stAtv.getNav ()):

                #** -------------------------------------------------------------------------------
                #*  this is a nav select - draw target
                #*/
                l_navPos = self._icnAtvTarget.get_rect ()
                #assert ( l_navPos )

                l_navPos.center = l_tScrPos

                #** -------------------------------------------------------------------------------
                #*  transfere para a tela
                #*/
                #l_srf.set_colorkey ( l_srf.get_at (( 0, 0 )))
                self._screen.blit ( self._icnAtvTarget, l_navPos )

            #** -----------------------------------------------------------------------------------
            #*  exibe o percurso ?
            #*/
            if (( None != f_stAtv.getPercurso ()) and ( f_stAtv.getShowPercurso ())):

                #** -------------------------------------------------------------------------------
                #*  exibe o percurso da aeronave
                #*/
                self.showPercurso ( self._screen, f_stAtv )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza a strip da aeronave
        #*/
        self._stripList.doUpdate ( self._screen, f_iI, f_stAtv )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )
    """
    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::updateAnv
    #*  -------------------------------------------------------------------------------------------
    #*  updates the display from the flights in the flightlist
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_iI   - DOCUMENT ME!
    #*  @param  f_oAtv - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateAnv ( self, f_iI, f_oAtv ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewPiloto::updateAnv"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert ( f_oAtv )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._scope )
        #assert ( self._screen )
        
        #** ---------------------------------------------------------------------------------------
        #*  atualiza a strip da aeronave
        #*/
        #self._stripList.doUpdate ( self._screen, f_iI, f_oAtv )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza o scope
        #*/
        self._scope.doDraw ( self._screen, f_oAtv )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::updateFlights
    #*  -------------------------------------------------------------------------------------------
    #*  updates the display from the flights in the flightlist
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def updateFlights ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::updateFlights"


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
        #assert ( self._scope )
               
        #** ---------------------------------------------------------------------------------------
        #*  trava a lista de vôos
        #*/
        glbData.g_lckFlight.acquire ()

        #** ---------------------------------------------------------------------------------------
        #*/
        try:

            #** -----------------------------------------------------------------------------------
            #*  obtém a lista de vôos
            #*/
            l_lstFlight = self._fc.getListFlight ()

            #** -----------------------------------------------------------------------------------
            #*  existem vôos na lista ?
            #*/
            for l_iI in xrange ( len ( l_lstFlight )):
            
                #** -------------------------------------------------------------------------------
                #*  obtém o flight engine
                #*/
                l_fe = l_lstFlight [ l_iI ]
                #assert ( l_fe )

                #** -------------------------------------------------------------------------------
                #*  obtém a área de dados da aeronave ativa
                #*/
                l_oAtv = l_fe.getAtv ()
                #assert ( l_oAtv )

                #** -------------------------------------------------------------------------------
                #*  atualiza a posição da aeronave
                #*/
                self.updateAnv ( l_iI, l_oAtv )

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

    #** ===========================================================================================
    #*  acesso a area de dados do objeto
    #*  ===========================================================================================
    #*/

    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::getGuiApp
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getGuiApp ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::getGuiApp"


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
        return ( self._guiApp )

    #** -------------------------------------------------------------------------------------------
    #*  viewPiloto::getMenuBox
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getMenuBox ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        l_szMetodo = "viewPiloto::getMenuBox"


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
        return ( self._menuBox )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "viewPiloto" )

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
    l_vp = viewPiloto ( None )
    #assert ( l_vp )
                            
#** ----------------------------------------------------------------------------------------------- *#
