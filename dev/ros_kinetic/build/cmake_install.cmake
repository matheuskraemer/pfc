# Install script for directory: /home/matheus/Projects/pfc/dev/ros_kinetic/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/matheus/Projects/pfc/dev/ros_kinetic/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/matheus/Projects/pfc/dev/ros_kinetic/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/matheus/Projects/pfc/dev/ros_kinetic/install" TYPE PROGRAM FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/build/catkin_generated/installspace/_setup_util.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/matheus/Projects/pfc/dev/ros_kinetic/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/matheus/Projects/pfc/dev/ros_kinetic/install" TYPE PROGRAM FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/build/catkin_generated/installspace/env.sh")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/matheus/Projects/pfc/dev/ros_kinetic/install/setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/matheus/Projects/pfc/dev/ros_kinetic/install" TYPE FILE FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/build/catkin_generated/installspace/setup.bash")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/matheus/Projects/pfc/dev/ros_kinetic/install/setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/matheus/Projects/pfc/dev/ros_kinetic/install" TYPE FILE FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/build/catkin_generated/installspace/setup.sh")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/matheus/Projects/pfc/dev/ros_kinetic/install/setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/matheus/Projects/pfc/dev/ros_kinetic/install" TYPE FILE FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/build/catkin_generated/installspace/setup.zsh")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/matheus/Projects/pfc/dev/ros_kinetic/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/matheus/Projects/pfc/dev/ros_kinetic/install" TYPE FILE FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/gtest/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/catkin_simple/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/glog_catkin/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/mav_comm/mav_comm/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/octomap_mapping/octomap_mapping/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/rotors_simulator/rotors_description/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/rotors_simulator/rotors_model/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/rotors_simulator/rotors_simulator/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/mav_comm/mav_msgs/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_collect/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_description/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_3dnav/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_gazebo/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_octomap/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_planning/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/mav_comm/planning_msgs/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_joystick_interface/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/rotors_simulator/rotors_control/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/rotors_simulator/rotors_joy_interface/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/octomap_mapping/octomap_server/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_control/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/rotors_simulator/rotors_gazebo_plugins/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/geonav_transform/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/rotors_simulator/rotors_gazebo/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/action_controller/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/moveit_simple_controller_manager/cmake_install.cmake")
  include("/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_2dnav/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/matheus/Projects/pfc/dev/ros_kinetic/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
