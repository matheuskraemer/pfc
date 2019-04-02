import rospy
from sensor_msgs.msg import Joy


def pointCallback(msg):
    '''
    header:
      seq: 603
      stamp:
        secs: 2091
        nsecs: 518000000
      frame_id: ''
    axes: [-0.0, -0.0, -0.0, -0.0, 0.0, 0.0]
    buttons: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    '''
    print msg.buttons[8]

rospy.init_node("pickpoint")

rospy.Subscriber("quad/joy", Joy, pointCallback, queue_size=1)

r = rospy.Rate(0.25)

while (not rospy.is_shutdown()):
    r.sleep()

'''

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

'''

resultado planejamento

/move_group/result

header: 
  seq: 4
  stamp: 
    secs: 14468
    nsecs:  21000000
  frame_id: ''
status: 
  goal_id: 
    stamp: 
      secs: 14467
      nsecs: 987000000
    id: "/rviz-6-14467.987000000"
  status: 3
  text: "Motion plan was computed succesfully."
result: 
  error_code: 
    val: 1
  trajectory_start: 
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
      velocity: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
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
  planned_trajectory: 
    joint_trajectory: 
      header: 
        seq: 0
        stamp: 
          secs: 0
          nsecs:         0
        frame_id: ''
      joint_names: []
      points: []
    multi_dof_joint_trajectory: 
      header: 
        seq: 0
        stamp: 
          secs: 0
          nsecs:         0
        frame_id: "/world"
      joint_names: [virtual_joint]
      points: 
        - 
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
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 0
            nsecs:         0
        - 
          transforms: 
            - 
              translation: 
                x: 6.75492692499
                y: 21.35232158
                z: 5.88008539158
              rotation: 
                x: 8.93488881722e-05
                y: -3.36809489971e-05
                z: 0.541834687244
                w: 0.840485074934
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 1
            nsecs: 734999892
        - 
          transforms: 
            - 
              translation: 
                x: 5.78921812682
                y: 19.8473216878
                z: 6.05732388009
              rotation: 
                x: 8.10788077687e-05
                y: -2.43658990768e-05
                z: 0.561361135082
                w: 0.827570941179
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 3
            nsecs: 239999784
        - 
          transforms: 
            - 
              translation: 
                x: 4.82350932865
                y: 18.3423217957
                z: 6.23456236859
              rotation: 
                x: 7.27642909661e-05
                y: -1.50374952164e-05
                z: 0.580579919366
                w: 0.814203252503
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 4
            nsecs: 744999677
        - 
          transforms: 
            - 
              translation: 
                x: 3.85780053048
                y: 16.8373219035
                z: 6.41180085709
              rotation: 
                x: 6.44098947285e-05
                y: -5.70085010062e-06
                z: 0.599480506387
                w: 0.800389335429
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 6
            nsecs: 249999569
        - 
          transforms: 
            - 
              translation: 
                x: 2.89209173231
                y: 15.3323220113
                z: 6.58903934559
              rotation: 
                x: 5.60201978911e-05
                y: 3.63891904798e-06
                z: 0.618052536741
                w: 0.786136761061
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 7
            nsecs: 754999461
        - 
          transforms: 
            - 
              translation: 
                x: 1.92638293414
                y: 13.8273221191
                z: 6.76627783409
              rotation: 
                x: 4.7599798654e-05
                y: 1.29766932693e-05
                z: 0.636285830994
                w: 0.771453340941
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 9
            nsecs: 259999353
        - 
          transforms: 
            - 
              translation: 
                x: 0.960674135966
                y: 12.322322227
                z: 6.94351632259
              rotation: 
                x: 3.91533120654e-05
                y: 2.23073546665e-05
                z: 0.654170395243
                w: 0.756347122771
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 10
            nsecs: 764999245
        - 
          transforms: 
            - 
              translation: 
                x: -0.00503466220405
                y: 10.8173223348
                z: 7.1207548111
              rotation: 
                x: 3.06853674965e-05
                y: 3.16257892054e-05
                z: 0.671696426572
                w: 0.740826386001
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 12
            nsecs: 269999137
        - 
          transforms: 
            - 
              translation: 
                x: -0.970743460374
                y: 9.31232244263
                z: 7.2979932996
              rotation: 
                x: 2.22006061094e-05
                y: 4.09268895103e-05
                z: 0.688854318399
                w: 0.724899637302
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 14
            nsecs:   4999030
  executed_trajectory: 
    joint_trajectory: 
      header: 
        seq: 0
        stamp: 
          secs: 0
          nsecs:         0
        frame_id: ''
      joint_names: []
      points: []
    multi_dof_joint_trajectory: 
      header: 
        seq: 0
        stamp: 
          secs: 0
          nsecs:         0
        frame_id: ''
      joint_names: []
      points: []
  planning_time: 0.023206648
