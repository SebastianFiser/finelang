import validator
import lexer
import sys
import parser

filepath = "examples/hello.fine"

def main(filepath: str):
    with open(filepath, "r") as f:
        source = f.read()

    rules = validator.take_fine_filepath(filepath)
    cut_source = "\n".join(source.split("\n")[1:])
    tokens = lexer.tokenize(cut_source)
    body = parser.parse(tokens)
    print(body)

if __name__ == "__main__":
    main(sys.argv[1])
