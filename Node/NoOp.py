# No Operation (Dummy)
# Não contem filhos

from .Node import Node
from SymbolTable import ST

class NoOp(Node):
    
    def Evaluate(self):
        return ST.getter(self.value.value)
        