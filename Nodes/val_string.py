from .Node import Node
from SymbolTable import SymbolTable

class StringVal(Node):
    """
        String Value, não contém filhos
    """

    def Evaluate(self):
        ST = SymbolTable.pilhaST[-1]
        
        return (str, str(self.value.value))