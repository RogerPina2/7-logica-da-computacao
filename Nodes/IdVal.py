# Id value
# Não contem filhos

from .Node import Node
from SymbolTable import ST

class IdVal(Node):
    
    def Evaluate(self):
        if self.value.type == "ID":
            return ST.getter(self.value.value)