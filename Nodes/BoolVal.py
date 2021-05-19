# Boolean value
# Não contem filhos

from .Node import Node
from SymbolTable import ST

class BoolVal(Node):
    
    def Evaluate(self):
        if self.value.type == "BOOL":
            if self.value.value == 'true':
                return (bool, True)
            else:
                return (bool, False)