#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2008, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: guiSliders
#*
#*  Descrição: this class takes care of all interaction with the user
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  mlabru   2009/fev/12  version started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versao
#*  -----------------------------------------------------------------------------------------------
#*  start    2009/fev/12  version started
#*  1.2-0.1  2009/jun/20  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/

from __future__ import division

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

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.glbDefs as glbDefs
import model.locDefs as locDefs

#/ SiPAR / view
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
#*  guiSliders::guiSliders
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class guiSliders ( guiModel.guiModel ):

    #** -------------------------------------------------------------------------------------------
    #*  guiSliders::__init__
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
        #l_szMetodo = "guiSliders::__init__"


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
        guiModel.guiModel.__init__ ( self, f_cm, f_srf, f_tNW, f_tWH, u"parâmetros do PAR" )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o exercício
        #*/
        self._oExe = self._mm.getExercicio ()
        #assert ( self._oExe )
                                        
        #** ---------------------------------------------------------------------------------------
        #*  obtém o PAR
        #*/
        self._oPAR = self._oExe.getPAR ()
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  altura útil da caixa
        #*/
        self._iYTop = self._tNW [ 1 ] + locDefs.xSCR_HDR_Height

        #** ---------------------------------------------------------------------------------------
        #*  carrega a imagem dos sliders
        #*/
        self._imgSlider = viewUtils.loadImage ( "slider.png", True )
        #assert ( self._imgSlider )

        #** ---------------------------------------------------------------------------------------
        #*  variáveis de instância
        #*/
        self._fAAAnt = 0.
        self._bMudouAA = False

        self._fAEAnt = 0.
        self._bMudouAE = False

        self._aiLRAnt = [ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ]
        self._bMudouLR = False

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  guiSliders::cbkCheckSliders
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def cbkCheckSliders ( self, f_tMouse ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "guiSliders::cbkCheckSliders"


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
        #*  obtém a escala atual do desenho
        #*/
        l_iEsc = self._oExe.getEscala ()
        #assert ( l_iEsc in locDefs.xSET_EscalasValidas )
        
        l_iEsc -= 1

        #** ---------------------------------------------------------------------------------------
        #*  parâmetros da área
        #*/
        l_iXTop = self._tNW [ 0 ]
        l_iWide = self._tWH [ 0 ]

        #** ---------------------------------------------------------------------------------------
        #*  posição do mouse
        #*/
        l_iXM = f_tMouse [ 0 ]
        l_iYM = f_tMouse [ 1 ]

        #** ---------------------------------------------------------------------------------------
        #*  verifica coluna (x). Está entre as colunas limites do slider ?
        #*/
        if (( l_iXM >= ( l_iXTop + 10 )) and
            ( l_iXM <= ( l_iXTop + l_iWide - 10 ))):

            #** -----------------------------------------------------------------------------------
            #*  verifica linha (y). slider linha de referência
            #*/
            if (( l_iYM >= self._iYTop + 105 ) and
                ( l_iYM <= self._iYTop + 120 )):

                #** -------------------------------------------------------------------------------
                #*  altera o valor percentual da linha de referência
                #*/
                l_fVal = ( l_iXM - ( l_iXTop + 10 )) / ( l_iWide - 20 )

                #** -------------------------------------------------------------------------------
                #*  calcula o valor atual da linha de referência para esta escala
                #*/
                l_fLR = (( l_fVal * self._oPAR.getMaxHRefLine ( l_iEsc )) // 100 ) * 100

                #** -------------------------------------------------------------------------------
                #*  salva a linha de referência
                #*/
                self._oPAR.setHRefLine ( l_fLR )

                #** -------------------------------------------------------------------------------
                #*  avisa que mudou a linha de referência
                #*/
                self._oPAR.setMudouAlidades ( True )

                #** -------------------------------------------------------------------------------
                #*  avisa que mudou a linha de referência
                #*/
                self._bMudouLR = True

            #** -----------------------------------------------------------------------------------
            #*  verifica linha (y). slider alidade vertical
            #*/
            elif (( l_iYM >= self._iYTop + 65 ) and
                  ( l_iYM <= self._iYTop + 80 )):

                #** -------------------------------------------------------------------------------
                #*  altera o valor percentual da alidade vertical
                #*/
                l_fVal = ( l_iXM - ( l_iXTop + 10 )) / ( l_iWide - 20 )

                #** -------------------------------------------------------------------------------
                #*  calcula o valor atual da alidade vertical
                #*/
                l_fAA = ( l_fVal *
                        ( self._oPAR.getMaxAngAlidAzim () - self._oPAR.getMinAngAlidAzim ())) + \
                          self._oPAR.getMinAngAlidAzim ()

                #** -------------------------------------------------------------------------------
                #*  salva a alidade vertical
                #*/
                self._oPAR.setAngAlidAzim ( l_fAA )

                #** -------------------------------------------------------------------------------
                #*  avisa que mudou a alidade vertical
                #*/
                self._oPAR.setMudouAlidades ( True )

                #** -------------------------------------------------------------------------------
                #*  avisa que mudou a alidade vertical
                #*/
                self._bMudouAA = True

            #** -----------------------------------------------------------------------------------
            #*  verifica linha (y). slider alidade horizontal ?
            #*/
            elif (( l_iYM >= self._iYTop + 25 ) and
                  ( l_iYM <= self._iYTop + 40 )):

                #** -------------------------------------------------------------------------------
                #*  altera o valor percentual da alidade horizontal
                #*/
                l_fVal = ( l_iXM - ( l_iXTop + 10 )) / ( l_iWide - 20 )

                #** -------------------------------------------------------------------------------
                #*  calcula o valor atual da alidade horizontal
                #*/
                l_fAE = ( l_fVal *
                        ( self._oPAR.getMaxAngAlidElev () - self._oPAR.getMinAngAlidElev ())) + \
                          self._oPAR.getMinAngAlidElev ()

                #** -------------------------------------------------------------------------------
                #*  salva a alidade horizontal
                #*/
                self._oPAR.setAngAlidElev ( l_fAE )

                #** -------------------------------------------------------------------------------
                #*  avisa que mudou a alidade horizontal
                #*/
                self._oPAR.setMudouAlidades ( True )

                #** -------------------------------------------------------------------------------
                #*  avisa que mudou a alidade horizontal
                #*/
                self._bMudouAE = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  guiSliders::doDraw
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
        #l_szMetodo = "guiSliders::doDraw"


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
        #*  obtém o valor da alidade vertical
        #*/
        l_fAAAtu = self._oPAR.getAngAlidAzim ()

        #** ---------------------------------------------------------------------------------------
        #*  obtém o valor da alidade horizontal
        #*/
        l_fAEAtu = self._oPAR.getAngAlidElev ()

        #** ---------------------------------------------------------------------------------------
        #*  obtém o valor da linha de referência atual
        #*/
        l_iLRAtu = self._oPAR.getHRefLine ()

        #** ---------------------------------------------------------------------------------------
        #*  obtém a escala atual do desenho
        #*/
        l_iEsc = self._oExe.getEscala ()
        #assert ( l_iEsc in locDefs.xSET_EscalasValidas )
        
        l_iEsc -= 1

        #** ---------------------------------------------------------------------------------------
        #*  algo mudou ?
        #*/
        if (( self._bMudouAA ) or ( l_fAAAtu != self._fAAAnt ) or
            ( self._bMudouAE ) or ( l_fAEAtu != self._fAEAnt ) or
            ( self._bMudouLR ) or ( l_iLRAtu != self._aiLRAnt [ l_iEsc ] )):

            #** -----------------------------------------------------------------------------------
            #*  limpa o canvas
            #*/
            self._canvas.fill ( glbDefs.xCOR_black )

            #** -----------------------------------------------------------------------------------
            #*  desenha a área de controles
            #*/
            grUtils.drawRect ( self._canvas, ( 0, 0, self._tWH [ 0 ],
                                                     self._tWH [ 1 ] - locDefs.xSCR_HDR_Height ), 2 )

            #** -----------------------------------------------------------------------------------
            #*  escreve "alidade horizontal"
            #*/
            self.drawText ( self._canvas, 12, "alidade horizontal", locDefs.xCOR_Vers, ( 10, 5 ), 7 )

            #** -----------------------------------------------------------------------------------
            #*  desenha o controle 
            #*/
            grUtils.drawRect ( self._canvas, ( 10, 25, self._tWH [ 0 ] - 20, 15 ))

            #** -----------------------------------------------------------------------------------
            #*  desenha a escala
            #*/
            for l_Step in xrange ( 0, 230, 5 ):

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                l_posEsc = 15 + l_Step

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                pygame.draw.line ( self._canvas, locDefs.xCOR_SLD_AH, ( l_posEsc, 26 ), ( l_posEsc, 38 ))

            #** -----------------------------------------------------------------------------------
            #*  recalcula o valor percentual
            #*/
            l_fVal = 230. * (( l_fAEAtu + ( self._oPAR.getMinAngAlidElev () * -1 )) /
                            ( self._oPAR.getMaxAngAlidElev () - self._oPAR.getMinAngAlidElev ()))

            #** -----------------------------------------------------------------------------------
            #*  posiciona o slider
            #*/
            self._canvas.blit ( self._imgSlider, (( 14 + l_fVal ), 26 ))

            #** -----------------------------------------------------------------------------------
            #*  salva o valor atual
            #*/
            self._fAEAnt = l_fAEAtu
             
            #** -----------------------------------------------------------------------------------
            #*  reseta flag
            #*/
            self._bMudouAE = False


            #** -----------------------------------------------------------------------------------
            #*  escreve "alidade vertical"
            #*/
            self.drawText ( self._canvas, 12, "alidade vertical", locDefs.xCOR_Vers, ( 10, 45 ), 7 )

            #** -----------------------------------------------------------------------------------
            #*  desenha o controle 
            #*/
            grUtils.drawRect ( self._canvas, ( 10, 65, self._tWH [ 0 ] - 20, 15 ))

            #** -----------------------------------------------------------------------------------
            #*  desenha a escala
            #*/
            for l_Step in xrange ( 0, 230, 5 ):

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                l_posEsc = 15 + l_Step

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                pygame.draw.line ( self._canvas, locDefs.xCOR_SLD_AV, ( l_posEsc, 66 ), ( l_posEsc, 78 ))

            #** -----------------------------------------------------------------------------------
            #*  recalcula o valor percentual
            #*/
            l_fVal = 230. * (( l_fAAAtu + ( self._oPAR.getMinAngAlidAzim () * -1 )) /
                             ( self._oPAR.getMaxAngAlidAzim () - self._oPAR.getMinAngAlidAzim ()))

            #** -----------------------------------------------------------------------------------
            #*  posiciona o slider
            #*/
            self._canvas.blit ( self._imgSlider, (( 14 + l_fVal ), 66 ))

            #** -----------------------------------------------------------------------------------
            #*  salva o valor atual
            #*/
            self._fAAAnt = l_fAAAtu
             
            #** -----------------------------------------------------------------------------------
            #*  reseta flag
            #*/
            self._bMudouAA = False


            #** -----------------------------------------------------------------------------------
            #*  escreve "linha de referência"
            #*/
            self.drawText ( self._canvas, 12, u"linha de referência", locDefs.xCOR_Vers, ( 10, 85 ), 7 )

            #** -----------------------------------------------------------------------------------
            #*  desenha o controle 
            #*/
            grUtils.drawRect ( self._canvas, ( 10, 105, self._tWH [ 0 ] - 20, 15 ))

            #** -----------------------------------------------------------------------------------
            #*  desenha a escala
            #*/
            for l_Step in xrange ( 0, 230, 5 ):

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                l_posEsc = 15 + l_Step

                #** -------------------------------------------------------------------------------
                #*  desenha um step da escala
                #*/
                pygame.draw.line ( self._canvas, locDefs.xCOR_SLD_LR, ( l_posEsc, 106 ), ( l_posEsc, 118 ))

            #** -----------------------------------------------------------------------------------
            #*  recalcula o valor percentual
            #*/
            l_fVal = 230. * ( l_iLRAtu / self._oPAR.getMaxHRefLine ( l_iEsc ))

            #** -----------------------------------------------------------------------------------
            #*  posiciona o slider
            #*/
            self._canvas.blit ( self._imgSlider, (( 14 + int ( round ( l_fVal ))), 106 ))

            #** -----------------------------------------------------------------------------------
            #*  salva o valor atual
            #*/
            self._aiLRAnt [ l_iEsc ] = l_iLRAtu
             
            #** -----------------------------------------------------------------------------------
            #*  reseta flag
            #*/
            self._bMudouLR = False

            #** -----------------------------------------------------------------------------------
            #*  transfere o canvas para a superfície recebida (tela)
            #*/
            self.drawCanvas ( f_srf )

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
logger = logging.getLogger ( "guiSliders" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
