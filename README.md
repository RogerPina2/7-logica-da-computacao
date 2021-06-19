# 7-logica-da-computacao
Projeto Simple Calculator

# Status dos testes
![git status](http://3.129.230.99/svg/RogerPina2/7-logica-da-computacao/)

# Diagrama sintático

![Diagrama_Sintatico-P1](src/img/DS-P1.png)
![Diagrama_Sintatico-P2](src/img/DS-P2.png)
![Diagrama_Sintatico-P3](src/img/DS-P3.png)
![Diagrama_Sintatico-P4](src/img/DS-P4.png)

# EBNF

FUNCDEFBLOCK = FUNC, {FUNC};

FUNC = TYPE, IDENTIFIER, "(", PARAM, ")", COMMAND ; 

PARAM = TYPE, IDENTIFIER, {",", TYPE, IDENTIFIER};

BLOCK = "{", { COMMAND }, "}" ;

COMMAND = (ASSIGNMENT | ASSIGNMENT_TYPE | PRINT | BLOCK | LOOP | CONDITION | RETURN | FUNCCALL), ";" ;

ASSIGNMENT_TYPE = (λ | TYPE), IDENTIFIER, (λ | "=", OREXPR) ; 

ASSIGNMENT = IDENTIFIER, "=", OREXPR ;

RETURN = "return", OREXPR ;

FUNCCALL = IDENTIFIER, "(", OREXPR, {",", OREXPR} , ")" ;

PRINT = "println", "(", OREXPR, ")" ;

LOOP = "while", "(", OREXPR, ")", COMMAND ;

CONDITION= "if", "(", OREXPR, ")", COMMAND, ( λ | "else", COMMAND) ;

OREXPR = ANDEXPR, { "||", ANDEXPR } ;

ANDEXPR = EQEXPR, { "&&", EQEXPR } ;

EQEXPR = RELEXPR, { "==", RELEXPR } ;

RELEXPR = EXPRESSION, { (">" | "<"), EXPRESSION } ;

EXPRESSION = TERM, { ("+" | "-"), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = NUMBER | IDENTIFIER | (("+" | "-" | "!"), FACTOR) | "(", OREXPR, ")" | READ ;

READ = "readln", "(", ")";

TYPE = ("int" | "bool" | "string") ;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
