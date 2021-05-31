# Integer value
# Não contem filhos

from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class IntVal(Node):
    
    def Evaluate(self):
        GeradorAssembly.addString(f'MOV EBX, {self.value.value}')
        return (int, int(self.value.value), None)
