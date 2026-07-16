def parse(tokens):
    body = []
    pos = 0
    while pos < len(tokens):
        current_token = tokens[pos]
        if current_token[0] == "KEYWORD" and current_token[1] == "let":
            if tokens[pos + 1][0] == "IDENTIFIER" and tokens[pos + 2][0] == "SYMBOL" and tokens[pos + 3][0] == "NUMBER":
                body.append({
                    "type": "let",
                    "name": tokens[pos + 1][1],
                    "value": int(tokens[pos + 3][1])
                })
                pos += 4
                continue
        elif current_token[0] == "KEYWORD" and current_token[1] == "print":
            if tokens[pos +1][0] == "SYMBOL" and tokens[pos + 1][1] == "(" and tokens[pos + 3][0] == "SYMBOL" and tokens[pos + 3][1] == ")":
                if tokens[pos + 2][0] == "STRING":
                    body.append({
                        "type": "print",
                        "value": tokens[pos + 2][1]
                    })
                    pos += 4
                    continue
        elif current_token[0] == "KEYWORD" and current_token[1] == "return":
            if tokens[pos + 1][0] == "NUMBER":
                body.append({
                    "type": "return",
                    "value": int(tokens[pos + 1][1])
                })
                pos += 2
                continue
        elif current_token[0] == "KEYWORD" and current_token[1] == "FUNCTION":
            if tokens[pos + 1][0] == "IDENTIFIER" and tokens[pos + 2][0] == "SYMBOL" and tokens[pos + 2][1] == "(" and tokens[pos + 3][0] == "SYMBOL" and tokens[pos + 3][1] == ")" and tokens[pos + 4][0] == "SYMBOL" and tokens[pos + 4][1] == ":":
                body.append({
                    "type": "function",
                    "name": tokens[pos + 1][1],
                    "body": parse(tokens[pos + 5:])
                })
                pos += 5
                break
        pos += 1

    return body