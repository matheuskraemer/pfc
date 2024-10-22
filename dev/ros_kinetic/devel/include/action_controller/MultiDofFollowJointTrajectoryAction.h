// Generated by gencpp from file action_controller/MultiDofFollowJointTrajectoryAction.msg
// DO NOT EDIT!


#ifndef ACTION_CONTROLLER_MESSAGE_MULTIDOFFOLLOWJOINTTRAJECTORYACTION_H
#define ACTION_CONTROLLER_MESSAGE_MULTIDOFFOLLOWJOINTTRAJECTORYACTION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <action_controller/MultiDofFollowJointTrajectoryActionGoal.h>
#include <action_controller/MultiDofFollowJointTrajectoryActionResult.h>
#include <action_controller/MultiDofFollowJointTrajectoryActionFeedback.h>

namespace action_controller
{
template <class ContainerAllocator>
struct MultiDofFollowJointTrajectoryAction_
{
  typedef MultiDofFollowJointTrajectoryAction_<ContainerAllocator> Type;

  MultiDofFollowJointTrajectoryAction_()
    : action_goal()
    , action_result()
    , action_feedback()  {
    }
  MultiDofFollowJointTrajectoryAction_(const ContainerAllocator& _alloc)
    : action_goal(_alloc)
    , action_result(_alloc)
    , action_feedback(_alloc)  {
  (void)_alloc;
    }



   typedef  ::action_controller::MultiDofFollowJointTrajectoryActionGoal_<ContainerAllocator>  _action_goal_type;
  _action_goal_type action_goal;

   typedef  ::action_controller::MultiDofFollowJointTrajectoryActionResult_<ContainerAllocator>  _action_result_type;
  _action_result_type action_result;

   typedef  ::action_controller::MultiDofFollowJointTrajectoryActionFeedback_<ContainerAllocator>  _action_feedback_type;
  _action_feedback_type action_feedback;





  typedef boost::shared_ptr< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> const> ConstPtr;

}; // struct MultiDofFollowJointTrajectoryAction_

typedef ::action_controller::MultiDofFollowJointTrajectoryAction_<std::allocator<void> > MultiDofFollowJointTrajectoryAction;

typedef boost::shared_ptr< ::action_controller::MultiDofFollowJointTrajectoryAction > MultiDofFollowJointTrajectoryActionPtr;
typedef boost::shared_ptr< ::action_controller::MultiDofFollowJointTrajectoryAction const> MultiDofFollowJointTrajectoryActionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace action_controller

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'action_controller': ['/home/matheus/Projects/pfc/dev/ros_kinetic/devel/share/action_controller/msg', '/home/matheus/Projects/pfc/dev/ros_kinetic/devel/share/action_controller/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c9d632efe8ad62964a8057cf20eccfea";
  }

