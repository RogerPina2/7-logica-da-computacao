from Tokenizer import Tokenizer
from Token import tokens, getToken
from Erros import Erros
from PrePro import PrePro

error = Erros()

class Parser():

    def __init__(self, tokenizer=None, prepro=None):
        self.tokens = tokenizer     # Objeto da classe que irá ler o código fonte e aliimentar o Analisador    
        self.prepro = prepro

    def parseExpression(self, result = None, r = False):
        """
            This function consumes the tokens from Tokenizer 
            and analyzes whether the sintax is adherent to the proposed grammar 
            and returns the result of the analyzed expression.
        """
        
        result = 0 if result is None else result;

        if self.tokens.actual.type == "SPACE":
            self.tokens.selectNext()

        while self.tokens.actual.type != "EOF":
            result = self.parseTerm(result)
            
            while self.tokens.actual.type in ['PLUS', 'MINUS']:
                operador = self.tokens.actual.type
                
                self.tokens.selectNext()

                if self.tokens.actual.type in ['INT', 'PLUS', 'MINUS', 'L_PAR']:

                    value = self.parseTerm(self.tokens.actual.value)
    
                    if operador == 'PLUS':
                        result += value
                    else:
                        result -= value

                elif self.tokens.actual.type == 'EOF':
                    error.operador_no_final()

                else:
                    error.sequencia_de_operadores()
            
            if self.tokens.actual.type == 'INT':
                error.entrada_nao_aceita()

            if self.tokens.actual.type == 'R_PAR':
                if r:
                    return int(result)
                else:
                    error.parenteses()


        return int(result)

    def parseTerm(self, result):
        while self.tokens.actual.type != "EOF":
            result = self.parseFactor(result)

            while self.tokens.actual.type in ['MULT', 'DIV']:
                operador = self.tokens.actual.type
                
                self.tokens.selectNext()

                if self.tokens.actual.type in ['INT', 'PLUS', 'MINUS', 'L_PAR']:

                    value = self.parseExpression(self.tokens.actual.value)
                    
                    if operador == 'MULT':
                        result *= value
                    else:
                        result /= value

                elif self.tokens.actual.type == 'EOF':
                    error.operador_no_final()
                else:
                    error.sequencia_de_operadores()
            
            return result

    def parseFactor(self, result):
        if self.tokens.actual.type == 'INT':
            value = self.tokens.actual.value
            self.tokens.selectNext()
            return value

        elif self.tokens.actual.type in ['PLUS', 'MINUS']:
            if self.tokens.actual.type == 'PLUS':
                self.tokens.selectNext()
                value = self.parseFactor(result)
                return value
            else:
                self.tokens.selectNext()
                value = -self.parseFactor(result)
                return value
            
        elif self.tokens.actual.type == 'L_PAR':
            self.tokens.selectNext()
            value = self.tokens.actual.value
            result = self.parseExpression(value, True)

            if self.tokens.actual.type == 'R_PAR':
                self.tokens.selectNext()
                return result
        
            if self.tokens.actual.type == 'EOF':
                error.parenteses()

    def run(self, cf):
        """
            This function takes the source code as an argument, 
            initializes a tokenizer object 
            and returns the resut of parseExpression(). 
            This method willbe called by main(). 
        """

        self.prepro = PrePro()
        cf_filtred = self.prepro.filter(cf)

        for token in tokens: token
    
        self.tokens = Tokenizer(cf_filtred, 0)

        return print(self.parseExpression())
