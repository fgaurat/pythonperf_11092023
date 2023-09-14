

from abc import ABCMeta,abstractmethod 




class IMetaCalcGeo(metaclass=ABCMeta):

    @property
    @abstractmethod
    def surface(self):
        pass