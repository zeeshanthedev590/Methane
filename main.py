from lexer import lexer
from parser import Parser


def main(file_path):
    code = lexer.read_code_from_file(file_path)
    tokens = lexer.tokenize(code)

    parser = Parser(tokens)
    parser.parse()


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <source_file>")
    else:
        main(sys.argv[1])
