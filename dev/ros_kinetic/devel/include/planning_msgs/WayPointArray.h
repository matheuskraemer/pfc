// Generated by gencpp from file planning_msgs/WayPointArray.msg
// DO NOT EDIT!


#ifndef PLANNING_MSGS_MESSAGE_WAYPOINTARRAY_H
#define PLANNING_MSGS_MESSAGE_WAYPOINTARRAY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <planning_msgs/WayPoint.h>

namespace planning_msgs
{
template <class ContainerAllocator>
struct WayPointArray_
{
  typedef WayPointArray_<ContainerAllocator> Type;

  WayPointArray_()
    : waypoints()  {
    }
  WayPointArray_(const ContainerAllocator& _alloc)
    : waypoints(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector< ::planning_msgs::WayPoint_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::planning_msgs::WayPoint_<ContainerAllocator> >::other >  _waypoints_type;
  _waypoints_type waypoints;





  typedef boost::shared_ptr< ::planning_msgs::WayPointArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::planning_msgs::WayPointArray_<ContainerAllocator> const> ConstPtr;

}; // struct WayPointArray_

typedef ::planning_msgs::WayPointArray_<std::allocator<void> > WayPointArray;

typedef boost::shared_ptr< ::planning_msgs::WayPointArray > WayPointArrayPtr;
typedef boost::shared_ptr< ::planning_msgs::WayPointArray const> WayPointArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::planning_msgs::WayPointArray_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::planning_msgs::WayPointArray_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace planning_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'planning_msgs': ['/home/matheus/Projects/pfc/dev/ros_kinetic/src/mav_comm/planning_msgs/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'octomap_msgs': ['/opt/ros/kinetic/share/octomap_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::planning_msgs::WayPointArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::planning_msgs::WayPointArray_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::planning_msgs::WayPointArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::planning_msgs::WayPointArray_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::planning_msgs::WayPointArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::planning_msgs::WayPointArray_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::planning_msgs::WayPointArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "016d2aea6905a87be0cba110c54b2674";
  }

  static const char* value(const ::planning_msgs::WayPointArray_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x016d2aea6905a87bULL;
  static const uint64_t static_value2 = 0xe0cba110c54b2674ULL;
};

template<class ContainerAllocator>
struct DataType< ::planning_msgs::WayPointArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "planning_msgs/WayPointArray";
  }

  static const char* value(const ::planning_msgs::WayPointArray_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::planning_msgs::WayPointArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "WayPoint[] waypoints\n\
\n\
================================================================================\n\
MSG: planning_msgs/WayPoint\n\
Header header\n\
float64[] x       # holds motion primitive for the x-axis\n\
float64[] y       # holds motion primitive for the y-axis\n\
float64[] z       # holds motion primitive for the z-axis\n\
float64[] yaw     # holds motion primitive for yaw\n\
int32 type        # defines the type of the waypoint\n\
float64 time      # time for that waypoint. If it is a \"real\" point, this is the time to stay on that point. In case of a polynomial, it is the time [0...time] for which the polynomial is valid\n\
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
";
  }

  static const char* value(const ::planning_msgs::WayPointArray_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::planning_msgs::WayPointArray_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.waypoints);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct WayPointArray_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::planning_msgs::WayPointArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::planning_msgs::WayPointArray_<ContainerAllocator>& v)
  {
    s << indent << "waypoints[]" << std::endl;
    for (size_t i = 0; i < v.waypoints.size(); ++i)
    {
      s << indent << "  waypoints[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::planning_msgs::WayPoint_<ContainerAllocator> >::stream(s, indent + "    ", v.waypoints[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // PLANNING_MSGS_MESSAGE_WAYPOINTARRAY_H
