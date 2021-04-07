# Binary Operation
# Contem 2 filhos

from .Node import Node

class BinOp(Node):
    
    def Evaluate(self):
        if self.value.type == 'PLUS':
            return int(self.children[0].Evaluate() + self.children[1].Evaluate())
        
        elif self.value.type == 'MINUS':
            return int(self.children[0].Evaluate() - self.children[1].Evaluate())
        
        elif self.value.type == 'MULT':
            return int(self.children[0].Evaluate() * self.children[1].Evaluate())
        
        else:
            return int(self.children[0].Evaluate() / self.children[1].Evaluate())
        