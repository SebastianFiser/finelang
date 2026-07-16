import validator
import lexer
import sys
import parser
import codegen
import subprocess

def main(filepath: str):
    with open(filepath, "r") as f:
        source = f.read()

    rules = validator.take_fine_filepath(filepath)
    cut_source = "\n".join(source.split("\n")[1:])
    tokens = lexer.tokenize(cut_source)
    print(tokens)
    body = parser.parse(tokens)
    print(body)
    code = codegen.generate(body[0])
    print(code)

    with open("output.c", "w") as f:
        f.write(code)

    result = subprocess.run(["gcc", "output.c", "-o", "output"], capture_output=True, text=True)
    if result.returncode != 0:
        print("Compilation failed:")
        print(result.stderr)
        return
    else:
        print("Compilation succeeded. Running the program:")
        run_result = subprocess.run(["./output"], capture_output=True, text=True)
        print(run_result.stdout)

if __name__ == "__main__":
    main(sys.argv[1])
