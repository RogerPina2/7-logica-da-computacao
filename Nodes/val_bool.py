from .Node import Node
from SymbolTable import SymbolTable

class BoolVal(Node):
    """
        Boolean Value, Não contem filhos
    """
    
    def Evaluate(self):
        ST = SymbolTable.pilhaST[-1]
        
        if self.value.type == "BOOL":
            if self.value.value == 'true':
                return (bool, True)
            else:
                return (bool, False)