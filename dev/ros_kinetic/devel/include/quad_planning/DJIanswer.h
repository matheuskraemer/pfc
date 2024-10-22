// Generated by gencpp from file quad_planning/DJIanswer.msg
// DO NOT EDIT!


#ifndef QUAD_PLANNING_MESSAGE_DJIANSWER_H
#define QUAD_PLANNING_MESSAGE_DJIANSWER_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace quad_planning
{
template <class ContainerAllocator>
struct DJIanswer_
{
  typedef DJIanswer_<ContainerAllocator> Type;

  DJIanswer_()
    : position_reached(0)
    , image_processing_result(0)  {
    }
  DJIanswer_(const ContainerAllocator& _alloc)
    : position_reached(0)
    , image_processing_result(0)  {
  (void)_alloc;
    }



   typedef int32_t _position_reached_type;
  _position_reached_type position_reached;

   typedef int32_t _image_processing_result_type;
  _image_processing_result_type image_processing_result;





  typedef boost::shared_ptr< ::quad_planning::DJIanswer_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::quad_planning::DJIanswer_<ContainerAllocator> const> ConstPtr;

}; // struct DJIanswer_

typedef ::quad_planning::DJIanswer_<std::allocator<void> > DJIanswer;

typedef boost::shared_ptr< ::quad_planning::DJIanswer > DJIanswerPtr;
typedef boost::shared_ptr< ::quad_planning::DJIanswer const> DJIanswerConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::quad_planning::DJIanswer_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::quad_planning::DJIanswer_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace quad_planning

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'quad_planning': ['/home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/quad_planning/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::quad_planning::DJIanswer_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::quad_planning::DJIanswer_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::quad_planning::DJIanswer_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::quad_planning::DJIanswer_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::quad_planning::DJIanswer_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::quad_planning::DJIanswer_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::quad_planning::DJIanswer_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7c7d7f35308ecd11c127fbb2710e52ba";
  }

  static const char* value(const ::quad_planning::DJIanswer_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7c7d7f35308ecd11ULL;
  static const uint64_t static_value2 = 0xc127fbb2710e52baULL;
};

template<class ContainerAllocator>
struct DataType< ::quad_planning::DJIanswer_<ContainerAllocator> >
{
  static const char* value()
  {
    return "quad_planning/DJIanswer";
  }

  static const char* value(const ::quad_planning::DJIanswer_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::quad_planning::DJIanswer_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 position_reached\n\
int32 image_processing_result\n\
";
  }

  static const char* value(const ::quad_planning::DJIanswer_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::quad_planning::DJIanswer_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.position_reached);
      stream.next(m.image_processing_result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DJIanswer_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::quad_planning::DJIanswer_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::quad_planning::DJIanswer_<ContainerAllocator>& v)
  {
    s << indent << "position_reached: ";
    Printer<int32_t>::stream(s, indent + "  ", v.position_reached);
    s << indent << "image_processing_result: ";
    Printer<int32_t>::stream(s, indent + "  ", v.image_processing_result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // QUAD_PLANNING_MESSAGE_DJIANSWER_H
