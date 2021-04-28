from .Node import Node

class PrintOp(Node):
    
    def Evaluate(self): #variant
        print(self.children[0].Evaluate())
