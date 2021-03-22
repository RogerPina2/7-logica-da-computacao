# 7-logica-da-computacao

Para utilizar o código você deve inserir a entrada como no exemplo do roteiro 0

![image](https://user-images.githubusercontent.com/38434902/109440618-aa973100-7a11-11eb-9e10-4f649c20e85a.png)

# Diagrama sintático

![Diagrama_Sintatico](DS.png)

# EBNF
EXPRESSION = TERM, { ("+" | "-"), TERM };

TERM = FACTOR, { ("*" | "/"), FACTOR };

FACTOR = ("+" | "-"), FACTOR | "(", EXPRESSION, ")" | number;
