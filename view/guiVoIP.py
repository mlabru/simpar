#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2008, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: pyACME
#*  Classe...: guiVoIP
#*
#*  Descrição: this class takes care of all interaction with the user
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  mlabru   2009/set  1.0  versão para Linux
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  mlabru   2009/set  1.0  version started
#*  mlabru   2011/jan  1.01 release 01
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  includes
#*  -----------------------------------------------------------------------------------------------
#*/

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ pyGame (biblioteca gráfica)
#/ ------------------------------------------------------------------------------------------------
import pygame
import pygame.font

from pygame.locals import *

#/ pyACME / model
#/ ------------------------------------------------------------------------------------------------
import model.glbDefs as glbDefs
import model.locDefs as locDefs

#/ pyACME / view
#/ ------------------------------------------------------------------------------------------------
import view.grUtils as grUtils
import view.guiModel as guiModel
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
#*  guiVoIP::guiVoIP
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class guiVoIP ( guiModel.guiModel ):

    #** -------------------------------------------------------------------------------------------
    #*  guiVoIP::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the voip area
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_cm, f_srf, f_tNW, f_tWH ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "guiVoIP::__init__"


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

        #assert ( f_srf )
        #assert ( f_tNW )
        #assert ( f_tWH )

        #** ---------------------------------------------------------------------------------------
        #*  initialize super classe
        #*/
        guiModel.guiModel.__init__ ( self, f_cm, f_srf, f_tNW, f_tWH, u"comunicacao VoIP" )

        #** ---------------------------------------------------------------------------------------
        #*  carrega a biblioteca de VoIP
        #*/
        self._voip = f_cm.getVoIP ()
        #assert ( self._voip )

        #** ---------------------------------------------------------------------------------------
        #*  altura útil da caixa
        #*/
        self._iWrkY = self._tNW [ 1 ] + locDefs.xSCR_HDR_Height

        #** ---------------------------------------------------------------------------------------
        #*  carrega a imagem dos sliders
        #*/
        self._imgSlider = viewUtils.loadImage ( "slider.png", True )
        #assert ( self._imgSlider )

        #** ---------------------------------------------------------------------------------------
        #*  variáveis de instância
        #*/
        self._fVolOut = None
        self._fVolMic = None

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  guiVoIP::cbkCheckVoIP
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkCheckVoIP ( self, f_tMouse ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "guiVoIP::cbkCheckVoIP"


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
        #*  verifica coluna (x)
        #*/
        if (( f_tMouse [ 0 ] >= self._tNW [ 0 ] + 14 ) and
            ( f_tMouse [ 0 ] <= ( self._tNW [ 0 ] + self._tWH [ 0 ] - 20 ))):

            #** -----------------------------------------------------------------------------------
            #*  verifica linha (y)
            #*/
            if (( f_tMouse [ 1 ] >= self._iWrkY + 25 ) and
                ( f_tMouse [ 1 ] <= self._iWrkY + 40 )):

                #** -------------------------------------------------------------------------------
                #*  altera o volume de saida
                #*/
                glbDefs.xSND_Vol_Out = ( f_tMouse [ 0 ] - ( self._tNW [ 0 ] + 14 )) / 225.0
                #l_log.info ( "glbDefs.xSND_Vol_Out: " + str ( glbDefs.xSND_Vol_Out ))

                #** -------------------------------------------------------------------------------
                #*  altera o volume de saida
                #*/
                #self._voip.soundPlayVol ( int ( glbDefs.xSND_Vol_Out * 100 ) % 101 )
                #l_log.info ( "soundPlayVol: " + str ( glbDefs.xSND_Vol_Out * 100 ))

            #** -----------------------------------------------------------------------------------
            #*  verifica linha (y)
            #*/
            if (( f_tMouse [ 1 ] >= self._iWrkY + 65 ) and
                ( f_tMouse [ 1 ] <= self._iWrkY + 80 )):

                #** -------------------------------------------------------------------------------
                #*  altera o volume do microfone
                #*/
                glbDefs.xSND_Vol_Mic = ( f_tMouse [ 0 ] - ( self._tNW [ 0 ] + 14 )) / 225.0
                #l_log.info ( "glbDefs.xSND_Vol_Mic: " + str ( glbDefs.xSND_Vol_Mic ))

                #** -------------------------------------------------------------------------------
                #*  altera o volume do microfone
                #*/
                #self._voip.soundRecGain ( int ( glbDefs.xSND_Vol_Mic * 100 ) % 101 )
                #l_log.info ( "soundRecGain: " + str ( glbDefs.xSND_Vol_Mic * 100 ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  guiVoIP::doDraw
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the info area
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def doDraw ( self, f_srf ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "guiVoIP::doDraw"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert ( f_srf )

        #** ---------------------------------------------------------------------------------------
        #*  algo mudou ?
        #*/
        if (( glbDefs.xSND_Vol_Out != self._fVolOut ) or 
            ( glbDefs.xSND_Vol_Mic != self._fVolMic )):

            #** -----------------------------------------------------------------------------------
            #*  limpa o canvas
            #*/
            self._canvas.fill ( glbDefs.xCOR_black )

            #** -----------------------------------------------------------------------------------
            #*  desenha a area de controles VoIP
            #*/
            grUtils.drawRect ( self._canvas, ( 0, 0, self._tWH [ 0 ],
                                                     self._tWH [ 1 ] - locDefs.xSCR_HDR_Height ), 2 )

            #** -----------------------------------------------------------------------------------
            #*  escreve "volume do alto-falante"
            #*/
            self.drawText ( self._canvas, 12, "volume de saida", locDefs.xCOR_Vers, ( 10, 5 ), 7 )

            #** -----------------------------------------------------------------------------------
            #*  desenha o controle 
            #*/
            grUtils.drawRect ( self._canvas, ( 10, 25, self._tWH [ 0 ] - 20, 15 ))

            #** -----------------------------------------------------------------------------------
            #*  desenha a escala
            #*/
            for l_Step in xrange ( 2, 225, 5 ):

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                l_posEsc = 16 + l_Step

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                pygame.draw.line ( self._canvas, locDefs.xCOR_SLD_Out, ( l_posEsc, 26 ), ( l_posEsc, 38 ))

                #** -------------------------------------------------------------------------------
                #*  posiciona o slider
                #*/
                self._canvas.blit ( self._imgSlider, ( 14 + ( 225.0 * glbDefs.xSND_Vol_Out ), 26 ))

            #** -----------------------------------------------------------------------------------
            #*  escreve "volume do microfone"
            #*/
            self.drawText ( self._canvas, 12, "volume do microfone", locDefs.xCOR_Vers, ( 10, 45 ), 7 )

            #** -----------------------------------------------------------------------------------
            #*  desenha o controle 
            #*/
            grUtils.drawRect ( self._canvas, ( 10, 65, self._tWH [ 0 ] - 20, 15 ))

            #** -----------------------------------------------------------------------------------
            #*  desenha a escala
            #*/
            for l_Step in xrange ( 2, 225, 5 ):

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                l_posEsc = 16 + l_Step

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                pygame.draw.line ( self._canvas, locDefs.xCOR_SLD_Mic, ( l_posEsc, 66 ), ( l_posEsc, 78 ))

                #** -------------------------------------------------------------------------------
                #*  posiciona o slider
                #*/
                self._canvas.blit ( self._imgSlider, ( 14 + ( 225.0 * glbDefs.xSND_Vol_Mic ), 66 ))

            #** -----------------------------------------------------------------------------------
            #*  transfere o canvas para a superfície recebida (tela)
            #*/
            self.drawCanvas ( f_srf )

            #** -----------------------------------------------------------------------------------
            #*  salva os valores atuais
            #*/
            self._fVolOut = glbDefs.xSND_Vol_Out
            self._fVolMic = glbDefs.xSND_Vol_Mic

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** ===========================================================================================
    #*  acesso a área de dados do objeto
    #*  ===========================================================================================
    #*/

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "guiVoIP" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
