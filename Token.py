import re

class Token():

    def __init__(self, _type, value):
        self.type = _type
        self.value = value

def getToken(typeName):
    for token in tokens:
        if token.type == typeName:
            return token
    
    for token in tokens_reservados:
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
    Token("EQUAL",  re.compile(r'==')),
    Token("ASSIGN", re.compile(r'=')),
    Token("ID",     re.compile(r'[A-Za-z][A-Za-z0-9_]*')),
    Token("END",    re.compile(r';')),
    Token("L_KEY",  re.compile(r'{')),
    Token("R_KEY",  re.compile(r'}')),
    Token("BIG",    re.compile(r'>')),
    Token("SMALL",  re.compile(r'<')),
    Token("AND",    re.compile(r'&&')),
    Token("OR",     re.compile(r'\|\|')),
    Token("NOT",    re.compile(r'!')),
    Token("STRING", re.compile(r'".*?"')),
]

keywords = [
    'println', 'readln', 'if', 'else', 'while', 'int', 'bool', 'string', 'true', 'false'
]

tokens_reservados = [
    Token("PRINT",  re.compile(r'println')),
    Token("READ",   re.compile(r'readln')),
    Token("IF",     re.compile(r'if')),
    Token("ELSE",   re.compile(r'else')),
    Token("LOOP",   re.compile(r'while')),
    Token("TYPING", re.compile(r'int|bool|string')),
    Token("TYPING", re.compile(r'int|bool|string')),
    Token("TYPING", re.compile(r'int|bool|string')),
    Token("BOOL",   re.compile(r'true|false')),
    Token("BOOL",   re.compile(r'true|false'))
]