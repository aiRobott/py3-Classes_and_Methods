'Classes and Objects : Docstrings (Documentation Strings) in Py3'


class Point:
    'This is a docstring for class Point'

    
    def __init__(self, x, y, z):
        'This is initializer method for class Point'
        self.assign(x, y, z)

                    
    def assign(self, x, y, z):
        'This method assigns the values to the co-ordinates of Point'
        self.x = x
        self.y = y
        self.z = z
        

    def printPoint(self):
        'This method prints the values of the co-ordinates of Point'
        print(self.x, self.y, self.z)

p1 = Point(0, 0, 0)
print(help(p1))




# It's Output is :

"""
Help on Point in module __main__ object:

class Point(builtins.object)
 |  This is a docstring for class Point
 |  
 |  Methods defined here:
 |  
 |  __init__(self, x, y, z)
 |      This is initializer method for class Point
 |  
 |  assign(self, x, y, z)
 |      This method assigns the values to the co-ordinates of Point
 |  
 |  printPoint(self)
 |      This method prints the values of the co-ordinates of Point
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

None
"""
