from DivBy12Error import DivBy12Error

def div(a,b):
    if b ==12:
        raise DivBy12Error()
    return a/b


def call_div(a:int,b:int)->float:
    """Call div function"""
    try:
        print("avant")
        r = div(a,b)

    finally:
        print("après")

    return r



def main():
    try:
        a= 2
        # b=int(input("valeur b : "))
        b = 12
        c=call_div(a,b)

        print(c)
    except ZeroDivisionError as e:
        print('ZeroDivisionError',e)
    except TypeError as e:
        print('TypeError',e)
    except DivBy12Error as e:
        print('DivBy12Error',e)
    else:
        print("OK")

    print("La suite du code")

if __name__=='__main__':
    main()

