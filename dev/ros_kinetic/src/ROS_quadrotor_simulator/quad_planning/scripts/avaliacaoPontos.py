import pyproj
import math
import copy
project = pyproj.Proj('+proj=utm +zone=23J +datum=WGS84 +units=m +no_defs')
import geonav_transform.geonav_conversions as gc
reload(gc)

olat = -27.605003
olon = -48.519530

x0, y0 = project(olat, olon)

#enviados
enviados = [[-27.6050030098, -48.5195299906, 2.01425293983],
            [-27.6050191158, -48.5195134094, 2.01475906577],
            [-27.6050443355, -48.5195166385, 2.01541081051],
            [-27.6050389567, -48.5195767868, 2.01446971725],
            [-27.6049986173, -48.5195660681, 2.01565377887]]

recebidos = [[-27.6050038655, -48.519523064, 2.29999995232],
             [-27.6050233768, -48.5195091899, 2.29999995232],
             [-27.6050509603, -48.5195175906, 2.20000004768],
             [-27.6050357309, -48.5195801182, 2.79999995232],
             [-27.604992714, -48.5195650491, 2.59999990463]]


print "pontos enviados"
for enviado in enviados:
    print enviado
enviados_utm_corrigido = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(enviados)):
    x, y = gc.ll2xy(enviados[i][0],enviados[i][1], olat, olon)
    enviados_utm_corrigido[i][0] = x
    enviados_utm_corrigido[i][1] = y
    enviados_utm_corrigido[i][2] = enviados[i][2]
    print enviados_utm_corrigido[i]
print "--------------------"

print "pontos recebidos"
for recebido in recebidos:
    print recebido

recebidos_utm_corrigido = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(recebidos)):
    x, y = gc.ll2xy(recebidos[i][0],recebidos[i][1], olat, olon)
    recebidos_utm_corrigido[i][0] = x
    recebidos_utm_corrigido[i][1] = y
    recebidos_utm_corrigido[i][2] = recebidos[i][2]
    print recebidos_utm_corrigido[i]
print "--------------------"


enviados_utm = copy.copy(enviados)

recebidos_utm = copy.copy(recebidos)




for i in range(len(enviados)):
    enviados_utm[i][0], enviados_utm[i][1] = project(enviados[i][0], enviados[i][1])

    recebidos_utm[i][0], recebidos_utm[i][1] = project(recebidos[i][0], recebidos[i][1])


print "pontos enviados"
for enviado in enviados_utm:
    print enviado
print "pontos recebidos"
for recebido in recebidos_utm:
    print recebido
print "--------------------"




distancias = list()
distancias_x = list()
distancias_y = list()
distancias_z = list()
distancias_xy = list()

for i in range(len(enviados)):
    diff_x = abs(enviados_utm_corrigido[i][0] - recebidos_utm_corrigido[i][0])
    diff_y = abs(enviados_utm_corrigido[i][1] - recebidos_utm_corrigido[i][1])
    diff_z = abs(enviados_utm_corrigido[i][2] - recebidos_utm_corrigido[i][2])

    distancias.append(math.sqrt(diff_x*diff_x + diff_y*diff_y + diff_z*diff_z))
    distancias_xy.append(math.sqrt(diff_x*diff_x + diff_y*diff_y))
    distancias_x.append(diff_x)
    distancias_y.append(diff_y)
    distancias_z.append(diff_z)


for idx, dist in enumerate(distancias):
    print "Distancia xyz " +str(idx) + " :", dist
print "--------------------"


for idx, dist in enumerate(distancias_xy):
    print "Distancia xy " +str(idx) + " :", dist
print "--------------------"

for idx, dist in enumerate(distancias_x):
    print "Distancia x " +str(idx) + " :", dist
print "--------------------"

for idx, dist in enumerate(distancias_y):
    print "Distancia y " +str(idx) + " :", dist
print "--------------------"

for idx, dist in enumerate(distancias_z):
    print "Distancia z " +str(idx) + " :", dist
print "--------------------"

















