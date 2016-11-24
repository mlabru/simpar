#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: clsPAR
#*
#*  Descrição: mantém os detalhes de um radar PAR
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

from __future__ import division

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
import model.glbDefs as glbDefs
import model.locDefs as locDefs

#** -----------------------------------------------------------------------------------------------
#*  defines
#*  -----------------------------------------------------------------------------------------------
#*/

#/ posição da antena
#/ ------------------------------------------------------------------------------------------------
#w_iXPosAntena1 =  20
#w_iXPosAntena0 = 620

#/ ponto de toque
#/ ------------------------------------------------------------------------------------------------
w_iXPonToque1    =  40
w_iXPonToque0    = 560
w_iYPonToqueElev = 220
w_iYPonToqueAzim = 360

#/ ângulos de elevação
#/ ------------------------------------------------------------------------------------------------
w_fAngExpElevSup =   9.0
w_fAngExpElevInf =  -1.0

#/ ângulos de azimute
#/ ------------------------------------------------------------------------------------------------
w_fAngExpAzimSup =   7.0
w_fAngExpAzimInf = -13.0

#/ fator de amplitude
#/ ------------------------------------------------------------------------------------------------
w_fFatorAmpAngAzim  = 2.00  # era 2.0
w_fFatorAmpAngElev  = 3.00  # era 3.0
w_fFatorAmpAngRampa = 4.50  # era 4.5

#/ marcadores
#/ ------------------------------------------------------------------------------------------------
w_aiMarkHiLight = [  5,  4,  2 ]
w_aiNumMarks    = [ 14, 14,  7 ]
w_aiPixStepMark = [ 36, 36, 72 ]

#/ alcance
#/ ------------------------------------------------------------------------------------------------
w_afRangeMax    = [ 14.0, 7.0, 3.5 ]

#/ fator de escala
#/ ------------------------------------------------------------------------------------------------
#w_afFatorEscX     = [ 0.0194384437, 0.0388768874, 0.0777537748 ]
#w_afFatorEscYAzim = [ 0.0394719690, 0.0789439380, 0.1578878760 ]
#w_afFatorEscYElev = [ 0.0890470371, 0.1780940740, 0.3561881480 ]

