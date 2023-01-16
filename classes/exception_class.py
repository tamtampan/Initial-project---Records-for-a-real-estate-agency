class InputNotValid(Exception):
    def __init__(self, message):
        super().__init__(message)


class InputNotDigit(InputNotValid):
    def __init__(self):
        super().__init__("Input not digit.")
