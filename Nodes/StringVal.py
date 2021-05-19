# String value
# Não contem filhos

from .Node import Node
from SymbolTable import ST

class StringVal(Node):
    
    def Evaluate(self):
        if self.value.type == "STRING":
            return (str, str(self.value.value))