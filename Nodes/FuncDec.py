from .Node import Node
from SymbolTable import SymbolTable

class FuncDec(Node):
    """
        filho 0: vardec 
        filho 1: statements
    """
    
    def Evaluate(self):
        # Registra função na symboltable
        tokenType, tokenVarName = self.children[0].children[0].Evaluate()

        result = None
        try:
            result = SymbolTable.getterFunc(tokenVarName.value)
        except:
            pass

        if result != None:
            raise Exception()
        
        SymbolTable.setterFunc(tokenVarName.value, tokenVarName.type, self)

class Dec(Node):
    """
        children[0] = type
        children[1] = var_name
    """

    def Evaluate(self):
        return self.children[0], self.children[1]

class FuncCall(Node):
    """
        n children: id || expressions 
        all children = params
    """

    def Evaluate(self):
        c = 0
        ST = SymbolTable()
        
        types = {
                'int'       : int,
                'bool'      : bool,
                'string'    : str
            }

        if len(self.children) == 0:
            funcType, funcValue = SymbolTable.getterFunc('main')
            self.children.append(None)
        else:
            funcType, funcValue = SymbolTable.getterFunc(self.children[0].value)

        [funcVarDec, funcBlock] = funcValue.children
        if funcType == 'FUNC':
    
            # Verifica se o número de argumentos passados bate com a quantidade de parâmetros da função
            if len(funcVarDec.children) != len(self.children):
                raise Exception(f'Erro na quantidade de argumentos passados pra função {self.children[0].value}')

            # Cria os parâmetors da função na SymbolTable da função
            for idx in range(1, len(funcVarDec.children)):

                param = funcVarDec.children[idx].children

                ST.setter(
                    param[1].value,
                    types[param[0].value], 
                    self.children[idx].Evaluate()[1]
                    )

            SymbolTable.pilhaST.append(ST)
            ret = funcBlock.Evaluate()
            SymbolTable.pilhaST.pop(-1)

            _type = types[funcVarDec.children[0].children[0].value]

            if ret is not None:
                if _type != ret[0]:
                    raise Exception("Tipo do valor de retorno errado")

            return ret
            
        else:
            raise Exception()