# Integer value
# Não contem filhos

from .Node import Node

class IntVal(Node):
    
    def Evaluate(self):
        return int(self.value.value)
        