import re

class Token():

    def __init__(self, _type, value):
        self.type = _type
        self.value = value

tokens = [
    Token("INT", re.compile(r'[0-9]+')),
    Token("PLUS", re.compile(r'\+')),
    Token("MINUS", re.compile(r'-')),
    Token("SPACE", re.compile(r' '))
]