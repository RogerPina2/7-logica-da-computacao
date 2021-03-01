import sys

def main():

    arg = ''.join(sys.argv[1:])

    if arg[0] != "'" or arg[-1] != "'":
        raise Exception("Entrada não esperada")

    arg = str(sys.argv[1])[1:-1]

    arg_char_list = list(arg.strip())

    total = 0
    actual_number = ''
    next_operation = '+'

    for char in arg_char_list:

        if char == '+' or char == '-':
            pass
        else:
            try:
                int(char)
            except Exception:
                raise Exception(f'Caracter {char} não esperado')

        if (char != '+') and (char != '-'):
            actual_number += char
        else:
            if next_operation == '+':
                total += int(actual_number)
            else:
                total -= int(actual_number)

            next_operation = char
            actual_number = ''
            
    if next_operation == '+':
        total += int(actual_number)
    else:
        total -= int(actual_number)

    print(total)

if __name__ == "__main__":
    main()