import re
pattern = r'"[^"]*"|[A-Za-z_][A-Za-z0-9_]*|[0-9]+\.[0-9]+|[0-9]+|[():=;><]'

keywords = {"FUNCTION", "let", "print", "return", "if", "otherwise", "loop", "stop", "maybe", "NOTHING", "INTENT", "REALITY", "FORGIVE"}
symbols = {"(", ")", ":", "=", ";"}
operators = {"add", "subtract", "times", "divide"}
comparators = {"==", "!=", ">", "<", ">=", "<="}

def tokenize(source: str, rules: dict) -> list:
    tokens = []
    indent_stack = [0]
    lines = source.split("\n")
    str_spacing = rules["indentation"]
    if (str_spacing == "spaces_4"):
        spacing = "4"
    elif (str_spacing == "spaces_3"):
        spacing = "3"
    elif (str_spacing == "emdash"):
        spacing = "—"


    for line in lines:
        if (line.strip() == ""):
            continue

        if (spacing == "4" or spacing == "3"):
            n = len(line) - len(line.lstrip(" "))
            if (n % int(spacing) == 0):
                n = n 
            else:
                raise ValueError(f"Invalid indentation, provided indentation is : {n} spaces \n")
        elif (spacing == "—"):
            n = len(line) - len(line.lstrip(spacing))

        if (n > indent_stack[-1]):
            indent_stack.append(n)
            tokens.append(("INDENT", None))
        elif (n < indent_stack[-1]):
            while (n < indent_stack[-1]):
                indent_stack.pop()
                tokens.append(("DEDENT", None))
            if (n != indent_stack[-1]):
                raise ValueError(f"Invalid indentation, provided indentation is : {n} spaces \n")
        else:
            pass
        
        stripped = line.strip()
        pieces = re.findall(pattern, stripped)
        for piece in pieces:
            if piece in keywords:
                tokens.append(("KEYWORD", piece))
            elif piece in operators:
                tokens.append(("OPERATOR", piece))
            elif piece in comparators:
                tokens.append(("COMPARATOR", piece))
            elif piece.startswith('"') and piece.endswith('"'):
                tokens.append(("STRING", piece[1:-1]))
            elif "." in piece:
                tokens.append(("FLOAT", float(piece)))
            elif piece.isdigit():
                tokens.append(("NUMBER", int(piece)))
            elif piece in symbols:
                tokens.append(("SYMBOL", piece))
            else:
                tokens.append(("IDENTIFIER", piece))
        tokens.append(("NEWLINE", None))
    
    while len(indent_stack) > 1:
        indent_stack.pop()
        tokens.append(("DEDENT", None))
    return tokens
