# Unary Operation
# Contem um filho

from .Node import Node
from SymbolTable import ST

class UnOp(Node):
    
    def Evaluate(self):
        if self.value.type == "PLUS":
            return self.children[0].Evaluate()

        elif self.value.type == "MINUS":
            return -self.children[0].Evaluate()

        elif self.value.type == "NOT":
            return int(not self.children[0].Evaluate())

        elif self.value.type == "PRINT":
            print(self.children[0].Evaluate())

        