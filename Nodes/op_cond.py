# Conditional Operation
# Contains 2 or 3 children

from GeradorAssembly import GeradorAssembly
from .Node import Node

class ConOp(Node):
    
    def Evaluate(self):
        if self.value.type == 'LOOP':

            GeradorAssembly.addString(f'LOOP_{self.id}:')

            self.children[0].Evaluate()

            GeradorAssembly.addString('CMP EBX, False')
            GeradorAssembly.addString(f'JE EXIT_{self.id}')

            self.children[1].Evaluate()

            GeradorAssembly.addString(f'JMP LOOP_{self.id}')
            GeradorAssembly.addString(f'EXIT_{self.id}:')

        if self.value.type == 'IF':
            GeradorAssembly.addString(f'COND_{self.id}:')

            _type, value, shift = self.children[0].Evaluate()
            if _type is str:
                raise Exception()

            GeradorAssembly.addString('CMP EBX, False')
            GeradorAssembly.addString(f'JE EXIT_{self.id}')

            self.children[1].Evaluate()
            
            if len(self.children) > 2:
                GeradorAssembly.addString(f'JMP EXIT2_{self.id}')    

            GeradorAssembly.addString(f'EXIT_{self.id}:')

            if len(self.children) > 2:
                self.children[2].Evaluate()
                GeradorAssembly.addString(f'EXIT2_{self.id}:')