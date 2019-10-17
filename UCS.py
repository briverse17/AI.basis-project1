#import matplotlib.pyplot as plt
#from shapely.geometry import Polygon
#import numpy as np

from shapely.geometry import Point, Polygon
from shapely.geometry.polygon import LinearRing
import matplotlib.pyplot as plt

a = [4,1,1,4,4,7,7,4]
a1 = []
for i in range(0, len(a) - 1, 2):
    a1.append((a[i], a[i+1]))

#a = [(4, 4), (5, 9), (8, 10), (9, 5),]
b = [(8, 12), (8, 17), (13, 12)]
#print(a,"\n")

polys = []
#polys.append(Polygon(a))
polys.append(Polygon(a1))
polys.append(Polygon(b))
x,y = polys[0].exterior.xy
c,d = polys[1].exterior.xy
#polygon = Polygon([(4,4),(5,9),(8,10),(9,5),])

linearring = LinearRing(list(polys[0].exterior.coords))
print(linearring)
print(polys[0].contains(Point(4,2)))
#print(polygon.touches(Point(4,4)))
#print(polygon.intersects(Point(5,9)))
#print(linearring.contains(Point(4,4)))
#print(polygon.intersection(linearring))
#x,y = polygon.exterior.xy
plt.plot(x,y)
plt.plot(c,d)
plt.show()