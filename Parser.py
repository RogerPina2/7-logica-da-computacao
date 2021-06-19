from re import S
from Nodes.FuncDec import FuncCall
from Tokenizer import Tokenizer
from Token import tokens, tokens_reservados, getToken
from Erros import Erros

from PrePro import PrePro

from Nodes.importNodes import *

error = Erros()

class Parser():

    def __init__(self, tokenizer=None):
        self.tokens = tokenizer     # Objeto da classe que irá ler o código fonte e aliimentar o Analisador
        self.rpar = False    

    def parseFuncBlock(self):
        tree = FuncDec()

        vardec = Statements()

        if self.tokens.actual.type == 'TYPING':
            func = Dec()
            func.children.append(self.tokens.actual)
            self.tokens.selectNext()
        
            if self.tokens.actual.type == 'FUNC':
                func.children.append(self.tokens.actual)
                self.tokens.selectNext()

                vardec.children.append(func)

                if self.tokens.actual.type == 'L_PAR':
                    self.tokens.selectNext()

                    while self.tokens.actual.type != 'R_PAR':
                        param = Dec()
                        if self.tokens.actual.type == 'TYPING':
                            param.children.append(self.tokens.actual)
                            self.tokens.selectNext()
                            
                            if self.tokens.actual.type == 'ID':
                                param.children.append(self.tokens.actual)
                                self.tokens.selectNext()

                                if self.tokens.actual.type == 'COMMA':
                                    self.tokens.selectNext()
                                    if self.tokens.actual.type == 'R_PAR':
                                        raise Exception()
                        
                        else:
                            raise Exception()
                        
                        vardec.children.append(param)

                    self.tokens.selectNext()
                
                stm = self.parseBlock()
                tree.children.append(vardec)
                tree.children.append(stm)

        return tree
    
    def parseBlock(self):
        tree = Statements()

        if self.tokens.actual.type == 'L_KEY':
            self.tokens.selectNext()

            while self.tokens.actual.type != 'R_KEY':
                
                node = self.parseCommand()
                tree.children.append(node)

                if self.tokens.actual.type == 'EOF':
                    raise Exception()

            self.tokens.selectNext()
            
        else:
            raise Exception()

        return tree

    def parseCommand(self):
        tree = None

        # TYPING
        if self.tokens.actual.type == 'TYPING':
            node_type = NoOp(self.tokens.actual)
            self.tokens.selectNext()

            if self.tokens.actual.type == 'ID':
                node = IdVal(self.tokens.actual)
                self.tokens.selectNext()

                if self.tokens.actual.type == 'ASSIGN':
                    tree = AssignOp(self.tokens.actual)
                    tree.children.append(node)
                    tree.children.append(node_type)
                    self.tokens.selectNext()
                    node = self.parseOrExp()
                    tree.children.append(node)

                elif self.tokens.actual.type == 'END':
                    tree = AssignOp(node_type.value)
                    tree.children.append(node)
                    tree.children.append(node_type)
                    tree.children.append(NoOp())
                    self.tokens.selectNext()

                    return tree
            else:
                raise Exception()
                

        # IDENTIFIER
        if self.tokens.actual.type == 'ID':
            node = IdVal(self.tokens.actual)
            self.tokens.selectNext()

            if self.tokens.actual.type == 'ASSIGN':
                tree = AssignOp(self.tokens.actual)
                tree.children.append(node)
                self.tokens.selectNext()
                node = self.parseOrExp()
                tree.children.append(node)

            else:
                raise Exception()

        # RETURN
        elif self.tokens.actual.type == 'RETURN':
            tree = UnIOOp(self.tokens.actual)
            self.tokens.selectNext()
            node = self.parseOrExp()
            tree.children.append(node)

        # FUNCTION
        elif self.tokens.actual.type == 'FUNC':
            tree = FuncCall()
            tree.children.append(self.tokens.actual)
            self.tokens.selectNext()
            
            if self.tokens.actual.type == 'L_PAR':
                self.tokens.selectNext()
                
                while self.tokens.actual.type != 'R_PAR':
                    node = self.parseOrExp()
                    tree.children.append(node)
                    if self.tokens.actual.type == 'COMMA':
                        self.tokens.selectNext()
                        if self.tokens.actual.type == 'R_PAR':
                            raise Exception()

                self.tokens.selectNext()

        # PRINTLN
        elif self.tokens.actual.type == 'PRINT':
            tree = UnIOOp(self.tokens.actual)
            self.tokens.selectNext()

            if self.tokens.actual.type == 'L_PAR':
                self.tokens.selectNext()
         
                node = self.parseOrExp()
                tree.children.append(node)

                if self.tokens.actual.type == 'R_PAR':
                    self.tokens.selectNext()
                else:
                    raise Exception()
            else:
                raise Exception()

        # BLOCK
        elif self.tokens.actual.type == 'L_KEY':
            tree = self.parseBlock()
            return tree

        # WHILE
        elif self.tokens.actual.type == 'LOOP':
            tree = ConOp(self.tokens.actual)
            self.tokens.selectNext()

            if self.tokens.actual.type == 'L_PAR':
                self.tokens.selectNext()
                 
                node = self.parseOrExp()
                tree.children.append(node)
            
                if self.tokens.actual.type == 'R_PAR':
                    self.tokens.selectNext()
                    
                    node = self.parseCommand()
                    tree.children.append(node)

                    return tree
                    
                else:
                    raise Exception()
            else:
                raise Exception()

        # IF
        elif self.tokens.actual.type == 'IF':
            tree = ConOp(self.tokens.actual)
            self.tokens.selectNext()

            if self.tokens.actual.type == 'L_PAR':
                self.tokens.selectNext()
                 
                node = self.parseOrExp()
                tree.children.append(node)
            
                if self.tokens.actual.type == 'R_PAR':
                    self.tokens.selectNext()
                    
                    node = self.parseCommand()
                    tree.children.append(node)
                    
                    # ELSE
                    if self.tokens.actual.type == 'ELSE':
                        self.tokens.selectNext()

                        node = self.parseCommand()
                        tree.children.append(node)
                
                    return tree

                else:
                    raise Exception()
            else:
                raise Exception()

        if self.tokens.actual.type == 'END':
            if tree == None:
                tree = NoOp(self.tokens.actual)
                self.tokens.selectNext()
                return tree

            self.tokens.selectNext()
            return tree

        else:
            # print(f'ERRO: {self.tokens.actual.type}')
            raise Exception()

    def parseOrExp(self):
        tree = None
        node = self.parseAndExp()
        
        while self.tokens.actual.type == 'OR':
            if tree is not None:
                node = tree

            tree = BinOp(self.tokens.actual)
            tree.children.append(node)
            self.tokens.selectNext()
            node = self.parseAndExp()
            tree.children.append(node)

        return tree if tree is not None else node

    def parseAndExp(self):
        tree = None
        node = self.parseEqExp()
        
        while self.tokens.actual.type == 'AND':
            if tree is not None:
                node = tree

            tree = BinOp(self.tokens.actual)
            tree.children.append(node)
            self.tokens.selectNext()
            node = self.parseEqExp()
            tree.children.append(node)

        return tree if tree is not None else node

    def parseEqExp(self):
        tree = None
        node = self.parseRelExp()
        
        while self.tokens.actual.type == 'EQUAL':
            if tree is not None:
                node = tree

            tree = BinOp(self.tokens.actual)
            tree.children.append(node)
            self.tokens.selectNext()
            node = self.parseRelExp()
            tree.children.append(node)

        return tree if tree is not None else node

    def parseRelExp(self):
        tree = None
        node = self.parseExpression()
        
        while self.tokens.actual.type in ['BIG', 'SMALL']:
            if tree is not None:
                node = tree

            tree = BinOp(self.tokens.actual)
            tree.children.append(node)
            self.tokens.selectNext()
            node = self.parseExpression()
            tree.children.append(node)

        return tree if tree is not None else node
        
    def parseExpression(self, flag = None):
        """
            This function consumes the tokens from Tokenizer 
            and analyzes whether the sintax is adherent to the proposed grammar 
            and returns the result of the analyzed expression.
        """
        tree = None
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

        return tree if tree is not None else node

    def parseFactor(self):
        # number
        if self.tokens.actual.type == 'INT':
            tree = IntVal(self.tokens.actual)
            self.tokens.selectNext()

        # boolean
        elif self.tokens.actual.type == 'BOOL':
            tree = BoolVal(self.tokens.actual)
            self.tokens.selectNext()

        # string
        elif self.tokens.actual.type == 'STRING':
            tree = StringVal(self.tokens.actual)
            self.tokens.selectNext()

        # identific
        elif self.tokens.actual.type == 'ID':
            tree = IdVal(self.tokens.actual)
            self.tokens.selectNext()
            
        # FUNCTION
        elif self.tokens.actual.type == 'FUNC':
            tree = FuncCall()
            tree.children.append(self.tokens.actual)
            self.tokens.selectNext()
                
            if self.tokens.actual.type == 'L_PAR':
                self.tokens.selectNext()

                while self.tokens.actual.type != 'R_PAR':
                    node = self.parseOrExp()
                    tree.children.append(node)
                    if self.tokens.actual.type == 'COMMA':
                        self.tokens.selectNext()
                        if self.tokens.actual.type == 'R_PAR':
                            raise Exception()

                self.tokens.selectNext()


        elif self.tokens.actual.type in ['PLUS', 'MINUS', 'NOT']:
            tree = UnOp(self.tokens.actual)
            self.tokens.selectNext()
            tree.children.append(self.parseFactor())

        elif self.tokens.actual.type == 'L_PAR':
            self.tokens.selectNext()
            tree = self.parseOrExp()
            # print(self.tokens.actual.type)

            if self.tokens.actual.type == 'R_PAR':
                self.tokens.selectNext()
                # print(self.tokens.actual.type)

            elif self.tokens.actual.type == 'END':
                raise Exception()

            elif self.tokens.actual.type == 'EOF':
                error.parenteses()

        elif self.tokens.actual.type == 'READ':
            tree = UnIOOp(self.tokens.actual)
            self.tokens.selectNext()

            if self.tokens.actual.type == 'L_PAR':
                self.tokens.selectNext()
                
                if self.tokens.actual.type == 'R_PAR':
                    self.tokens.selectNext()
                    
        return tree

    def run(self, cf):
        """
            This function takes the source code as an argument, 
            initializes a tokenizer object 
            and returns the resut of parseExpression(). 
            This method will be called by main(). 
        """
        for token in tokens: token
        for token in tokens_reservados: token

        cf = PrePro().filter(cf)
        
        self.tokens = Tokenizer(cf, 0)
    
        while self.tokens.actual.type != 'EOF':
            tree = self.parseFuncBlock()
            tree.Evaluate()
        
        FC = FuncCall()
        return FC.Evaluate()
    
        
