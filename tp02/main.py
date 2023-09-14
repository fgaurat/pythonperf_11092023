


def do_log(prefix=""):
    def wrapper_f(func):
        print("do_log",func)
        def wrapper(*args,**kwargs):
            print(f"{prefix} LOG BEFORE",args,kwargs)
            r = func(*args,**kwargs)
            print(f"{prefix} LOG AFTER",r)
            return r
        return wrapper
    return wrapper_f

@do_log('THELOG')
def say_hello(name):

    return f"Hello {name}"


def main():
    name ="fred"

    h = say_hello(name)


    print(h )


if __name__=='__main__':
    main()