  static const char* value(const ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc9d632efe8ad6296ULL;
  static const uint64_t static_value2 = 0x4a8057cf20eccfeaULL;
};

template<class ContainerAllocator>
struct DataType< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "action_controller/MultiDofFollowJointTrajectoryAction";
  }

  static const char* value(const ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
MultiDofFollowJointTrajectoryActionGoal action_goal\n\
MultiDofFollowJointTrajectoryActionResult action_result\n\
MultiDofFollowJointTrajectoryActionFeedback action_feedback\n\
\n\
================================================================================\n\
MSG: action_controller/MultiDofFollowJointTrajectoryActionGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalID goal_id\n\
MultiDofFollowJointTrajectoryGoal goal\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalID\n\
# The stamp should store the time at which this goal was requested.\n\
# It is used by an action server when it tries to preempt all\n\
# goals that were requested before a certain time\n\
time stamp\n\
\n\
# The id provides a way to associate feedback and\n\
# result message with specific goal requests. The id\n\
# specified must be unique.\n\
string id\n\
\n\
\n\
================================================================================\n\
MSG: action_controller/MultiDofFollowJointTrajectoryGoal\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# The joint trajectory to follow\n\
trajectory_msgs/MultiDOFJointTrajectory trajectory\n\
\n\
================================================================================\n\
MSG: trajectory_msgs/MultiDOFJointTrajectory\n\
# The header is used to specify the coordinate frame and the reference time for the trajectory durations\n\
Header header\n\
\n\
# A representation of a multi-dof joint trajectory (each point is a transformation)\n\
# Each point along the trajectory will include an array of positions/velocities/accelerations\n\
# that has the same length as the array of joint names, and has the same order of joints as \n\
# the joint names array.\n\
\n\
string[] joint_names\n\
MultiDOFJointTrajectoryPoint[] points\n\
\n\
================================================================================\n\
MSG: trajectory_msgs/MultiDOFJointTrajectoryPoint\n\
# Each multi-dof joint can specify a transform (up to 6 DOF)\n\
geometry_msgs/Transform[] transforms\n\
\n\
# There can be a velocity specified for the origin of the joint \n\
geometry_msgs/Twist[] velocities\n\
\n\
# There can be an acceleration specified for the origin of the joint \n\
geometry_msgs/Twist[] accelerations\n\
\n\
duration time_from_start\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Transform\n\
# This represents the transform between two coordinate frames in free space.\n\
\n\
Vector3 translation\n\
Quaternion rotation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Twist\n\
# This expresses velocity in free space broken into its linear and angular parts.\n\
Vector3  linear\n\
Vector3  angular\n\
\n\
================================================================================\n\
MSG: action_controller/MultiDofFollowJointTrajectoryActionResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
MultiDofFollowJointTrajectoryResult result\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalStatus\n\
GoalID goal_id\n\
uint8 status\n\
uint8 PENDING         = 0   # The goal has yet to be processed by the action server\n\
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server\n\
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing\n\
                            #   and has since completed its execution (Terminal State)\n\
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)\n\
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due\n\
                            #    to some failure (Terminal State)\n\
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,\n\
                            #    because the goal was unattainable or invalid (Terminal State)\n\
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing\n\
                            #    and has not yet completed execution\n\
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,\n\
                            #    but the action server has not yet confirmed that the goal is canceled\n\
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing\n\
                            #    and was successfully cancelled (Terminal State)\n\
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be\n\
                            #    sent over the wire by an action server\n\
\n\
#Allow for the user to associate a string with GoalStatus for debugging\n\
string text\n\
\n\
\n\
================================================================================\n\
MSG: action_controller/MultiDofFollowJointTrajectoryResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
int32 error_code\n\
int32 SUCCESSFUL = 0\n\
int32 INVALID_GOAL = -1\n\
int32 INVALID_JOINTS = -2\n\
int32 OLD_HEADER_TIMESTAMP = -3\n\
int32 PATH_TOLERANCE_VIOLATED = -4\n\
int32 GOAL_TOLERANCE_VIOLATED = -5\n\
\n\
\n\
================================================================================\n\
MSG: action_controller/MultiDofFollowJointTrajectoryActionFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
MultiDofFollowJointTrajectoryFeedback feedback\n\
\n\
================================================================================\n\
MSG: action_controller/MultiDofFollowJointTrajectoryFeedback\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
Header header\n\
string[] joint_names\n\
trajectory_msgs/MultiDOFJointTrajectoryPoint desired\n\
trajectory_msgs/MultiDOFJointTrajectoryPoint actual\n\
trajectory_msgs/MultiDOFJointTrajectoryPoint error\n\
\n\
";
  }

  static const char* value(const ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.action_goal);
      stream.next(m.action_result);
      stream.next(m.action_feedback);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MultiDofFollowJointTrajectoryAction_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::action_controller::MultiDofFollowJointTrajectoryAction_<ContainerAllocator>& v)
  {
    s << indent << "action_goal: ";
    s << std::endl;
    Printer< ::action_controller::MultiDofFollowJointTrajectoryActionGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.action_goal);
    s << indent << "action_result: ";
    s << std::endl;
    Printer< ::action_controller::MultiDofFollowJointTrajectoryActionResult_<ContainerAllocator> >::stream(s, indent + "  ", v.action_result);
    s << indent << "action_feedback: ";
    s << std::endl;
    Printer< ::action_controller::MultiDofFollowJointTrajectoryActionFeedback_<ContainerAllocator> >::stream(s, indent + "  ", v.action_feedback);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ACTION_CONTROLLER_MESSAGE_MULTIDOFFOLLOWJOINTTRAJECTORYACTION_H
