#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2010, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: locDefs
#*
#*  Descrição: defines do sistema
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Alteração
#*  -----------------------------------------------------------------------------------------------
#*  well     1997/jun/20  versão 1.0 started
#*  mlabru   2009/set/01  versão 3.0 started
#*  -----------------------------------------------------------------------------------------------
#*  Detalhes de Versão
#*  -----------------------------------------------------------------------------------------------
#*  start    1997/jun/20  versão inicial
#*  3.01-01  2009/set/01  versão para Linux
#*  -----------------------------------------------------------------------------------------------
#*/

#** -----------------------------------------------------------------------------------------------
#*  includes
#*  -----------------------------------------------------------------------------------------------
#*/
import model.glbDefs as glbDefs

#** ===============================================================================================
#*  cores
#*  ===============================================================================================
#*/

#** -----------------------------------------------------------------------------------------------
#*  try to load pyGame (biblioteca gráfica)
#*/
try:

    #** -------------------------------------------------------------------------------------------
    #*  import Psyco if available
    #*/
    from pygame.color import THECOLORS

    #/ cores dos elementos de tela (I)
    #/ --------------------------------------------------------------------------------------------
    xCOR_Alt1      = glbDefs.xCOR_red
    xCOR_Alt2      = glbDefs.xCOR_green
    xCOR_Alt3      = glbDefs.xCOR_blue
    xCOR_Av1       = glbDefs.xCOR_red
    xCOR_Av2       = glbDefs.xCOR_green
    xCOR_Av3       = glbDefs.xCOR_blue
    xCOR_Av4       = glbDefs.xCOR_red
    xCOR_Bus1      = glbDefs.xCOR_red
    xCOR_Bus2      = glbDefs.xCOR_green
    xCOR_Climb     = glbDefs.xCOR_red
    xCOR_Horz      = glbDefs.xCOR_red
    xCOR_Joy1      = glbDefs.xCOR_red
    xCOR_Joy2      = glbDefs.xCOR_green
    xCOR_Joy3      = glbDefs.xCOR_blue
    xCOR_Veloc     = glbDefs.xCOR_red

    #/ cores dos elementos de tela (alidades eletrônicas azimute)
    #/ --------------------------------------------------------------------------------------------
    xCOR_AEA       = glbDefs.xCOR_white

    #/ cores dos elementos de tela (alidades eletrônicas elevação)
    #/ --------------------------------------------------------------------------------------------
    xCOR_AEE       = glbDefs.xCOR_white

    #/ cores dos elementos de tela (baliza de cabeceira)
    #/ --------------------------------------------------------------------------------------------
    xCOR_BAL       = glbDefs.xCOR_red

    #/ cores dos elementos de tela (baliza de ponto de toque)
    #/ --------------------------------------------------------------------------------------------
    xCOR_BPT       = glbDefs.xCOR_red

    #/ cores dos elementos de tela (cone de segurança azimute)
    #/ --------------------------------------------------------------------------------------------
    xCOR_CSA_Inf   = glbDefs.xCOR_blue
    xCOR_CSA_Mid   = glbDefs.xCOR_blue
    xCOR_CSA_Sup   = glbDefs.xCOR_blue

    #/ cores dos elementos de tela (cone de segurança elevação)
    #/ --------------------------------------------------------------------------------------------
    xCOR_CSE_Inf   = glbDefs.xCOR_blue
    xCOR_CSE_Mid   = glbDefs.xCOR_blue
    xCOR_CSE_Sup   = glbDefs.xCOR_blue

    #/ cores dos elementos de tela (linha de referência de altitude)
    #/ --------------------------------------------------------------------------------------------
    xCOR_LRA       = glbDefs.xCOR_red

    #/ cores dos elementos de tela (range mark azimute)
    #/ --------------------------------------------------------------------------------------------
    xCOR_RMA_HiL   = THECOLORS [ "darkolivegreen2" ]
    xCOR_RMA_Ini   = glbDefs.xCOR_green
    xCOR_RMA_Nrm   = THECOLORS [ "darkgreen" ]

    #/ cores dos elementos de tela (range mark elevação)
    #/ --------------------------------------------------------------------------------------------
    xCOR_RME_HiL   = THECOLORS [ "darkolivegreen2" ]
    xCOR_RME_Ini   = glbDefs.xCOR_green
    xCOR_RME_Nrm   = THECOLORS [ "darkgreen" ]

    #/ cores dos elementos de tela (vetor linha do solo)
    #/ --------------------------------------------------------------------------------------------
    xCOR_VLS       = glbDefs.xCOR_brown

    #/ cores dos elementos de tela (II)
    #/ --------------------------------------------------------------------------------------------
    xCOR_Aer       = glbDefs.xCOR_black
    xCOR_Circuito  = glbDefs.xCOR_red
    xCOR_Congelado = glbDefs.xCOR_red
