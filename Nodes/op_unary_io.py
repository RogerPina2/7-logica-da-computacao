# Unary Operation IN/OUT
# Contem um filho

from .Node import Node
from SymbolTable import SymbolTable

class UnIOOp(Node):
    
    def Evaluate(self):
        ST = SymbolTable.pilhaST[-1]

        _type, value = self.children[0].Evaluate()

        if self.value.type == "PRINT":
            if _type is str:
                print(_type(value[1:-1]))
            elif value is None:
                print(value)
            else:
                print(_type(value))

        elif self.value.type == 'READ':
            try:
                entrada = int(input())
            except:
                raise Exception("Valor de entrada não permitido. Readln apenas le valores do tipo int")

            return (int, entrada)

        elif self.value.type == "RETURN":
            return (_type, value)
