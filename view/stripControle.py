#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2008, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: stripControle
#*
#*  Descrição: this class takes care of all interaction with the user
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  mlabru   2008/fev/12  version started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    2008/fev/12  version started
#*  1.2-0.1  2008/jun/20  DOCUMENT ME!
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

from pygame.locals import *

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.glbDefs as glbDefs
import model.locDefs as locDefs

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
import view.guiStrip as guiStrip

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  stripControle::stripControle
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class stripControle ( guiStrip.guiStrip ):

    #** -------------------------------------------------------------------------------------------
    #*  stripControle::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the scope area
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_cm, f_srf, f_tNW, f_tWH ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "stripControle::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parametros de entrada
        #*/
        #assert ( f_cm )

        #assert ( f_srf )
        #assert ( f_tNW )
        #assert ( f_tWH )

        #** ---------------------------------------------------------------------------------------
        #*  inicia a superclass
        #*/
        guiStrip.guiStrip.__init__ ( self, f_cm, f_srf, f_tNW, f_tWH )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  stripControle::drawStripText
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*  @notes  Status,  Ident, Tipo,
    #*          Proa, Velocidade, Nivel,
    #*          ProaDem, VelDem,  NivDem,
    #*          Azimite, Distancia, QDM
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawStripText ( self, f_screen, f_tStripPos, f_stAtv ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "stripControle::drawStripText"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parametros de entrada
        #*/
        #assert ( f_screen )
        #assert ( f_tStripPos )
        #assert ( f_stAtv )

        #** ---------------------------------------------------------------------------------------
        #*  the positions of the center of the text fields
        #** ---------------------------------------------------------------------------------------
        #*  Matr | _SSR_ NAU | XXXX XXXX | ARR
        #*  Tipo | hh:mm 999 |           | RPL
        #** ---------------------------------------------------------------------------------------
        #*/
        l_lstPos = (( 30,  9 ), ( 86,  9 ), ( 124,  9 ), ( 157,  9 ), ( 193,  9 ), ( 230,  9 ),
                    ( 30, 28 ), ( 86, 28 ), ( 124, 28 ), ( 157, 28 ), ( 193, 28 ), ( 230, 28 ))

        #** ---------------------------------------------------------------------------------------
        #*  the colors of the fields
        #*/
        l_lstCor = ( glbDefs.xCOR_black, glbDefs.xCOR_black, glbDefs.xCOR_black,
                     glbDefs.xCOR_black, glbDefs.xCOR_black, glbDefs.xCOR_black,
                     glbDefs.xCOR_black, glbDefs.xCOR_black, glbDefs.xCOR_black,
                     glbDefs.xCOR_black, glbDefs.xCOR_black, glbDefs.xCOR_black )

        #** -----------------------------------------------------------------------------------
        #*  what to put in front of the points
        #*/
        l_lstTitle = ( '', '', '', '', '', '', '', '', '', '', '', '' )

        #** ---------------------------------------------------------------------------------------
        #*  get the data
        #*/
        l_lstData = f_stAtv.getStripData ()
        #assert ( l_lstData )

        #** -----------------------------------------------------------------------------------
        #*  format the data
        #*/
        l_lstData = self.formatData ( l_lstData )
        #assert ( l_lstData )

        #** ---------------------------------------------------------------------------------------
        #*  percorre a lista de dados a exibir na strip...
        #*/
        for l_iI in xrange ( len ( l_lstData )):

            #** -----------------------------------------------------------------------------------
            #*  monta o texto
            #*/
            l_szTxt = l_lstTitle [ l_iI ] + l_lstData [ l_iI ]
            #assert ( l_szTxt )

            #** -----------------------------------------------------------------------------------
            #*  cria o texto
            #*/
            l_szTxt = self._font.render ( l_szTxt, 1, l_lstCor [ l_iI ] )
            #assert ( l_szTxt )

            #** -----------------------------------------------------------------------------------
            #*  calcula a posição do texto
            #*/
            l_txtPos = l_szTxt.get_rect ()
            #assert ( l_txtPos )

            l_txtPos.center = ( l_lstPos [ l_iI ][ 0 ] + f_tStripPos [ 0 ],
                                l_lstPos [ l_iI ][ 1 ] + f_tStripPos [ 1 ] )

            #** -----------------------------------------------------------------------------------
            #*  transfere o texto para a tela
            #*/
            f_screen.blit ( l_szTxt, l_txtPos )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  stripControle::formatData
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*  Matr  _SSR_ NAU XXXX XXXX ARR
    #*  Tipo  hh:mm 999 XXXX XXXX RPL
    #** -------------------------------------------------------------------------------------------
    #*/
    def formatData ( self, l_lstData ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "stripControle::formatData"

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_szStat  = str ( l_lstData [ 0 ] )
        l_szIdent = str ( l_lstData [ 1 ] )
        l_szTipo  = str ( l_lstData [ 2 ] )
        l_fAlt    = float ( l_lstData [ 3 ] )

        #** ---------------------------------------------------------------------------------------
        #*  aeronave no solo ?
        #*/
        if ( 'S' == l_szStat [ 0 ] ):
        
            #** -----------------------------------------------------------------------------------
            #*  aguardando ?
            #*/
            if ( l_szStat in [ "SS", "SP" ] ):
            
                #** -------------------------------------------------------------------------------
                #*  aguardando
                #*/
                l_szStt = "wACC"

            #** -----------------------------------------------------------------------------------
            #*  acionado ?
            #*/
            if ( l_szStat in [ "SC", "SD", "ST" ] ):
            
                #** -------------------------------------------------------------------------------
                #*  acionado
                #*/
                l_szStt = "ACIO"

            #** -----------------------------------------------------------------------------------
            #*  na pista ?
            #*/
            if ( l_szStat in [ "SY" ] ):
            
                #** -------------------------------------------------------------------------------
                #*  na pista
                #*/
                l_szStt = "RWY"

            #** -----------------------------------------------------------------------------------
            #*  senao, aeronave no solo
            #*/
            else:
            
                #** -------------------------------------------------------------------------------
                #*  provavel decolagem
                #*/
                l_szStt = "DEP"

        #** ---------------------------------------------------------------------------------------
        #*  senao, aeronave em voo
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  em apx ?
            #*/
            if ( l_szStat in [ "VN" ] ):
            
                #** -------------------------------------------------------------------------------
                #*  apx
                #*/
                l_szStt = "APP"

            #** -----------------------------------------------------------------------------------
            #*  em contato ?
            #*/
            if ( l_szStat in [ "VC", "VD", "VF", "VK", "VP", "VV" ] ):
            
                #** -------------------------------------------------------------------------------
                #*  contato
                #*/
                l_szStt = "CONT"

            #** -----------------------------------------------------------------------------------
            #*  senao, aeronave em voo para pouso
            #*/
            else:
            
                #** -------------------------------------------------------------------------------
                #*  provável pouso
                #*/
                l_szStt = "ARR"
                
        #** ---------------------------------------------------------------------------------------
        #*  nível
        #*/
        l_szNiv = "%03d" % int ( round (( l_fAlt * glbDefs.xCNV_M2ft ) / 100. ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  Matr | SSR  NAU | xxxx xxxx | ARR
        #*  Tipo | Hora 999 |           | RPL
        #*/
        return (( l_szIdent, "_ssr_", "nau",   "____", "____", l_szStt,
                  l_szTipo,  "hh:mm", l_szNiv, "____", "____", "RPL" ))

    #** -------------------------------------------------------------------------------------------
    #*  guiStrip::makeIcon
    #*  -------------------------------------------------------------------------------------------
    #*  create a strip icon
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def makeIcon ( self, f_tCor ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "guiStrip::makeIcon"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  cria um icone de strip
        #*/
        l_srfIcn = pygame.Surface (( self._tWH [ 0 ], locDefs.xSCR_STP_Height - 2 ))
        #assert ( l_srfIcn )

        l_srfIcn.set_colorkey ( None )

        #** ---------------------------------------------------------------------------------------
        #*  preeche com a cor de fundo
        #*/
        l_srfIcn.fill ( f_tCor )
        #l_srfIcn.set_colorkey ( l_srfIcn.get_at (( 1, 1 )))

        #** ---------------------------------------------------------------------------------------
        #*  desenha as linhas internas do icone de strip
        #*/
        pygame.draw.line ( l_srfIcn, glbDefs.xCOR_black, (  61, 1 ), (  61, 36 ))
        #pygame.draw.line ( l_srfIcn, glbDefs.xCOR_black, ( 160, 1 ), ( 160, 36 ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  retorna o icone
        #*/
        return ( l_srfIcn )

    #** ===========================================================================================
    #*  acesso a área de dados do objeto
    #*  ===========================================================================================
    #*/

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "stripControle" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#