#    xCOR_DeclMag   = glbDefs.xCOR_white
#    xCOR_FlightNo  = THECOLORS [ "grey98" ]
    xCOR_Header    = THECOLORS [ "grey40" ]
    xCOR_Hora      = THECOLORS [ "grey98" ]
    xCOR_IMet      = glbDefs.xCOR_LYellow1
    xCOR_Messages  = THECOLORS [ "grey98" ]
    xCOR_Scope     = THECOLORS [ "darkolivegreen4" ]
#    xCOR_Selected  = glbDefs.xCOR_green
    xCOR_Vers      = THECOLORS [ "grey82" ]

    #/ lista de cores dos status
    #/ --------------------------------------------------------------------------------------------
    xCOR_ST = THECOLORS [ "lightblue" ]
    xCOR_VN = glbDefs.xCOR_white

    #/ lista de cores dos sliders
    #/ --------------------------------------------------------------------------------------------
    xCOR_SLD_AV  = ( 104, 104, 104 )
    xCOR_SLD_AH  = ( 104, 104, 104 )
    xCOR_SLD_LR  = ( 104, 104, 104 )

    xCOR_SLD_Mic = ( 104, 104, 104 )
    xCOR_SLD_Out = ( 104, 104, 104 )

#** -----------------------------------------------------------------------------------------------
#*  psyco not found ?
#*/
except ImportError:

    #** -------------------------------------------------------------------------------------------
    #*  get pyGame !
    #*/
    print "get pyGame !"

#** ===============================================================================================
#*  máximos
#*  ===============================================================================================
#*/

#/ quantidade máxima de aeródromos
#/ ------------------------------------------------------------------------------------------------
xMAX_Aerodromos = 1

#/ número máximo de aeronaves na tabela
#/ ------------------------------------------------------------------------------------------------
xMAX_Aeronaves = 100

#/ quantidade máxima de ângulos de elevação ( -04..36 )
#/ ------------------------------------------------------------------------------------------------
xMAX_AngEleMax =  36
xMAX_AngEleMin = -4

#/ quantidade máxima de ângulos de azimute ( -26..26 )
#/ ------------------------------------------------------------------------------------------------
xMAX_AngAziMax =  26
xMAX_AngAziMin = -26

#/ quantidade máxima de aeronaves ativas
#/ ------------------------------------------------------------------------------------------------
xMAX_Ativas = 1

#/ número de cabeceiras de pista
#/ ------------------------------------------------------------------------------------------------
xMAX_Cabeceiras = 2

#/ número máximo de escalas
#/ ------------------------------------------------------------------------------------------------
xMAX_Escalas = 3

#/ número máximo de exercícios na tabela
#/ ------------------------------------------------------------------------------------------------
xMAX_Exercicios = 100

#/ quantidade máxima de gravações para replay
#/ ------------------------------------------------------------------------------------------------
#xMAX_Gravacoes = 5000

