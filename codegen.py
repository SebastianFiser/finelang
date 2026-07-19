import errors
import mappings

def generate(ast):
    lines = []
    lines.append("#include <stdio.h>")
    lines.append("int main() {")

    symbol_table = {}
    expr_parts = []
    main_function = None

    for node in ast:
        if node["type"] == "function" and node["name"] == "main":
            main_function = node
            break

    if main_function is None:
        raise errors.UnfoundMainError("Initial main function wasnt found")

    statement_lines = generate_statements(main_function["body"], 1, symbol_table, expr_parts)
    lines.append("\n".join(statement_lines))

    lines.append("}")
    return "\n".join(lines)



def generate_statements(body, indentation_level, symbol_table, expr_parts):
    lines = []
    for node in body:
        if node["type"] == "let":
            if(node["d_type"] == "whole"):
                lines.append(f"{" " * indentation_level * 5}int {node['name']} = {node['value']};")
            elif(node["d_type"] == "words"):
                lines.append(f"{" " * indentation_level * 5}char* {node['name']} = \"{node['value']}\";")
            elif(node["d_type"] == "piece"):
                lines.append(f"{" " * indentation_level * 5}float {node['name']} = {node['value']};")
            elif(node["d_type"] == "placeholder"):
                is_piece = False
                for token_type, token_value in node["value"]:
                    if (token_type == "OPERATOR"):
                        expr_parts.append(mappings.word_to_operator(token_value))
                    elif (token_type == "NUMBER"):
                        expr_parts.append(str(token_value))
                    elif(token_type == "IDENTIFIER"):
                        if token_value in symbol_table:
                            if symbol_table[token_value] == "whole":
                                expr_parts.append(str(token_value))
                            elif symbol_table[token_value] == "words":
                                raise errors.InvalidLetValueTypeError(f"Invalid let value, Value type provided : {token_type} \n")
                            elif symbol_table[token_value] == "piece":
                                is_piece = True
                                expr_parts.append(str(token_value))
                        else:
                            raise errors.UndefinedVariableError(f"Undefined variable: {token_value}")
                    elif (token_type == "FLOAT"):
                        is_piece = True
                        expr_parts.append(str(token_value))
                expression = " ".join(expr_parts)
                if (is_piece):
                    node["d_type"] = "piece"
                    lines.append(f"{" " * indentation_level * 5}float {node['name']} = {expression};")
                else:
                    node["d_type"] = "whole"
                    lines.append(f"{" " * indentation_level * 5}int {node['name']} = {expression};")
                expr_parts = []

            symbol_table[node["name"]] = node["d_type"]

        elif node["type"] == "print":
            if node["value_type"] == "STRING":
                lines.append(f"{" " * indentation_level * 5}printf(\"{node['value']}\\n\");")
            elif node["value_type"] == "IDENTIFIER":
                if node["value"] in symbol_table:
                    if symbol_table[node["value"]] == "whole":
                        lines.append(f"{" " * indentation_level * 5}printf(\"%d\\n\", {node['value']});")
                    elif symbol_table[node["value"]] == "words":
                        lines.append(f"{" " * indentation_level * 5}printf(\"%s\\n\", {node['value']});")
                    elif symbol_table[node["value"]] == "piece":
                        lines.append(f"{" " * indentation_level * 5}printf(\"%f\\n\", {node['value']});")
                else:
                    raise errors.UndefinedVariableError(f"Undefined variable: {node['value']}")

        elif node["type"] == "if":
            for token_type, token_value in node["condition"]:
                if (token_type == "OPERATOR"):
                    expr_parts.append(mappings.word_to_operator(token_value))
                elif (token_type == "NUMBER"):
                    expr_parts.append(str(token_value))
                elif(token_type == "IDENTIFIER"):
                    if token_value in symbol_table:
                        if symbol_table[token_value] == "whole":
                            expr_parts.append(str(token_value))
                        elif symbol_table[token_value] == "words":
                            raise errors.InvalidLetValueTypeError(f"Invalid let value, Value type provided : {token_type} \n")
                        elif symbol_table[token_value] == "piece":
                            expr_parts.append(str(token_value))
                    else:
                        raise errors.UndefinedVariableError(f"Undefined variable: {token_value}")
                elif (token_type == "FLOAT"):
                    expr_parts.append(str(token_value))
                elif (token_type == "COMPARATOR"):
                    if (token_value == "is" or token_value == "is not" or token_value == "greater_than" or token_value == "less_than" or token_value == "greater_than_or_equal_to" or token_value == "less_than_or_equal_to"):
                        expr_parts.append(mappings.word_to_comparator(token_value))
                    else:
                        expr_parts.append(token_value)
            node["condition"] = " ".join(expr_parts)
            expr_parts = []
            condition = node["condition"]
            lines.append(f"{" " * indentation_level * 5}if ({condition}) {{")
            nested_lines = generate_statements(node["body"], indentation_level + 1, symbol_table, expr_parts)
            lines.extend(nested_lines)
            lines.append(f"{" " * indentation_level * 5}}}")

        elif node["type"] == "return":
            lines.append(f"{" " * indentation_level * 5}return {node['value']};")

    return lines
