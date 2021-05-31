# Binary Operation
# Contains 2 children

from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class BinAritOp(Node):
    
    def Evaluate(self):

        _type1, value1, shift = self.children[0].Evaluate()
        GeradorAssembly.addString("PUSH EBX")
        _type2, value2, shift = self.children[1].Evaluate()
        GeradorAssembly.addString("POP EAX")

        # arithmetic operations
        if self.value.type == 'PLUS':
            result = int(value1) + int(value2)
            GeradorAssembly.addString("ADD EAX, EBX")
                
        elif self.value.type == 'MINUS':
            result = int(value1) - int(value2)
            GeradorAssembly.addString("SUB EAX, EBX")

        elif self.value.type == 'MULT':
            result = int(value1) * int(value2)
            GeradorAssembly.addString("IMUL EAX, EBX")

        elif self.value.type == 'DIV':
            result = int(value1) / int(value2)
            GeradorAssembly.addString("DIV EAX, EBX")

        GeradorAssembly.addString("MOV EBX, EAX")
        return (int, result, None)