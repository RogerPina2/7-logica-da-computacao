# Binary Operation
# Contem 2 filhos

from .Node import Node
from SymbolTable import ST

class BinOp(Node):
    
    def Evaluate(self):
        if self.value.type == 'PLUS':
            return int(self.children[0].Evaluate() + self.children[1].Evaluate())
        
        elif self.value.type == 'MINUS':
            return int(self.children[0].Evaluate() - self.children[1].Evaluate())
        
        elif self.value.type == 'MULT':
            return int(self.children[0].Evaluate() * self.children[1].Evaluate())
        
        elif self.value.type == 'DIV':
            return int(self.children[0].Evaluate() / self.children[1].Evaluate())
        
        elif self.value.type == 'ASSIGN':
            ST.setter(self.children[0].value.value, self.children[1].Evaluate())

        elif self.value.type == 'BIG':
            return int(self.children[0].Evaluate() > self.children[1].Evaluate())

        elif self.value.type == 'SMALL':
            return int(self.children[0].Evaluate() < self.children[1].Evaluate())

        elif self.value.type == 'EQUAL':
            return int(self.children[0].Evaluate() == self.children[1].Evaluate())
        
        elif self.value.type == 'AND':
            return int(self.children[0].Evaluate() & self.children[1].Evaluate())

        elif self.value.type == 'OR':
            return int(self.children[0].Evaluate() or self.children[1].Evaluate())