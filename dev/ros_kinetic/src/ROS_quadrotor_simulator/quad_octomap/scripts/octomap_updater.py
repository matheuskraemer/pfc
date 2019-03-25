#!/usr/bin/env python
import rospy
import roslib
from octomap_msgs.msg import Octomap
from moveit_msgs.msg import PlanningSceneWorld, PlanningScene, LinkPadding
from geometry_msgs.msg import Transform, TransformStamped
import tf
mapMsg = PlanningScene()
flag = None

def cb(msg):
    global mapMsg
    global flag

    psw = PlanningSceneWorld()
    psw.octomap.header.stamp = rospy.Time.now()
    psw.octomap.header.frame_id = "world"
    psw.octomap.octomap = msg
    psw.octomap.octomap.header.frame_id = "world"

    psw.octomap.origin.position.x = 0
    psw.octomap.origin.orientation.w = 1

    test = PlanningScene()

    test.world = psw

    mapMsg = test

    flag = 1


def planning_scene(msg):
    #print msg.robot_model_name
    #print msg.fixed_frame_transforms
    #print msg.world.octomap.octomap.header.frame_id
    #print msg.is_diff
    #print msg.robot_state.multi_dof_joint_state.transforms
    pass

rospy.init_node("teste")

rospy.Subscriber("octomap_full", Octomap, cb, queue_size=1)

rospy.Subscriber('move_group/monitored_planning_scene', PlanningScene, planning_scene, queue_size=1)
#move_group/monitored_planning_scene
pub = rospy.Publisher('/planning_scene', PlanningScene, queue_size=1)

r = rospy.Rate(0.25)


listener = tf.TransformListener()
listener.waitForTransform('/base_link', '/world', rospy.Time(), rospy.Duration(4))

while(not rospy.is_shutdown()):

    mapMsg.robot_state.joint_state.header.stamp = rospy.Time.now()
    mapMsg.robot_state.joint_state.header.frame_id = "world"
    mapMsg.robot_state.joint_state.name = ["quad/ground_truth/odometry_sensorgt_joint", "quad/imu_joint",
                                           "quad/imugt_joint", "rotor_0_joint",
                                           "rotor_1_joint", "rotor_2_joint", "rotor_3_joint"]
    mapMsg.robot_state.joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    mapMsg.robot_state.multi_dof_joint_state.header.frame_id = "world"
    mapMsg.robot_state.multi_dof_joint_state.joint_names = ["virtual_joint"]

    mapMsg.robot_model_name = "quad"

    transform_stamped = TransformStamped()
    transform_stamped.header.frame_id = "/world"
    transform_stamped.child_frame_id = "/world"
    transform_stamped.transform.rotation.x = 0
    transform_stamped.transform.rotation.y = 0
    transform_stamped.transform.rotation.z = 0
    transform_stamped.transform.rotation.x = 0
    transform_stamped.transform.rotation.y = 0
    transform_stamped.transform.rotation.z = 0
    transform_stamped.transform.rotation.w = 1

    mapMsg.fixed_frame_transforms = [transform_stamped]

    mapMsg.is_diff = True

    link_padding = list()

    links = ["base_link_inertia"]

    for link in links:
        link_new = LinkPadding()
        link_new.link_name = link
        link_new.padding = 0.5
        link_padding.append(link_new)

    mapMsg.link_padding = link_padding

    if (flag is not None):


        try:
            (trans, rot) = listener.lookupTransform('/world', '/base_link', rospy.Time(0))
            #print (trans, rot)
        except:
            pass

        transform = Transform()
        transform.translation.x = trans[0]
        transform.translation.y = trans[1]
        transform.translation.z = trans[2]

        transform.rotation.x = rot[0]
        transform.rotation.y = rot[1]
        transform.rotation.z = rot[2]
        transform.rotation.w = rot[3]

        #print transform
        mapMsg.robot_state.multi_dof_joint_state.transforms = [transform]

        pub.publish(mapMsg)
        #rospy.signal_shutdown('Quit')
    else:
        pass
    r.sleep()
