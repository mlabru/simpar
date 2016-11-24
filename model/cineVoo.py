#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: cineVoo
#*
#*  Descrição: this file is the flight class of the SiPAR. The flight class holds information about
#*             a flight and holds the commands the flight has been given.
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
import math

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.cineCalc as cineCalc
import model.cineClss as cineClss

import model.glbDefs as glbDefs

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#/ ângulo máximo da asa
#/ ------------------------------------------------------------------------------------------------
w_fAngAsaMax = 60.0

#/ ângulo máximo de arfagem
#/ ------------------------------------------------------------------------------------------------
w_fAngArfMax = 60.0

#** -----------------------------------------------------------------------------------------------
#*  cineVoo::cineVoo
#*  -----------------------------------------------------------------------------------------------
#*  the object holding all information concerning a flight
#*  -----------------------------------------------------------------------------------------------
#*/
class cineVoo ( cineClss.cineClss ):

    #** -------------------------------------------------------------------------------------------
    #*  cineVoo::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  inicia parâmetros de vôo
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_cm   - DOCUMENT ME!
    #*  @param  f_oAtv - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_cm, f_oAtv ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "cineVoo::__init__"


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
        #assert ( f_oAtv )

        #** ---------------------------------------------------------------------------------------
        #*  inicia a super classe
        #*/
        cineClss.cineClss.__init__ ( self, f_cm, f_oAtv )

        #** ---------------------------------------------------------------------------------------
        #*  salva o control manager
        #*/
        self._cm = f_cm

        #** ---------------------------------------------------------------------------------------
        #*  calcula a velocidade do vento em m/s
        #*/
        self._fVentoVel = self._oExe.getVentoVel () * glbDefs.xCNV_Knots2Ms
        #l_log.info ( "self._fVentoVel (kts): " + str ( self._oExe.getVentoVel () ))
        #l_log.info ( "self._fVentoVel (m/s): " + str ( self._fVentoVel ))

        #** ---------------------------------------------------------------------------------------
        #*  inverte a direção do vento (calcula a proa do vento !)
        #*/
        l_fVentoProa = float ( int ( self._oExe.getVentoDir () + 180 ) % 360 )
        #l_log.info ( "l_fVentoProa (A): " + str ( l_fVentoProa ))

        #** ---------------------------------------------------------------------------------------
        #*  converte a proa em direção
        #*/
        l_fVentoDir = cineCalc.convProa2Direcao (( l_fVentoProa, self._oAtv._iDecl ))
        #l_log.info ( "l_fVentoDir (D): " + str ( l_fVentoDir ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a componente do vento em X
        #*/
        self._fVentoX = self._fVentoVel * math.cos ( math.radians ( l_fVentoDir ))
        #l_log.info ( "self._fVentoX: " + str ( self._fVentoX ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a componente do vento em Y
        #*/
        self._fVentoY = self._fVentoVel * math.sin ( math.radians ( l_fVentoDir ))
        #l_log.info ( "self._fVentoY: " + str ( self._fVentoY ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a razão de descida máxima em m/s
        #*/
        self._fRazMaxDesc = self._oAtv.getAnvRazaoMaxDescida () * glbDefs.xCNV_ftMin2Ms
        #l_log.info ( "self._fRazMaxDesc (ft/m): " + str ( self._oAtv.getAnvRazaoMaxDescida ()))
        #l_log.info ( "self._fRazMaxDesc (m/s):  " + str ( self._fRazMaxDesc ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a razão de descida máxima em m/s
        #*/
        self._fRazMaxSub = self._oAtv.getAnvRazaoMaxSubida () * glbDefs.xCNV_ftMin2Ms
        #l_log.info ( "self._fRazMaxSub (ft/m): " + str ( self._oAtv.getAnvRazaoMaxSubida ()))
        #l_log.info ( "self._fRazMaxSub (m/s):  " + str ( self._fRazMaxSub ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a razão de curva em graus/s
        #*/
        self._fRazMaxCurv = self._oAtv.getAnvRazaoMaxCurva ()
        #l_log.info ( "self._fRazMaxCurv (gr/s): " + str ( self._fRazMaxCurv ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula o altitude máxima em metros
        #*/
        self._fTetoMax = self._oAtv.getAnvAltitudeMaxima () * glbDefs.xCNV_ft2M
        #l_log.info ( "self._fTetoMax (ft): " + str ( self._oAtv.getAnvAltitudeMaxima ()))
        #l_log.info ( "self._fTetoMax (m): "  + str ( self._fTetoMax ))

        #** ---------------------------------------------------------------------------------------
        #*  velocidade
        #*/
        self._fVelX = 0.0
        self._fVelY = 0.0

        #** ---------------------------------------------------------------------------------------
        #*  ângulos de arfagem e asa
        #*/
        self._fAngAsaAux = 0.0
        self._fAngArfAux = 0.0

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  cineVoo::atualizaAltitude
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_lDeltaT - delta de tempo desde a última atualização
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def atualizaAltitude ( self, f_lDeltaT ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "cineVoo::atualizaAltitude"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #l_log.info ( "f_lDeltaT: " + str ( f_lDeltaT ))

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições para execução
        #*/
        #assert ( self._oAtv )
        
        if ( not self._oAtv._bActive ):

            #** -----------------------------------------------------------------------------------
            #*  m.poirot logger
            #*/
            #l_log.debug ( "<< " )

            #** -----------------------------------------------------------------------------------
            #*  cai fora...
            #*/
            return ( 0, False )

        #** ---------------------------------------------------------------------------------------
        #*  está variando a altura ?
        #*/
        if ( 0 != self._oAtv._fAngArf ):

            #** -----------------------------------------------------------------------------------
            #*  está descendo ?
            #*/
            if ( self._oAtv._fAngArf > 0 ):

                #** -------------------------------------------------------------------------------
                #*  calcula a razão de descida atual (em m/s)
                #*/
                self._oAtv._fRazaoAtu = -1.0 * self._fRazMaxDesc * ( self._fAngArfAux / w_fAngArfMax )
                #l_log.info ( "self._oAtv._fRazaoAtu (m/s) (v): " + str ( self._oAtv._fRazaoAtu ))

            #** -----------------------------------------------------------------------------------
            #*  senão, está subindo
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*  calcula a razão de subida atual (em m/s)
                #*/
                self._oAtv._fRazaoAtu = -1.0 * self._fRazMaxSub * ( self._fAngArfAux / w_fAngArfMax )
                #l_log.info ( "self._oAtv._fRazaoAtu (m/s) (^): " + str ( self._oAtv._fRazaoAtu ))

            #** -----------------------------------------------------------------------------------
            #*  calcula a nova altura ( z = zo + vt )
            #*/
            self._oAtv._fAlt += ( self._oAtv._fRazaoAtu * f_lDeltaT )
            #l_log.info ( "self._oAtv._fAlt: " + str ( self._oAtv._fAlt ))

            #** -----------------------------------------------------------------------------------
            #*  limita a altura
            #*/
            if ( self._oAtv._fAlt > self._fTetoMax ):

                self._oAtv._fAlt = self._fTetoMax

            if ( self._oAtv._fAlt <= 0.0 ):

                self._oAtv._fAlt = 0.0
                #PFlagPouso = True

            #** -----------------------------------------------------------------------------------
            #*  calcula o ângulo de ... ?
            #*/
            l_fAlfa = math.asin ( self._oAtv._fRazaoAtu / self._oAtv.getVelocidade ())
            #l_log.info ( "l_fAlfa: " + str ( l_fAlfa ))

        else:

            #** -----------------------------------------------------------------------------------
            #*/
            l_fAlfa = 0.

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  retorna o ângulo calculado
        #*/
        return ( l_fAlfa )

    #** -------------------------------------------------------------------------------------------
    #*  cineVoo::atualizaPosicao
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_lDeltaT - delta de tempo desde a última atualização
    #*  @param  f_fAlfa   - ?
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def atualizaPosicao ( self, f_lDeltaT, f_fAlfa ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "cineVoo::atualizaPosicao"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #l_log.info ( "f_lDeltaT: " + str ( f_lDeltaT ))
        #l_log.info ( "f_fAlfa..: " + str ( f_fAlfa ))

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições para execução
        #*/
        #assert ( self._oAtv )
        
        if ( not self._oAtv._bActive ):

            #** -----------------------------------------------------------------------------------
            #*  m.poirot logger
            #*/
            #l_log.debug ( "<< " )

            #** -----------------------------------------------------------------------------------
            #*  cai fora...
            #*/
            return

        #** ---------------------------------------------------------------------------------------
        #*  decompõem a velocidade em seus componentes x e y
        #*/
        l_fVx = self._fVelX * math.cos ( f_fAlfa )
        #l_log.info ( "self._fVelX....: " + str ( self._fVelX ))
        #l_log.info ( "Velocidade em X: " + str ( l_fVx ))

        l_fVy = self._fVelY * math.cos ( f_fAlfa )
        #l_log.info ( "self._fVelY....: " + str ( self._fVelY ))
        #l_log.info ( "Velocidade em Y: " + str ( l_fVy ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula os componentes x e y da posição atual ( x = xo + vt )
        #*/
        l_fAtuX = self._oAtv._tPosicao [ 0 ] + ( l_fVx * f_lDeltaT )
        l_fAtuY = self._oAtv._tPosicao [ 1 ] + ( l_fVy * f_lDeltaT )

        #** ---------------------------------------------------------------------------------------
        #*  salva a posição atual calculada
        #*/
        self._oAtv._tPosicao = ( l_fAtuX, l_fAtuY )
        #l_log.info ( "PosicaoAtu: " + str ( self._oAtv._tPosicao ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a distância da aeronave
        #*/
        self._oAtv._fDist = l_fAtuX
        #self._oAtv._fDist = math.sqrt (( l_fAtuX ** 2 ) + ( l_fAtuY ** 2 ))
        #l_log.info ( "self._oAtv._fDist: " + str ( self._oAtv._fDist ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula o afastamento da aeronave
        #*/
        self._oAtv._fAfast = l_fAtuY
        #l_log.info ( "self._oAtv._fAfast: " + str ( self._oAtv._fAfast ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  cineVoo::atualizaProa
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_lDeltaT - delta de tempo desde a última atualização
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def atualizaProa ( self, f_lDeltaT ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "cineVoo::atualizaProa"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #l_log.info ( "f_lDeltaT: " + str ( f_lDeltaT ))

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições para execução
        #*/
        #assert ( self._oAtv )
        
        if ( not self._oAtv._bActive ):

            #** -----------------------------------------------------------------------------------
            #*  m.poirot logger
            #*/
            #l_log.debug ( "<< " )

            #** -----------------------------------------------------------------------------------
            #*  cai fora...
            #*/
            return

        #** ---------------------------------------------------------------------------------------
        #*  obtém a proa atual
        #*/
        l_fProaAtu = self._oAtv.getProa ()
        #l_log.info ( "Proa Atual..: " + str ( l_fProaAtu ))
        #l_log.info ( "Ang da Asa..: " + str ( self._fAngAsaAux ))

        #** ---------------------------------------------------------------------------------------
        #*  está curvando ?
        #*/
        if ( 0 != self._oAtv._fAngAsa ):

            #** -----------------------------------------------------------------------------------
            #*  calcula o ângulo de rotação
            #*/
            l_fDeltaP = self._fRazMaxCurv * f_lDeltaT * ( self._fAngAsaAux / w_fAngAsaMax )
            #l_log.info ( "l_fDeltaP: " + str ( l_fDeltaP ))

            #** -----------------------------------------------------------------------------------
            #*  curva a direita ?
            #*/
            if ( self._oAtv._fAngAsa > 0 ):

                #** -------------------------------------------------------------------------------
                #*  incrementa a proa atual do ângulo de rotação calculado
                #*/
                l_fProaAtu += l_fDeltaP

            #** -----------------------------------------------------------------------------------
            #*  senão, curva a esquerda
            #*/
            else:

                #** -------------------------------------------------------------------------------
                #*  decrementa a proa atual do ângulo de rotação calculado
                #*/
                l_fProaAtu -= l_fDeltaP

            #** -----------------------------------------------------------------------------------
            #*  salva a proa atual
            #*/
            self._oAtv._fProa = l_fProaAtu
            #l_log.info ( "self._oAtv._fProa: " + str ( self._oAtv._fProa ))

            #** -----------------------------------------------------------------------------------
            #*  limita ângulo de proa
            #*/
            if ( self._oAtv._fProa < 0.0 ):

                self._oAtv._fProa += 360.0

            if ( self._oAtv._fProa > 360.0 ):

                self._oAtv._fProa -= 360.0

            #** -----------------------------------------------------------------------------------
            #*  converte a proa atual em direção
            #*/
            self._oAtv._fDirAtu = cineCalc.convProa2Direcao (( l_fProaAtu, self._oAtv._iDecl ))
            #l_log.info ( "self._oAtv._fDirAtu: " + str ( self._oAtv._fDirAtu ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  cineVoo::atualizaVelocidade
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def atualizaVelocidade ( self ):

        #/ nome do método (logger)
        #/ -----------------------------------------------------------------------------------------
        #l_szMetodo = "cineVoo::atualizaVelocidade"


        #** ----------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições para execução
        #*/
        #assert ( self._oAtv )
        
        if ( not self._oAtv._bActive ):

            #** -----------------------------------------------------------------------------------
            #*  m.poirot logger
            #*/
            #l_log.debug ( "<< " )

            #** -----------------------------------------------------------------------------------
            #*  cai fora...
            #*/
            return

        #** ---------------------------------------------------------------------------------------
        #*  converte a direção atual da aeronave para radianos
        #*/
        l_fDirAtu = math.radians ( self._oAtv._fDirAtu )
        #l_log.info ( "l_fDirAtu (g)..: " + str ( self._oAtv._fDirAtu ))
        #l_log.info ( "l_fDirAtu (rad): " + str ( l_fDirAtu ))

        #** ---------------------------------------------------------------------------------------
        #*  calculo da componente da velocidade projetada no plano XY (cos (ang_arf))
        #*/
        l_fVelXY = self._oAtv.getVelocidade () * math.cos ( math.radians ( self._oAtv._fAngArf ))
        #l_log.info ( "l_fVelXY: " + str ( l_fVelXY ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a componente em X da velocidade (distância)
        #*/
        self._fVelX = l_fVelXY * math.cos ( l_fDirAtu )
        #l_log.info ( "self._fVelX: " + str ( self._fVelX ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a componente em Y da velocidade (afastamento)
        #*/
        self._fVelY = l_fVelXY * math.sin ( l_fDirAtu )
        #l_log.info ( "self._fVelY: " + str ( self._fVelY ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a componente do vento na velocidade
        #*/
        self._fVelX += self._fVentoX
        #l_log.info ( "self._fVentoX: " + str ( self._fVentoX ))
        #l_log.info ( "self._fVelX..: " + str ( self._fVelX ))

        self._fVelY += self._fVentoY
        #l_log.info ( "self._fVentoY: " + str ( self._fVentoY ))
        #l_log.info ( "self._fVelY..: " + str ( self._fVelY ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  cineVoo::calculaAnguloArfagem
    #*  -------------------------------------------------------------------------------------------
    #*  calcula os ângulos da asa e de arfagem da aeronave
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def calculaAnguloArfagem ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "cineVoo::calculaAnguloArfagem"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._cm )
        #assert ( self._oAtv )

        #** ---------------------------------------------------------------------------------------
        #*  obtem a posição do manche da aeronave
        #*/
        l_iJoxY = self._cm.getJoyY ()
        #l_log.info ( "l_iJoxY: " + str ( l_iJoxY ))

        #** ---------------------------------------------------------------------------------------
        #*  manche à trás (sobe)
        #*/
        if (( l_iJoxY > 0 ) and (( self._oAtv._fAngArf <= 60.0 ) or ( self._oAtv._fAngArf > 300.0 ))):

            #** -----------------------------------------------------------------------------------
            #*  diminui o ângulo de arfagem
            #*/
            self._oAtv._fAngArf -= 0.5
            #l_log.info ( "self._oAtv._fAngArf (sobe): " + str ( self._oAtv._fAngArf ))

        #** ---------------------------------------------------------------------------------------
        #*  manche à frente (desce)
        #*/
        elif (( l_iJoxY < 0 ) and (( self._oAtv._fAngArf < 60.0 ) or ( self._oAtv._fAngArf >= 300.0 ))):

            #** -----------------------------------------------------------------------------------
            #*  aumenta o ângulo de arfagem
            #*/
            self._oAtv._fAngArf += 0.5
            #l_log.info ( "self._oAtv._fAngArf (desce): " + str ( self._oAtv._fAngArf ))

        #** ---------------------------------------------------------------------------------------
        #*  limita ângulo de arfagem
        #*/
        if ( self._oAtv._fAngArf < 0.0 ):

            self._oAtv._fAngArf += 360.0

        if ( self._oAtv._fAngArf > 360.0 ):

            self._oAtv._fAngArf -= 360.0

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( self._oAtv._fAngArf >= 300.0 ):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngArfAux = self._oAtv._fAngArf - 360.0

        #** ---------------------------------------------------------------------------------------
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngArfAux = self._oAtv._fAngArf

        #l_log.info ( "self._fAngArfAux: " + str ( self._fAngArfAux ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  cineVoo::calculaAnguloAsa
    #*  -------------------------------------------------------------------------------------------
    #*  calcula os ângulos da asa e de arfagem da aeronave
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def calculaAnguloAsa ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "cineVoo::calculaAnguloAsa"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._cm )
        #assert ( self._oAtv )

        #** ---------------------------------------------------------------------------------------
        #*  obtem a posição do manche da aeronave
        #*/
        l_iJoxX = self._cm.getJoyX ()
        #l_log.info ( "l_iJoxX: " + str ( l_iJoxX ))

        #** ---------------------------------------------------------------------------------------
        #*  manche à direita (curva à direita)
        #*/
        if (( l_iJoxX > 0 ) and (( self._oAtv._fAngAsa < 60.0 ) or ( self._oAtv._fAngAsa >= 300.0 ))):

            #** -----------------------------------------------------------------------------------
            #*  aumenta o ângulo da asa
            #*/
            self._oAtv._fAngAsa += 1.0
            #l_log.info ( "self._oAtv._fAngAsa (direita): " + str ( self._oAtv._fAngAsa ))

        #** ---------------------------------------------------------------------------------------
        #*  manche à esquerda (curva à esquerda)
        #*/
        elif (( l_iJoxX < 0 ) and (( self._oAtv._fAngAsa <= 60.0 ) or ( self._oAtv._fAngAsa > 300.0 ))):

            #** -----------------------------------------------------------------------------------
            #*  diminui o ângulo da asa
            #*/
            self._oAtv._fAngAsa -= 1.0
            #l_log.info ( "self._oAtv._fAngAsa (esquerda): " + str ( self._oAtv._fAngAsa ))

        #** ---------------------------------------------------------------------------------------
        #*  limita ângulo da asa
        #*/
        if ( self._oAtv._fAngAsa < 0.0 ):

            self._oAtv._fAngAsa += 360.0

        if ( self._oAtv._fAngAsa > 360.0 ):

            self._oAtv._fAngAsa -= 360.0

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( self._oAtv._fAngAsa >= 300.0 ):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAsaAux = self._oAtv._fAngAsa - 360.0

        #** ---------------------------------------------------------------------------------------
        #*/
        else:

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAsaAux = self._oAtv._fAngAsa

        #l_log.info ( "self._fAngAsaAux: " + str ( self._fAngAsaAux ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  cineVoo::procVooNormal
    #*  -------------------------------------------------------------------------------------------
    #*  calcula a posição da aeronave
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def procVooNormal ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "cineVoo::procVooNormal"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições para execução
        #*/
        #assert ( self._st )
        #assert ( self._oAtv )

        if ( not self._oAtv._bActive ):

            #** -----------------------------------------------------------------------------------
            #*  m.poirot logger
            #*/
            #l_log.debug ( "<< " )

            #** -----------------------------------------------------------------------------------
            #*  cai fora...
            #*/
            return ( False )

        #** ---------------------------------------------------------------------------------------
        #*  obtem a hora atual (seg)
        #*/
        l_lTempoAtu = self._st.obtemHoraSim ()
        #l_log.info ( "l_lTempoAtu: %d" % ( l_lTempoAtu ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a variação de tempo desde a última atualização (seg)
        #*/
        l_lDeltaT = l_lTempoAtu - self._oAtv._lTempoAnt
        #l_log.info ( "l_lDeltaT: " + str ( l_lDeltaT ))

        #** ---------------------------------------------------------------------------------------
        #*  checa se passou algum tempo (1/10th)
        #*/
        if ( l_lDeltaT < .1 ):

            #** -----------------------------------------------------------------------------------
            #*  m.poirot logger
            #*/
            #l_log.debug ( "<< " )

            #** -----------------------------------------------------------------------------------
            #*  cai fora...
            #*/
            return ( False )

        #** ---------------------------------------------------------------------------------------
        #*  calcula o ângulo de arfagem
        #*/
        self.calculaAnguloArfagem ()

        #** ---------------------------------------------------------------------------------------
        #*  calcula o ângulo da asa
        #*/
        self.calculaAnguloAsa ()

        #** ---------------------------------------------------------------------------------------
        #*  calcula a proa da aeronave
        #*/
        self.atualizaProa ( l_lDeltaT )

        #** ---------------------------------------------------------------------------------------
        #*  calcula a nova velocidade e a velocidade média do percurso
        #*/
        self.atualizaVelocidade ()

        #** ---------------------------------------------------------------------------------------
        #*  calcula a nova altura e a variação de altura
        #*/
        l_fAlfa = self.atualizaAltitude ( l_lDeltaT )

        #** ---------------------------------------------------------------------------------------
        #*  calcula a nova posição da aeronave
        #*/
        self.atualizaPosicao ( l_lDeltaT, l_fAlfa )

        #** ---------------------------------------------------------------------------------------
        #*  salva a hora atual
        #*/
        self._oAtv._lTempoAnt = l_lTempoAtu

        #** ---------------------------------------------------------------------------------------
        #*  envia os dados para o controle
        #*/
        self.sendData ()

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( True )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "cineVoo" )

#** -----------------------------------------------------------------------------------------------
#*/
logger.setLevel ( w_logLvl )

#** ----------------------------------------------------------------------------------------------- *#
