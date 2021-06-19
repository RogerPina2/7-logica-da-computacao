class SymbolTable():
    def __init__(self):
        self.dic = {}

    def getter(self, symbol):
        if symbol not in self.dic.keys():
            raise Exception("Variável não existe no dicionário")
        return self.dic[symbol]
        
    def setter(self, symbol, _type, value=None):
        self.dic[symbol] = (_type, value)

    pilhaST = []

    funcDic = {}

    @staticmethod
    def getterFunc(symbol):
        if symbol not in SymbolTable.funcDic.keys():
            raise Exception()
        return SymbolTable.funcDic[symbol]

    @staticmethod
    def setterFunc(symbol, _type, value=None):
        SymbolTable.funcDic[symbol] = (_type, value)