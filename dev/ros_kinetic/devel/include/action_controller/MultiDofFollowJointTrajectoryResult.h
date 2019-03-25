// Generated by gencpp from file action_controller/MultiDofFollowJointTrajectoryResult.msg
// DO NOT EDIT!


#ifndef ACTION_CONTROLLER_MESSAGE_MULTIDOFFOLLOWJOINTTRAJECTORYRESULT_H
#define ACTION_CONTROLLER_MESSAGE_MULTIDOFFOLLOWJOINTTRAJECTORYRESULT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace action_controller
{
template <class ContainerAllocator>
struct MultiDofFollowJointTrajectoryResult_
{
  typedef MultiDofFollowJointTrajectoryResult_<ContainerAllocator> Type;

  MultiDofFollowJointTrajectoryResult_()
    : error_code(0)  {
    }
  MultiDofFollowJointTrajectoryResult_(const ContainerAllocator& _alloc)
    : error_code(0)  {
  (void)_alloc;
    }



   typedef int32_t _error_code_type;
  _error_code_type error_code;



  enum {
    SUCCESSFUL = 0,
    INVALID_GOAL = -1,
    INVALID_JOINTS = -2,
    OLD_HEADER_TIMESTAMP = -3,
    PATH_TOLERANCE_VIOLATED = -4,
    GOAL_TOLERANCE_VIOLATED = -5,
  };


  typedef boost::shared_ptr< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> const> ConstPtr;

}; // struct MultiDofFollowJointTrajectoryResult_

typedef ::action_controller::MultiDofFollowJointTrajectoryResult_<std::allocator<void> > MultiDofFollowJointTrajectoryResult;

typedef boost::shared_ptr< ::action_controller::MultiDofFollowJointTrajectoryResult > MultiDofFollowJointTrajectoryResultPtr;
typedef boost::shared_ptr< ::action_controller::MultiDofFollowJointTrajectoryResult const> MultiDofFollowJointTrajectoryResultConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace action_controller

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'action_controller': ['/home/matheus/Projects/pfc/dev/ros_kinetic/devel/share/action_controller/msg', '/home/matheus/Projects/pfc/dev/ros_kinetic/devel/share/action_controller/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6243274b5d629dc838814109754410d5";
  }

  static const char* value(const ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6243274b5d629dc8ULL;
  static const uint64_t static_value2 = 0x38814109754410d5ULL;
};

template<class ContainerAllocator>
struct DataType< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "action_controller/MultiDofFollowJointTrajectoryResult";
  }

  static const char* value(const ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
int32 error_code\n\
int32 SUCCESSFUL = 0\n\
int32 INVALID_GOAL = -1\n\
int32 INVALID_JOINTS = -2\n\
int32 OLD_HEADER_TIMESTAMP = -3\n\
int32 PATH_TOLERANCE_VIOLATED = -4\n\
int32 GOAL_TOLERANCE_VIOLATED = -5\n\
\n\
";
  }

  static const char* value(const ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.error_code);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MultiDofFollowJointTrajectoryResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::action_controller::MultiDofFollowJointTrajectoryResult_<ContainerAllocator>& v)
  {
    s << indent << "error_code: ";
    Printer<int32_t>::stream(s, indent + "  ", v.error_code);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ACTION_CONTROLLER_MESSAGE_MULTIDOFFOLLOWJOINTTRAJECTORYRESULT_H
