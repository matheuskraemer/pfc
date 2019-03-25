#!/usr/bin/env python
import rospy
from octomap_msgs.msg import Octomap
from moveit_msgs.msg import PlanningSceneWorld, PlanningScene

mapMsg = None

def cb(msg):
    global mapMsg

    psw = PlanningSceneWorld()
    psw.octomap.header.stamp = rospy.Time.now()
    psw.octomap.header.frame_id = "map"
    psw.octomap.octomap = msg

    psw.octomap.origin.position.x = 0
    psw.octomap.origin.orientation.w = 1

    test = PlanningScene()

    test.world = psw


    mapMsg = test


rospy.init_node("teste")

rospy.Subscriber("octomap_full", Octomap, cb, queue_size=1)

pub = rospy.Publisher('move_group/monitored_planning_scene', PlanningScene, queue_size=1)

r = rospy.Rate(0.25)


while(not rospy.is_shutdown()):

    if (mapMsg is not None):
        pub.publish(mapMsg)
        rospy.signal_shutdown('Quit')
    else:
        pass
        r.sleep()
