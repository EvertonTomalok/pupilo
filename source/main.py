import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.getcwd())


from errors import *
from lexical.automato import token_verify
from util.regular_expression import extract_tokens


def main():
    if len(sys.argv) == 1:
        info()
        sys.exit(2)
    elif len(sys.argv) == 2:
        file = f"{os.path.dirname(sys.argv[0])}/{sys.argv[1]}"
        pup_file = get_pup_file(file)
        output_file = sys.argv[1].replace(".pup", ".obj")
    else:
        file = f"{os.path.dirname(sys.argv[0])}/{sys.argv[1]}"
        pup_file = get_pup_file(file)
        output_file = get_obj(sys.argv[2])

    line_index = 1
    for line in pup_file.split("\n"):

        for token in extract_tokens(line):
            try:
                print(token, " -> ", token_verify(token))
            except LexicalError:
                start_char = line.find(token)
                if start_char > 0:
                    error_tracer = " " * start_char
                    error_tracer += "\033[1;31m^\033[m"
                else:
                    error_tracer = "^"

                print(f"\n\nError line: {line_index}, char: {start_char}")
                print(line)
                print(error_tracer)
                print("Error INFO: ", str(LexicalError()))

                sys.exit(1)
        line_index += 1


def get_pup_file(file):
    if not file.endswith(".pup"):
        raise FileError(file)

    with open(file) as fp:
        content = fp.read()

    return content


def get_obj(obj_name):
    if not obj_name.endswith(".obj"):
        raise OutputInvalid(sys.argv[2])

    return obj_name


def info():
    print("\n\033[1;42mPUPILO++ v1.0.0\033[m")
    print("   \033[1;32mUSAGE\033[m:")
    print("       pupilo <*.pup> <*.obj>(OPTIONAL)")


if __name__ == '__main__':
    main()
