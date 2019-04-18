#!/usr/bin/env python

import rospy
from time import sleep
import pickle
import sys
from moveit_msgs.msg import MoveGroupActionGoal, Constraints, JointConstraint, MoveGroupAction, MoveGroupGoal, PlanningSceneComponents, MoveGroupResult, MoveGroupActionResult
from moveit_msgs.srv import GetPlanningScene
import actionlib
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovariance, Quaternion
from tf.transformations import euler_from_quaternion
import math

# Import geonav tranformation module
import geonav_transform.geonav_conversions as gc
reload(gc)
# Import AlvinXY transformation module
import alvinxy.alvinxy as axy
reload(axy)

#topic to write the dji commands
dji_command = rospy.Publisher("dji/command", String, queue_size=1)

olat = -27.5891397
olon = -48.54069

'''
x_s = 24
y_s = 80
z_s = 20
x_c = 9
y_c = 22
z_c = 10
'''

x_off = 5
y_off = 5
z_off = 5

flag = 0
flag_dji = 0
flag_dji_adaptative = 0
started = 0
uploaded = 0
configured = 0
cleared = 0


#read the file to get all the positions
with open(sys.argv[1], "r") as f:
    dump = pickle.load(f)

#initialization of the node
rospy.init_node("planning_calculator")


#action lib to communicate with the move_group
client = actionlib.SimpleActionClient('/move_group', MoveGroupAction)
client.wait_for_server()

#service to get the initial state
getPlanningScene = rospy.ServiceProxy("/get_planning_scene", GetPlanningScene)
getPlanningScene.wait_for_service()


#topic to write the dji trajectory messages
dji_traj_pub = rospy.Publisher("/dji/waypoint", PoseWithCovariance, queue_size=10)

#set loop execution rate at 1 Hz
r = rospy.Rate(1)

rate_points = rospy.Rate(5)


#get the currently DRONE currently position
components = PlanningSceneComponents()
components.components = 2
robot_state = getPlanningScene(components).scene.robot_state


'''
print dump[0]               
if robot_state.multi_dof_joint_state.transforms[0].translation.x == dump[0][0].multi_dof_joint_state.transforms[0].translation.x \
        and robot_state.multi_dof_joint_state.transforms[0].translation.y == dump[0].multi_dof_joint_state.transforms[0].translation.y\
        and robot_state.multi_dof_joint_state.transforms[0].translation.z == dump[0].multi_dof_joint_state.transforms[0].translation.z\
        and robot_state.multi_dof_joint_state.transforms[0].orientation.x == dump[0].multi_dof_joint_state.transforms[0].orientation.x\
        and robot_state.multi_dof_joint_state.transforms[0].orientation.y == dump[0].multi_dof_joint_state.transforms[0].orientation.y\
        and robot_state.multi_dof_joint_state.transforms[0].orientation.z == dump[0].multi_dof_joint_state.transforms[0].orientation.z\
        and robot_state.multi_dof_joint_state.transforms[0].orientation.w == dump[0].multi_dof_joint_state.transforms[0].orientation.w:
    pass
else:

'''
dump.insert(0, [robot_state, 0])


def DJICallback(msg):
    print msg
    global flag_dji, flag_dji_adaptative, configured, started, uploaded, cleared

    if msg.data == "chegou":
        flag_dji = 1

    if msg.data == "configured":
        configured = 1

    if msg.data == "uploaded":
        uploaded = 1

    if msg.data == "started":
        started = 1

    if msg.data == "cleared":
        cleared = 1

    flag_dji_adaptative = 1

#get the pathplanning results
rospy.Subscriber("/dji/status", String, DJICallback, queue_size=10)


def calcDist(point1, point2):
    x = (point1.transforms[0].translation.x - point2.transforms[0].translation.x) ** 2
    y = (point1.transforms[0].translation.y - point2.transforms[0].translation.y) ** 2
    z = (point1.transforms[0].translation.z - point2.transforms[0].translation.z) ** 2

    d = math.sqrt(x + y + z)

    return d

