""" This is a simple programme on Classes
    and Objects : Adding attributes to a class in Py3"""


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

print(p1)
print(p1.x,p1.y,p1.z)
print(p2)
print(p2.x,p2.y,p2.z)


# It's Output is :
# <__main__.Point object at 0x021EA7B0>
# 2 3 5
# <__main__.Point object at 0x0229A650>
# 6 2 -4
