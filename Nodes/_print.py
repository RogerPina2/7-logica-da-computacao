from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class Print(Node):
    
    def Evaluate(self):
        _type, value, shift = self.children[0].Evaluate()

        GeradorAssembly.addString('PUSH EBX')
        GeradorAssembly.addString('CALL print')
        GeradorAssembly.addString('POP EBX')
