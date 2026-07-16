def generate(ast):
    lines = []
    lines.append("#include <stdio.h>")
    lines.append("int main() {")

    for node in ast["body"]:
        if node ["type"] == "let":
            if node["d_type"] == "whole":
                data_type = "int"
            elif node["d_type"] == "words":
                data_type = "char*"
            else:
                data_type = node["d_type"]

        if node["type"] == "let":
            lines.append(f"     {data_type} {node['name']} = {node['value']};")
        elif node["type"] == "print":
            lines.append(f"     printf(\"{node['value']}\");")
        elif node["type"] == "return":
            lines.append(f"     return {node['value']};")

    lines.append("}")
    return "\n".join(lines)