#/ número máximo de PAR's
#/ ------------------------------------------------------------------------------------------------
xMAX_PAR = 10

#/ número máximo de pistas no aeródromo
#/ ------------------------------------------------------------------------------------------------
xMAX_Pistas = 2

#/ quantidade máxima de range marks ( 0..14 )
#/ ------------------------------------------------------------------------------------------------
xMAX_RMarks = 15

#** ===============================================================================================
#*  sets
#*  ===============================================================================================
#*/

#/ 
#/ ------------------------------------------------------------------------------------------------
xSET_CabsValidas    = [ 0, 1 ]
xSET_ConfValidas    = [ 'S', 'N' ]
xSET_EscalasValidas = [ 1, 2, 3 ]
xSET_Escalas        = [ 14., 7., 3.5 ]

#** ===============================================================================================
#*  tela
#*  ===============================================================================================
#*/

#/ altura do header em pixels
#/ ------------------------------------------------------------------------------------------------
xSCR_HDR_Height = 12
xSCR_HDR_FntSiz = 12

#/ altura da strip em pixels
#/ ------------------------------------------------------------------------------------------------
xSCR_STP_Height = 40

#/ tamanho da tela (resolução de 800x600)
#/ ------------------------------------------------------------------------------------------------
xSCR_Size = ( 896, 610 )

glbDefs.xSCR_POS [ glbDefs.xSCR_Scope ]   = ((   0,   0 ), ( 640, 480 ))
glbDefs.xSCR_POS [ glbDefs.xSCR_Info ]    = (( 640,   0 ), ( 256,  60 ))

glbDefs.xSCR_PIL [ glbDefs.xSCR_Strip ]   = (( 640,  60 ), ( 256, 380 ))  # (380 - 12) / xSCR_STP_Height = 15,..(640)
glbDefs.xSCR_PIL [ glbDefs.xSCR_Menu ]    = (( 640, 380 ), ( 256, 100 ))

glbDefs.xSCR_PIL [ glbDefs.xSCR_Msg ]     = ((   0, 480 ), ( 640, 130 ))
glbDefs.xSCR_PIL [ glbDefs.xSCR_VoIP ]    = (( 640, 480 ), ( 256, 130 ))

glbDefs.xSCR_CTR [ glbDefs.xSCR_Strip ]   = (( 640,  60 ), ( 256, 280 ))  # (280 - 12) / xSCR_STP_Height = 17,..(680)
glbDefs.xSCR_CTR [ glbDefs.xSCR_Sliders ] = (( 640, 340 ), ( 256, 140 ))
glbDefs.xSCR_CTR [ glbDefs.xSCR_IMet ]    = ((   0, 480 ), ( 256, 130 ))
glbDefs.xSCR_CTR [ glbDefs.xSCR_Msg ]     = (( 256, 480 ), ( 384, 130 ))
glbDefs.xSCR_CTR [ glbDefs.xSCR_VoIP ]    = (( 640, 480 ), ( 256, 130 ))

#/ distância entre a aeronave e o 'click' considerada aceitável
#/ ------------------------------------------------------------------------------------------------
xSCR_CLK_Dist = 9

#** ===============================================================================================
#*  texts
#*  ===============================================================================================
#*/

#/ versão
#/ ------------------------------------------------------------------------------------------------
xTXT_Mjr = "3"
xTXT_Mnr = "01"
xTXT_Rls = "9.01p"
xTXT_Vrs = xTXT_Mjr + "." + xTXT_Mnr
xTXT_Bld = xTXT_Vrs + "-" + xTXT_Rls

#/ programa
#/ ------------------------------------------------------------------------------------------------
xTXT_Prg = "SiPAR"
xTXT_Tit = xTXT_Prg + " " + xTXT_Vrs
xTXT_Hdr = xTXT_Prg + " " + xTXT_Bld

#** ----------------------------------------------------------------------------------------------- *#
