# Integer value
# Não contem filhos

from .Node import Node
from SymbolTable import ST

class IntVal(Node):
    
    def Evaluate(self):
        if self.value.type == "INT":
            return int(self.value.value)
        
        elif self.value.type == "ID":
            return ST.getter(self.value.value)
        