#** -----------------------------------------------------------------------------------------------
#*  variaveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  clsPAR::clsPAR
#*  -----------------------------------------------------------------------------------------------
#*  mantém os detalhes de um radar PAR
#*  -----------------------------------------------------------------------------------------------
#*/
class clsPAR:

    #** -------------------------------------------------------------------------------------------
    #*  variáveis de classe
    #*/

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  inicia as variáveis de instância de um objeto radar PAR
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_lstData - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self, f_lstData=None ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  número da cabeceira principal
        #*/
        self._iCab0 = 0

        #** ---------------------------------------------------------------------------------------
        #*  pontos de toque (primário e secundário)
        #*/
        self._iXPonToque = [ 0 for _ in xrange ( 2 ) ]

        self._iYPonToqueElev = 0
        self._iYPonToqueAzim = 0

        #** ---------------------------------------------------------------------------------------
        #*  ângulos de elevação
        #*/
        self._fAngExpElevSup = 0.
        self._fAngExpElevInf = 0.

        #** ---------------------------------------------------------------------------------------
        #*  ângulos de azimute
        #*/
        self._fAngExpAzimSup = 0.
        self._fAngExpAzimInf = 0.

        #** ---------------------------------------------------------------------------------------
        #*  fator de amplitude dos ângulos
        #*/
        self._fFatorAmpAngAzim  = 0.
        self._fFatorAmpAngElev  = 0.
        self._fFatorAmpAngRampa = 0.

        #** ---------------------------------------------------------------------------------------
        #*  ângulos de elevação
        #*/
        self._fAngElevSup = 0.
        self._fAngElevInf = 0.

        #** ---------------------------------------------------------------------------------------
        #*  ângulos de azimute
        #*/
        self._fAngAzimSup = 0.
        self._fAngAzimInf = 0.

        #** ---------------------------------------------------------------------------------------
        #*  ângulos de rampa
        #*/
        self._fAngRampa = 0.
        self._fAngRampaDisplay = 0.

        #** ---------------------------------------------------------------------------------------
        #*  dados da antena
        #*/
        self._aiXAntena     = [[ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ] for _ in xrange ( locDefs.xMAX_Pistas ) ]
        self._aiYAntenaElev = [[ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ] for _ in xrange ( locDefs.xMAX_Pistas ) ]
        self._aiYAntenaAzim = [[ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ] for _ in xrange ( locDefs.xMAX_Pistas ) ]

        #** ---------------------------------------------------------------------------------------
        #*  retardo da antena
        #*/
        self._aiRetardo = [ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ]

        #** ---------------------------------------------------------------------------------------
        #*  distância da antena
        #*/
        self._aiDistAntPT0T = [[ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ] for _ in xrange ( locDefs.xMAX_Pistas ) ]
        self._aiDistAntPT1T = [[ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ] for _ in xrange ( locDefs.xMAX_Pistas ) ]

        #** ---------------------------------------------------------------------------------------
        #*  marcadores
        #*/
        self._aiNumMarks    = [ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ]
        self._aiMarkHiLight = [ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ]
        self._aiPixStepMark = [ 0 for _ in xrange ( locDefs.xMAX_Escalas ) ]

        #** ---------------------------------------------------------------------------------------
        #*  fator de escala
        #*/
        self._afFatorEscX     = [ 0. for _ in xrange ( locDefs.xMAX_Escalas ) ]
        self._afFatorEscYElev = [ 0. for _ in xrange ( locDefs.xMAX_Escalas ) ]
        self._afFatorEscYAzim = [ 0. for _ in xrange ( locDefs.xMAX_Escalas ) ]

        #** ---------------------------------------------------------------------------------------
        #*  cria as matrizes
        #*/
        self._MatrizAzi = [[[[ ( 0, 0 ) for _ in xrange ( locDefs.xMAX_Cabeceiras ) ] \
                                        for _ in xrange ( locDefs.xMAX_RMarks + 1 ) ] \
                                        for _ in xrange ( locDefs.xMAX_AngAziMin, locDefs.xMAX_AngAziMax ) ] \
                                        for _ in xrange ( locDefs.xMAX_Escalas ) ]

        self._MatrizEle = [[[[ ( 0, 0 ) for _ in xrange ( locDefs.xMAX_Cabeceiras ) ] \
                                        for _ in xrange ( locDefs.xMAX_RMarks + 1 ) ] \
                                        for _ in xrange ( locDefs.xMAX_AngEleMin, locDefs.xMAX_AngEleMax ) ] \
                                        for _ in xrange ( locDefs.xMAX_Escalas ) ]

        #** ---------------------------------------------------------------------------------------
        #*  dados de configuração do PAR
        #*/
        self._szKey = None
        self._szDescr = None

        self._fHAnt1 = None
        self._fHAnt0 = None

        self._fDstAntPT0 = None
        self._fDstAntPT1 = None
        self._fDstAntEixo = None

        self._iDecl = None

        #** ---------------------------------------------------------------------------------------
        #*  checa se recebeu uma lista de dados
        #*/
        if ( f_lstData is not None ):
                                
            #** -----------------------------------------------------------------------------------
            #*  cria um radar PAR
            #*/
            self.makePAR ( f_lstData )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._fAngStep = 0.5

        #** ---------------------------------------------------------------------------------------
        #*  alidades
        #*/
        self._fAngAlidAzim = self._fAngRampa
        #l_log.info ( "_fAngAlidAzim: " + str ( self._fAngAlidAzim ))
                                
        self._fAngAlidElev = 0.0
        #l_log.info ( "_fAngAlidElev: " + str ( self._fAngAlidElev ))
                                                    
        #** ---------------------------------------------------------------------------------------
        #*/
        self._fAngAlidAzimDisplay = self._fAngAlidAzim * self._fFatorAmpAngRampa
        #l_log.info ( "_fAngAlidAzimDisplay: " + str ( self._fAngAlidAzimDisplay ))
                                
        self._fAngAlidElevDisplay = self._fAngAlidElev * self._fFatorAmpAngAzim
        #l_log.info ( "_fAngAlidElevDisplay: " + str ( self._fAngAlidElevDisplay ))
                                                        
        #** ---------------------------------------------------------------------------------------
        #*/
        self._fAngAzimStepDisplay = self._fAngStep * self._fFatorAmpAngAzim
        #l_log.info ( "_fAngAzimStepDisplay: " + str ( self._fAngAzimStepDisplay ))
                                                                                        
        self._fAngElevStepDisplay = self._fAngStep * self._fFatorAmpAngElev
        #l_log.info ( "_fAngElevStepDisplay: " + str ( self._fAngElevStepDisplay ))
                                                                                                                
        #** ---------------------------------------------------------------------------------------
        #*  linhas de referência para as escalas
        #*/
        self._iHRefLine = 1900

        self._aiMaxHRefLine = [ 8000, 4000, 2000 ]

        #** ---------------------------------------------------------------------------------------
        #*  flag mudança nas alidades
        #*/
        self._bMudouAlidades = False

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::calculaFatorEscala
    #*  -------------------------------------------------------------------------------------------
    #*  calcula os fatores de multiplicação para transformar coordenadas do mundo real em
    #*  coordenadas de tela
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def calculaFatorEscala ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::calculaFatorEscala"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        l_fTan1 = math.tan ( math.radians ( w_fAngExpAzimSup ))     #  7.0
        l_fTan2 = math.tan ( math.radians ( self._fAngAzimSup ))    # 14.0

        #** ---------------------------------------------------------------------------------------
        #*/
        l_fTan3 = math.tan ( math.radians ( self._fAngRampa ))
        l_fTan4 = math.tan ( math.radians ( self._fAngRampaDisplay ))

        #** ---------------------------------------------------------------------------------------
        #*  percorre todas as escalas...
        #*/
        for l_iEsc in xrange ( locDefs.xMAX_Escalas ):

            #** -----------------------------------------------------------------------------------
            #*  calcula o fator de escala em X
            #*/
            self._afFatorEscX [ l_iEsc ] = ( w_aiNumMarks [ l_iEsc ] * w_aiPixStepMark [ l_iEsc ] ) / \
                                           ( w_afRangeMax [ l_iEsc ] * glbDefs.xCNV_NM2M )
            #l_log.info ( "_afFatorEscX: " + str ( self._afFatorEscX [ l_iEsc ] ))

            #** -----------------------------------------------------------------------------------
            #*  calcula o fator de escala em Y azimute
            #*/
            self._afFatorEscYAzim [ l_iEsc ] = self._afFatorEscX [ l_iEsc ] * ( l_fTan2 / l_fTan1 )
            #l_log.info ( "_afFatorEscYAzim: " + str ( self._afFatorEscYAzim [ l_iEsc ] ))

            #** -----------------------------------------------------------------------------------
            #*  calcula o fator de escala em Y elevação
            #*/
            self._afFatorEscYElev [ l_iEsc ] = self._afFatorEscX [ l_iEsc ] * ( l_fTan4 / l_fTan3 )
            #l_log.info ( "_afFatorEscYElev: " + str ( self._afFatorEscYElev [ l_iEsc ] ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::calculaPosicaoAntena
    #*  -------------------------------------------------------------------------------------------
    #*  calcula as coordenadas dos pontos de localização da antena
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def calculaPosicaoAntena ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::calculaPosicaoAntena"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  calcula os fatores de escala
        #*/
        self.calculaFatorEscala ()

        #** ---------------------------------------------------------------------------------------
        #*  dados da antena para as 3 escalas...
        #*/
        for l_iEsc in xrange ( locDefs.xMAX_Escalas ):

            #** -----------------------------------------------------------------------------------
            #*  calcula distância da antena ao ponto de toque (em pixels)
            #*/
            self._aiDistAntPT0T [ 0 ][ l_iEsc ] = int ( round ( self._fDstAntPT0 * self._afFatorEscX [ l_iEsc ] ))
            #l_log.info ( "_aiDistAntPT0T: " + str ( self._aiDistAntPT0T [ 0 ][ l_iEsc ] ))

            self._aiDistAntPT1T [ 1 ][ l_iEsc ] = int ( round ( self._fDstAntPT1 * self._afFatorEscX [ l_iEsc ] ))
            #l_log.info ( "_aiDistAntPT1T: " + str ( self._aiDistAntPT1T [ 1 ][ l_iEsc ] ))

            #** -----------------------------------------------------------------------------------
            #*  ponto X da antena
            #*/
            self._aiXAntena [ 0 ][ l_iEsc ] = w_iXPonToque0 + self._aiDistAntPT0T [ 0 ][ l_iEsc ]
            #l_log.info ( "_aiXAntena: " + str ( self._aiXAntena [ 0 ][ l_iEsc ] ))

            self._aiXAntena [ 1 ][ l_iEsc ] = w_iXPonToque1 - self._aiDistAntPT1T [ 1 ][ l_iEsc ]
            #l_log.info ( "_aiXAntena: " + str ( self._aiXAntena [ 1 ][ l_iEsc ] ))

            #** -----------------------------------------------------------------------------------
            #*  ponto Y da azimute da antena
            #*/
            self._aiYAntenaAzim [ 0 ][ l_iEsc ] = w_iYPonToqueAzim - int ( round ( self._fDstAntEixo * self._afFatorEscYAzim [ l_iEsc ] ))
            #l_log.info ( "_aiYAntenaAzim: " + str ( self._aiYAntenaAzim [ 0 ][ l_iEsc ] ))

            self._aiYAntenaAzim [ 1 ][ l_iEsc ] = w_iYPonToqueAzim - int ( round ( self._fDstAntEixo * self._afFatorEscYAzim [ l_iEsc ] ))
            #l_log.info ( "_aiYAntenaAzim: " + str ( self._aiYAntenaAzim [ 1 ][ l_iEsc ] ))

            #** -----------------------------------------------------------------------------------
            #*  ponto Y da elevação da antena
            #*/
            self._aiYAntenaElev [ 0 ][ l_iEsc ] = w_iYPonToqueElev - int ( round ( self._fHAnt0 * self._afFatorEscYElev [ l_iEsc ] ))
            #l_log.info ( "_aiYAntenaElev: " + str ( self._aiYAntenaElev [ 0 ][ l_iEsc ] ))

            self._aiYAntenaElev [ 1 ][ l_iEsc ] = w_iYPonToqueElev - int ( round ( self._fHAnt1 * self._afFatorEscYElev [ l_iEsc ] ))
            #l_log.info ( "_aiYAntenaElev: " + str ( self._aiYAntenaElev [ 1 ][ l_iEsc ] ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::decAlidAzim
    #*  -------------------------------------------------------------------------------------------
    #*  preenche os dados do radar PAR
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def decAlidAzim ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::decAlidAzim"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  decrementa o ângulo de alidade azimutal
        #*/
        self._fAngAlidAzim -= self._fAngStep

        #** ---------------------------------------------------------------------------------------
        #*  decrementa o ângulo de alidade azimutal para display
        #*/
        self._fAngAlidAzimDisplay -= self._fAngElevStepDisplay

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( self._fAngAlidAzim < ( self._fAngExpElevInf + 1.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzim = self._fAngExpElevInf + 1.5

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzimDisplay = self._fAngElevInf + 4.5
                
        #** ---------------------------------------------------------------------------------------
        #*  seta flag avisando que algo mudou nas alidades
        #*/
        self._bMudouAlidades = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::decAlidElev
    #*  -------------------------------------------------------------------------------------------
    #*  preenche os dados do radar PAR
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def decAlidElev ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::decAlidElev"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._fAngAlidElev -= self._fAngStep

        #** ---------------------------------------------------------------------------------------
        #*/
        self._fAngAlidElevDisplay -= self._fAngAzimStepDisplay

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( self._fAngAlidElev < ( self._fAngExpAzimInf + 1.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElev = self._fAngExpAzimInf + 1.5

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElevDisplay = self._fAngAzimInf + 3.0

        #** ---------------------------------------------------------------------------------------
        #*  seta flag avisando que algo mudou nas alidades
        #*/
        self._bMudouAlidades = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::incAlidAzim
    #*  -------------------------------------------------------------------------------------------
    #*  preenche os dados do radar PAR
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def incAlidAzim ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::incAlidAzim"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        self._fAngAlidAzim += self._fAngStep
        #l_log.info ( "self._fAngAlidAzim: " + str ( self._fAngAlidAzim ))

        #** ---------------------------------------------------------------------------------------
        #*/
        self._fAngAlidAzimDisplay += self._fAngElevStepDisplay
        #l_log.info ( "self._fAngAlidAzimDisplay: " + str ( self._fAngAlidAzimDisplay ))
        #l_log.info ( "Fator....................: " + str ( self._fAngAlidAzimDisplay / self._fAngAlidAzim ))

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( self._fAngAlidAzim > ( self._fAngExpElevSup - 1.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzim = self._fAngExpElevSup - 1.5

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzimDisplay = self._fAngElevSup - 4.5

        #** ---------------------------------------------------------------------------------------
        #*  seta flag avisando que algo mudou nas alidades
        #*/
        self._bMudouAlidades = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::incAlidElev
    #*  -------------------------------------------------------------------------------------------
    #*  preenche os dados do radar PAR
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def incAlidElev ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::incAlidElev"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  incrementa o ângulo de alidade elevação
        #*/
        self._fAngAlidElev += self._fAngStep
        #l_log.info ( "self._fAngAlidElev: " + str ( self._fAngAlidElev ))

        #** ---------------------------------------------------------------------------------------
        #*  decrementa o ângulo de alidade azimutal para display
        #*/
        self._fAngAlidElevDisplay += self._fAngAzimStepDisplay
        #l_log.info ( "self._fAngAlidElevDisplay: " + str ( self._fAngAlidElevDisplay ))
        #l_log.info ( "Fator....................: " + str ( self._fAngAlidElevDisplay / self._fAngAlidElev ))

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( self._fAngAlidElev > ( self._fAngExpAzimSup - 1.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElev = self._fAngExpAzimSup - 1.5

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElevDisplay = self._fAngAzimSup - 3.0

        #** ---------------------------------------------------------------------------------------
        #*  seta flag avisando que algo mudou nas alidades
        #*/
        self._bMudouAlidades = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::makePAR
    #*  -------------------------------------------------------------------------------------------
    #*  preenche os dados do radar PAR
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def makePAR ( self, f_lstData ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::makePAR"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  chave do PAR
        #*/
        self._szKey = str ( f_lstData [ 0 ] ).upper ()
        #l_log.info ( "_szKey: " + str ( self._szKey ))

        #** ---------------------------------------------------------------------------------------
        #*  descrição do PAR
        #*/
        self._szDescr = str ( f_lstData [ 1 ] ).upper ()
        #l_log.info ( "_szDescr: " + str ( self._szDescr ))

        #** ---------------------------------------------------------------------------------------
        #*  número da cabeceira principal
        #*/
        self._iCab0 = int ( f_lstData [ 2 ] )
        #l_log.info ( "_iCab0: " + str ( self._iCab0 ))

        #** ---------------------------------------------------------------------------------------
        #*  altura da antena relativo ao ponto toque principal
        #*/
        self._fHAnt0 = float ( f_lstData [ 3 ] )
        #l_log.info ( "self._fHAnt0: " + str ( self._fHAnt0 ))

        #** ---------------------------------------------------------------------------------------
        #*  altura da antena relativo ao ponto toque secundário
        #*/
        self._fHAnt1 = float ( f_lstData [ 4 ] )
        #l_log.info ( "self._fHAnt1: " + str ( self._fHAnt1 ))

        #** ---------------------------------------------------------------------------------------
        #*  afastamento da antena ao eixo da pista
        #*/
        self._fDstAntEixo = float ( f_lstData [ 5 ] )
        #l_log.info ( "self._fDstAntEixo: " + str ( self._fDstAntEixo ))

        if ( self._fDstAntEixo < 100.0 ):

            print u'Afastamento da antena eixo da pista incompatível com recomendações ICAO.'

        #** ---------------------------------------------------------------------------------------
        #*  distância da antena ao ponto toque principal
        #*/
        self._fDstAntPT0 = float ( f_lstData [ 6 ] )
        #l_log.info ( "self._fDstAntPT0: " + str ( self._fDstAntPT0 ))

        if (( self._fDstAntEixo >= 100.0 ) and ( self._fDstAntEixo <= 185.0 )):

            if ( self._fDstAntPT0 < 685.0 ):

                print u'Distância da antena ao ponto de toque incompatível com recomendações da ICAO.'

        elif ( self._fDstAntPT0 < 915.0 ):

            print u'Distância da antena ao ponto de toque incompatível com recomendações da ICAO.'

        #** ---------------------------------------------------------------------------------------
        #*  distância da antena ao ponto toque secundário
        #*/
        self._fDstAntPT1 = float ( f_lstData [ 7 ] )
        #l_log.info ( "self._fDstAntPT1: " + str ( self._fDstAntPT1 ))

        #** ---------------------------------------------------------------------------------------
        #*  ângulo da rampa de aproximação
        #*/
        self._fAngRampa = float ( f_lstData [ 8 ] )
        #l_log.info ( "self._fAngRampa: " + str ( self._fAngRampa ))

        #** ---------------------------------------------------------------------------------------
        #*  retardos para as 3 escalas
        #*/
        for l_iEsc in xrange ( locDefs.xMAX_Escalas ):

            #** -----------------------------------------------------------------------------------
            #*  retardos
            #*/
            self._aiRetardo [ l_iEsc ] = int ( f_lstData [ 9 ] )
            #l_log.info ( "_aiRetardo: " + str ( self._aiRetardo [ l_iEsc ] ))

        #** ---------------------------------------------------------------------------------------
        #*  ponto de toque
        #*/
        self._iXPonToque [ 0 ] = w_iXPonToque0
        #l_log.info ( "_iXPonToque [ 0 ]: " + str ( self._iXPonToque [ 0 ] ))

        self._iXPonToque [ 1 ] = w_iXPonToque1
        #l_log.info ( "_iXPonToque [ 1 ]: " + str ( self._iXPonToque [ 1 ] ))

        self._iYPonToqueElev = w_iYPonToqueElev
        #l_log.info ( "_iYPonToqueElev.: " + str ( self._iYPonToqueElev ))

        self._iYPonToqueAzim = w_iYPonToqueAzim
        #l_log.info ( "_iYPonToqueAzim.: " + str ( self._iYPonToqueAzim ))

        #** ---------------------------------------------------------------------------------------
        #*  ângulo Exp azimute
        #*/
        self._fAngExpAzimSup = w_fAngExpAzimSup
        #l_log.info ( "_fAngExpAzimSup.: " + str ( self._fAngExpAzimSup ))

        self._fAngExpAzimInf = w_fAngExpAzimInf
        #l_log.info ( "_fAngExpAzimInf.: " + str ( self._fAngExpAzimInf ))

        #** ---------------------------------------------------------------------------------------
        #*  ângulo Exp elevação
        #*/
        self._fAngExpElevSup = w_fAngExpElevSup
        #l_log.info ( "_fAngExpElevSup.: " + str ( self._fAngExpElevSup ))

        self._fAngExpElevInf = w_fAngExpElevInf
        #l_log.info ( "_fAngExpElevInf.: " + str ( self._fAngExpElevInf ))

        #** ---------------------------------------------------------------------------------------
        #*  fator de amplitude do ângulo
        #*/
        self._fFatorAmpAngAzim = w_fFatorAmpAngAzim
        #l_log.info ( "_fFatorAmpAngAzim.: " + str ( self._fFatorAmpAngAzim ))

        self._fFatorAmpAngElev = w_fFatorAmpAngElev
        #l_log.info ( "_fFatorAmpAngElev.: " + str ( self._fFatorAmpAngElev ))

        self._fFatorAmpAngRampa = w_fFatorAmpAngRampa
        #l_log.info ( "_fFatorAmpAngRampa.: " + str ( self._fFatorAmpAngRampa ))

        #** ---------------------------------------------------------------------------------------
        #*  ângulo de azimute
        #*/
        self._fAngAzimSup = w_fAngExpAzimSup * w_fFatorAmpAngAzim
        #l_log.info ( "_fAngAzimSup: " + str ( self._fAngAzimSup ))

        self._fAngAzimInf = w_fAngExpAzimInf * w_fFatorAmpAngAzim
        #l_log.info ( "_fAngAzimInf: " + str ( self._fAngAzimInf ))

        #** ---------------------------------------------------------------------------------------
        #*  ângulo de elevação
        #*/
        self._fAngElevSup = w_fAngExpElevSup * w_fFatorAmpAngElev
        #l_log.info ( "_fAngElevSup: " + str ( self._fAngElevSup ))

        self._fAngElevInf = w_fAngExpElevInf * w_fFatorAmpAngElev
        #l_log.info ( "_fAngElevInf: " + str ( self._fAngElevInf ))

        #** ---------------------------------------------------------------------------------------
        #*  ângulo da rampa
        #*/
        #self._fAngRampa = self._fAngRampa
        #l_log.info ( "_fAngRampa: " + str ( self._fAngRampa ))

        self._fAngRampaDisplay = self._fAngRampa * w_fFatorAmpAngRampa
        #l_log.info ( "_fAngRampaDisplay: " + str ( self._fAngRampaDisplay ))

        #** ---------------------------------------------------------------------------------------
        #*  calcula a posição da antena
        #*/
        self.calculaPosicaoAntena ()

        #** ---------------------------------------------------------------------------------------
        #*  dados da antena para as 3 escalas
        #*/
        for l_iEsc in xrange ( locDefs.xMAX_Escalas ):

            #** -----------------------------------------------------------------------------------
            #*/
            self._aiPixStepMark [ l_iEsc ] = w_aiPixStepMark [ l_iEsc ]
            #l_log.info ( "_aiPixStepMark: " + str ( self._aiPixStepMark [ l_iEsc ] ))

            #** -----------------------------------------------------------------------------------
            #*/
            self._aiNumMarks [ l_iEsc ] = w_aiNumMarks [ l_iEsc ]
            #l_log.info ( "_aiNumMarks: " + str ( self._aiNumMarks [ l_iEsc ] ))

            #** -----------------------------------------------------------------------------------
            #*/
            self._aiMarkHiLight [ l_iEsc ] = w_aiMarkHiLight [ l_iEsc ]
            #l_log.info ( "_aiMarkHiLight: " + str ( self._aiMarkHiLight [ l_iEsc ] ))

        #** ---------------------------------------------------------------------------------------
        #*  declinação magnética do PAR
        #*/
        self._iDecl = int ( f_lstData [ 10 ] )
        #l_log.info ( "_iDecl: " + str ( self._iDecl ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** ===========================================================================================
    #*  rotinas de exportação de dados do PAR
    #*  ===========================================================================================
    #*/

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getAngAlidAzim
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getAngAlidAzim ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getAngAlidAzim"


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
        return ( self._fAngAlidAzim )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getAngAlidElev
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getAngAlidElev ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getAngAlidElev"


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
        return ( self._fAngAlidElev )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getCab0
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o número da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getCab0 ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getCab0"


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
        #*  retorna o número da cabeceira principal
        #*/
        return ( self._iCab0 )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getCabeceiras
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o número da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getCabeceiras ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getCabeceiras"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  calcula a cabeceira secundária
        #*/
        l_iCab1 = ( self._iCab0 + 18 ) % 36

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  retorna os números das cabeceiras
        #*/
        return ( [ self._iCab0, l_iCab1 ] )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getDescricao
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getDescricao ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getDescricao"


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
        return ( self._szDescr )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getHRefLine
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getHRefLine ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getHRefLine"


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
        #*  retorna a altura da linha de referência
        #*/
        return ( self._iHRefLine )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getMaxAngAlidAzim
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getMaxAngAlidAzim ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getMaxAngAlidAzim"


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
        #*  retorna o ângulo máximo da alidade vertical
        #*/
        return ( self._fAngExpElevSup - 1.5 )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getMaxAngAlidElev
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getMaxAngAlidElev ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getMaxAngAlidElev"


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
        #*  retorna o ângulo máximo da alidade horizontal
        #*/
        return ( self._fAngExpAzimSup - 1.5 )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getMaxHRefLine
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getMaxHRefLine ( self, f_iEsc ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getMaxHRefLine"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert (( f_iEsc + 1 ) in locDefs.xSET_EscalasValidas )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  retorna a altura máxima da linha de referência para a escala
        #*/
        return ( self._aiMaxHRefLine [ f_iEsc ] )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getMinAngAlidAzim
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getMinAngAlidAzim ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getMinAngAlidAzim"


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
        #*  retorna o ângulo mínimo de alidade vertical
        #*/
        return ( self._fAngExpElevInf + 1.5 )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getMinAngAlidElev
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getMinAngAlidElev ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getMinAngAlidElev"


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
        #*  retorna o ângulo mínimo de alidade horizontal
        #*/
        return ( self._fAngExpAzimInf + 1.5 )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getMudouAlidades
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getMudouAlidades ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getMudouAlidades"


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
        return ( self._bMudouAlidades )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getRumoPista
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getRumoPista ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getRumoPista"


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
        #*  retorna o rumo da cabeceira principal
        #*/
        return ( self._iCab0 * 10 )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::getKey
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getKey ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::getKey"


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
        return ( self._szKey )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::setAngAlidAzim
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def setAngAlidAzim ( self, f_fVal ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::setAngAlidAzim"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza o ângulo
        #*/
        self._fAngAlidAzim = float ( f_fVal )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza o ângulo
        #*/
        self._fAngAlidAzimDisplay = self._fAngAlidAzim * self._fFatorAmpAngRampa
        #l_log.info ( "_fAngAlidAzimDisplay: " + str ( self._fAngAlidAzimDisplay ))
                                
        #** ---------------------------------------------------------------------------------------
        #*  limita o ângulo self._fAngAlidAzim
        #*/
        if ( self._fAngAlidAzim < ( self._fAngExpElevInf + 1.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzim = self._fAngExpElevInf + 1.5

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzimDisplay = self._fAngElevInf + 4.5
                
        #** ---------------------------------------------------------------------------------------
        #*  limita o ângulo self._fAngAlidAzim
        #*/
        elif ( self._fAngAlidAzim > ( self._fAngExpElevSup - 1.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzim = self._fAngExpElevSup - 1.5

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzimDisplay = self._fAngElevSup - 4.5

        #** ---------------------------------------------------------------------------------------
        #*  limita o ângulo self._fAngAlidAzimDisplay
        #*/
        if ( self._fAngAlidAzimDisplay < ( self._fAngElevInf + 4.5 )):
                
            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzimDisplay = self._fAngElevInf + 4.5
                
        #** ---------------------------------------------------------------------------------------
        #*  limita o ângulo self._fAngAlidAzimDisplay
        #*/
        elif ( self._fAngAlidAzimDisplay > ( self._fAngElevSup - 4.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidAzimDisplay = self._fAngElevSup - 4.5

        #** ---------------------------------------------------------------------------------------
        #*  seta flag avisando que algo mudou nas alidades
        #*/
        self._bMudouAlidades = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::setAngAlidElev
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def setAngAlidElev ( self, f_fVal ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::setAngAlidElev"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza o ângulo
        #*/
        self._fAngAlidElev = float ( f_fVal )

        #** ---------------------------------------------------------------------------------------
        #*  atualiza o ângulo
        #*/
        self._fAngAlidElevDisplay = self._fAngAlidElev * self._fFatorAmpAngAzim
        #l_log.info ( "_fAngAlidElevDisplay: " + str ( self._fAngAlidElevDisplay ))

        #** ---------------------------------------------------------------------------------------
        #*  limita o ângulo self._fAngAlidElev
        #*/
        if ( self._fAngAlidElev < ( self._fAngExpAzimInf + 1.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElev = self._fAngExpAzimInf + 1.5

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElevDisplay = self._fAngAzimInf + 3.0

        #** ---------------------------------------------------------------------------------------
        #*  limita o ângulo self._fAngAlidElev
        #*/
        elif ( self._fAngAlidElev > ( self._fAngExpAzimSup - 1.5 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElev = self._fAngExpAzimSup - 1.5

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElevDisplay = self._fAngAzimSup - 3.0

        #** ---------------------------------------------------------------------------------------
        #*  limita o ângulo self._fAngAlidElevDisplay
        #*/
        if ( self._fAngAlidElevDisplay < ( self._fAngAzimInf + 3.0 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElevDisplay = self._fAngAzimInf + 3.0

        #** ---------------------------------------------------------------------------------------
        #*  limita o ângulo self._fAngAlidElevDisplay
        #*/
        elif ( self._fAngAlidElevDisplay > ( self._fAngAzimSup - 3.0 )):

            #** -----------------------------------------------------------------------------------
            #*/
            self._fAngAlidElevDisplay = self._fAngAzimSup - 3.0
      
        #** ---------------------------------------------------------------------------------------
        #*  seta flag avisando que algo mudou nas alidades
        #*/
        self._bMudouAlidades = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::setHRefLine
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def setHRefLine ( self, f_iVal ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::setHRefLine"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  salva o novo valor da linha de referência
        #*/
        self._iHRefLine = int ( f_iVal )

        #** ---------------------------------------------------------------------------------------
        #*  seta flag avisando que algo mudou nas alidades
        #*/
        self._bMudouAlidades = True

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  clsPAR::setMudouAlidades
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o rumo da cabeceira principal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def setMudouAlidades ( self, f_bVal ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "clsPAR::setMudouAlidades"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*/
        if ( type ( True ) == type ( f_bVal )):
                        
            #** -----------------------------------------------------------------------------------
            #*/
            self._bMudouAlidades = f_bVal

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "clsPAR" )

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
    l_PAR = clsPAR ( [ "CO", "Canoas", 12, 13.0, 13.0, 150.0, 1000.0, 1150.0, 3.0, 4, -10 ] )
    #assert ( l_PAR )

#** ----------------------------------------------------------------------------------------------- *#
