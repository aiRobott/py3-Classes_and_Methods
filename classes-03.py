""" This is a simple programme on Classes
    and Objects : Methods in Py3"""

class Point:
    
    def assign(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def printPoint(self):
        print(self.x, self.y, self.z)


    

p1 = Point()

p1.assign(2,3,5)
p1.printPoint()

p2 = Point()

p2.assign(6,2,-4)
p2.printPoint()



# It's Output is :
# 2 3 5
# 6 2 -4
