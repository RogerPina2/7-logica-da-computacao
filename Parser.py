from Tokenizer import Tokenizer
from Token import tokens
from Erros import Erros

error = Erros()

class Parser:

    def __init__(self, tokenizer=None):
        self.tokens = tokenizer     # Objeto da classe que irá ler o código fonte e aliimentar o Analisador
        
    def parseExpression(self):
        """
            This function consumes the tokens from Tokenizer 
            and analyzes whether the sintax is adherent to the proposed grammar 
            and returns the result of the analyzed expression.
        """
        result = 0

        if self.tokens.actual.type == "INT":
            result += self.tokens.actual.value

            self.tokens.selectNext()

            if self.tokens.actual.type in ['EOF', 'INT']:
                error.entrada_nao_aceita()

            while self.tokens.actual.type in ['PLUS', 'MINUS']:
                operador = self.tokens.actual.type
                
                self.tokens.selectNext()

                if self.tokens.actual.type == 'INT':
                    if operador == 'PLUS':
                        result += self.tokens.actual.value
                    else:
                        result -= self.tokens.actual.value    
                elif self.tokens.actual.type == 'EOF':
                    error.operador_no_final()
                else:
                    error.sequencia_de_operadores()
            
                self.tokens.selectNext()
                if self.tokens.actual.type == 'INT':
                    error.entrada_nao_aceita()

            return result

        else:
            error.entrada_nao_aceita()

    def run(self, cf):
        """
            This function takes the source code as an argument, 
            initializes a tokenizer object 
            and returns the resut of parseExpression(). 
            This method willbe called by main(). 
        """

        for token in tokens: token
    
        self.tokens = Tokenizer(cf, 0)

        return print(self.parseExpression())