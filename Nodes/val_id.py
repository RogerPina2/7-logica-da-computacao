from .Node import Node
from SymbolTable import SymbolTable

class IdVal(Node):
    """
        ID Value, não contem filhos
    """
    
    def Evaluate(self):
        ST = SymbolTable.pilhaST[-1]
        
        return ST.getter(self.value.value)