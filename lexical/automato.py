from collections import OrderedDict
from string import ascii_letters, ascii_lowercase, punctuation, whitespace

try:
    from errors import LexicalError
except ModuleNotFoundError:
    import sys, os

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from errors import LexicalError

try:
    from lexical.automato_base import AutomatoBase
except ModuleNotFoundError:
    from automato_base import AutomatoBase


class SE(AutomatoBase):
    def __init__(self):
        super().__init__("SE")

        self.insert_alphabet(["S", "E"])
        self.insert_starting_state([], ["S"])
        self.insert_new_state([], ["E"], final=True)


class ENTÃO(AutomatoBase):
    def __init__(self):
        super().__init__("ENTÃO")

        self.insert_alphabet(["E", "N", "T", "Ã", "O"])
        self.insert_starting_state([], ["E"])
        self.insert_new_state([], ["N"])
        self.insert_new_state([], ["T"])
        self.insert_new_state([], ["Ã"])
        self.insert_new_state([], ["O"], final=True)


class SENÃO(AutomatoBase):
    def __init__(self):
        super().__init__("SENÃO")

        self.insert_alphabet(["S", "E", "N", "Ã", "O"])
        self.insert_starting_state([], ["S"])
        self.insert_new_state([], ["E"])
        self.insert_new_state([], ["N"])
        self.insert_new_state([], ["Ã"])
        self.insert_new_state([], ["O"], final=True)


class FIMSE(AutomatoBase):
    def __init__(self):
        super().__init__("FIMSE")

        self.insert_alphabet(["S", "E", "F", "I", "M"])
        self.insert_starting_state([], ["F"])
        self.insert_new_state([], ["I"])
        self.insert_new_state([], ["M"])
        self.insert_new_state([], ["S"])
        self.insert_new_state([], ["E"], final=True)


class ENQUANTO(AutomatoBase):
    def __init__(self):
        super().__init__("ENQUANTO")

        self.insert_alphabet(["E", "N", "Q", "U", "A", "N", "T", "O"])
        self.insert_starting_state([], ["E"])
        self.insert_new_state([], ["N"])
        self.insert_new_state([], ["Q"])
        self.insert_new_state([], ["U"])
        self.insert_new_state([], ["A"])
        self.insert_new_state([], ["N"])
        self.insert_new_state([], ["T"])
        self.insert_new_state([], ["O"], final=True)


class PARA(AutomatoBase):
    def __init__(self):
        super().__init__("PARA")

        self.insert_alphabet(["P", "A", "R"])
        self.insert_starting_state([], ["P"])
        self.insert_new_state([], ["A"])
        self.insert_new_state([], ["R"])
        self.insert_new_state([], ["A"], final=True)


class ATÉ(AutomatoBase):
    def __init__(self):
        super().__init__("ATÉ")

        self.insert_alphabet(["A", "T", "É"])
        self.insert_starting_state([], ["A"])
        self.insert_new_state([], ["T"])
        self.insert_new_state([], ["É"], final=True)


class PASSO(AutomatoBase):
    def __init__(self):
        super().__init__("PASSO")

        self.insert_alphabet(["P", "A", "S", "O"])
        self.insert_starting_state([], ["P"])
        self.insert_new_state([], ["A"])
        self.insert_new_state([], ["S"])
        self.insert_new_state([], ["S"])
        self.insert_new_state([], ["O"], final=True)


class FIMPARA(AutomatoBase):
    def __init__(self):
        super().__init__("FIMPARA")

        self.insert_alphabet(["F", "I", "M", "P", "A", "R"])
        self.insert_starting_state([], ["F"])
        self.insert_new_state([], ["I"])
        self.insert_new_state([], ["M"])
        self.insert_new_state([], ["P"])
        self.insert_new_state([], ["A"])
        self.insert_new_state([], ["R"])
        self.insert_new_state([], ["A"], final=True)


class INICIO(AutomatoBase):
    def __init__(self):
        super().__init__("INICIO")

        self.insert_alphabet(["I", "N", "C", "O"])
        self.insert_starting_state([], ["I"])
        self.insert_new_state([], ["N"])
        self.insert_new_state([], ["I"])
        self.insert_new_state([], ["C"])
        self.insert_new_state([], ["I"])
        self.insert_new_state([], ["O"], final=True)


class FIM(AutomatoBase):
    def __init__(self):
        super().__init__("FIM")

        self.insert_alphabet(["F", "I", "M"])
        self.insert_starting_state([], ["F"])
        self.insert_new_state([], ["I"])
        self.insert_new_state([], ["M"], final=True)


class ESCREVA(AutomatoBase):
    def __init__(self):
        super().__init__("ESCREVA")

        self.insert_alphabet(["E", "S", "C", "R",  "V", "A"])
        self.insert_starting_state([], ["E"])
        self.insert_new_state([], ["S"])
        self.insert_new_state([], ["C"])
        self.insert_new_state([], ["R"])
        self.insert_new_state([], ["E"])
        self.insert_new_state([], ["V"])
        self.insert_new_state([], ["A"], final=True)


