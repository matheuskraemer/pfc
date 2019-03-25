# Path planning implementation

## Normal installation:

To install the ROSquad_rotors follow the instructions here:
https://github.com/wilselby/ROS_quadrotor_simulator

To parse your model to the path planning solution follow:
https://www.wilselby.com/research/ros-integration/3d-mapping-navigation/


Tip:
1. To run a path planning example it is not necessary to go through the moveit procedure at after installation is possible to run "roslaunch quad_3dnav quad_3dnav.launch" to visualize the path planning feature
2. If you did not have follow the instruction to change GazeboX(your version) to Gazebo2, what is great, the rotors_gazebo_plugins package need to be modified. The instruction is here:
https://github.com/ethz-asl/rotors_simulator/commit/71c1ddef1ff42345090a2dd8e112683ecf7ac46f?_pjax=%23js-repo-pjax-container#diff-3cf18422550da5a0e7b8ad5bdb3ad8c6


## Lunar installation:

Whether the ROS version is Lunar and the OS is Ubuntu 16.04, it is possible to face some problems. Below is one description in how install at Lunar
This case was more difficult because the moveit package was installed from source. The moveit package for ubuntu 16-04 for Lunar seems to be corrupted via apt-get giving a lot of "segmentation errors" even with moveit on tutorials
It can be possible that with another set like: more newer Ubuntus or ROS distros the installation reliable from the repositories (apt-get)



1.  install mav_comm and octomap package
2.  instlal catkin_simple package
3.  install glog package
4.  install joystick package
5.  install rotors_simulator
6.  case moveit is needed to be installed from source go on, or jump to 6 (if the moveit with apt-get is with problem, in my case with lunar there were a lot of segmentation problems)
	* install moveit from source
    * install ROS_quad_motors without moveit_simple_controller_manager package
    * replace the moveit/moveit_plugins/moveit_simple_controller_manager for the one on the ROS_quad_rotors package
    * add the the line "add_compile_options(-std=c++11)" to the CMakeLists.txt from the moveit_simple_controller_manager
    * install all packages
    * jump to 8

7.  install ROS_quad_motors
8.  install the xbox drivers as described here https://github.com/wilselby/ROS_quadrotor_simulator
9.  case a xbox controller is not available it is possible to simulate one form the keyboard with the command:
xboxdrv --evdev /dev/input/event12 --evdev-keymap KEY_X=x,KEY_Y=y,KEY_A=a,KEY_B=b,KEY_KP1=lb,KEY_KP2=rb,KEY_KP4=lt,KEY_KP5=rt,KEY_KP9=tl,KEY_KP8=tr --mimic-xpad
the /dev/input/xxxx should be replaced by the event where the keyboard is. It is possible to hear one input using evtest /dev/inputs/name of the port

Note:

1.	The keys can be changed in the xboxdrv command whether the user wants

## Path planning

How perform the path planning with the quad_3dnav.launch example file

* execute the xbox simulation or connect a real xbox controller
* execute "roslaunch quad_3dnav quad_3dnav.launch"
* press LB at the controller or press number 1 on the numeric keyboard to active the 3Dnav mode
* on the Rviz GUI go to the Planning tab
* on the visualization put the marker at a desired position, not so far from the known map
* click Plan and wait until the track appear
* click execute whether the track is good and observe the drone flying

Note:

1.	At the Context tab different path planning algorithms can be tested depending on the requirements.

# PX4 via mavros

* to run the following examples it is necessary to install and the px4 toolchain. How to do that is described here https://dev.px4.io/en/setup/getting_started.html
* install mavros from source https://github.com/mavlink/mavros, without mavros_extras

## PX4 at Gazebo

* go to the dev/px4_src/src/Firmware
* in a terminal execute the command "make px4_sitl_default gazebo" (the first time can take several minutes, but from this time the simulation will run very fast)
* the iris model is launched at Gazebo

## Mavros to control the PX4 at Gazebo

* install mavros from apt-get or source https://github.com/mavlink/mavros, the mavros_extras can generate some erros, if so it is not necessary it can be excluded from the ros folder
* run PX4 at Gazebo
* in a terminal execute " roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557" "

Note:
1.	The command "roslaunch mavros px4.launch fcu_url:="udp://:14540@127.0.0.1:14557"" can be used to access a real px4 FC. Mavros is used to access simulated or real FCs

Note:
1.  More information about ROS and Gazebo simulation see at: https://dev.px4.io/en/simulation/ros_interface.html


## Commanding the simulation via MAVROS


* run PX4 at Gazebo
* run Mavros
* in a terminal execute the commando "rqt"
* open a service caller plugin for "/mavros/cmd/arming"
* open a service caller plugin for "/mavros/set_mode"
* open a message publisher plugin for "/mavros/setpoint_position/local"
* set a generic position at /mavros/setpoint_position/local and start publisher
* change the custom_mode field on "/mavros/set_mode" to "OFFBOARD"
* change the custom_mode field on "/mavros/cmd/arming" to "True"
* call the service "/mavros/set_mode"
* call the service "/mavros/cmd/arming"
* visualize the drone moving around Gazebo
* change the topic for make the drone move around

Note:
1.	This procedure is based on the c++ file described here: https://dev.px4.io/en/ros/mavros_offboard.html
2.	Scripts in c++ or python can access the ros framework and the same procedure did on rqt can be written at one of this programming languages
