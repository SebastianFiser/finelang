import errors

def generate(ast):
    lines = []
    lines.append("#include <stdio.h>")
    lines.append("int main() {")

    symbol_table = {}

    for node in ast["body"]:
        if node["type"] == "let":
            if(node["d_type"] == "whole"):
                lines.append(f"     int {node['name']} = {node['value']};")
            elif(node["d_type"] == "words"):
                lines.append(f"     char* {node['name']} = \"{node['value']}\";")

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
                else:
                    raise errors.UndefinedVariableError(f"Undefined variable: {node['value']}")

        elif node["type"] == "return":
            lines.append(f"     return {node['value']};")

    lines.append("}")
    return "\n".join(lines)