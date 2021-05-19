# Assignment Operation
# Contains 2 children

import re
from .Node import Node
from SymbolTable import ST

class AssignOp(Node):
    
    def Evaluate(self):

        # assignment operation
        if self.value.type == 'ASSIGN' or self.value.type == 'TYPING':

            if len(self.children) == 3:
                value = self.children[2].Evaluate() 
                if type(value) == tuple:
                    value = value[1]

                result = None
                try:
                    result = ST.getter(self.children[0].value.value)
                    raise Exception()

                except:
                    if result != None:
                        raise Exception()

                if self.children[1].value.value == 'int':
                    ST.setter(self.children[0].value.value, int, value)

                elif self.children[1].value.value == 'bool':
                    ST.setter(self.children[0].value.value, bool, value)

                elif self.children[1].value.value == 'string':
                    ST.setter(self.children[0].value.value, str, value)

            elif len(self.children) == 2:
                _type, v = ST.getter(self.children[0].value.value) # raise Exception se o símbolo n estiver no dicionário
                
                value = self.children[1].Evaluate()
                if type(value) == tuple:
                    value = value[1]
                    
                ST.setter(self.children[0].value.value, _type, _type(value))