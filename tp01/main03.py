from collections import deque

def main():
    l=[10,20,30]

    # l.insert(0,0)
    print(l)
    last_value = l.pop()
    print(last_value)

    d = deque(l)
    d.appendleft(0)
    print(d)

if __name__=='__main__':
    main()
