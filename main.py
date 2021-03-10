import sys

from Parser import Parser

parser = Parser()

def main():

    args = ' '.join(sys.argv[1:])

    parser.run(args)

if __name__ == "__main__":
    main()