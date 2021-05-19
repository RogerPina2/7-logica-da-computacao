from Token import Token, tokens, keywords, tokens_reservados

class Tokenizer():

    def __init__(self, origin, position, actual=None):
        self.origin = origin                    # Código-fonte que será tokenizado
        self.position = position                # Posição atual que o Tokenizador está separando
        self.actual = self.getActual()          # O último token separado

    def selectNext(self):
        """
            This function reads the next token and updates the actual attribute
        """

        if self.position < len(self.origin):
            self.position += len(str(self.actual.value))
            self.actual = self.getActual()

        if self.actual.type == 'SPACE':
            self.selectNext()

    def getActual(self):

        for token in tokens:
            cf = self.origin
            pos = self.position

            if token.value.match(cf[pos:]) != None:
                
                num_dig = token.value.match(cf[pos:]).span()[1]
                _type = token.type
                value = int(cf[pos:pos + num_dig]) if _type == 'INT' else cf[pos:pos + num_dig]

                if _type == 'ID' and value in keywords:
                    idx = keywords.index(value)
                    _type = tokens_reservados[idx].type
                    
                tk = Token(_type, value)
                return tk

        err = 'Entrada não aceita'
        raise ValueError(err)