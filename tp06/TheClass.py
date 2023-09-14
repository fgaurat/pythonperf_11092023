from typing import Any


class TheClass:


    def __new__(cls):
        print("def __new__(cls) -> Self")
        return super(TheClass,cls).__new__(cls)
    
    def __init__(self) -> None:
        print("def __init__(self)")


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__")


def main():
    obj= TheClass()

    obj()

if __name__=='__main__':
    main()


