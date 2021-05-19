# Binary Operation
# Contains 2 children

import re
from .Node import Node
from SymbolTable import ST

class BinOp(Node):
    
    def Evaluate(self):

        _type1, value1 = self.children[0].Evaluate()
        _type2, value2 = self.children[1].Evaluate()
        
        if _type1 == str or _type2 == str:
            if self.value.type == 'EQUAL':
                result = value1 == value2
                return (bool, result)

            else:
                raise Exception()

        # arithmetic operations
        if self.value.type == 'PLUS':
            result = int(value1) + int(value2)
            return (int, result)
        
        elif self.value.type == 'MINUS':
            result = int(value1) - int(value2)
            return (int, result)
        
        elif self.value.type == 'MULT':
            result = int(value1) * int(value2)
            return (int, result)
        
        elif self.value.type == 'DIV':
            result = int(value1) / int(value2)
            return (int, result)
        
        
        # relational operations
        elif self.value.type == 'BIG':
            result = int(value1) > int(value2)
            return (bool, result)

        elif self.value.type == 'SMALL':
            result = int(value1) < int(value2)
            return (bool, result)

        elif self.value.type == 'EQUAL':
            v1 = _type1(value1)
            v2 = _type2(value2)
            result = v1 == v2
            return (bool, result)


        # logic operations
        elif self.value.type == 'AND':
            result = bool(value1) & bool(value2)
            return (bool, result)

        elif self.value.type == 'OR':
            result = bool(value1) or bool(value2)
            return (bool, result)