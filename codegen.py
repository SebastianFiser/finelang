import errors
import mappings

def generate(ast):
    lines = []
    lines.append("#include <stdio.h>")
    lines.append("int main() {")

    symbol_table = {}
    expr_parts = []

    for node in ast["body"]:
        if node["type"] == "let":
            if(node["d_type"] == "whole"):
                lines.append(f"     int {node['name']} = {node['value']};")
            elif(node["d_type"] == "words"):
                lines.append(f"     char* {node['name']} = \"{node['value']}\";")
            elif(node["d_type"] == "piece"):
                lines.append(f"     float {node['name']} = {node['value']};")
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
                    lines.append(f"     float {node['name']} = {expression};")
                else:
                    node["d_type"] = "whole"
                    lines.append(f"     int {node['name']} = {expression};")
                expr_parts = []

            symbol_table[node["name"]] = node["d_type"]

        elif node["type"] == "print":
            if node["value_type"] == "STRING":
                lines.append(f"     printf(\"{node['value']}\\n\");")
            elif node["value_type"] == "IDENTIFIER":
                if node["value"] in symbol_table:
                    if symbol_table[node["value"]] == "whole":
                        lines.append(f"     printf(\"%d\\n\", {node['value']});")
                    elif symbol_table[node["value"]] == "words":
                        lines.append(f"     printf(\"%s\\n\", {node['value']});")
                    elif symbol_table[node["value"]] == "piece":
                        lines.append(f"     printf(\"%f\\n\", {node['value']});")
                else:
                    raise errors.UndefinedVariableError(f"Undefined variable: {node['value']}")

        elif node["type"] == "return":
            lines.append(f"     return {node['value']};")

    lines.append("}")
    return "\n".join(lines)