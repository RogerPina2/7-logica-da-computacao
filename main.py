#!/usr/bin/env python
"""Projeto 'Simple Calculator' de Lógica de Computação

"""

__author__ = "Roger Pina"
__copyright__ = "" #"Copyright 2021, -"
__credits__ = ["Roger Pina"]

__license__ = ""
__version__ = "2.1.1"
__maintainer__ = "Roger Pina"
__email__ = "rogerrfp@al.insper.edu.br"
__status__ = "Production"

import sys

from PrePro import PrePro
from Parser import Parser
from Node.BS import BS

from SymbolTable import ST

parser = Parser()

def main():
    """
        Arquivo main 
    """

    # args = path do arquivo teste
    args = ' '.join(sys.argv[1:])

    # cf = lista das linhas do arquivo teste
    with open(f'{args}', 'r') as c_file:
        cf = [line.strip() for line in c_file.readlines()]

    BState = BS()
    
    for line in cf:
        if line != '':
            # pré-processamento da linha de comando
            command = PrePro().filter(line)
            ast = parser.run(command)
            BState.children.append(ast)
    
    # print(BState.children)
    BState.Evaluate()

if __name__ == "__main__":
    main()