# Binary Operation
# Contains 2 children

import re
from .Node import Node
from SymbolTable import ST

class BinOp(Node):
    
    def Evaluate(self):
        
        if self.children[1].Evaluate()[0] == str or self.children[0].Evaluate()[0] == str:
            if self.value.type == 'EQUAL':
                result = self.children[0].Evaluate()[1] == self.children[1].Evaluate()[1]
                return (bool, result)

            else:
                raise Exception()

        # arithmetic operations
        if self.value.type == 'PLUS':
            result = int(self.children[0].Evaluate()[1]) + int(self.children[1].Evaluate()[1])
            return (int, result)
        
        elif self.value.type == 'MINUS':
            result = int(self.children[0].Evaluate()[1]) - int(self.children[1].Evaluate()[1])
            return (int, result)
        
        elif self.value.type == 'MULT':
            result = int(self.children[0].Evaluate()[1]) * int(self.children[1].Evaluate()[1])
            return (int, result)
        
        elif self.value.type == 'DIV':
            result = int(self.children[0].Evaluate()[1]) / int(self.children[1].Evaluate()[1])
            return (int, result)
        
        # logic operations
        elif self.value.type == 'BIG':
            result = bool(self.children[0].Evaluate()[1]) > bool(self.children[1].Evaluate()[1])
            return (bool, result)

        elif self.value.type == 'SMALL':
            result = bool(self.children[0].Evaluate()[1]) < bool(self.children[1].Evaluate()[1])
            return (bool, result)

        elif self.value.type == 'EQUAL':
            result = bool(self.children[0].Evaluate()[1]) == bool(self.children[1].Evaluate()[1])
            return (bool, result)
        
        elif self.value.type == 'AND':
            result = bool(self.children[0].Evaluate()[1]) & bool(self.children[1].Evaluate()[1])
            return (bool, result)

        elif self.value.type == 'OR':
            result = bool(self.children[0].Evaluate()[1]) or bool(self.children[1].Evaluate()[1])
            return (bool, result)