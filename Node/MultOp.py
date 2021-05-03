from .Node import Node

class MultOp(Node):
    
    def Evaluate(self): #variant
        for child in self.children:
            child.Evaluate()
