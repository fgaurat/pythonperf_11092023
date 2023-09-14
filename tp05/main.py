from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from IMetaCalcGeo import IMetaCalcGeo



def show_surface(o:IMetaCalcGeo):
    print(o.surface)


def main():
    c = Carre(3)
    ce = Cercle(3)
    print(c)
    print(c.surface)

    c.cote = 4
    print(ce.surface)
    show_surface(c)
    show_surface(ce)


if __name__=='__main__':
    main()