ponto_ultimo = None
def resultCallback(msg):

    global olat, olon, cleared, started, uploaded, configured, flag_dji, ponto_ultimo

    # logica de limpeza de pontos antigos
    print "Limpando pontos antigos..."
    dji_command.publish("clear")
    while cleared == 0:
        r.sleep()

    cleared = 0

    sleep(5)


    points = msg.result.planned_trajectory.multi_dof_joint_trajectory.points

    points_filtered = list()

    points_filtered.append(points[0])

    #points = points[1:]

    ultimo = False
    distancia = 0
    for i in range(len(points) - 1):
        distancia += calcDist(points[i], points[i+1])

        if distancia > 0.8:
            distancia = 0
            points_filtered.append(points[i + 1])
            if i + 1 == (len(points)-1):
                ultimo = True


    if (not ultimo):
        points_filtered[len(points_filtered) - 1] = points[len(points) - 1]
        pass

    #points_filtered = points_filtered[1:]

    i = 0

    #for i in range(len(points_filtered) - 1):
    #    print calcDist(points_filtered[i], points_filtered[i+1])


    print "Manda trajetoria"
    #points_filtered = points_filtered[8:]
    for point in points_filtered: #msg.result.planned_trajectory.multi_dof_joint_trajectory.points:
        waypoint = PoseWithCovariance()

        '''
        waypoint.pose.position.x = point.transforms[0].translation.x
        waypoint.pose.position.y = point.transforms[0].translation.y
        waypoint.pose.position.z = point.transforms[0].translation.z

        waypoint.pose.orientation.x = point.transforms[0].rotation.x
        waypoint.pose.orientation.y = point.transforms[0].rotation.y
        waypoint.pose.orientation.z = point.transforms[0].rotation.z
        waypoint.pose.orientation.w = point.transforms[0].rotation.w

        '''

        #x/y to lat/long conversion
        #lat, lon = gc.xy2ll(point.transforms[0].translation.x, point.transforms[0].translation.y, olat, olon)

        lat, lon = axy.xy2ll(point.transforms[0].translation.x, point.transforms[0].translation.y, olat, olon)

        #calculation of rpy angles
        rpy = euler_from_quaternion([point.transforms[0].rotation.x,point.transforms[0].rotation.y,point.transforms[0].rotation.z,point.transforms[0].rotation.w])

        #print point.transforms[0].translation.x
        #print point.transforms[0].translation.y
        #print point.transforms[0].translation.z
        #print "---------------------------------------------"

        waypoint.pose.position.x = lat
        waypoint.pose.position.y = lon
        waypoint.pose.position.z = point.transforms[0].translation.z

        waypoint.pose.orientation.x = point.transforms[0].rotation.x
        waypoint.pose.orientation.y = point.transforms[0].rotation.y
        waypoint.pose.orientation.z = point.transforms[0].rotation.z
        waypoint.pose.orientation.w = round(math.degrees(rpy[2]))

        dji_traj_pub.publish(waypoint)

        i += 1
        rate_points.sleep()

    #print len(points_filtered)

    sleep(1)
    #logica de controle#


    rate_points.sleep()
    if len(points_filtered) <= 1:

        print "Esta na posicao"
        flag_dji = 1

    else:

        # logica de configuracao dos pontos
        print "Configurando..."
        dji_command.publish("config")
        while configured == 0:
            r.sleep()

        configured = 0

        sleep(1)

        # logica de upload
        print "Uploading..."
        dji_command.publish("upload")
        while uploaded == 0:
            r.sleep()

        uploaded = 0

        sleep(1)

        # logica de start mission
        print "Mission Start..."
        dji_command.publish("start")
        while started == 0:
            r.sleep()

        started = 0
        sleep(1)
        print "Comecou!"



#get the pathplanning results
rospy.Subscriber("/move_group/result", MoveGroupResult, resultCallback, queue_size=10)


