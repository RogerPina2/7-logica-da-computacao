class Node():
    def __init__(self, value):
        self.value = value # Variant
        self.children = [] #list of nodes
        
    def Evaluate(self): #variant
        for child in self.children:
            child.Evaluate()