# Conditional Operation
# Contains 2 or 3 children

from .Node import Node

class ConOp(Node):
    
    def Evaluate(self):
        if self.value.type == 'LOOP':
            while (self.children[0].Evaluate()[1]):
                self.children[1].Evaluate()

        if self.value.type == 'IF':
            _type, value = self.children[0].Evaluate()
            if _type is str:
                raise Exception()
            
            if value:
                self.children[1].Evaluate()
            else:
                if len(self.children) > 2:
                    self.children[2].Evaluate()