# 7-logica-da-computacao
Projeto Simple Calculator

# Diagrama sintático

![Diagrama_Sintatico](src/img/DS.png)

# EBNF
EXPRESSION = TERM, { ("+" | "-"), TERM };

TERM = FACTOR, { ("*" | "/"), FACTOR };

FACTOR = ("+" | "-"), FACTOR | "(", EXPRESSION, ")" | number;
