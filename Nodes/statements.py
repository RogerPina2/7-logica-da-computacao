from Nodes.op_unary_io import UnIOOp
from .Node import Node
from SymbolTable import SymbolTable

class Statements(Node):
    
    def Evaluate(self): #variant
        ST = SymbolTable.pilhaST[-1]

        for child in self.children:
            if type(child) is UnIOOp:
                if child.value.type == 'RETURN':
                    _t, v = child.Evaluate()
                    ST.setter('___RETURN', _t, v) 
            child.Evaluate()

            retorno = None
            try:
                retorno = ST.getter('___RETURN')
            except:
                pass

            if retorno != None:
                return retorno

                
