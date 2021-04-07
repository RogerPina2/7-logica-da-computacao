# Unary Operation
# Contem um filho

from .Node import Node

class UnOp(Node):
    
    def Evaluate(self):
        if self.value.type == "PLUS":
            return self.children[0].Evaluate()

        else:
            return -self.children[0].Evaluate()
        