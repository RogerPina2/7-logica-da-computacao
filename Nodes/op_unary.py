from .Node import Node
from SymbolTable import SymbolTable

class UnOp(Node):
    """
        Unary Operations, contem um filho.
    """
    
    def Evaluate(self):
        ST = SymbolTable.pilhaST[-1]
        
        _type, value = self.children[0].Evaluate()

        options = {
            "PLUS"  : value, 
            "MINUS" : -value, 
            "NOT"   : not value
            }
            
        return (_type, options[_type])
        