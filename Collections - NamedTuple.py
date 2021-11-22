# Access things by element. Good for large-scaled programming projects
import collections 
from collections import namedtuple


Point = namedtuple("Point", {'x':0,'y':4, 'z':9})

newP = Point(7, 8, 9)

print(newP.x, newP.y, newP.z)
print(newP._replace(y=2, x=6))

p3 = Point._make(['a','b','c'])
print(p3) 