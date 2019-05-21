#!/usr/bin/env python
# coding: utf-8


class FileError(Exception):
    def __init__(self, file_name):

        self._file_name = file_name
        # Call the base class constructor with the parameters it needs
        self.message = (
            f"\n\n\033[1;31m{file_name}\033[m isn't a *.pup file.\n"
            f"\033[1;32mUSAGE\033[m: pupilo <*.pup> <*.obj>(OPTIONAL)"
        )
        super().__init__(self.message)

    def __call__(self, *args, **kwargs):
        # Calling itself to raise custom error
        raise FileError(self._file_name)


class OutputInvalid(Exception):
    def __init__(self, output_name):

        self.output_name = output_name
        # Call the base class constructor with the parameters it needs
        self.message = (
            f"\n\n\033[1;31m{output_name}\033[m isn't a valid output."
            f"\n\033[1;32mUSAGE\033[m: pupilo <*.pup> <*.obj>(OPTIONAL)"
        )
        super().__init__(self.message)

    def __call__(self, *args, **kwargs):
        # Calling itself to raise custom error
        raise FileError(self.output_name)


class AlphabetNotDefined(Exception):
    def __init__(self):

        self.message = (
            f"\n\n\033[1;31mThe alphabet wasn't defined yet...\033[m"
        )
        super().__init__(self.message)

    def __call__(self, *args, **kwargs):
        # Calling itself to raise custom error
        raise AlphabetNotDefined()


class ItemNotInAlphabet(Exception):
    def __init__(self, item):

        self.item = item

        self.message = (
            f"\n\n\033[1;31mThe '{item}' wasn't defined in the alphabet...\033[m"
        )
        super().__init__(self.message)

    def __call__(self, *args, **kwargs):
        # Calling itself to raise custom error
        raise ItemNotInAlphabet(self.item)

