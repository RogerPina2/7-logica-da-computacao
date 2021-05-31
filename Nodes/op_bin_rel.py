# Binary Operation
# Contains 2 children

from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class BinRelOp(Node):
    
    def Evaluate(self):

        _type1, value1, shift = self.children[0].Evaluate()
        GeradorAssembly.addString("PUSH EBX")
        _type2, value2, shift = self.children[1].Evaluate()
        GeradorAssembly.addString("POP EAX")

        if _type1 == str or _type2 == str:
            if self.value.type == 'EQUAL':
                result = value1 == value2
                return (bool, result)

            else:
                raise Exception()

        # relational operations
        elif self.value.type == 'BIG':
            result = int(value1) > int(value2)

        elif self.value.type == 'SMALL':
            result = int(value1) < int(value2)

        elif self.value.type == 'EQUAL':
            v1 = _type1(value1)
            v2 = _type2(value2)
            result = v1 == v2
        
        
        return (bool, result, None)

