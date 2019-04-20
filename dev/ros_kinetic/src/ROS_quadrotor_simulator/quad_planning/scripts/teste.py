import math
import pyproj
import geonav_transform

wgs84=pyproj.Proj("+init=EPSG:4326") # LatLon with WGS84 datum used by GPS units and Google Earth

#x1, y1 = wgs84(-27.5891397, -48.54069)

project = pyproj.Proj('+proj=merc +ellps=WGS84 +datum=WGS84 +units=m +no_defs')

#project = pyproj.Proj('+proj=utm +zone=22J, +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs')

x1, y1 = project(-27.5891397, -48.54069)

lat, long = project(x1, y1, inverse=True)



print x1, y1
print lat, long


'''
#print calcDist(6.42751474785,8.09074873072,5.32631520265, 6.36056897518, 7.43481324873, 5.03054635012)

def calcDist(x1,y1,z1,x2,y2,z2):
    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    z = (z1 - z2) ** 2

    return math.sqrt(x + y + z)

'''
print "teste"