class LEIA(AutomatoBase):
    def __init__(self):
        super().__init__("LEIA")

        self.insert_alphabet(["L", "E", "I", "A"])
        self.insert_starting_state([], ["L"])
        self.insert_new_state([], ["E"])
        self.insert_new_state([], ["I"])
        self.insert_new_state([], ["A"], final=True)


class OPMAIS(AutomatoBase):
    def __init__(self):
        super().__init__("OPMAIS")

        self.insert_alphabet(["+"])
        self.insert_starting_state([], ["+"], final=True)


class OPMENOS(AutomatoBase):
    def __init__(self):
        super().__init__("OPMENOS")

        self.insert_alphabet(["-"])
        self.insert_starting_state([], ["-"], final=True)


class OPDIV(AutomatoBase):
    def __init__(self):
        super().__init__("OPDIV")

        self.insert_alphabet(["/"])
        self.insert_starting_state([], ["/"], final=True)


class OPMULT(AutomatoBase):
    def __init__(self):
        super().__init__("OPMULT")

        self.insert_alphabet(["*"])
        self.insert_starting_state([], ["*"], final=True)


class TIPOINT(AutomatoBase):
    def __init__(self):
        super().__init__("TIPOINT")

        self.insert_alphabet([str(n) for n in range(0, 10)])
        self.insert_starting_state([], [str(n) for n in range(0, 10)], final=True)
        self.insert_new_state([str(n) for n in range(0, 10)], [], final=True)


class INTEIRO(AutomatoBase):
    def __init__(self):
        super().__init__("INTEIRO")

        self.insert_alphabet(["I", "N", "T", "E", "R", "O"])
        self.insert_starting_state([], ["I"])
        self.insert_new_state([], ["N"])
        self.insert_new_state([], ["T"])
        self.insert_new_state([], ["E"])
        self.insert_new_state([], ["I"])
        self.insert_new_state([], ["R"])
        self.insert_new_state([], ["O"], final=True)


class ATRIB(AutomatoBase):
    def __init__(self):
        super().__init__("ATRIB")

        self.insert_alphabet([":", "="])
        self.insert_starting_state([], [":"])
        self.insert_new_state([], ["="], final=True)


class PARENA(AutomatoBase):
    def __init__(self):
        super().__init__("PARENA")

        self.insert_alphabet(["("])
        self.insert_starting_state([], ["("], final=True)


class PARENF(AutomatoBase):
    def __init__(self):
        super().__init__("PARENF")

        self.insert_alphabet([")"])
        self.insert_starting_state([], [")"], final=True)


class LOGE(AutomatoBase):
    def __init__(self):
        super().__init__("LOGE")

        self.insert_alphabet(["^"])
        self.insert_starting_state([], ["^"], final=True)


class LOGOU(AutomatoBase):
    def __init__(self):
        super().__init__("LOGOU")

        self.insert_alphabet(["v"])
        self.insert_starting_state([], ["v"], final=True)


class LOGNAO(AutomatoBase):
    def __init__(self):
        super().__init__("LOGNAO")

        self.insert_alphabet(["~"])
        self.insert_starting_state([], ["~"], final=True)


class RELMAIOR(AutomatoBase):
    def __init__(self):
        super().__init__("RELMAIOR")

        self.insert_alphabet([">"])
        self.insert_starting_state([], [">"], final=True)


class RELMENOR(AutomatoBase):
    def __init__(self):
        super().__init__("RELMENOR")

        self.insert_alphabet(["<"])
        self.insert_starting_state([], ["<"], final=True)


class RELMAIORIGUAL(AutomatoBase):
    def __init__(self):
        super().__init__("RELMAIORIGUAL")

        self.insert_alphabet([">", "="])
        self.insert_starting_state([], [">"])
        self.insert_new_state([], ["="], final=True)


class RELMENORIGUAL(AutomatoBase):
    def __init__(self):
        super().__init__("RELMENORIGUAL")

        self.insert_alphabet(["<", "="])
        self.insert_starting_state([], ["<"])
        self.insert_new_state([], ["="], final=True)


class RELIGUAL(AutomatoBase):
    def __init__(self):
        super().__init__("RELIGUAL")

        self.insert_alphabet(["="])
        self.insert_starting_state([], ["="], final=True)


class RELDIFF(AutomatoBase):
    def __init__(self):
        super().__init__("RELDIFF")

        self.insert_alphabet(["~", "="])
        self.insert_starting_state([], ["~"])
        self.insert_new_state([], ["="], final=True)


class PF(AutomatoBase):
    def __init__(self):
        super().__init__("PF")

        self.insert_alphabet(["."])
        self.insert_starting_state([], ["."], final=True)


class VARIAVEL(AutomatoBase):
    def __init__(self):
        super().__init__("VARIAVEL")

        self.insert_alphabet(list(ascii_letters) + [str(n) for n in range(0, 10)])
        self.insert_starting_state([], list(ascii_lowercase), final=True)
        self.insert_new_state(list(ascii_letters) + [str(n) for n in range(0, 10)], [], final=True)


