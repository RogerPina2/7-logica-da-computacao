from .Node import Node
from SymbolTable import SymbolTable

class IntVal(Node):
    """
        Integer value, mão contem filhos
    """
    
    def Evaluate(self):
        ST = SymbolTable.pilhaST[-1]
        
        if self.value.type == "INT":
            return (int, int(self.value.value))
                
        