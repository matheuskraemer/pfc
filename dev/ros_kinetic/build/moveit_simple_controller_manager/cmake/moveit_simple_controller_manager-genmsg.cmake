# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(WARNING "Invoking generate_messages() without having added any message or service file before.
You should either add add_message_files() and/or add_service_files() calls or remove the invocation of generate_messages().")
message(STATUS "moveit_simple_controller_manager: 0 messages, 0 services")

set(MSG_I_FLAGS "-Iaction_controller:/home/matheus/Projects/pfc/dev/ros_kinetic/devel/share/action_controller/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Itrajectory_msgs:/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(moveit_simple_controller_manager_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_cpp(moveit_simple_controller_manager
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_controller_manager
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(moveit_simple_controller_manager_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(moveit_simple_controller_manager_generate_messages moveit_simple_controller_manager_generate_messages_cpp)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(moveit_simple_controller_manager_gencpp)
add_dependencies(moveit_simple_controller_manager_gencpp moveit_simple_controller_manager_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS moveit_simple_controller_manager_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_eus(moveit_simple_controller_manager
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/moveit_simple_controller_manager
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(moveit_simple_controller_manager_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(moveit_simple_controller_manager_generate_messages moveit_simple_controller_manager_generate_messages_eus)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(moveit_simple_controller_manager_geneus)
add_dependencies(moveit_simple_controller_manager_geneus moveit_simple_controller_manager_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS moveit_simple_controller_manager_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_lisp(moveit_simple_controller_manager
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_controller_manager
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(moveit_simple_controller_manager_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(moveit_simple_controller_manager_generate_messages moveit_simple_controller_manager_generate_messages_lisp)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(moveit_simple_controller_manager_genlisp)
add_dependencies(moveit_simple_controller_manager_genlisp moveit_simple_controller_manager_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS moveit_simple_controller_manager_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_nodejs(moveit_simple_controller_manager
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/moveit_simple_controller_manager
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(moveit_simple_controller_manager_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(moveit_simple_controller_manager_generate_messages moveit_simple_controller_manager_generate_messages_nodejs)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(moveit_simple_controller_manager_gennodejs)
add_dependencies(moveit_simple_controller_manager_gennodejs moveit_simple_controller_manager_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS moveit_simple_controller_manager_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_py(moveit_simple_controller_manager
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_controller_manager
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(moveit_simple_controller_manager_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(moveit_simple_controller_manager_generate_messages moveit_simple_controller_manager_generate_messages_py)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(moveit_simple_controller_manager_genpy)
add_dependencies(moveit_simple_controller_manager_genpy moveit_simple_controller_manager_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS moveit_simple_controller_manager_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_controller_manager)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/moveit_simple_controller_manager
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET action_controller_generate_messages_cpp)
  add_dependencies(moveit_simple_controller_manager_generate_messages_cpp action_controller_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/moveit_simple_controller_manager)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/moveit_simple_controller_manager
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET action_controller_generate_messages_eus)
  add_dependencies(moveit_simple_controller_manager_generate_messages_eus action_controller_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_controller_manager)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/moveit_simple_controller_manager
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET action_controller_generate_messages_lisp)
  add_dependencies(moveit_simple_controller_manager_generate_messages_lisp action_controller_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/moveit_simple_controller_manager)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/moveit_simple_controller_manager
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET action_controller_generate_messages_nodejs)
  add_dependencies(moveit_simple_controller_manager_generate_messages_nodejs action_controller_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_controller_manager)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_controller_manager\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/moveit_simple_controller_manager
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET action_controller_generate_messages_py)
  add_dependencies(moveit_simple_controller_manager_generate_messages_py action_controller_generate_messages_py)
endif()
