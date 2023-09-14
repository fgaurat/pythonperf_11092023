

class DivBy12Error(Exception):

    def __init__(self) -> None:
        super().__init__("Division /12")