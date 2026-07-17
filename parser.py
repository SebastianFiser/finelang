import errors

def parse(tokens):
    body = []
    pos = 0
    while pos < len(tokens):
        current_token = tokens[pos]
        if current_token[0] == "NEWLINE":
            pos += 1
            continue
        elif current_token[0] == "KEYWORD" and current_token[1] == "let":
            if tokens[pos + 2][1] == ":" and tokens[pos + 4][1] == "=":
                body.append({
                    "type": "let",
                    "name": tokens[pos + 1][1],
                    "d_type": tokens[pos + 3][1],
                    "value": tokens[pos + 5][1]
                })
                pos += 6
            elif tokens[pos + 1][0] == "IDENTIFIER" and tokens[pos + 2][0] == "SYMBOL":
                if tokens[pos + 2][1] == "=":
                    statement_len = find_end_of_statement(tokens, pos + 3)
                    if (statement_len - (pos + 3) == 1):
                        if tokens[pos + 3][0] == "NUMBER":
                            body.append({
                                "type": "let",
                                "name": tokens[pos + 1][1],
                                "d_type": "whole",
                                "value": tokens[pos + 3][1]
                            })
                            pos += 4
                        elif tokens[pos + 3][0] == "STRING":
                            body.append({
                                "type": "let",
                                "name": tokens[pos + 1][1],
                                "d_type": "words",
                                "value": tokens[pos + 3][1]
                            })
                            pos += 4
                        elif tokens[pos + 3][0] == "FLOAT":
                            body.append({
                                "type": "let",
                                "name": tokens[pos + 1][1],
                                "d_type": "piece",
                                "value": tokens[pos + 3][1]
                            })
                            pos += 4
                        else:
                            raise errors.InvalidLetValueTypeError(f"Invalid let value, Value type provided : {tokens[pos + 3][0]} \n")
                    else:
                        body.append({
                            "type": "let",
                            "name": tokens[pos + 1][1],
                            "d_type": "placeholder",
                            "value": tokens[pos + 3:statement_len]
                        })
                        pos = statement_len
                else:
                    raise errors.InvalidIdentifierError(f"Invalid symbol, provided symbol is : {tokens[pos + 2][1]} \n")
            else:
                raise errors.InvalidIdentifierError(f"Invalid symbol, provided symbol is : {tokens[pos + 2][1]} \n")
            continue
        elif current_token[0] == "KEYWORD" and current_token[1] == "print":
            if tokens[pos +1][0] == "SYMBOL" and tokens[pos + 1][1] == "(" and tokens[pos + 3][0] == "SYMBOL" and tokens[pos + 3][1] == ")":
                if tokens[pos + 2][0] == "STRING":
                    body.append({
                        "type": "print",
                        "value": tokens[pos + 2][1],
                        "value_type": tokens[pos + 2][0]
                    })
                    pos += 4
                elif tokens[pos + 2][0] == "IDENTIFIER":
                    body.append({
                        "type": "print",
                        "value": tokens[pos + 2][1],
                        "value_type": tokens[pos + 2][0]
                    })
                    pos += 4
                else:
                    raise errors.InvalidValueError(f"Invalid print value, Value type provided : {tokens[pos + 2][0]} \n")
            else:
                raise errors.InvalidPrintSyntaxError(f"Invalid print syntax, provided symbols are : {tokens[pos + 1][1]} and {tokens[pos + 3][1]} \n")
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

def find_end_of_statement(tokens, start_pos):
    pos = start_pos
    while pos < len(tokens):
        if tokens[pos][0] == "NEWLINE":
            return pos
        pos += 1
    return len(tokens)