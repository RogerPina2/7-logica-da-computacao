# 7-logica-da-computacao

Para utilizar o código você deve inserir a entrada como no exemplo do roteiro 0

![image](src/img/DS.png)

# Diagrama sintático

![Diagrama_Sintatico](DS.png)

# EBNF
EXPRESSION = TERM, { ("+" | "-"), TERM };

TERM = FACTOR, { ("*" | "/"), FACTOR };

FACTOR = ("+" | "-"), FACTOR | "(", EXPRESSION, ")" | number;
