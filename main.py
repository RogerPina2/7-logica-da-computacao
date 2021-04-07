#!/usr/bin/env python
"""Projeto 'Simple Calculator' de Lógica de Computação

"""

__author__ = "Roger Pina"
__copyright__ = "" #"Copyright 2021, -"
__credits__ = ["Roger Pina"]

__license__ = ""
__version__ = "2.0.1"
__maintainer__ = "Roger Pina"
__email__ = "rogerrfp@al.insper.edu.br"
__status__ = "Production"

import sys

from Parser import Parser

parser = Parser()

def main():
    """
        Arquivo main 
    """

    # Recebe os valores de entrada e armazena em args
    # Transforma uma cadeia de espaços em um único espaço
    args = ' '.join(sys.argv[1:])

    with open(f'{args}', 'r') as c_file:
        cf = c_file.read()

    AST_montada = parser.run(cf)

    print(AST_montada.Evaluate())

if __name__ == "__main__":
    main()