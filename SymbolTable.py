class SymbolTable():

    def __init__(self):
        self.dic = {}

    def getter(self, symbol):
        if symbol not in self.dic.keys():
            return Exception()

        return self.dic[symbol]
        
    def setter(self, symbol, value):
        self.dic[symbol] = value

ST = SymbolTable()