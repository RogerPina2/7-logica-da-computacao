# String value
# Não contem filhos

from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class StringVal(Node):
    
    def Evaluate(self):
        if self.value.type == "STRING":
            GeradorAssembly.addString(str, str(self.value.value), None)