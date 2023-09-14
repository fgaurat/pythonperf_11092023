from Rectangle import Rectangle
from ICalcGeo import ICalcGeo
from IMetaCalcGeo import IMetaCalcGeo
import math
class Cercle(IMetaCalcGeo):

    def __init__(self, rayon):
        self.__rayon=rayon

    @property
    def rayon(self):
        return self.__rayon
    
    @rayon.setter
    def rayon(self,rayon):
        self.longueur = rayon 
        self.largeur = rayon 
        self.__rayon = rayon
    
    @property
    def surface(self):
        return math.pi*self.__rayon**2
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__rayon=}"

    def __del__(self):
        print("__del__ Cercle")

    def __eq__(self, __value:object) -> bool:
        return __value.__rayon == self.__rayon
