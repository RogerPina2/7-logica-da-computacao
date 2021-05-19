class SymbolTable():

    def __init__(self):
        self.dic = {}

    def getter(self, symbol):
        if symbol not in self.dic.keys():
            raise Exception()

        return self.dic[symbol]
        
    def setter(self, symbol, _type, value=None):
        self.dic[symbol] = (_type, value)

ST = SymbolTable()