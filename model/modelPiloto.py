#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2008, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: modelPiloto
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

#/ log4Py (logger)
#/ ------------------------------------------------------------------------------------------------
import logging

#/ SiPAR / model
#/ ------------------------------------------------------------------------------------------------
import model.clsAnv as clsAnv
import model.clsExe as clsExe
import model.clsPAR as clsPAR

import model.modelManager as modelManager

#** -----------------------------------------------------------------------------------------------
#*  variáveis globais
#*  -----------------------------------------------------------------------------------------------
#*/

#/ logging level
#/ ------------------------------------------------------------------------------------------------
#w_logLvl = logging.INFO
w_logLvl = logging.DEBUG

#** -----------------------------------------------------------------------------------------------
#*  modelPiloto::modelPiloto
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
class modelPiloto ( modelManager.modelManager ):

    #** -------------------------------------------------------------------------------------------
    #*  modelPiloto::__init__
    #*  -------------------------------------------------------------------------------------------
    #*  initializes the display
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def __init__ ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "modelPiloto::__init__"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  inicia a superclass
        #*/
        modelManager.modelManager.__init__ ( self )

        #** ---------------------------------------------------------------------------------------
        #*  inicia variáveis de instância
        #*/
        self._iCanal = None
        
        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** -------------------------------------------------------------------------------------------
    #*  modelPiloto::iniciaBaseDados
    #*  -------------------------------------------------------------------------------------------
    #*  DOCUMENT ME!
    #*  -------------------------------------------------------------------------------------------
    #*  @param  f_szExe - DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def iniciaBaseDados ( self, f_szExe ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "modelPiloto::iniciaBaseDados"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica parâmetros de entrada
        #*/
        #assert (( f_szExe ) and ( "" != f_szExe ))

        #** ---------------------------------------------------------------------------------------
        #*  carrega o arquivo de configuração de exercício
        #*/
        self.loadConfigExe ( f_szExe )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*/
        return ( True )

    #** -------------------------------------------------------------------------------------------
    #*  modelPiloto::loadConfigExe
    #*  -------------------------------------------------------------------------------------------
    #*  initialize airplane class
    #*  -------------------------------------------------------------------------------------------
    #*  @param  DOCUMENT ME!
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def loadConfigExe ( self, f_szCfg ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "modelPiloto::loadConfigExe"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( f_szCfg )
        #l_log.info ( u"Configuração de exercício a carregar: " + f_szCfg )

        #** ---------------------------------------------------------------------------------------
        #*  abre o arquivo de configuração
        #*/
        l_fdCfg = open ( f_szCfg, "r" )
        #assert ( l_fdCfg )

        #** ---------------------------------------------------------------------------------------
        #*  cria a área de dados
        #*/
        l_data = []

        #** ---------------------------------------------------------------------------------------
        #*  percorre todas as linhas do arquivo de configuração
        #*/
        for l_line in l_fdCfg.readlines ():

            #** -----------------------------------------------------------------------------------
            #*  checa se é uma linha de comentário ou vazia
            #*/
            if (( not l_line.startswith ( "#" )) and
                ( not l_line.startswith ( "\n" ))):

                #** -------------------------------------------------------------------------------
                #*  checa end-of-line
                #*/
                if ( l_line.endswith ( "\n" ) or l_line.endswith ( "\x1a" )):

                    #** ---------------------------------------------------------------------------
                    #*  aceita o valor sem o end-of-line
                    #*/
                    l_data.extend ( l_line [ :-1 ].split ())

                #** -------------------------------------------------------------------------------
                #*/
                else:

                    #** ---------------------------------------------------------------------------
                    #*  aceita o valor
                    #*/
                    l_data.extend ( l_line.split ())

        #** ---------------------------------------------------------------------------------------
        #*  fecha o arquivo
        #*/
        l_fdCfg.close ()

        #** ---------------------------------------------------------------------------------------
        #*  carrega a parte do exercício
        #*/
        self._oExe = clsExe.clsExe ( l_data [ 0 : 10 ] )
        #assert ( self._oExe )

        #** ---------------------------------------------------------------------------------------
        #*  carrega a parte do PAR
        #*/
        l_oPAR = clsPAR.clsPAR ( l_data [ 10 : 21 ] )
        #assert ( l_oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  salva o PAR no exercício
        #*/
        self._oExe.setPAR ( l_oPAR )

        #** ---------------------------------------------------------------------------------------
        #*  carrega a parte da aeronave
        #*/
        l_oAnv = clsAnv.clsAnv ( l_data [ 21 : 28 ] )
        #assert ( l_oAnv )

        #** ---------------------------------------------------------------------------------------
        #*  salva a aeronave no exercício
        #*/
        self._oExe.setAnv ( l_oAnv )

        #** ---------------------------------------------------------------------------------------
        #*  carrega a parte de comunicação
        #*/
        self._iCanal = int ( l_data [ 28 ] )
        #assert ( 2 < self._iCanal < 28 )

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

    #** ===========================================================================================
    #*  acesso a area de dados do objeto
    #*  ===========================================================================================
    #*/

    #** -------------------------------------------------------------------------------------------
    #*  modelPiloto::getAnv
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o objeto aeronave
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getAnv ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "modelPiloto::getAnv"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._oExe )
        #assert ( isinstance ( self._oExe, clsExe.clsExe ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  retorna o objeto aeronave
        #*/
        return ( self._oExe.getAnv ())

    #** -------------------------------------------------------------------------------------------
    #*  modelPiloto::getCanal
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o canal
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getCanal ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "modelPiloto::getCanal"


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
        #*  retorna o objeto Canal
        #*/
        return ( self._iCanal )

    #** -------------------------------------------------------------------------------------------
    #*  modelPiloto::getPAR
    #*  -------------------------------------------------------------------------------------------
    #*  retorna o objeto aeronave
    #*  -------------------------------------------------------------------------------------------
    #*  @param  nenhum
    #*
    #*  @return nenhum
    #*  -------------------------------------------------------------------------------------------
    #*/
    def getPAR ( self ):

        #/ nome do método (logger)
        #/ ----------------------------------------------------------------------------------------
        #l_szMetodo = "modelPiloto::getPAR"


        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log = logging.getLogger ( l_szMetodo )
        #l_log.setLevel ( w_logLvl )
        #l_log.debug ( ">> " )

        #** ---------------------------------------------------------------------------------------
        #*  verifica condições de execução
        #*/
        #assert ( self._oExe )
        #assert ( isinstance ( self._oExe, clsExe.clsExe ))

        #** ---------------------------------------------------------------------------------------
        #*  m.poirot logger
        #*/
        #l_log.debug ( "<< " )

        #** ---------------------------------------------------------------------------------------
        #*  retorna o objeto aeronave
        #*/
        return ( self._oExe.getPAR ())

#** -----------------------------------------------------------------------------------------------
#*/
logger = logging.getLogger ( "modelPiloto" )

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
    l_mm = modelPiloto ()
    #assert ( l_mm )

#** ----------------------------------------------------------------------------------------------- *#