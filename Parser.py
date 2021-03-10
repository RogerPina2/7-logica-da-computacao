from Tokenizer import Tokenizer
from Token import tokens

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

        if self.tokens.actual == "INT":
            
        
        # result = 0

        # while self.tokens.position < len(self.tokens.origin):

        #     _type, num_dig = self.tokens.get_token_type()
            
        #     if num_dig == 0:    
        #         raise ValueError("ERRO")
        #         break
        #     else:
        #         for e in range(num_dig):
        #             self.tokens.selectNext()
        # return

    def run(self, cf):
        """
            This function takes the source code as an argument, 
            initializes a tokenizer object 
            and returns the resut of parseExpression(). 
            This method willbe called by main(). 
        """

        for token in tokens:
            token
    
        self.tokens = Tokenizer(cf, 0)

        return self.parseExpression()