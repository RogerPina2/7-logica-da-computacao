from Tokenizer import Tokenizer
from Token import tokens, getToken
from Erros import Erros

from Node.BinOp import BinOp
from Node.UnOp import UnOp
from Node.IntVal import IntVal
from Node.NoOp import NoOp

from SymbolTable import ST

error = Erros()

class Parser():

    def __init__(self, tokenizer=None):
        self.tokens = tokenizer     # Objeto da classe que irá ler o código fonte e aliimentar o Analisador
        self.rpar = False    

    def parseExpression(self, flag = None):
        """
            This function consumes the tokens from Tokenizer 
            and analyzes whether the sintax is adherent to the proposed grammar 
            and returns the result of the analyzed expression.
        """
        tree = None

        while self.tokens.actual.type != 'EOF':
            node = self.parseTerm()
            if self.rpar:
                self.rpar = False
                return node

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

            if self.tokens.actual.type == 'R_PAR' and flag:
                error.parenteses()

            if tree is None:
                tree = node

            return tree

    def parseTerm(self):
        tree = None
        node = self.parseFactor()

        while self.tokens.actual.type in ['MULT', 'DIV']:
            if tree is not None:
                node = tree

            tree = BinOp(self.tokens.actual)
            tree.children.append(node)
            self.tokens.selectNext()
            node = self.parseFactor()
            tree.children.append(node)

        if self.tokens.actual.type == 'R_PAR':
            self.rpar = True

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
            # print(self.tokens.actual.type)

            if self.tokens.actual.type == 'R_PAR':
                self.tokens.selectNext()
                # print(self.tokens.actual.type)

            elif self.tokens.actual.type == 'EOF':
                error.parenteses()

        # identific
        elif self.tokens.actual.type == 'ID':
            node = NoOp(self.tokens.actual)

            self.tokens.selectNext()
            
            if self.tokens.actual.type == 'ASSIGN':
                tree = BinOp(self.tokens.actual)
                tree.children.append(node)
                self.tokens.selectNext()
                node = self.parseExpression()
                tree.children.append(node)

            else: 
                tree = node

            if self.tokens.actual.type == 'END':
                self.tokens.selectNext()

        elif self.tokens.actual.type == 'PRINT':
            tree = UnOp(self.tokens.actual)

            self.tokens.selectNext()

            if self.tokens.actual.type != 'L_PAR':
                error.parenteses()
            
            self.tokens.selectNext()
            
            node = self.parseExpression()
            tree.children.append(node)

            if self.tokens.actual.type != 'R_PAR':
                error.parenteses()

            self.tokens.selectNext()

            if self.tokens.actual.type != 'END':
                # self.tokens.selectNext()
                error.parenteses()

        return tree

    def run(self, cf):
        """
            This function takes the source code as an argument, 
            initializes a tokenizer object 
            and returns the resut of parseExpression(). 
            This method will be called by main(). 
        """

        for token in tokens: token
    
        self.tokens = Tokenizer(cf, 0)

        return self.parseExpression(True)
