from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    r = Rectangle(3,2)
    r1 = Rectangle(3,2)
    dr = DataRectangle(12)
    print(dr.largeur) 
    print(dr.longueur) 
    # print(r.get_longueur()) #3
    # print(r.get_largeur()) #2
    # print(r.get_surface()) #6
    # print("_largeur",r._Rectangle__largeur)

    print(r)
    if r==r1:
        print("ok")
    else:
        print("ko")
    
    
    r.longueur = 12
    print(r.longueur)
    print(r.surface)
if __name__=='__main__':
    main()
