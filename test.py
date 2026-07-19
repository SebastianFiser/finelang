import re
pattern = r'"[^"]*"|[A-Za-z_][A-Za-z0-9_]*|[0-9]+\.[0-9]+|[0-9]+|[():=;><]'

print(re.findall(pattern, "if x > 3:"))