#send goal
def send_goal(current, goal):
    global flag_dji

    goal_msg = MoveGroupActionGoal()

    goal_msg.goal_id = "teste"



    goal_msg.goal.request.start_state.joint_state.header.frame_id = "/world"
    goal_msg.goal.request.start_state.joint_state.name = ["quad/ground_truth/odometry_sensorgt_joint", "quad/imu_joint",
                                                          "quad/imugt_joint", "rotor_0_joint",
                                                          "rotor_1_joint", "rotor_2_joint", "rotor_3_joint"]
    goal_msg.goal.request.start_state.joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    goal_msg.goal.request.start_state.multi_dof_joint_state = current.multi_dof_joint_state

    trans_x = JointConstraint()
    trans_y = JointConstraint()
    trans_z = JointConstraint()
    rot_x = JointConstraint()
    rot_y = JointConstraint()
    rot_z = JointConstraint()
    rot_w = JointConstraint()

    trans_x.weight = 1
    trans_x.weight = 1
    trans_x.tolerance_above = 0.0001
    trans_x.tolerance_below = 0.0001
    trans_x.position = goal.multi_dof_joint_state.transforms[0].translation.x
    trans_x.joint_name = "virtual_joint/trans_x"

    trans_y.weight = 1
    trans_y.tolerance_above = 0.0001
    trans_y.tolerance_below = 0.0001
    trans_y.position = goal.multi_dof_joint_state.transforms[0].translation.y
    trans_y.joint_name = "virtual_joint/trans_y"

    trans_z.weight = 1
    trans_z.tolerance_above = 0.0001
    trans_z.tolerance_below = 0.0001
    trans_z.position = goal.multi_dof_joint_state.transforms[0].translation.z
    trans_z.joint_name = "virtual_joint/trans_z"

    rot_x.weight = 1
    rot_x.tolerance_above = 0.0001
    rot_x.tolerance_below = 0.0001
    rot_x.position = goal.multi_dof_joint_state.transforms[0].rotation.x
    rot_x.joint_name = "virtual_joint/rot_x"

    rot_y.weight = 1
    rot_y.tolerance_above = 0.0001
    rot_y.tolerance_below = 0.0001
    rot_y.position = goal.multi_dof_joint_state.transforms[0].rotation.y
    rot_y.joint_name = "virtual_joint/rot_y"

    rot_z.weight = 1
    rot_z.tolerance_above = 0.0001
    rot_z.tolerance_below = 0.0001
    rot_z.position = goal.multi_dof_joint_state.transforms[0].rotation.z
    rot_z.joint_name = "virtual_joint/rot_z"

    rot_w.weight = 1
    rot_w.tolerance_above = 0.0001
    rot_w.tolerance_below = 0.0001
    rot_w.position = goal.multi_dof_joint_state.transforms[0].rotation.w
    rot_w.joint_name = "virtual_joint/rot_w"

    join_constrains_list = list()
    join_constrains_list.append(trans_x)
    join_constrains_list.append(trans_y)
    join_constrains_list.append(trans_z)
    join_constrains_list.append(rot_x)
    join_constrains_list.append(rot_y)
    join_constrains_list.append(rot_z)
    join_constrains_list.append(rot_w)

    goal_constrains = Constraints()
    goal_constrains.name = ""

    goal_constrains.joint_constraints = join_constrains_list

    goal_msg.goal.request.goal_constraints = [goal_constrains]

    goal_msg.goal.request.group_name = "Quad_base"
    goal_msg.goal.request.num_planning_attempts = 10
    goal_msg.goal.request.allowed_planning_time = 5
    goal_msg.goal.request.max_velocity_scaling_factor = 1
    goal_msg.goal.request.max_acceleration_scaling_factor = 1

    goal_msg.goal.planning_options.planning_scene_diff.is_diff = False

    goal_msg.goal.planning_options.plan_only = True
    goal_msg.goal.planning_options.look_around = False
    goal_msg.goal.planning_options.replan = False


    x_c = current.multi_dof_joint_state.transforms[0].translation.x + (goal.multi_dof_joint_state.transforms[0].translation.x - current.multi_dof_joint_state.transforms[0].translation.x)/2
    y_c = current.multi_dof_joint_state.transforms[0].translation.y + (goal.multi_dof_joint_state.transforms[0].translation.y - current.multi_dof_joint_state.transforms[0].translation.y)/2
    z_c = current.multi_dof_joint_state.transforms[0].translation.z + (goal.multi_dof_joint_state.transforms[0].translation.z - current.multi_dof_joint_state.transforms[0].translation.z)/2

    diff_x = abs(goal.multi_dof_joint_state.transforms[0].translation.x - current.multi_dof_joint_state.transforms[0].translation.x)
    diff_y = abs(goal.multi_dof_joint_state.transforms[0].translation.y - current.multi_dof_joint_state.transforms[0].translation.y)
    diff_z = abs(goal.multi_dof_joint_state.transforms[0].translation.z - current.multi_dof_joint_state.transforms[0].translation.z)

    goal_msg.goal.request.workspace_parameters.header.frame_id = "/world"
    goal_msg.goal.request.workspace_parameters.min_corner.x = x_c - (diff_x / 2) - x_off # -30
    goal_msg.goal.request.workspace_parameters.min_corner.y = y_c - (diff_y / 2) - y_off # -30
    goal_msg.goal.request.workspace_parameters.min_corner.z = 0 # z_c - (diff_z / 2) - z_off # -30
    goal_msg.goal.request.workspace_parameters.max_corner.x = x_c + (diff_x / 2) + x_off # 30
    goal_msg.goal.request.workspace_parameters.max_corner.y = y_c + (diff_y / 2) + y_off # 30
    goal_msg.goal.request.workspace_parameters.max_corner.z = z_c + (diff_z / 2) + z_off # 30

    '''
    
    print x_c
    print y_c
    print z_c

    print diff_x
    print diff_y
    print diff_z
    print goal_msg.goal.request.workspace_parameters
    '''

    '''
    goal_msg.goal.request.workspace_parameters.header.frame_id = "/world"
    goal_msg.goal.request.workspace_parameters.min_corner.x = x_c - (x_s / 2)  # -30
    goal_msg.goal.request.workspace_parameters.min_corner.y = y_c - (y_s / 2)  # -30
    goal_msg.goal.request.workspace_parameters.min_corner.z = z_c - (z_s / 2)  # -30
    goal_msg.goal.request.workspace_parameters.max_corner.x = (x_s / 2) + x_c  # 30
    goal_msg.goal.request.workspace_parameters.max_corner.y = (y_s / 2) + y_c  # 30
    goal_msg.goal.request.workspace_parameters.max_corner.z = (z_s / 2) + z_c  # 30
    '''
    print "Planejando e simulando"
    # print goal_msg.goal
    action = MoveGroupGoal
    action = goal_msg.goal

    client.send_goal(action)
    client.wait_for_result()
    print "Enviou posicao:"
    print "Aguardando...:"
    flag_dji = 0
    while (flag_dji == 0):
        r.sleep()

    flag_dji = 0

    print "Chegou!"
    print "-----------------"


