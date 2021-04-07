from Tokenizer import Tokenizer
from Token import tokens, getToken
from Erros import Erros
from PrePro import PrePro

from Node.BinOp import BinOp
from Node.UnOp import UnOp
from Node.IntVal import IntVal
from Node.NoOp import NoOp

error = Erros()

class Parser():

    def __init__(self, tokenizer=None, prepro=None):
        self.tokens = tokenizer     # Objeto da classe que irá ler o código fonte e aliimentar o Analisador    
        self.prepro = prepro

    def parseExpression(self):
        """
            This function consumes the tokens from Tokenizer 
            and analyzes whether the sintax is adherent to the proposed grammar 
            and returns the result of the analyzed expression.
        """
        tree = None

        while self.tokens.actual.type != 'EOF':
            node = self.parseTerm()

            while self.tokens.actual.type in ['PLUS', 'MINUS']:
                if tree is not None:
                    node = tree

                tree = BinOp(self.tokens.actual)
                tree.children.append(node)
                self.tokens.selectNext()
                node = self.parseTerm()
                tree.children.append(node)

            if self.tokens.actual.type == 'INT':
                error.entrada_nao_aceita()

            if tree is None:
                tree = node
            return tree

    def parseTerm(self):
        tree = None
        node = self.parseFactor()

        while self.tokens.actual.type in ['MULT', 'DIV']:
            if tree is not  None:
                node = tree

            tree = BinOp(self.tokens.actual)
            tree.children.append(node)
            self.tokens.selectNext()
            node = self.parseFactor()
            tree.children.append(node)

        if tree is None:
            tree = node
        return tree

    def parseFactor(self):
        if self.tokens.actual.type == 'INT':
            tree = IntVal(self.tokens.actual)
            self.tokens.selectNext()

        elif self.tokens.actual.type in ['PLUS', 'MINUS']:
            tree = UnOp(self.tokens.actual)
            self.tokens.selectNext()
            tree.children.append(self.parseFactor())

        elif self.tokens.actual.type == 'L_PAR':
            self.tokens.selectNext()
            tree = self.parseExpression()

            if self.tokens.actual.type == 'R_PAR':
                self.tokens.selectNext()

        return tree

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

        return self.parseExpression()
