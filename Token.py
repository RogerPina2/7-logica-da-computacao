import re

class Token():

    def __init__(self, _type, value):
        self.type = _type
        self.value = value

def getToken(typeName):
    for token in tokens:
        if token.type == typeName:
            return token

tokens = [
    Token("INT",    re.compile(r'[0-9]+')),
    Token("PLUS",   re.compile(r'\+')),
    Token("MINUS",  re.compile(r'-')),
    Token("MULT",   re.compile(r'\*')),
    Token("DIV",    re.compile(r'/')),
    Token("SPACE",  re.compile(r' ')),
    Token("EOF",    re.compile(r'$')),
    Token("L_PAR",  re.compile(r'\(')),
    Token("R_PAR",  re.compile(r'\)')),
    Token("ASSIGN", re.compile(r'=')),
    Token("PRINT",  re.compile('println')),
    Token("ID",     re.compile(r'[A-Za-z][A-Za-z0-9_]*')),
    Token("END",    re.compile(r';'))
]