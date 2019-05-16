#!/usr/bin/env python

import pickle
import sys
from tf.transformations import euler_from_quaternion
import math

#read the file to get all the positions
with open(sys.argv[1], "r") as f:
    dump = pickle.load(f)

print "x","y","z","orientacao"
for ponto in dump:

    translation = ponto[0].multi_dof_joint_state.transforms[0].translation
    rotation = ponto[0].multi_dof_joint_state.transforms[0].rotation

    rpy = euler_from_quaternion(
        [rotation.x, rotation.y, rotation.z,
         rotation.w])

    #print [rotation.x, rotation.y, rotation.z, rotation.w]

    degree = round(90 - math.degrees(rpy[2]))

    if abs(round(90-math.degrees(rpy[2]))) > 180:
        if degree<0:
            degree += 360
        else:
            degree -= 360

    orientacao = degree


    print translation.x, translation.y, translation.z, degree