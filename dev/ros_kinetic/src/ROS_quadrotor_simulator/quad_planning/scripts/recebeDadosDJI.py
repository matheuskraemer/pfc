#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovariance

taxa = 10
i = 0
def resultCallback(msg):
    global i, taxa

    i += 1

    if i == taxa:
        i = 0
        print msg


rospy.init_node("current_position_reader")

rospy.Subscriber("/dji/current_pose", PoseWithCovariance, resultCallback, queue_size=10)

rate_points = rospy.Rate(5)

while(not rospy.is_shutdown()):
    rate_points.sleep()