class LITERAL(AutomatoBase):
    def __init__(self):
        super().__init__("LITERAL")
        alphabet = list(ascii_letters) + [str(n) for n in range(0, 10)] + list(punctuation) + list(whitespace)
        self.insert_alphabet(alphabet)
        alphabet.remove('"')
        self.insert_starting_state([], ['"'])
        self.insert_new_state(alphabet, ['"'], final=True)


class ESPACO(AutomatoBase):
    def __init__(self):
        super().__init__("<ESPACO>")
        self.insert_alphabet(list(whitespace))
        self.insert_starting_state([], [' '], final=True)


def get_all_classes():
    return {
        "SENÃO": SENÃO,
        "SE": SE,
        "OPMENOS": OPMENOS,
        "TIPOINT": TIPOINT,
        "INTEIRO": INTEIRO,
        "OPMAIS": OPMAIS,
        "ATRIB": ATRIB,
        "ENTÃO": ENTÃO,
        "FIMSE": FIMSE,
        "ENQUANTO": ENQUANTO,
        "PARA": PARA,
        "ATÉ": ATÉ,
        "PASSO": PASSO,
        "FIMPARA": FIMPARA,
        "ESCREVA": ESCREVA,
        "LEIA": LEIA,
        "OPDIV": OPDIV,
        "OPMULT": OPMULT,
        "PARENF": PARENF,
        "PARENA": PARENA,
        "LOGOU": LOGOU,
        "LOGE": LOGE,
        "LOGNAO": LOGNAO,
        "RELMAIOR": RELMAIOR,
        "RELMENOR": RELMENOR,
        "RELMAIORIGUAL": RELMAIORIGUAL,
        "RELMENORIGUAL": RELMENORIGUAL,
        "RELIGUAL": RELIGUAL,
        "RELDIFF": RELDIFF,
        "PF": PF,
        "VARIAVEL": VARIAVEL,
        "LITERAL": LITERAL,
        "INICIO": INICIO,
        "FIM": FIM,
        "ESPACO": ESPACO,
    }


def token_verify(token):
    allclasses = OrderedDict(get_all_classes())
    for class_name, class_ in allclasses.items():
        if class_().scan_token(token):
            return class_().name
    else:
        raise LexicalError()


def run_automato_with_argv(name, token):
    classes = get_all_classes()

    if name in classes:

        print(classes[name]())
        print(f"AUTOMATO {name} -> {token }\n"
              f"Reconhece: {classes[name]().scan_token(token)}\n\n")
    else:
        print(f"\nAutomato \033[1;31m'{name}'\033[m não existe.\n"
              f"Automatos existentes -> \n" 
              f"{[automato for automato in classes]}\n\n")


if __name__ == '__main__':
    import argparse
    from sys import argv

    parser = argparse.ArgumentParser(description='Verificar se um automato processa o token por linha de comando')

    parser.add_argument('-a', '--automato', action="store", dest="automato", help="Nome do automato. Ex: INTEIRO")
    parser.add_argument('-t', '--token', action="store", dest="token", help="Passe o valor do token a ser verificado")
    parser.add_argument(
        '-l',
        '--listar',
        action='store_true',
        dest="listagem",
        help="Listar os AUTOMATOS disponíveis",
        default=False,
    )
    parser.add_argument(
        '-v',
        '--verificar',
        action='store',
        dest="verificar",
        help="Descobrir qual automato processa o token",
    )

    if len(argv) == 1:
        print("""usage: automato.py [-h] [-a AUTOMATO] [-t TOKEN] [-l] [-v]

                Verificar se um automato processa o token por linha de comando
                
                optional arguments:
                  -h, --help            show this help message and exit
                  -a AUTOMATO, --automato AUTOMATO
                                        Nome do automato. Ex: INTEIRO
                  -t TOKEN, --token TOKEN
                                        Passe o valor do token a ser verificado
                  -l, --listar          Listar os AUTOMATOS disponíveis
                  -v, --verificar       Descobrir qual automato processa o token

                """
              )

    else:
        automato = parser.parse_args().automato
        token = parser.parse_args().token
        listagem = parser.parse_args().listagem
        token_para_veriricar = parser.parse_args().verificar

        if automato or token:
            if (automato and not token) or (not automato and token):
                print("\033[1;32mUSAGE:\033[m")
                print("\tpython automato.py "
                      "-a <AUTOMATO>\033[1;31m(OBRIGATÓRIO)\033[m "
                      "-t <token>\033[1;31m(OBRIGATÓRIO)\033[m")
            else:
                run_automato_with_argv(automato, token)
        elif listagem:
            from pprint import pprint
            print("AUTOMATOS DISPONÍVEIS:")
            pprint([class_ for class_ in get_all_classes()])
        elif token_para_veriricar:
            classes = OrderedDict(get_all_classes())
            for key, class_ in classes.items():
                if class_().scan_token(token_para_veriricar):
                    print(token_para_veriricar, " -> ", f"\033[1;32m{key}\033[m")
                    break
            else:
                print(token_para_veriricar, " -> \033[1;31mNão foi reconhecido\33[m")
