# Unary Operation
# Contem um filho

from .Node import Node
from SymbolTable import ST

class UnOp(Node):
    
    def Evaluate(self):
        _type, value = self.children[0].Evaluate()

        if self.value.type == "PLUS":
            return (_type, value)

        elif self.value.type == "MINUS":
            return (_type, -value)

        elif self.value.type == "NOT":
            return (_type, not value)
