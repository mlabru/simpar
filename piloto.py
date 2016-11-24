#!/usr/bin/env python
# -*- coding: utf-8 -*-
#** -----------------------------------------------------------------------------------------------
#*  pyACME
#*  Copyright (c) 2009, Milton Abrunhosa
#*  -----------------------------------------------------------------------------------------------
#*  Package..: SiPAR
#*  Classe...: piloto
#*
#*  Descricao: this class initiates the actual application classes and starts everything.
#*             Furthermore, this class takes care of all interaction with the user
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

#/ Python library
#/ ------------------------------------------------------------------------------------------------

#/ log4Py
#/ ------------------------------------------------------------------------------------------------
import logging

#/ SiPAR / control
#/ ------------------------------------------------------------------------------------------------
import control.controlPiloto as controlPiloto

#** -----------------------------------------------------------------------------------------------
#*  piloto::main
#*  -----------------------------------------------------------------------------------------------
#*  DOCUMENT ME!
#*  -----------------------------------------------------------------------------------------------
#*/
def main ():

    #** -------------------------------------------------------------------------------------------
    #*  m.poirot logger
    #*/
    logging.basicConfig ()

    #** -------------------------------------------------------------------------------------------
    #*  m.poirot logger
    #*
    logger = logging.getLogger ( "piloto" )

    #** -------------------------------------------------------------------------------------------
    #*  set verbosity to show all messages of severity >= DEBUG
    #*
    logger.setLevel ( logging.DEBUG )

    #** -------------------------------------------------------------------------------------------
    #*  instancia o controller
    #*
    l_cp = controlPiloto.controlPiloto ()
    assert ( l_cp )

    #** -------------------------------------------------------------------------------------------
    #*  ativa o controle
    #*
    l_cp.run ()

#** -----------------------------------------------------------------------------------------------
#*  this is the bootstrap process
#*/
if ( '__main__' == __name__ ):

    #** -------------------------------------------------------------------------------------------
    #*  try to load psyco
    #*/
    try:

        #** ---------------------------------------------------------------------------------------
        #*  import psyco if available
        #*/
        import psyco

        #** ---------------------------------------------------------------------------------------
        #*/
        psyco.log ()
        psyco.full ()
        #psyco.profile ( 0.05 )

    #** -------------------------------------------------------------------------------------------
    #*  psyco not found ?
    #*/
    except ImportError:

        #** ---------------------------------------------------------------------------------------
        #*  get psyco !
        #*/
        print "Get psyco !"

    #** -------------------------------------------------------------------------------------------
    #*  run application
    #*/
    main ()

#** ----------------------------------------------------------------------------------------------- *#
