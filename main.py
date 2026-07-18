import validator
import lexer
import sys
import parser
import codegen
import subprocess

def main(filepath: str, flag: str):
    with open(filepath, "r") as f:
        source = f.read()

    rules = validator.take_fine_filepath(filepath)
    cut_source = "\n".join(source.split("\n")[1:])
    tokens = lexer.tokenize(cut_source, rules)

    body = parser.parse(tokens)

    code = codegen.generate(body[0])

    with open("output.c", "w") as f:
        f.write(code)

    if (flag == "--compile"):
        result = subprocess.run(["gcc", "output.c", "-o", "output"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Compilation failed:")
            print(result.stderr)
            return
        else:
            print("Compilation succeeded. Running the program:")
            run_result = subprocess.run(["./output"], capture_output=True, text=True)
            print(run_result.stdout)
    elif (flag == "--debug"):
        print("Compilation skipped. Use --compile flag to compile and run the program.")
        print(tokens)
        print(body)
        print(code)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
