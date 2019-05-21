import sys
sys.path.append("..")
from collections import namedtuple
from errors import AlphabetNotDefined, ItemNotInAlphabet

ESTADO = namedtuple("ESTADO", "estado repeticoes transicao final")


class AutomatoBase:

    def __init__(self, name, scan_token: str = None):
        self.states = []
        self.alphabet = []
        self.control_state = 0
        self.initial = ""
        self.finals = []
        self.name = name

        if scan_token:
            self.scan_token(scan_token)

    def __repr__(self):
        return f"\n\033[1;42m                                                                                 \033[m\n\n"\
               f"\033[1;32mName:\033[m {self.name}\n" \
               f"\033[1;34mStates:\033[m {self.states}\n" \
               f"\033[1;35mInitial State:\033[m {self.initial}\n"\
               f"\033[1;33mFinals States:\033[m {self.finals}\n" \
               f"\n\033[1;42m                                                                                 \033[m\n"

    def __call__(self, *args, **kwargs):
        if "scan_token" in kwargs:
            return self.scan_token(kwargs["scan_token"])
        else:
            return None

    def insert_new_state(self, repeticoes: list, transicao: list, final: bool = False):

        self.all_in_alphabet(set(repeticoes + transicao), raise_error=True)

        if self.control_state == 0:
            self.insert_starting_state(repeticoes, transicao, final)
        else:
            state_name = f"q{self.control_state}"
            self.states.append(ESTADO(state_name, repeticoes, transicao, final))
            self.control_state += 1

            if final:
                self.finals.append(state_name)

    def insert_starting_state(self, repeticoes: list, transicao: list, final: bool = False):
        self.all_in_alphabet(set(repeticoes + transicao), raise_error=True)
        if self.control_state == 0:
            state_name = f"q{self.control_state}"
            self.initial = state_name
            self.states.append(ESTADO(state_name, repeticoes, transicao, final))
            self.control_state += 1
            if final:
                self.finals.append(state_name)
        else:
            print('Estado inicial ja definido')

    def insert_alphabet(self, alphabet):
        self.alphabet = set(alphabet)

    def scan_token(self, token):

        if not self.all_in_alphabet(token):
            return False

        state = 0
        len_token = len(token)

        for tok_position, tok in enumerate(token):
            try:
                actual_state = self.states[state]
            except IndexError:
                return False

            if tok_position == len_token - 1:
                if actual_state.final and (actual_state.transicao != []):
                    if tok in actual_state.transicao:
                        return True
                    elif actual_state.final and tok in actual_state.repeticoes:
                        return True
                    else:
                        return False
                elif actual_state.final and tok in actual_state.repeticoes:
                    return True
                else:
                    return False

            if tok in actual_state.repeticoes:
                continue
            elif tok in actual_state.transicao:
                state += 1
            elif tok not in (set(actual_state.transicao + actual_state.repeticoes)):
                return False

    def all_in_alphabet(self, iterable, raise_error=False):
        if len(self.alphabet) == 0:
            raise AlphabetNotDefined()

        for item in iterable:
            if item not in self.alphabet:
                if raise_error:
                    raise ItemNotInAlphabet(item)
                return False
        return True
