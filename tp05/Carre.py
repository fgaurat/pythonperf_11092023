from Rectangle import Rectangle

class Carre(Rectangle):

    def __init__(self, cote):
        self.__cote=cote
        super().__init__(cote, cote)

    @property
    def cote(self):
        return self.__cote
    
    @cote.setter
    def cote(self,cote):
        self.longueur = cote 
        self.largeur = cote 
        self.__cote = cote
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__cote=}"

    def __del__(self):
        print("__del__ Carre")

    def __eq__(self, __value:object) -> bool:
        return __value.__cote == self.__cote