print("Pronto para executar " + str(len(dump)) + " posicoes")





#main

for i in range(1, len(dump)): #len(dump)):

    current = dump[i - 1]
    goal = dump[i]

    if (i==1 or goal[1] <= current[1] and goal[1] != -9999 and current[1]!=-9999):
        send_goal(current[0], goal[0])

    elif (current[1] == -9999):
        print "Ignorando ponto intermediario"
        pass

    else:
        print "Aguardando resultado para rota adaptativa"
        #flag_dji_adaptative = input("flag:")
        while (flag_dji_adaptative == 0):
            r.sleep()

        if (flag_dji_adaptative == 1):
            print "Seguinto para proximo ponto da rota"
            #nao realizar rota adaptativa
            flag_dji_adaptative = 0
            for pos in dump[i:]:
                if pos[1] == current[1]:
                    goal = pos
                    send_goal(current[0], goal[0])
                    break
                else:
                    pos[1] = -9999

        if (flag_dji_adaptative == -1):
            print "Executando rota adaptativa"
            #realizar rota adaptativa
            flag_dji_adaptative = 0
            send_goal(current[0], goal[0])


#while (not rospy.is_shutdown()):
#    r.sleep()


'''
moveit_msgs/MoveGroupActionGoal
goal do planejamento

/move_group/goal

header: 
  seq: 4
  stamp: 
    secs: 14467
    nsecs: 987000000
  frame_id: ''
goal_id: 
  stamp: 
    secs: 14467
    nsecs: 987000000
  id: "/rviz-6-14467.987000000"
goal: 
  request: 
    workspace_parameters: 
      header: 
        seq: 0
        stamp: 
          secs: 14467
          nsecs: 987000000
        frame_id: "/world"
      min_corner: 
        x: -2500.0
        y: -2500.0
        z: -2498.5
      max_corner: 
        x: 2500.0
        y: 2500.0
        z: 2501.5
    start_state: 
      joint_state: 
        header: 
          seq: 0
          stamp: 
            secs: 0
            nsecs:         0
          frame_id: "/world"
        name: [quad/ground_truth/odometry_sensorgt_joint, quad/imu_joint, quad/imugt_joint, rotor_0_joint,
  rotor_1_joint, rotor_2_joint, rotor_3_joint]
        position: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        velocity: []
        effort: []
      multi_dof_joint_state: 
        header: 
          seq: 0
          stamp: 
            secs: 0
            nsecs:         0
          frame_id: "/world"
        joint_names: [virtual_joint]
        transforms: 
          - 
            translation: 
              x: 7.72063572316
              y: 22.8573214722
              z: 5.70284690308
            rotation: 
              x: 9.75699995794e-05
              y: -4.29775396294e-05
              z: 0.522011278109
              w: 0.852938575842
        twist: []
        wrench: []
      attached_collision_objects: []
      is_diff: False
    goal_constraints: 
      - 
        name: ''
        joint_constraints: 
          - 
            joint_name: "virtual_joint/trans_x"
            position: -0.97068554163
            tolerance_above: 0.0001
            tolerance_below: 0.0001
            weight: 1.0
          - 
            joint_name: "virtual_joint/trans_y"
            position: 9.31223392487
            tolerance_above: 0.0001
            tolerance_below: 0.0001
            weight: 1.0
          - 
            joint_name: "virtual_joint/trans_z"
            position: 7.297955513
            tolerance_above: 0.0001
            tolerance_below: 0.0001
            weight: 1.0
          - 
            joint_name: "virtual_joint/rot_x"
            position: 5.76210401719e-13
            tolerance_above: 0.0001
            tolerance_below: 0.0001
            weight: 1.0
          - 
            joint_name: "virtual_joint/rot_y"
            position: -2.38880330584e-12
            tolerance_above: 0.0001
            tolerance_below: 0.0001
            weight: 1.0
          - 
            joint_name: "virtual_joint/rot_z"
            position: 0.688921439457
            tolerance_above: 0.0001
            tolerance_below: 0.0001
            weight: 1.0
          - 
            joint_name: "virtual_joint/rot_w"
            position: 0.724836004603
            tolerance_above: 0.0001
            tolerance_below: 0.0001
            weight: 1.0
        position_constraints: []
        orientation_constraints: []
        visibility_constraints: []
    path_constraints: 
      name: ''
      joint_constraints: []
      position_constraints: []
      orientation_constraints: []
      visibility_constraints: []
    trajectory_constraints: 
      constraints: []
    planner_id: ''
    group_name: "Quad_base"
    num_planning_attempts: 10
    allowed_planning_time: 5.0
    max_velocity_scaling_factor: 1.0
    max_acceleration_scaling_factor: 1.0
  planning_options: 
    planning_scene_diff: 
      name: ''
      robot_state: 
        joint_state: 
          header: 
            seq: 0
            stamp: 
              secs: 0
              nsecs:         0
            frame_id: ''
          name: []
          position: []
          velocity: []
          effort: []
        multi_dof_joint_state: 
          header: 
            seq: 0
            stamp: 
              secs: 0
              nsecs:         0
            frame_id: ''
          joint_names: []
          transforms: []
          twist: []
          wrench: []
        attached_collision_objects: []
        is_diff: True
      robot_model_name: ''
      fixed_frame_transforms: []
      allowed_collision_matrix: 
        entry_names: []
        entry_values: []
        default_entry_names: []
        default_entry_values: []
      link_padding: []
      link_scale: []
      object_colors: []
      world: 
        collision_objects: []
        octomap: 
          header: 
            seq: 0
            stamp: 
              secs: 0
              nsecs:         0
            frame_id: ''
          origin: 
            position: 
              x: 0.0
              y: 0.0
              z: 0.0
            orientation: 
              x: 0.0
              y: 0.0
              z: 0.0
              w: 0.0
          octomap: 
            header: 
              seq: 0
              stamp: 
                secs: 0
                nsecs:         0
              frame_id: ''
            binary: False
            id: ''
            resolution: 0.0
            data: []
      is_diff: True
    plan_only: True
    look_around: False
    look_around_attempts: 0
    max_safe_execution_cost: 0.0
    replan: False
    replan_attempts: 0
    replan_delay: 0.0
---
'''