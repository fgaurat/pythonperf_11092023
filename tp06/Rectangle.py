


class Rectangle:
    
    _cpt =0 # static

    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle._cpt+=1

    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur
    @longueur.setter
    def longueur(self,longueur):
        self.__longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        self.__largeur = largeur

    @property
    def surface(self):
        return self.__largeur *self.__longueur

    
    @staticmethod
    def get_cpt():
        return Rectangle._cpt
    
    @classmethod
    def build_from_str(cls,value):
        a,b = [int(i) for i in value.split(",")]
        return cls(a,b)

    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=},{self.__longueur=}"

    def __del__(self):
        print("__del__ Rectangle")

    def __eq__(self, __value:object) -> bool:
        return __value.__longueur == self.__longueur and __value.__largeur == self.__largeur 