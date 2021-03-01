import sys

def main():

    #Junta todos argumentos após o nome do arquivo numa string 
    arg = ''.join(sys.argv[1:])
    
    try:
        #Verifica se o argumento esta no modelo de entrada (cadeia de operações entre aspas simples)
        if arg[0] != "'" or arg[-1] != "'":
            raise ValueError
        
        arg = arg[1:-1] #Remove as aspas simples do inicio e do fim da string
        arg_chars_list = list(arg) #Lista dos caracteres do arg

        #Se o símbolo de operação estivar nas pontas da erro
        if arg_chars_list[0] in ['+', '-'] or arg_chars_list[-1] in ['+', '-']:
            raise ValueError

        op = 0
        #Passa por todos caracteres e remove letras e símbolos não aceitos além de dar erro se houver dois
        #símbolos de operação juntos
        for char in arg_chars_list:
            if char in ['+', '-']:
                op += 1
                if op == 2: raise ValueError 
            else:
                op = 0
                try:
                    int(char)
                except:
                    raise TypeError
            
    except ValueError:
        err = f'Entrada {arg} não é válida, tente uma entrada em que a cadeia de operações esteja entre aspas simples e somente 1 operador sempre entre números.'
        raise ValueError(err)

    except TypeError:
        err = f'Caracter "{char}" não aceito, tente utilizar somente números e operadores "+" e "-".'
        raise TypeError(err)

    result = 0 #variável de retorno
    actual_num = '' #número que será operacionalizado
    next_op = '+' #próxima operação que será realizada

    #Passa por todos caracteres
    for char in arg_chars_list:
        #Junta digitos para formar um número até chegar no operador
        if char not in ['+', '-']:
            actual_num += char
        
        else:
            #Ao encontrar o operador o número formado é somado ao resultado
            if next_op == '+':
                result += int(actual_num) 
            else:
                result -= int(actual_num)

            next_op = char
            actual_num = ''
            
    if next_op == '+':
        result += int(actual_num) 
    else:
        result -= int(actual_num)

    #Retorna o resutado das operações
    print(result)

if __name__ == "__main__":
    main()