---



'''

'''
goal da trajetoria

/execute_trajectory/goal

header: 
  seq: 1
  stamp: 
    secs: 14489
    nsecs: 415000000
  frame_id: ''
goal_id: 
  stamp: 
    secs: 14489
    nsecs: 415000000
  id: "/rviz-7-14489.415000000"
goal: 
  trajectory: 
    joint_trajectory: 
      header: 
        seq: 0
        stamp: 
          secs: 0
          nsecs:         0
        frame_id: ''
      joint_names: []
      points: []
    multi_dof_joint_trajectory: 
      header: 
        seq: 0
        stamp: 
          secs: 0
          nsecs:         0
        frame_id: "/world"
      joint_names: [virtual_joint]
      points: 
        - 
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
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 0
            nsecs:         0
        - 
          transforms: 
            - 
              translation: 
                x: 6.75492692499
                y: 21.35232158
                z: 5.88008539158
              rotation: 
                x: 8.93488881722e-05
                y: -3.36809489971e-05
                z: 0.541834687244
                w: 0.840485074934
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 1
            nsecs: 734999892
        - 
          transforms: 
            - 
              translation: 
                x: 5.78921812682
                y: 19.8473216878
                z: 6.05732388009
              rotation: 
                x: 8.10788077687e-05
                y: -2.43658990768e-05
                z: 0.561361135082
                w: 0.827570941179
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 3
            nsecs: 239999784
        - 
          transforms: 
            - 
              translation: 
                x: 4.82350932865
                y: 18.3423217957
                z: 6.23456236859
              rotation: 
                x: 7.27642909661e-05
                y: -1.50374952164e-05
                z: 0.580579919366
                w: 0.814203252503
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 4
            nsecs: 744999677
        - 
          transforms: 
            - 
              translation: 
                x: 3.85780053048
                y: 16.8373219035
                z: 6.41180085709
              rotation: 
                x: 6.44098947285e-05
                y: -5.70085010062e-06
                z: 0.599480506387
                w: 0.800389335429
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 6
            nsecs: 249999569
        - 
          transforms: 
            - 
              translation: 
                x: 2.89209173231
                y: 15.3323220113
                z: 6.58903934559
              rotation: 
                x: 5.60201978911e-05
                y: 3.63891904798e-06
                z: 0.618052536741
                w: 0.786136761061
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 7
            nsecs: 754999461
        - 
          transforms: 
            - 
              translation: 
                x: 1.92638293414
                y: 13.8273221191
                z: 6.76627783409
              rotation: 
                x: 4.7599798654e-05
                y: 1.29766932693e-05
                z: 0.636285830994
                w: 0.771453340941
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 9
            nsecs: 259999353
        - 
          transforms: 
            - 
              translation: 
                x: 0.960674135966
                y: 12.322322227
                z: 6.94351632259
              rotation: 
                x: 3.91533120654e-05
                y: 2.23073546665e-05
                z: 0.654170395243
                w: 0.756347122771
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 10
            nsecs: 764999245
        - 
          transforms: 
            - 
              translation: 
                x: -0.00503466220405
                y: 10.8173223348
                z: 7.1207548111
              rotation: 
                x: 3.06853674965e-05
                y: 3.16257892054e-05
                z: 0.671696426572
                w: 0.740826386001
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 12
            nsecs: 269999137
        - 
          transforms: 
            - 
              translation: 
                x: -0.970743460374
                y: 9.31232244263
                z: 7.2979932996
              rotation: 
                x: 2.22006061094e-05
                y: 4.09268895103e-05
                z: 0.688854318399
                w: 0.724899637302
          velocities: []
          accelerations: []
          time_from_start: 
            secs: 14
            nsecs:   4999030
---


'''