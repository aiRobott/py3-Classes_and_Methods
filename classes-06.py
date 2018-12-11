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


    
print(__doc__)

# It's Output is :
# Classes and Objects : Docstrings (Documentation Strings) in Py3
