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
#print(help(p1))

print(p1.assign.__doc__)
print(help(p1.assign))


# It's Output is :

"""
This method assigns the values to the co-ordinates of Point
Help on method assign in module __main__:

assign(x, y, z) method of __main__.Point instance
    This method assigns the values to the co-ordinates of Point

None
"""
