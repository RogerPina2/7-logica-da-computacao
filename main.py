#!/usr/bin/env python
"""Projeto 'Simple Calculator' de Lógica de Computação

"""

__author__ = "Roger Pina"
__copyright__ = "" #"Copyright 2021, -"
__credits__ = ["Roger Pina"]

__license__ = ""
__version__ = "3.0.1"
__maintainer__ = "Roger Pina"
__email__ = "rogerrfp@al.insper.edu.br"
__status__ = "Production"

import sys

from Parser import Parser
from GeradorAssembly import GeradorAssembly

parser = Parser()

def main():
    """
        Arquivo main 
    """

    # args = path do arquivo teste
    args = ' '.join(sys.argv[1:])

    # cf = lista das linhas do arquivo teste
    with open(f'{args}', 'r') as c_file:
        cf = ' '.join(c_file.read().split())
        
    parser.run(cf)
    GeradorAssembly.gerarExe('executavel')

if __name__ == "__main__":
    main()