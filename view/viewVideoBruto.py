#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: viewVideoBruto
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

#/ Python libraries
#/ ------------------------------------------------------------------------------------------------
import math
import time

#/ log4Py
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

#** -----------------------------------------------------------------------------------------------
#*  defines
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  viewVideoBruto::viewVideoBruto
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class viewVideoBruto:

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  seta os parâmetros de entrada para início do exercício como escala, gate de entrada da
    #*  aeronave, altura da linha de referência (HRefLine) e inicia os ângulos de alidade.
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_cm  - control manager
    #*  @param  f_tWH - tupla com largura e altura do scope
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_cm, f_srf, f_tNW, f_tWH ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::__init__"


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
        #*  obtém o model manager
        #*/
        l_mm = f_cm.getMM ()
        #assert ( l_mm )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o objeto exercício
        #*/
        self._oExe = l_mm.getExercicio ()
        #assert ( self._oExe )

        #** ---------------------------------------------------------------------------------------
        #*  obtém o objeto PAR
        #*/
        self._oPAR = self._oExe.getPAR ()
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  salva o tamanho do scope localmente
        #*/
        self._tWH = f_tWH

        #** ---------------------------------------------------------------------------------------
        #*  cria a lista de ângulos de azimute
        #*/
        l_lst = [ x for x in xrange ( int ( self._oPAR._fAngAzimSup ) - 1,
                                      int ( self._oPAR._fAngAzimInf ), -1 ) ] 
        l_lst.reverse ()

        self._aiAngAzim = [ x for x in xrange ( int ( self._oPAR._fAngAzimSup ),
                                                int ( self._oPAR._fAngAzimInf ) - 1, -1 ) ]
        self._aiAngAzim.extend ( l_lst )

        #** ---------------------------------------------------------------------------------------
        #*  cria o índice da lista de ângulos de azimute
        #*/
        self._iIdxAzim = 0

        #** ---------------------------------------------------------------------------------------
        #*  cria a lista de ângulos de elevação
        #*/
        l_lst = [ x for x in xrange ( int ( self._oPAR._fAngElevSup ) - 1,
                                      int ( self._oPAR._fAngElevInf ), -1 ) ]
        l_lst.reverse ()

        self._aiAngElev = [ x for x in xrange ( int ( self._oPAR._fAngElevSup ),
                                                int ( self._oPAR._fAngElevInf ) - 1, -1 ) ]
        self._aiAngElev.extend ( l_lst )
        
        #** ---------------------------------------------------------------------------------------
        #*  cria o índice da lista de ângulos de elevação
        #*/
        self._iIdxElev = 0

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::calculaAnguloPlote
    #*  -------------------------------------------------------------------------------------------
    #*  calcula o ângulo em que o plote deve aparecer, em elevação, com relação ao plano da antena
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def calculaAnguloPlote ( self, f_iEsc, f_iCab, f_iXP, f_iYP, f_bElev ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::calculaAnguloPlote"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  cabeceira em uso é a principal ?
        #*/
        if ( 0 == f_iCab ):

            #** -----------------------------------------------------------------------------------
            #*  calcula a projeção em X da posição da aeronave
            #*/
            l_iDltX = int ( self._oPAR._aiXAntena [ 0 ][ f_iEsc ] ) - f_iXP

        #** ---------------------------------------------------------------------------------------
        #*  senão, é a cabeceira secundária
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  calcula a projeção em X da posição da aeronave
            #*/
            l_iDltX = f_iXP - int ( self._oPAR._aiXAntena [ 1 ][ f_iEsc ] )

        #** ---------------------------------------------------------------------------------------
        #*  calcula ângulo de elevação ?
        #*/
        if ( f_bElev ):

            #** -----------------------------------------------------------------------------------
            #*  calcula a projeção em Y da posição da aeronave
            #*/
            l_iDltY = int ( self._oPAR._aiYAntenaElev [ f_iCab ][ f_iEsc ] ) - f_iYP

        #** ---------------------------------------------------------------------------------------
        #*  senão, calcula ângulo de azimute ?
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  calcula a projeção em Y da posição da aeronave
            #*/
            l_iDltY = int ( self._oPAR._aiYAntenaAzim [ f_iCab ][ f_iEsc ] ) - f_iYP

        #** ---------------------------------------------------------------------------------------
        #*  calcula o valor do ângulo
        #*/
        l_iTeta = int ( round ( math.degrees ( math.atan ( float ( l_iDltY ) / float ( l_iDltX )))))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( l_iTeta )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::calculaPosicaoPlote
    #*  -------------------------------------------------------------------------------------------
    #*  calcula XPlot, YPlotElev e YPlotAzim a partir das coordenadas da aeronave transformadas
    #*  para coordenadas de tela
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_oFlt - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def calculaPosicaoPlote ( self, f_oFlt, f_iEsc, f_iCab ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::calculaPosicaoPlote"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( f_oFlt )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a posição do vôo
        #*/
        l_tAnvPos = f_oFlt.getPosicao ()
        #assert ( l_tAnvPos )

        #** ---------------------------------------------------------------------------------------
        #*  converte para coordenadas de tela
        #*/
        l_iD = int ( l_tAnvPos [ 0 ] * self._oPAR._afFatorEscX [ f_iEsc ] )
        l_iA = int ( l_tAnvPos [ 1 ] * self._oPAR._afFatorEscYAzim [ f_iEsc ] )
        l_iH = int ( f_oFlt.getAlt () * self._oPAR._afFatorEscYElev [ f_iEsc ] )

        #** ---------------------------------------------------------------------------------------
        #*  cálculo de l_iXPlot
        #*/
        l_iXPlot = self._oPAR._iXPonToque [ f_iCab ] + l_iD

        #** ---------------------------------------------------------------------------------------
        #*  cabeceira em uso é a principal ?
        #*/
        if ( 0 == f_iCab ):

            #** -----------------------------------------------------------------------------------
            #*  valida a posição de plot
            #*/
            if (( abs ( l_iD ) >= self._oPAR._iXPonToque    [ 0 ] ) or 
                      ( l_iD   >= self._oPAR._aiDistAntPT0T [ 0 ][ f_iEsc ] )):

                l_iXPlot = -1

        #** ---------------------------------------------------------------------------------------
        #*  senão, é cabeceira secundária
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  valida a posição de plot
            #*/
            if (( l_iD >= ( self._tWH [ 0 ] - self._oPAR._iXPonToque [ 1 ] )) or
                ( l_iD <= ( -1 * self._oPAR._aiDistAntPT1T [ 1 ][ f_iEsc ] ))):

                l_iXPlot = -1

        #** ---------------------------------------------------------------------------------------
        #*  cálculo de l_iYPlotAzm
        #*/
        if ( l_iA >= 0 ):

            #** -----------------------------------------------------------------------------------
            #*/
            if ( l_iA > ( self._oPAR._iYPonToqueAzim - ( self._tWH [ 1 ] / 2 ))):

                l_iYPlotAzm = -1

            else:

                l_iYPlotAzm = self._oPAR._iYPonToqueAzim - l_iA

        #** ---------------------------------------------------------------------------------------
        #*  senão, l_iA < 0
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            if ( abs ( l_iA ) > (( self._tWH [ 1 ] -1 ) - self._oPAR._iYPonToqueAzim )):

                l_iYPlotAzm = -1

            else:

                l_iYPlotAzm = self._oPAR._iYPonToqueAzim + abs ( l_iA )

        #** ---------------------------------------------------------------------------------------
        #*  cálculo de l_iYPlotElv
        #*/
        if (( l_iH < 0 ) or ( l_iH >= self._oPAR._iYPonToqueElev )):

            l_iYPlotElv = -1

        else:

            l_iYPlotElv = self._oPAR._iYPonToqueElev - l_iH

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( l_iXPlot, l_iYPlotAzm, l_iYPlotElv )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::doDraw
    #*  -------------------------------------------------------------------------------------------
    #*  desenha as informações de vídeo bruto, como varredura e plote
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_oFlt - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def doDraw ( self, f_srf, f_oFlt ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::doDraw"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução (I)
        #*/
        #assert ( f_srf )
        #assert ( f_oFlt )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução (II)
        #*/
        #assert ( self._oExe )
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a escala atual do desenho
        #*/
        l_iEsc = self._oExe.getEscala ()
        #assert ( l_iEsc in locDefs.xSET_EscalasValidas )

        l_iEsc -= 1

        #** ---------------------------------------------------------------------------------------
        #*  obtém a cabeceira atual em uso
        #*/
        l_iCab = self._oExe.getCabAtu ()
        #assert ( l_iCab in locDefs.xSET_CabsValidas )

        #** ---------------------------------------------------------------------------------------
        #*  posição da antena
        #*/
        l_iXAnt = self._oPAR._aiXAntena [ l_iCab ][ l_iEsc ]

        #** ---------------------------------------------------------------------------------------
        #*  posição válida ?
        #*/
        if ( l_iXAnt >= 0 ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_iYAnt = self._oPAR._aiYAntenaAzim [ l_iCab ][ l_iEsc ]

            #** -----------------------------------------------------------------------------------
            #*/
            self.plotarPontos ( f_srf, 2, ( l_iXAnt, l_iYAnt ), glbDefs.xCOR_white )
            
            #** -----------------------------------------------------------------------------------
            #*/
            l_iYAnt = self._oPAR._aiYAntenaElev [ l_iCab ][ l_iEsc ]

            #** -----------------------------------------------------------------------------------
            #*/
            self.plotarPontos ( f_srf, 2, ( l_iXAnt, l_iYAnt ), glbDefs.xCOR_white )
            
        #** ---------------------------------------------------------------------------------------
        #*  desenha o plote da aeronave
        #*/
        self.drawAnv ( f_srf, f_oFlt, l_iCab, l_iEsc )

        #** ---------------------------------------------------------------------------------------
        #*  desenha a varredura de azimute
        #*/
        self.drawAzimute ( f_srf, l_iCab, l_iEsc )

        #** ---------------------------------------------------------------------------------------
        #*  desenha a varredura de elevação
        #*/
        self.drawElevation ( f_srf, l_iCab, l_iEsc )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::drawAnv
    #*  -------------------------------------------------------------------------------------------
    #*  desenha as informações de plote de vídeo bruto
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_oFlt - DOCUMENT ME!
    #*  @param  f_iCab - DOCUMENT ME!
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawAnv ( self, f_srf, f_oFlt, f_iCab, f_iEsc ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::drawAnv"


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
        #assert ( f_oFlt )

        #** ---------------------------------------------------------------------------------------
        #*  calcula posição do plote
        #*/
        l_iXPlot, l_iYPlotAzim, l_iYPlotElev = self.calculaPosicaoPlote ( f_oFlt, f_iEsc, f_iCab )

        #** ---------------------------------------------------------------------------------------
        #*  verifica se o plote é válido
        #*/
        if ( -1 == l_iXPlot ):

            #** -----------------------------------------------------------------------------------
            #*  m.poirot logger
            #*/
            #l_log.debug ( "<< " )

            #** -----------------------------------------------------------------------------------
            #*/
            return

        #** ---------------------------------------------------------------------------------------
        #*  verifica se o plote é válido
        #*/
        if ( -1 != l_iYPlotAzim ):

            #** -----------------------------------------------------------------------------------
            #*  verifica se o ângulo atual corresponde ao ângulo de plote
            #*/
            if ( self._aiAngAzim [ self._iIdxAzim ] == self.calculaAnguloPlote ( f_iEsc, f_iCab, l_iXPlot, l_iYPlotAzim, False )):

                #** -------------------------------------------------------------------------------
                #*  plota a aeronave na área de azimute 
                #*/
                pygame.draw.ellipse ( f_srf, glbDefs.xCOR_white, (( l_iXPlot - 3, l_iYPlotAzim - 4 ), ( 6, 8 )), 0 )

        #** ---------------------------------------------------------------------------------------
        #*  verifica se o plote é válido
        #*/
        if ( -1 != l_iYPlotElev ):

            #** -----------------------------------------------------------------------------------
            #*  verifica se o ângulo atual corresponde ao ângulo de plote
            #*/
            if ( self._aiAngElev [ self._iIdxElev ] == self.calculaAnguloPlote ( f_iEsc, f_iCab, l_iXPlot, l_iYPlotElev, True )):

                #** -------------------------------------------------------------------------------
                #*  plota a aeronave na área de elevação
                #*/
                pygame.draw.ellipse ( f_srf, glbDefs.xCOR_white, (( l_iXPlot - 4, l_iYPlotElev - 3 ), ( 8, 6 )), 0 )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::drawAzimute
    #*  -------------------------------------------------------------------------------------------
    #*  desenha as informações de varredura de vídeo bruto em azimute
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_iCab - DOCUMENT ME!
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawAzimute ( self, f_srf, f_iCab, f_iEsc ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::drawAzimute"


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
        #*  ângulo de azimute
        #*/
        l_iAngAzm = self._aiAngAzim [ self._iIdxAzim ]
        
        #** ---------------------------------------------------------------------------------------
        #*  verifica se é para desenhar uma varredura de azimute negativa
        #*/
        if ( l_iAngAzm < 0 ):

            #** -----------------------------------------------------------------------------------
            #*  desenha varreduras azimute para baixo e desenha plote
            #*/
            self.drawAzimuteDown ( f_srf, f_iCab, f_iEsc, l_iAngAzm )

        #** ---------------------------------------------------------------------------------------
        #*  senão, é para desenhar uma varredura de azimute positiva
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  desenha varreduras azimute para cima e desenha plote
            #*/
            self.drawAzimuteUp ( f_srf, f_iCab, f_iEsc, l_iAngAzm )
        
        #** ---------------------------------------------------------------------------------------
        #*  incrementa o índice da lista de ângulos de azimute
        #*/
        self._iIdxAzim = ( self._iIdxAzim + 1 ) % len ( self._aiAngAzim )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::drawAzimuteDown
    #*  -------------------------------------------------------------------------------------------
    #*  desenha varreduras azimute para baixo e desenha plote
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_iCab - DOCUMENT ME!
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawAzimuteDown ( self, f_srf, f_iCab, f_iEsc, f_iAng ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::drawAzimuteDown"


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
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  para todos os range marks...
        #*/
        for l_iRMark in xrange ( self._oPAR._aiNumMarks [ f_iEsc ] + 1 ):

            #** -----------------------------------------------------------------------------------
            #*  é um range mark hilight ?
            #*/
            if ( 0 == (( l_iRMark + 1 ) % self._oPAR._aiMarkHiLight [ f_iEsc ] )):

                l_tCor = glbDefs.xCOR_white

            #** -----------------------------------------------------------------------------------
            #*  senão, é um range mark normal
            #*/
            else:

                l_tCor = glbDefs.xCOR_white

            #** -----------------------------------------------------------------------------------
            #*  calcula quantidade de pontos à desenhar
            #*/
            l_iN = ( l_iRMark // 3 ) + 1

            #** -----------------------------------------------------------------------------------
            #*  obtém o ponto via matriz
            #*/
            l_tXY = self._oPAR._MatrizAzi [ f_iEsc ][ f_iAng ][ l_iRMark ][ f_iCab ]

            #** -----------------------------------------------------------------------------------
            #*  verifica se o ponto Y está no range...
            #*/
            if (( l_tXY [ 1 ] > (( self._tWH [ 1 ] / 2 ) + 1 )) and ( l_tXY [ 1 ] < self._tWH [ 1 ] )):

                #** -------------------------------------------------------------------------------
                #*/
                self.plotarPontos ( f_srf, l_iN, l_tXY, l_tCor )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::drawAzimuteUp
    #*  -------------------------------------------------------------------------------------------
    #*  desenha varreduras azimute para cima e plote
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_iCab - DOCUMENT ME!
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawAzimuteUp ( self, f_srf, f_iCab, f_iEsc, f_iAng ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::drawAzimuteUp"


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
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  para todos os range marks...
        #*/
        for l_iRMark in xrange ( self._oPAR._aiNumMarks [ f_iEsc ] + 1 ):

            #** -----------------------------------------------------------------------------------
            #*  é um range mark hilight ?
            #*/
            if ( 0 == (( l_iRMark + 1 ) % self._oPAR._aiMarkHiLight [ f_iEsc ] )):

                l_tCor = glbDefs.xCOR_white

            #** -----------------------------------------------------------------------------------
            #*  senão, é um range mark normal
            #*/
            else:

                l_tCor = glbDefs.xCOR_white

            #** -----------------------------------------------------------------------------------
            #*  calcula quantidade de pontos à desenhar
            #*/
            l_iN = ( l_iRMark // 3 ) + 1

            #** -----------------------------------------------------------------------------------
            #*  obtém o ponto via matriz
            #*/
            l_tXY = self._oPAR._MatrizAzi [ f_iEsc ][ f_iAng ][ l_iRMark ][ f_iCab ]

            #** -----------------------------------------------------------------------------------
            #*  verifica se o ponto Y está no range...
            #*/
            if (( l_tXY [ 1 ] > (( self._tWH [ 1 ] / 2 ) + 1 )) and ( l_tXY [ 1 ] < self._tWH [ 1 ] )):

                #** -------------------------------------------------------------------------------
                #*/
                self.plotarPontos ( f_srf, l_iN, l_tXY, l_tCor )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::drawElevation
    #*  -------------------------------------------------------------------------------------------
    #*  desenha as informações de varredura de vídeo bruto em elevação
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_iCab - DOCUMENT ME!
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawElevation ( self, f_srf, f_iCab, f_iEsc ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::drawElevation"


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
        #*  ângulo de elevação
        #*/
        l_iAngElv = self._aiAngElev [ self._iIdxElev ]
        
        #** ---------------------------------------------------------------------------------------
        #*  verifica se é para desenhar uma varredura de elevação negativa
        #*/
        if ( l_iAngElv < 0 ):

            #** -----------------------------------------------------------------------------------
            #*  desenha varreduras elevação para baixo e plote
            #*/
            self.drawElevationDown ( f_srf, f_iCab, f_iEsc, l_iAngElv )

        #** ---------------------------------------------------------------------------------------
        #*  senão, é para desenhar uma varredura de elevação positiva
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  desenha varreduras elevação para cima e plote
            #*/
            self.drawElevationUp ( f_srf, f_iCab, f_iEsc, l_iAngElv )

        #** ---------------------------------------------------------------------------------------
        #*  incrementa o índice da lista de ângulos de elevação
        #*/
        self._iIdxElev = ( self._iIdxElev + 1 ) % len ( self._aiAngElev )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::drawElevationDown
    #*  -------------------------------------------------------------------------------------------
    #*  desenha varreduras elevação para baixo e plote
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_iCab - DOCUMENT ME!
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawElevationDown ( self, f_srf, f_iCab, f_iEsc, f_iAng ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::drawElevationDown"


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
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  para todos os range marks...
        #*/
        for l_iRMark in xrange ( self._oPAR._aiNumMarks [ f_iEsc ] + 1 ):

            #** -----------------------------------------------------------------------------------
            #*  é um range mark hilight ?
            #*/
            if ( 0 == (( l_iRMark + 1 ) % self._oPAR._aiMarkHiLight [ f_iEsc ] )):

                l_tCor = glbDefs.xCOR_white

            #** -----------------------------------------------------------------------------------
            #*  senão, é um range mark normal
            #*/
            else:

                l_tCor = glbDefs.xCOR_white

            #** -----------------------------------------------------------------------------------
            #*  calcula quantidade de pontos à desenhar
            #*/
            l_iN = ( l_iRMark // 3 ) + 1

            #** -----------------------------------------------------------------------------------
            #*  obtém o ponto via matriz
            #*/
            l_tXY = self._oPAR._MatrizEle [ f_iEsc ][ f_iAng ][ l_iRMark ][ f_iCab ]

            #** -----------------------------------------------------------------------------------
            #*/
            if (( l_tXY [ 1 ] >= 0 ) and ( l_tXY [ 1 ] < (( self._tWH [ 1 ] / 2 ) - 1 ))):

                #** ------------------------------------------------------------------------------
                #*  verifica se o ponto Y está no range...
                #*/
                self.plotarPontos ( f_srf, l_iN, l_tXY, l_tCor )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::drawElevationUp
    #*  -------------------------------------------------------------------------------------------
    #*  desenha varredura elevação para cima e plote
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_iCab - DOCUMENT ME!
    #*  @param  f_iEsc - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawElevationUp ( self, f_srf, f_iCab, f_iEsc, f_iAng ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::drawElevationUp"


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
        #assert ( self._oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  para todos os range marks...
        #*/
        for l_iRMark in xrange ( self._oPAR._aiNumMarks [ f_iEsc ] + 1 ):

            #** -----------------------------------------------------------------------------------
            #*  é um range mark hilight ?
            #*/
            if ( 0 == (( l_iRMark + 1 ) % self._oPAR._aiMarkHiLight [ f_iEsc ] )):

                l_tCor = glbDefs.xCOR_white

            #** -----------------------------------------------------------------------------------
            #*  senão, é um range mark normal
            #*/
            else:

                l_tCor = glbDefs.xCOR_white

            #** -----------------------------------------------------------------------------------
            #*  calcula quantidade de pontos à desenhar
            #*/
            l_iN = ( l_iRMark // 3 ) + 1

            #** -----------------------------------------------------------------------------------
            #*  obtém o ponto via matriz
            #*/
            l_tXY = self._oPAR._MatrizEle [ f_iEsc ][ f_iAng ][ l_iRMark ][ f_iCab ]

            #** -----------------------------------------------------------------------------------
            #*/
            if (( l_tXY [ 1 ] >= 0 ) and ( l_tXY [ 1 ] < (( self._tWH [ 1 ] / 2 ) - 1 ))):

                #** -------------------------------------------------------------------------------
                #*  verifica se o ponto Y está no range...
                #*/
                self.plotarPontos ( f_srf, l_iN, l_tXY, l_tCor )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoBruto::plotarPontos
    #*  -------------------------------------------------------------------------------------------
    #*  plota f_iN pontos na vertical a partir da coordenada (f_iX, f_iY) na direção vertical e
    #*  sentido para baixo na cor dada por f_tCor.
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf  - DOCUMENT ME!
    #*  @param  f_iN   - DOCUMENT ME!
    #*  @param  f_tXY  - DOCUMENT ME!
    #*  @param  f_tCor - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def plotarPontos ( self, f_srf, f_iN, f_tXY, f_tCor ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoBruto::plotarPontos"


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
        #*  plota f_iN pontos na vertical l_iY
        #*/
        for l_iY in xrange ( f_iN ):

            #** -----------------------------------------------------------------------------------
            #*  plota o ponto definido
            #*/
            f_srf.set_at (( f_tXY [ 0 ], f_tXY [ 1 ] + l_iY ), f_tCor )

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
logger = logging.getLogger ( "viewVideoBruto" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *
