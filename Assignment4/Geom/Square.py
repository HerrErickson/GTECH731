from .Geom import Geom
import math as mth

class Square(Geom):
    def __init__ (self,side):
        self.side = side
        super().__init__()
    def area(self):
        return self.side ** 2   