#!/usr/bin/env python

import rospy
import pickle
import sys
from moveit_msgs.msg import MoveGroupActionGoal, Constraints, JointConstraint, MoveGroupAction, MoveGroupGoal, PlanningSceneComponents, MoveGroupResult, MoveGroupActionResult
from moveit_msgs.srv import GetPlanningScene
from quad_planning.msg import DJIanswer
import actionlib

flag = 0
flag_dji = 0
flag_dji_adaptative = 0

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

#set loop execution rate at 1 Hz
r = rospy.Rate(1)


#get the currently DRONE currently position
components = PlanningSceneComponents()
components.components = 2
robot_state = getPlanningScene(components).scene.robot_state
dump.insert(0, [robot_state, 0])


def DJICallback(msg):
    global flag_dji, flag_dji_adaptative
    flag_dji = msg.position_reached
    flag_dji_adaptative = msg.image_processing_result


def resultCallback(msg):
    dji_traj_pub.publish(msg)


#send goal
def send_goal(current, goal):
    global flag_dji

    goal_msg = MoveGroupActionGoal()

    goal_msg.goal_id = "teste"

    goal_msg.goal.request.workspace_parameters.header.frame_id = "/world"
    goal_msg.goal.request.workspace_parameters.min_corner.x = -2500
    goal_msg.goal.request.workspace_parameters.min_corner.y = -2500
    goal_msg.goal.request.workspace_parameters.min_corner.z = -2500
    goal_msg.goal.request.workspace_parameters.max_corner.x = 2500
    goal_msg.goal.request.workspace_parameters.max_corner.y = 2500
    goal_msg.goal.request.workspace_parameters.max_corner.z = 2500

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

    goal_msg.goal.planning_options.planning_scene_diff.is_diff = True

    goal_msg.goal.planning_options.plan_only = False
    goal_msg.goal.planning_options.look_around = False
    goal_msg.goal.planning_options.replan = False


    print "Enviou posicao:"
    # print goal_msg.goal
    action = MoveGroupGoal
    action = goal_msg.goal

    client.send_goal(action)
    client.wait_for_result()

    print "Aguardando...:"
    while (flag_dji == 0):
        r.sleep()

    flag_dji = 0

    print "Chegou!"


print("Pronto para executar " + str(len(dump)) + " posicoes")

#get the pathplanning results
rospy.Subscriber("/move_group/result", MoveGroupResult, resultCallback, queue_size=10)


#get the pathplanning results
rospy.Subscriber("/dji/status", DJIanswer, DJICallback, queue_size=10)

#topic to write the dji trajectory messages
dji_traj_pub = rospy.Publisher("/dji/trajectory", MoveGroupActionResult, queue_size=10)


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