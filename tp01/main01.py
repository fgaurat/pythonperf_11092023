import  mon_module
import copy

from pprint import pprint


def main():
    a=3
    print(hex(id(a)))
    b=1
    c=1
    print(hex(id(b)))
    print(hex(id(c)))


    print(50*'-')
    l=[10,20,30,40,50]
    # l1=copy.copy(l)
    # l1=l.copy()
    l2 = l[2:4]
    l2 = l[2:]
    l_all = l[:]
    l[0]=1000
    print(l)
    print(l2)

    print(50*'-')
    l3 = [
        [10,20],
        [30,40],
        [50,60],
    ]

    l4 = copy.deepcopy(l3)
    l3[1][1] = 4000

    print(l3)
    print(l4)


if __name__=='__main__':
    main()


    