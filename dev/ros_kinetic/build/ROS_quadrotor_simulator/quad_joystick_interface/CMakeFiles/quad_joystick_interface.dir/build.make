# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/matheus/Projects/pfc/dev/ros_kinetic/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/matheus/Projects/pfc/dev/ros_kinetic/build

# Include any dependencies generated for this target.
include ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/depend.make

# Include the progress variables for this target.
include ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/progress.make

# Include the compile flags for this target's objects.
include ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/flags.make

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o: ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/flags.make
ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o: /home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_joystick_interface/src/joy.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/matheus/Projects/pfc/dev/ros_kinetic/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o"
	cd /home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_joystick_interface && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o -c /home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_joystick_interface/src/joy.cpp

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.i"
	cd /home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_joystick_interface && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_joystick_interface/src/joy.cpp > CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.i

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.s"
	cd /home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_joystick_interface && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_joystick_interface/src/joy.cpp -o CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.s

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o.requires:

.PHONY : ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o.requires

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o.provides: ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o.requires
	$(MAKE) -f ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/build.make ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o.provides.build
.PHONY : ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o.provides

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o.provides.build: ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o


# Object files for target quad_joystick_interface
quad_joystick_interface_OBJECTS = \
"CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o"

# External object files for target quad_joystick_interface
quad_joystick_interface_EXTERNAL_OBJECTS =

/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/build.make
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /opt/ros/kinetic/lib/libroscpp.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /opt/ros/kinetic/lib/librosconsole.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /opt/ros/kinetic/lib/librostime.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /opt/ros/kinetic/lib/libcpp_common.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface: ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/matheus/Projects/pfc/dev/ros_kinetic/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface"
	cd /home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_joystick_interface && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/quad_joystick_interface.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/build: /home/matheus/Projects/pfc/dev/ros_kinetic/devel/lib/quad_joystick_interface/quad_joystick_interface

.PHONY : ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/build

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/requires: ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/src/joy.cpp.o.requires

.PHONY : ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/requires

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/clean:
	cd /home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_joystick_interface && $(CMAKE_COMMAND) -P CMakeFiles/quad_joystick_interface.dir/cmake_clean.cmake
.PHONY : ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/clean

ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/depend:
	cd /home/matheus/Projects/pfc/dev/ros_kinetic/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/matheus/Projects/pfc/dev/ros_kinetic/src /home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_joystick_interface /home/matheus/Projects/pfc/dev/ros_kinetic/build /home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_joystick_interface /home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : ROS_quadrotor_simulator/quad_joystick_interface/CMakeFiles/quad_joystick_interface.dir/depend

