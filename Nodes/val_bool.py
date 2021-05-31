# Boolean value
# Não contem filhos

from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class BoolVal(Node):
    
    def Evaluate(self):
        if self.value.value == 'true':
            GeradorAssembly.addString(f'MOV EBX, {True}')
            return (bool, True, None)
        else:
            GeradorAssembly.addString(f'MOV EBX, {False}')
            return (bool, False, None)