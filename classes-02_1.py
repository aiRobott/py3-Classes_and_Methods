""" This is a simple programme on Classes
    and Objects : Adding attributes to a class in Py3"""

class test1:
    pass

class Point:
    pass

p1 = Point()
p1.x = 2
p1.y = 3
p1.z = 5

p2 = Point()
p2.x = 6
p2.y = 2
p2.z = -4

#print(p1)
#print(p1.x,p1.y,p1.z)
#print(p2)
#print(p2.x,p2.y,p2.z)

t1 = test1()
t1.test1 = "Hello World!"

print(t1.test1)

t1.var1 = 3.14
print(t1.var1)


# It's Output is :
# Hello World!
# 3.14
