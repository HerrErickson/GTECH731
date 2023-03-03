import math as mth
import random

#constructing class
class Geom():
    geomType = 'Generic Geometry Type'
 

    def __init__(self): 
        self.name = random.choice(['Neo','Morpheus','Trinity','Shippeng','Smith',])
        self.color = random.choice(['CHARTREUSE', 'OLIVE', 'EMERALD'])
        
#Properties for shapes to inheret 
    def print_name(self):
        print('My name is ',self.name, 'and my color is ',self.color)

    def makeString(self):
        return f"Name: {self.name}, Color: {self.color}, Area: {self.area()}"