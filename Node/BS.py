from .Node import Node

class BS(Node):

    def Evaluate(self): #variant
        for child in self.children:
            child.Evaluate()