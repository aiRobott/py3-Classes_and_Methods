""" Classes and Objects : Docstrings (Documentation Strings) in Py3
    This is an example for multi-line docstring  """


class Point:
    """This is a docstring for class Point
       This class defines a Point in 3 dimensional space """

    
    def __init__(self, x, y, z):
        """This is initializer method for class Point
            This method calls the assign() method of this class """
        self.assign(x, y, z)

                    
    def assign(self, x, y, z):
        'This method assigns the values to the co-ordinates of Point'
        self.x = x
        self.y = y
        self.z = z
        

    def printPoint(self):
        'This method prints the values of the co-ordinates of Point'
        print(self.x, self.y, self.z)


print(__doc__)
p1 = Point(0, 0, 0)
print(p1.__doc__)


# It's Output is :

"""
Classes and Objects : Docstrings (Documentation Strings) in Py3
    This is an example for multi-line docstring  
This is a docstring for class Point
       This class defines a Point in 3 dimensional space 
"""
