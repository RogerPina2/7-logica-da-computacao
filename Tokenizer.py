from Token import tokens

class Tokenizer:

    def __init__(self, origin, position, actual=None):
        self.origin = origin                    # Código-fonte que será tokenizado
        self.position = position                # Posição atual que o Tokenizador está separando
        self.actual = self.get_token_type()[0]  # O último token separado

    def selectNext(self):
        """
            This function reads the next token and updates the actual attribute
        """

        if self.position < len(self.origin):
            self.position += 1
            
    def get_token_type(self):

        num_dig = 0
        _type = None
        
        for e in range(len(tokens)):
            cf = self.origin
            pos = self.position
            if tokens[e].value.match(cf[pos:]) != None:
                num_dig = tokens[e].value.match(cf[pos:]).span()[1]
                _type = tokens[e].type
                break

        return _type, num_dig

