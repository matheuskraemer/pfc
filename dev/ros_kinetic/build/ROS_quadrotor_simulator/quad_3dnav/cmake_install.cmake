# Install script for directory: /home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_3dnav

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_3dnav/catkin_generated/installspace/quad_3dnav.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/quad_3dnav/cmake" TYPE FILE FILES
    "/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_3dnav/catkin_generated/installspace/quad_3dnavConfig.cmake"
    "/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_3dnav/catkin_generated/installspace/quad_3dnavConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/quad_3dnav" TYPE FILE FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_3dnav/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/quad_3dnav" TYPE DIRECTORY FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_3dnav/launch" REGEX "/setup\\_assistant\\.launch$" EXCLUDE)
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/quad_3dnav" TYPE DIRECTORY FILES "/home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_3dnav/config")
endif()

