# Binary Operation
# Contains 2 children

from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class BinLogOp(Node):
    
    def Evaluate(self):

        _type1, value1, shift = self.children[0].Evaluate()
        GeradorAssembly.addString("PUSH EBX")
        _type2, value2, shift2 = self.children[1].Evaluate()
        GeradorAssembly.addString("POP EAX")

        # logic operations
        if self.value.type == 'AND':
            result = bool(value1) & bool(value2)
            GeradorAssembly.addString("AND EAX, EBX")

        elif self.value.type == 'OR':
            result = bool(value1) or bool(value2)
            GeradorAssembly.addString("OR EAX, EBX")
        
        return (bool, result, None)
