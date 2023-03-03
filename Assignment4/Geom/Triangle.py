from .Geom import Geom
import math as mth

class Triangle(Geom):
    def __init__ (self,height):
        self.height = height
        super().__init__()
    def __init__ (self,base):
        self.base = base
        super().__init__()
    def __init__ (self,side):
        self.side = base * height
        super().__init__()
    def area(self):
        return self.side * 0.5 