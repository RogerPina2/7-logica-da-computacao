# Id value
# Não contem filhos

from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class IdVal(Node):
    
    def Evaluate(self):
        t, v, desl = ST.getter(self.value.value)
        GeradorAssembly.addString(f'MOV EBX, [EPB-{desl}]')
        return (t,v, None)
