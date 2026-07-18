from lexer import tokenize
from parser import parse
from rules import get_rules_for_level

source = """FUNCTION main():
    let x = 5
FUNCTION second():
    let y = 10
"""

rules = get_rules_for_level(1)
tokens = tokenize(source, rules)
ast = parse(tokens)

import json
print(json.dumps(ast, indent=2))