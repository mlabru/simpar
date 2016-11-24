#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2008-2011, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: view
#*  Classe...: guiInfo
#*
#*  Descrição: DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  mlabru   2009/set  1.0  versão para Linux
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
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

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  guiInfo::guiInfo
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class guiInfo ( guiModel.guiModel ):

    #** -------------------------------------------------------------------------------------------
    #*  guiInfo::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the info area
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_cm, f_srf, f_tNW, f_tWH ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "guiInfo::__init__"


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
        guiModel.guiModel.__init__ ( self, f_cm, f_srf, f_tNW, f_tWH, locDefs.xTXT_Hdr )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o simulation time engine
        #*/
        self._st = f_cm.getST ()
        #assert ( self._st )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o exercício
        #*/
        self._oExe = self._mm.getExercicio ()
        #assert ( self._oExe )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o indicativo do aeródromo (ou PAR)
        #*/
        self._szAer = self._oExe.getIndicativo ()
        #assert ( self._szAer )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o indicativo do aeródromo (ou PAR)
        #*/
        #self._szAer = self._oExe.getPAR ().getKey ()
        #assert ( self._szAer )

        #** ---------------------------------------------------------------------------------------
        #*  calcula a posição do texto (hora)
        #*/
        self._tPosHora = ( self._tCenter [ 0 ], self._tCenter [ 1 ] - 21 )
        #assert ( self._tPosHora ) 

        #** ---------------------------------------------------------------------------------------
        #*  calcula a posição do texto (exercício, aceleração e PAR)
        #*/
        self._tPosExe = ( self._tCenter [ 0 ], self._tCenter [ 1 ] - 2 )
        #assert ( self._tPosExe ) 

        #** ---------------------------------------------------------------------------------------
        #*  variáveis locais
        #*/
        self._fAccel = None
        self._szHora = None

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  guiInfo::doDraw
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def doDraw ( self, f_srf ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "guiInfo::doDraw"


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
        #*  verifica condições de execução
        #*/
        #assert ( self._st )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a hora formatada
        #*/
        l_szHora = self._st.getHoraFormat ()
        #assert ( l_szHora )

        #** ---------------------------------------------------------------------------------------
        #*  verifica se mudou a hora ou a velocidade do exercício
        #*/
        if (( l_szHora != self._szHora ) or ( glbDefs.xTIM_Accel != self._fAccel )):

            #** -----------------------------------------------------------------------------------
            #*  verifica condições de execução
            #*/
            #assert ( self._canvas )
            #assert ( self._oExe )
            #assert ( self._szAer )
            #assert ( self._tCenter )

            #** -----------------------------------------------------------------------------------
            #*  limpa o canvas
            #*/
            self._canvas.fill ( glbDefs.xCOR_black )

            #** -----------------------------------------------------------------------------------
            #*  desenha a área de informações
            #*/
            grUtils.drawRect ( self._canvas, ( 0, 0, self._tWH [ 0 ],
                                                     self._tWH [ 1 ] - locDefs.xSCR_HDR_Height ), 2 )

            #** -----------------------------------------------------------------------------------
            #*  escreve a hora
            #*/
            self.drawText ( self._canvas, 24, l_szHora, locDefs.xCOR_Hora, self._tPosHora, 5 )

            #** -----------------------------------------------------------------------------------
            #*  monta exercício, velocidade e aeródromo
            #*/
            l_szTxt = "%s(x%01d) - %s" % ( self._oExe.getKey (), glbDefs.xTIM_Accel, self._szAer )
            #assert ( l_szTxt )  

            #** -----------------------------------------------------------------------------------
            #*  escreve exercício, velocidade e aeródromo
            #*/
            self.drawText ( self._canvas, 12, l_szTxt, locDefs.xCOR_Vers, self._tPosExe, 5 )

            #** -----------------------------------------------------------------------------------
            #*  transfere o canvas para a superfície recebida (tela)
            #*/
            self.drawCanvas ( f_srf )

            #** -----------------------------------------------------------------------------------
            #*  salva os novos valores
            #*/
            self._fAccel = glbDefs.xTIM_Accel
            self._szHora = l_szHora

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
logger = logging.getLogger ( "guiInfo" )

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
    l_gui = guiInfo ( f_cm, f_srf, f_tNW, f_tWH )
    #assert ( l_gui )
                            
#** ----------------------------------------------------------------------------------------------- *#
