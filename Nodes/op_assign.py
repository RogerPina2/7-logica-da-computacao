# Assignment Operation
# Contains 2 children

from GeradorAssembly import GeradorAssembly
from .Node import Node
from SymbolTable import ST

class AssignOp(Node):
    
    def Evaluate(self):

        # assignment operation
        if self.value.type == 'ASSIGN' or self.value.type == 'TYPING':

            if len(self.children) == 3:
                GeradorAssembly.addString('PUSH DWORD 0')

                value = self.children[2].Evaluate() 
                if type(value) == tuple:
                    value = value[1]

                result = None
                try:
                    result = ST.getter(self.children[0].value.value)
                    raise Exception()
                except:
                    pass
                
                if result != None:
                    raise Exception()

                if self.children[1].value.value == 'int':
                    
                    ST.setter(self.children[0].value.value, int, value)

                elif self.children[1].value.value == 'bool':
                    ST.setter(self.children[0].value.value, bool, value)

                elif self.children[1].value.value == 'string':
                    ST.setter(self.children[0].value.value, str, value)

                t, v, desl = ST.getter(self.children[0].value.value)
                if value is not None:
                    GeradorAssembly.addString(f'MOV [EBP-{desl}], EBX')

            elif len(self.children) == 2:
                _type, _v, desl = ST.getter(self.children[0].value.value) # raise Exception se o símbolo n estiver no dicionário
                
                value = self.children[1].Evaluate()
                if type(value) == tuple:
                    value = value[1]
                    
                GeradorAssembly.addString(f'MOV [EBP-{desl}], EBX')
                ST.setter(self.children[0].value.value, _type, _type(value), desl)