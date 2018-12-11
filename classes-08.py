""" Classes and Objects : Everythong is an Object in Py3"""
    


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



p1 = Point(2, 3, 5)
p2 = Point(6, 2, -4)

a = 5
pi = 3.14
text = "Hello World!"


print(type(a))
print(type(pi))
print(type(text))
print(type(print))
print(type(Point))
print(type(type))
print(type(__doc__))



# It's Output is :

"""
<class 'int'>
<class 'float'>
<class 'str'>
<class 'builtin_function_or_method'>
<class 'type'>
<class 'type'>
<class 'str'>
"""
