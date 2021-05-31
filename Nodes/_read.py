from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class Read(Node):
    
    def Evaluate(self):
        try:
            entrada = int(input())
            GeradorAssembly.addString(f'MOV EBX, {entrada}')
            return (int, entrada)
        except:
            raise Exception()