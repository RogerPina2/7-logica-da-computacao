class Node():
    i = 0

    def __init__(self, value=None):
        self.id         = Node.newId()
        self.value      = value     # variant
        self.children   = []        # list of nodes
        
    @staticmethod
    def newId():
        Node.i += 1
        return Node.i

    def Evaluate(self): #variant
        return 

