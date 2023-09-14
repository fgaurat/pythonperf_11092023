def add(*l):

    r=0
    for i in l:
        r+=i

    return r



def hello(**kwargs):
    print("Hello",*kwargs.values())
    print("Hello",kwargs['name'])
    print("Hello",kwargs['firstname'])

    for k,v in kwargs.items():
        print(k,v)
    


def truc():
    a = 5
    b=12
    return a,b

def mult2(l):

    l2 = []

    for v in l:
        l2.append(v*2)
    return l2


def mult2item(i):
    return i*2


def main():
    l = [10,20,30]

    # r = add(l) # 60    
    # r = add(10,20,30,40) # 60    
    
    # print(r)


    a,b,c = l
    print(*l)
    print(l)
    hello(firstname="Frédéric",name="GAURAT")


    d =  {
        "key1":"value1",
        "key2":"value2",
        "key3":"value3",
    }

    print(list(d))

    print(50*'-')

    a,b = 1,2
    a,b =truc()
    print(50*'-')
    l = [10,20,30]
    l2 = mult2(l)
    l2 = list(map(mult2item,l))
    print(l2) # [20,40,60]
    l2 = list(map(lambda i:i*2,l))
    l2 = [i*2 for i in l]

    l3 = ["  ligne01   ","ligne02   ","   ligne03"]
    l3 = [s.strip() for s in l3]
    print(l3)

if __name__=='__main__':
    main()
