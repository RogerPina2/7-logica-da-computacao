from re import A


class SymbolTable():

    def __init__(self):
        self.dic = {}

    def getter(self, symbol):
        if symbol not in self.dic.keys():
            raise Exception("Variável não existe no dicionário")
        return self.dic[symbol]
        
    def setter(self, symbol, _type, value=None, shift=None):
        if shift is None:
            keys = list(self.dic.keys())
            shift = (len(keys) + 1) * 4
        
        self.dic[symbol] = (_type, value, shift)

ST = SymbolTable()

