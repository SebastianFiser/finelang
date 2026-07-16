import re
pattern = r'"[^"]*"|[A-Za-z_][A-Za-z0-9_]*|[0-9]+|[():=;]'

keywords = {"FUNCTION", "let", "print", "return", "if", "otherwise", "loop", "stop", "maybe", "NOTHING", "INTENT", "REALITY", "FORGIVE"}
symbols = {"(", ")", ":", "=", ";"}

def tokenize(source: str) -> list:
    tokens = []
    lines = source.split("\n")

    for line in lines:
        stripped = line.strip()
        pieces = re.findall(pattern, stripped)
        for piece in pieces:
            if piece in keywords:
                tokens.append(("KEYWORD", piece))
            elif piece.isdigit():
                tokens.append(("NUMBER", int(piece)))
            elif piece in symbols:
                tokens.append(("SYMBOL", piece))
            elif piece.startswith('"') and piece.endswith('"'):
                tokens.append(("STRING", piece[1:-1]))
            else:
                tokens.append(("IDENTIFIER", piece))
    return tokens
