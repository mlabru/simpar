#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: viewVideoSintetico
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

#/ math library
#/ ------------------------------------------------------------------------------------------------
import math

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

#/ SiPAR / view
#/ ------------------------------------------------------------------------------------------------
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
#*  viewVideoSintetico::viewVideoSintetico
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class viewVideoSintetico:

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  seta os parâmetros de entrada para início do exercício como escala, gate de entrada da
    #*  aeronave
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_cm  - control manager
    #*  @param  f_tWH - tupla com largura e altura do scope
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_cm, f_tWH ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::__init__"


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
        #*  superfície que define o vídeo sintético
        #*/
        self._srfVS = None

        #** ---------------------------------------------------------------------------------------
        #*  monta as matrizes
        #*/
        self.__montaMatrizes ()

        #** ---------------------------------------------------------------------------------------
        #*  inicia o desenho do vídeo sintético
        #*/
        self.doRedraw ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::__montaMatrizes
    #*  -------------------------------------------------------------------------------------------
    #*  monta as matrizes tridimensionais (Escala, Angulo, PixStepMark) dos pontos geradores das
    #*  imagens das varreduras para cada escala.
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __montaMatrizes ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::__montaMatrizes"


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
        #*  para todas as escalas...
        #*/
        for l_iEsc in xrange ( locDefs.xMAX_Escalas ):

            #** -----------------------------------------------------------------------------------
            #*  geração dos dados para todos os ângulos de azimute
            #*/
            for l_iAng in xrange ( int ( self._oPAR._fAngAzimSup ), int ( self._oPAR._fAngAzimInf ) - 1, -1 ):

                #** -------------------------------------------------------------------------------
                #*  cálculo da tangente do ângulo de azimute
                #*/
                l_fTan = math.tan ( math.radians ( float ( l_iAng )))

                #** -------------------------------------------------------------------------------
                #*  para todos os range marks...
                #*/
                for l_iRMrk in xrange ( self._oPAR._aiNumMarks [ l_iEsc ] + 1 ):

                    #** ---------------------------------------------------------------------------
                    #*  para as duas cabeceiras...
                    #*/
                    for l_iCab in xrange ( locDefs.xMAX_Cabeceiras ):

                        #** -----------------------------------------------------------------------
                        #*  deslocamento horizontal (em pixels)
                        #*/
                        l_iT = self._oPAR._aiPixStepMark [ l_iEsc ] * l_iRMrk

                        #** -----------------------------------------------------------------------
                        #*  cabeceira principal (0=principal/1=secundária) ?
                        #*/
                        if ( 0 == l_iCab ):

                            #** -------------------------------------------------------------------
                            #*  variação horizontal real (em pixels)
                            #*/
                            l_iDltX = self._oPAR._aiXAntena [ 0 ][ l_iEsc ] - self._oPAR._iXPonToque [ 0 ] + l_iT

                            #** -------------------------------------------------------------------
                            #*  ponto de cruzamento em X do feiche com o range mark
                            #*/
                            l_iX = self._oPAR._iXPonToque [ 0 ] - l_iT

                        #** -----------------------------------------------------------------------
                        #*  senão, cabeceira secundária
                        #*/
                        else:

                            #** -------------------------------------------------------------------
                            #*  variação horizontal real (em pixels)
                            #*/
                            l_iDltX = self._oPAR._iXPonToque [ 1 ] - self._oPAR._aiXAntena [ 1 ][ l_iEsc ] + l_iT

                            #** -------------------------------------------------------------------
                            #*  ponto de cruzamento em X do feiche com o range mark
                            #*/
                            l_iX = self._oPAR._iXPonToque [ 1 ] + l_iT

                        #** -----------------------------------------------------------------------
                        #*  variação vertical real (em pixels)
                        #*/
                        l_fDltY = l_iDltX * l_fTan

                        #** -----------------------------------------------------------------------
                        #*  ponto de cruzamento em Y do feiche com o range mark
                        #*/
                        l_iY = int ( round ( self._oPAR._aiYAntenaAzim [ l_iCab ][ l_iEsc ] - l_fDltY ))

                        #** -----------------------------------------------------------------------
                        #*  salva o valor na matriz
                        #*/
                        self._oPAR._MatrizAzi [ l_iEsc ][ l_iAng ][ l_iRMrk ][ l_iCab ] = ( l_iX, l_iY )

            #** -----------------------------------------------------------------------------------
            #*  geração dos dados para todos os ângulos de elevação...
            #*/
            for l_iAng in xrange ( int ( self._oPAR._fAngElevSup ), int ( self._oPAR._fAngElevInf ) - 1, -1 ):

                #** -------------------------------------------------------------------------------
                #*  cálculo da tangente do ângulo de elevação
                #*/
                l_fTan = math.tan ( math.radians ( l_iAng ))

                #** -------------------------------------------------------------------------------
                #*  para todos os range marks...
                #*/
                for l_iRMrk in xrange ( self._oPAR._aiNumMarks [ l_iEsc ] + 1 ):

                    #** ---------------------------------------------------------------------------
                    #*  para as duas cabeceiras...
                    #*/
                    for l_iCab in xrange ( locDefs.xMAX_Cabeceiras ):

                        #** -----------------------------------------------------------------------
                        #*  deslocamento horizontal (em pixels)
                        #*/
                        l_iT = self._oPAR._aiPixStepMark [ l_iEsc ] * l_iRMrk

                        #** -----------------------------------------------------------------------
                        #*  cabeceira principal (0=principal/1=secundária) ?
                        #*/
                        if ( 0 == l_iCab ):

                            #** -------------------------------------------------------------------
                            #*  variação horizontal real (em pixels)
                            #*/
                            l_iDltX = self._oPAR._aiXAntena [ 0 ][ l_iEsc ] - self._oPAR._iXPonToque [ 0 ] + l_iT

                            #** -----------------------------------------------------------------------
                            #*  ponto de cruzamento em X do feiche com o range mark
                            #*/
                            l_iX = self._oPAR._iXPonToque [ 0 ] - l_iT 

                        #** -----------------------------------------------------------------------
                        #*  senão, cabeceira secundária
                        #*/
                        else:

                            #** -------------------------------------------------------------------
                            #*  variação horizontal real (em pixels)
                            #*/
                            l_iDltX = self._oPAR._iXPonToque [ 1 ] - self._oPAR._aiXAntena [ 1 ][ l_iEsc ] + l_iT

                            #** -----------------------------------------------------------------------
                            #*  ponto de cruzamento em X do feiche com o range mark
                            #*/
                            l_iX = self._oPAR._iXPonToque [ 1 ] + l_iT
                            
                        #** -----------------------------------------------------------------------
                        #*  variação vertical real (em pixels)
                        #*/
                        l_fDltY = float ( l_iDltX ) * l_fTan

                        #** -----------------------------------------------------------------------
                        #*  ponto de cruzamento em Y do feiche com o range mark
                        #*/
                        l_iY = int ( round ( self._oPAR._aiYAntenaElev [ l_iCab ][ l_iEsc ] - l_fDltY ))
                            
                        #** -----------------------------------------------------------------------
                        #*  salva o valor na matriz
                        #*/
                        self._oPAR._MatrizEle [ l_iEsc ][ l_iAng ][ l_iRMrk ][ l_iCab ] = ( l_iX, l_iY )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::doDraw
    #*  -------------------------------------------------------------------------------------------
    #*  transfere o desenho do vídeo sintético para a superfície recebida
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_srf - superfície recebida onde desenhar o vídeo sintético
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def doDraw ( self, f_srf ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::doDraw"


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
        #*  camada 1. transfere o desenho do vídeo sintético para a superfície recebida
        #*/
        f_srf.blit ( self._srfVS, ( 0, 0 ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::doRedraw
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def doRedraw ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::doRedraw"


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
        #assert ( self._oExe )

        #** ---------------------------------------------------------------------------------------
        #*  obtém a escala atual do desenho
        #*/
        l_iEsc = self._oExe.getEscala ()
        #assert ( l_iEsc in locDefs.xSET_EscalasValidas )

        l_iEsc -= 1

        #** ---------------------------------------------------------------------------------------
        #*  obtém a cabeceira atual em uso (0=principal/1=secundária)
        #*/
        l_iCab = self._oExe.getCabAtu ()
        #assert ( l_iCab in locDefs.xSET_CabsValidas )

        #** ---------------------------------------------------------------------------------------
        #*  cria a superfície de vídeo sintético
        #*/
        self._srfVS = pygame.Surface ( self._tWH )
        #assert ( self._srfVS )
                                        
        self._srfVS.set_colorkey ( None )

        #** ---------------------------------------------------------------------------------------
        #*  limpa a superfície a desenhar
        #*/
        self._srfVS.fill ( glbDefs.xCOR_black )

        #** ---------------------------------------------------------------------------------------
        #*  desenha range marks azimute
        #*/
        self.drawAzimute ( self._srfVS, l_iEsc, l_iCab )

        #** ---------------------------------------------------------------------------------------
        #*  cone segurança azimute
        #*/
        self.drawConeAzimute ( self._srfVS, l_iEsc, l_iCab )

        #** ---------------------------------------------------------------------------------------
        #*  desenha uma linha dividindo a área de desenho em duas partes (azimute e elevação)
        #*/
        pygame.draw.line ( self._srfVS, glbDefs.xCOR_white, ( 0,                   self._tWH [ 1 ] / 2 ),
                                                            ( self._tWH [ 0 ] - 1, self._tWH [ 1 ] / 2 ))

        #** ---------------------------------------------------------------------------------------
        #*  desenha range marks elevação
        #*/
        self.drawElevation ( self._srfVS, l_iEsc, l_iCab )

        #** ---------------------------------------------------------------------------------------
        #*  calcula vetores dos cones de segurança
        #*/
        self.drawConeElevacao ( self._srfVS, l_iEsc, l_iCab )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::drawAzimute
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawAzimute ( self, f_srf, f_iEsc, f_iCab ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::drawAzimute"


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
        for l_iRMrk in xrange ( self._oPAR._aiNumMarks [ f_iEsc ] + 1 ):

            #** -----------------------------------------------------------------------------------
            #*  é um range mark hilight ?
            #*/
            if ( 0 == (( l_iRMrk + 1 ) % self._oPAR._aiMarkHiLight [ f_iEsc ] )):

                #** -------------------------------------------------------------------------------
                #*  se for, desenha na cor xCOR_RMA_HiL
                #*/
                l_tCor = locDefs.xCOR_RMA_HiL

            #** -----------------------------------------------------------------------------------
            #*  senão, é um range mark normal
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*  desenha o range mark na cor xCOR_RMA_Nrm
                #*/
                l_tCor = locDefs.xCOR_RMA_Nrm

            #** -----------------------------------------------------------------------------------
            #*  calcula o ponto X
            #*/
            l_iX = int ( self._oPAR._MatrizAzi [ f_iEsc ][ int ( self._oPAR._fAngAzimSup ) ][ l_iRMrk ][ f_iCab ][ 0 ] )

            #** -----------------------------------------------------------------------------------
            #*  calcula o Y inícial da linha vertical
            #*/
            l_iY1Int = self._oPAR._MatrizAzi [ f_iEsc ][ int ( self._oPAR._fAngAzimSup ) ][ l_iRMrk ][ f_iCab ][ 1 ]

            #** -----------------------------------------------------------------------------------
            #*  limita o valor do ponto inicial
            #*/
            if ( l_iY1Int < (( self._tWH [ 1 ] / 2 ) + 1 )):

                l_iY1 = ( self._tWH [ 1 ] / 2 ) + 1

            else:

                l_iY1 = int ( l_iY1Int )

            #** -----------------------------------------------------------------------------------
            #*  calcula o Y final da linha vertical
            #*/
            l_iY2Int = self._oPAR._MatrizAzi [ f_iEsc ][ int ( self._oPAR._fAngAzimInf ) ][ l_iRMrk ][ f_iCab ][ 1 ]

            #** ----------------------------------------------------------------------------------
            #*  limita o valor do ponto final
            #*/
            if ( l_iY2Int > ( self._tWH [ 1 ] - 1 )):

                l_iY2 = ( self._tWH [ 1 ] - 1 )

            else:

                l_iY2 = int ( l_iY2Int )

            #** -----------------------------------------------------------------------------------
            #*  desenha o range mark na cor selecionada
            #*/
            pygame.draw.line ( f_srf, l_tCor, ( l_iX, l_iY1 ), ( l_iX, l_iY2 ))

        #** ---------------------------------------------------------------------------------------
        #*  desenha o mark de cabeceira
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_RMA_Ini,
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueAzim - 40 ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueAzim + 20 ))

        #** ---------------------------------------------------------------------------------------
        #*  desenha a baliza de cabeceira
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_BAL,
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueAzim - 10 ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueAzim - 12 ))

        #** ---------------------------------------------------------------------------------------
        #*  desenha a baliza de ponto de toque
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_BPT,
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueAzim + 10 ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueAzim + 12 ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::drawConeAzimute
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawConeAzimute ( self, f_srf, f_iEsc, f_iCab ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::drawConeAzimute"


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
        #*  calcula vetores dos cones de segurança
        #*/
        l_iDltX = self._oPAR._aiPixStepMark [ f_iEsc ] * self._oPAR._aiNumMarks [ f_iEsc ]

        #** ---------------------------------------------------------------------------------------
        #*  cabeceira principal (0=principal/1=secundária) ?
        #*/
        if ( 0 == f_iCab ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_iX = self._oPAR._iXPonToque [ 0 ] - l_iDltX

        #** ---------------------------------------------------------------------------------------
        #*  senão, cabeceira secundária
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            l_iX = self._oPAR._iXPonToque [ 1 ] + l_iDltX

        #** ---------------------------------------------------------------------------------------
        #*  calcula vetores dos cones de segurança
        #*/
        l_iDltX = self._oPAR._aiPixStepMark [ f_iEsc ] * self._oPAR._aiNumMarks [ f_iEsc ]

        #** ---------------------------------------------------------------------------------------
        #*  cone segurança azimute
        #*/
        l_iDltY = int ( round ( l_iDltX * math.tan ( math.radians ( 1.5 ))))

        #** ---------------------------------------------------------------------------------------
        #*  desenha linha superior do cone segurança azimute
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_CSA_Sup,
                           ( l_iX,                              self._oPAR._iYPonToqueAzim - l_iDltY ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueAzim ))

        #** ---------------------------------------------------------------------------------------
        #*  desenha linha inferior do cone segurança azimute
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_CSA_Inf,
                           ( l_iX,                              self._oPAR._iYPonToqueAzim + l_iDltY ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueAzim ))

        #** ---------------------------------------------------------------------------------------
        #*  cabeceira principal (0=principal/1=secundária) ?
        #*/
        if ( 0 == f_iCab ):

            #** -----------------------------------------------------------------------------------
            #*  desenha linha central do cone segurança azimute
            #*/
            pygame.draw.line ( f_srf, locDefs.xCOR_CSA_Mid,
                               ( l_iX,                         self._oPAR._iYPonToqueAzim ),
                               ( self._oPAR._iXPonToque [ 0 ], self._oPAR._iYPonToqueAzim ))

        #** ---------------------------------------------------------------------------------------
        #*  senão, cabeceira secundária
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*  desenha linha central do cone segurança azimute
            #*/
            pygame.draw.line ( f_srf, locDefs.xCOR_CSA_Mid,
                               ( self._oPAR._iXPonToque [ 1 ], self._oPAR._iYPonToqueAzim ),
                               ( l_iX,                         self._oPAR._iYPonToqueAzim ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::drawElevation
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawElevation ( self, f_srf, f_iEsc, f_iCab ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::drawElevation"


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
        #*  desenha os range marks elevação
        #*/
        for l_iRMrk in xrange ( self._oPAR._aiNumMarks [ f_iEsc ] + 1 ):

            #** -----------------------------------------------------------------------------------
            #*  é um range mark hilight ?
            #*/
            if ( 0 == (( l_iRMrk + 1 ) % self._oPAR._aiMarkHiLight [ f_iEsc ] )):

                #** -------------------------------------------------------------------------------
                #*  se for, desenha na cor xCOR_RME_HiL
                #*/
                l_tCor = locDefs.xCOR_RME_HiL

            #** -----------------------------------------------------------------------------------
            #*  senão, é um range mark normal
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*  desenha o range mark na cor xCOR_RME_Nrm
                #*/
                l_tCor = locDefs.xCOR_RME_Nrm

            #** -----------------------------------------------------------------------------------
            #*  calcula o ponto X
            #*/
            l_iX = int ( self._oPAR._MatrizEle [ f_iEsc ][ int ( self._oPAR._fAngElevSup ) ][ l_iRMrk ][ f_iCab ][ 0 ] )

            #** -----------------------------------------------------------------------------------
            #*  calcula o Y inícial da linha vertical
            #*/
            l_iY1Int = self._oPAR._MatrizEle [ f_iEsc ][ int ( self._oPAR._fAngElevSup ) ][ l_iRMrk ][ f_iCab ][ 1 ]

            #** -----------------------------------------------------------------------------------
            #*  limita o valor do ponto inicial
            #*/
            if ( l_iY1Int < 0 ):

                l_iY1 = 0

            else:

                l_iY1 = int ( l_iY1Int )

            #** -----------------------------------------------------------------------------------
            #*  calcula o Y final da linha vertical
            #*/
            l_iY2Int = self._oPAR._MatrizEle [ f_iEsc ][ int ( self._oPAR._fAngElevInf ) ][ l_iRMrk ][ f_iCab ][ 1 ]

            #** -----------------------------------------------------------------------------------
            #*  limita o valor do ponto final
            #*/
            if ( l_iY2Int > (( self._tWH [ 1 ] / 2 ) - 1 )):

                l_iY2 = (( self._tWH [ 1 ] / 2 ) - 1 )

            else:

                l_iY2 = int ( l_iY2Int )

            #** -----------------------------------------------------------------------------------
            #*  desenha o range mark na cor selecionada
            #*/
            pygame.draw.line ( f_srf, l_tCor, ( l_iX, l_iY1 ), ( l_iX, l_iY2 ))

        #** ---------------------------------------------------------------------------------------
        #*  desenha marks de cabeceira na elevação
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_RME_Ini,
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueElev - 40 ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueElev ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::drawConeElevacao
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def drawConeElevacao ( self, f_srf, f_iEsc, f_iCab ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::drawConeElevacao"


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
        #*  calcula tangentes
        #*/
        l_fTan1 = math.tan ( math.radians ( self._oPAR._fAngRampaDisplay + 1.5 ))
        l_fTan2 = math.tan ( math.radians ( self._oPAR._fAngRampaDisplay ))
        l_fTan3 = math.tan ( math.radians ( self._oPAR._fAngRampaDisplay - 1.5 ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula vetores dos cones de segurança
        #*/
        l_iDltX = self._oPAR._aiPixStepMark [ f_iEsc ] * self._oPAR._aiNumMarks [ f_iEsc ]

        #** ---------------------------------------------------------------------------------------
        #*  cabeceira principal (0=principal/1=secundária) ?
        #*/
        if ( 0 == f_iCab ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_iX = self._oPAR._iXPonToque [ 0 ] - l_iDltX

            #** -----------------------------------------------------------------------------------
            #*  desenha o vetor linha do solo
            #*/
            pygame.draw.line ( f_srf, locDefs.xCOR_VLS,
                               ( l_iX,                         self._oPAR._iYPonToqueElev ),
                               ( self._oPAR._iXPonToque [ 0 ], self._oPAR._iYPonToqueElev ))

        #** ---------------------------------------------------------------------------------------
        #*  senão, cabeceira secundária
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            l_iX = self._oPAR._iXPonToque [ 1 ] + l_iDltX

            #** -----------------------------------------------------------------------------------
            #*  desenha o vetor linha do solo
            #*/
            pygame.draw.line ( f_srf, locDefs.xCOR_VLS,
                               ( self._oPAR._iXPonToque [ 1 ], self._oPAR._iYPonToqueElev ),
                               ( l_iX,                         self._oPAR._iYPonToqueElev ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula o vetor cone segurança elevação superior
        #*/
        l_iDltY = int ( round ( l_iDltX * l_fTan1 ))

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( l_iDltY > self._oPAR._iYPonToqueElev ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_iY = 0

            #** -----------------------------------------------------------------------------------
            #*  cabeceira principal (0=principal/1=secundária) ?
            #*/
            if ( 0 == f_iCab ):

                #** -------------------------------------------------------------------------------
                #*/
                l_iX += int ( l_fTan1 / float ( l_iDltY - self._oPAR._iYPonToqueElev ))

            #** -----------------------------------------------------------------------------------
            #*  senão, cabeceira secundária
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*/
                l_iX -= int ( l_fTan1 / float ( l_iDltY - self._oPAR._iYPonToqueElev ))

        #** ---------------------------------------------------------------------------------------
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            l_iY = self._oPAR._iYPonToqueElev - l_iDltY

        #** ---------------------------------------------------------------------------------------
        #*  desenha o vetor cone segurança elevação superior
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_CSE_Sup,
                           ( l_iX,                              l_iY ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueElev ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula o vetor rampa
        #*/
        l_iDltY = int ( round ( l_iDltX * l_fTan2 ))

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( l_iDltY > self._oPAR._iYPonToqueElev ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_iY = 0

            #** -----------------------------------------------------------------------------------
            #*  cabeceira principal (0=principal/1=secundária) ?
            #*/
            if ( 0 == f_iCab ):

                #** -------------------------------------------------------------------------------
                #*/
                l_iX += int ( l_fTan2 / float ( l_iDltY - self._oPAR._iYPonToqueElev ))

            #** -----------------------------------------------------------------------------------
            #*  senão, cabeceira secundária
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*/
                l_iX -= int ( l_fTan2 / float ( l_iDltY - self._oPAR._iYPonToqueElev ))

        #** ---------------------------------------------------------------------------------------
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            l_iY = self._oPAR._iYPonToqueElev - l_iDltY

        #** ---------------------------------------------------------------------------------------
        #*  desenha o vetor rampa do cone segurança elevação
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_CSE_Mid,
                           ( l_iX,                              l_iY ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueElev ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula o vetor cone seguranca elevação inferior
        #*/
        l_iDltY = int ( round ( l_iDltX * l_fTan3 ))

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( l_iDltY > self._oPAR._iYPonToqueElev ):

            #** -----------------------------------------------------------------------------------
            #*/
            l_iY = 0

            #** -----------------------------------------------------------------------------------
            #*  cabeceira principal (0=principal/1=secundária) ?
            #*/
            if ( 0 == f_iCab ):

                #** -------------------------------------------------------------------------------
                #*/
                l_iX += int ( l_fTan3 / float ( l_iDltY - self._oPAR._iYPonToqueElev ))

            #** -----------------------------------------------------------------------------------
            #*  senão, cabeceira secundária
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*/
                l_iX -= int ( l_fTan3 / float ( l_iDltY - self._oPAR._iYPonToqueElev ))

        #** ---------------------------------------------------------------------------------------
        #*/
        else:

            l_iY = self._oPAR._iYPonToqueElev - l_iDltY

        #** ---------------------------------------------------------------------------------------
        #*  desenha o vetor cone seguranca elevação inferior
        #*/
        pygame.draw.line ( f_srf, locDefs.xCOR_CSE_Inf,
                           ( l_iX,                              l_iY ),
                           ( self._oPAR._iXPonToque [ f_iCab ], self._oPAR._iYPonToqueElev ))


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  viewVideoSintetico::plotarPontos
    #*  -------------------------------------------------------------------------------------------
    #*  plota f_iN pontos na vertical a partir da coordenada (f_iX, f_iY) na direção vertical e
    #*  sentido para baixo na cor dada por Cor.
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def plotarPontos ( self, f_srf, f_iN, f_iX, f_iY, f_tCor ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "viewVideoSintetico::plotarPontos"


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
            f_srf.set_at (( f_iX, f_iY + l_iY ), f_tCor )

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
logger = logging.getLogger ( "viewVideoSintetico" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
