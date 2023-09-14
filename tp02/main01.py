def make_incrementor(inc_value,mult=False):
    print(f"create make_incrementor {inc_value=}")
    def inc_function(inc):
        return inc_value+inc

    def mult_function(inc):
        return inc_value*inc
    
    return inc_function,mult_function

def main():
    inc,mult = make_incrementor(10)
    inc2,mult2 = make_incrementor(20)
    v1 = inc(1) # 11
    v2 = inc2(10) # 30

    print(v1)
    print(v2)
if __name__=='__main__':
    main()
