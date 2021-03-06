/* Auto-generated by genmsg_cpp for file /home/caleb/ros_workspace/sandbox/manifold_systems/srv/Converse.srv */
#ifndef MANIFOLD_SYSTEMS_SERVICE_CONVERSE_H
#define MANIFOLD_SYSTEMS_SERVICE_CONVERSE_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace manifold_systems
{
template <class ContainerAllocator>
struct ConverseRequest_ {
  typedef ConverseRequest_<ContainerAllocator> Type;

  ConverseRequest_()
  : a1x(0.0)
  , a1y(0.0)
  , a1z(0.0)
  , a2x(0.0)
  , a2y(0.0)
  , a2z(0.0)
  , a3x(0.0)
  , a3y(0.0)
  , a3z(0.0)
  {
  }

  ConverseRequest_(const ContainerAllocator& _alloc)
  : a1x(0.0)
  , a1y(0.0)
  , a1z(0.0)
  , a2x(0.0)
  , a2y(0.0)
  , a2z(0.0)
  , a3x(0.0)
  , a3y(0.0)
  , a3z(0.0)
  {
  }

  typedef double _a1x_type;
  double a1x;

  typedef double _a1y_type;
  double a1y;

  typedef double _a1z_type;
  double a1z;

  typedef double _a2x_type;
  double a2x;

  typedef double _a2y_type;
  double a2y;

  typedef double _a2z_type;
  double a2z;

  typedef double _a3x_type;
  double a3x;

  typedef double _a3y_type;
  double a3y;

  typedef double _a3z_type;
  double a3z;


  typedef boost::shared_ptr< ::manifold_systems::ConverseRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::manifold_systems::ConverseRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ConverseRequest
typedef  ::manifold_systems::ConverseRequest_<std::allocator<void> > ConverseRequest;

typedef boost::shared_ptr< ::manifold_systems::ConverseRequest> ConverseRequestPtr;
typedef boost::shared_ptr< ::manifold_systems::ConverseRequest const> ConverseRequestConstPtr;


template <class ContainerAllocator>
struct ConverseResponse_ {
  typedef ConverseResponse_<ContainerAllocator> Type;

  ConverseResponse_()
  : x(0.0)
  , y(0.0)
  {
  }

  ConverseResponse_(const ContainerAllocator& _alloc)
  : x(0.0)
  , y(0.0)
  {
  }

  typedef double _x_type;
  double x;

  typedef double _y_type;
  double y;


  typedef boost::shared_ptr< ::manifold_systems::ConverseResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::manifold_systems::ConverseResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct ConverseResponse
typedef  ::manifold_systems::ConverseResponse_<std::allocator<void> > ConverseResponse;

typedef boost::shared_ptr< ::manifold_systems::ConverseResponse> ConverseResponsePtr;
typedef boost::shared_ptr< ::manifold_systems::ConverseResponse const> ConverseResponseConstPtr;

struct Converse
{

typedef ConverseRequest Request;
typedef ConverseResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Converse
} // namespace manifold_systems

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::manifold_systems::ConverseRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::manifold_systems::ConverseRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::manifold_systems::ConverseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2e00e0cb3b761a3f16551383fb447367";
  }

  static const char* value(const  ::manifold_systems::ConverseRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x2e00e0cb3b761a3fULL;
  static const uint64_t static_value2 = 0x16551383fb447367ULL;
};

template<class ContainerAllocator>
struct DataType< ::manifold_systems::ConverseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "manifold_systems/ConverseRequest";
  }

  static const char* value(const  ::manifold_systems::ConverseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::manifold_systems::ConverseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 a1x\n\
float64 a1y\n\
float64 a1z\n\
float64 a2x\n\
float64 a2y\n\
float64 a2z\n\
float64 a3x\n\
float64 a3y\n\
float64 a3z\n\
\n\
";
  }

  static const char* value(const  ::manifold_systems::ConverseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::manifold_systems::ConverseRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::manifold_systems::ConverseResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::manifold_systems::ConverseResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::manifold_systems::ConverseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "209f516d3eb691f0663e25cb750d67c1";
  }

  static const char* value(const  ::manifold_systems::ConverseResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x209f516d3eb691f0ULL;
  static const uint64_t static_value2 = 0x663e25cb750d67c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::manifold_systems::ConverseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "manifold_systems/ConverseResponse";
  }

  static const char* value(const  ::manifold_systems::ConverseResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::manifold_systems::ConverseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 x\n\
float64 y\n\
\n\
\n\
";
  }

  static const char* value(const  ::manifold_systems::ConverseResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::manifold_systems::ConverseResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::manifold_systems::ConverseRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.a1x);
    stream.next(m.a1y);
    stream.next(m.a1z);
    stream.next(m.a2x);
    stream.next(m.a2y);
    stream.next(m.a2z);
    stream.next(m.a3x);
    stream.next(m.a3y);
    stream.next(m.a3z);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ConverseRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::manifold_systems::ConverseResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.x);
    stream.next(m.y);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct ConverseResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<manifold_systems::Converse> {
  static const char* value() 
  {
    return "d55c807f317134af6b1b0dbdf90b9a40";
  }

  static const char* value(const manifold_systems::Converse&) { return value(); } 
};

template<>
struct DataType<manifold_systems::Converse> {
  static const char* value() 
  {
    return "manifold_systems/Converse";
  }

  static const char* value(const manifold_systems::Converse&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<manifold_systems::ConverseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d55c807f317134af6b1b0dbdf90b9a40";
  }

  static const char* value(const manifold_systems::ConverseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<manifold_systems::ConverseRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "manifold_systems/Converse";
  }

  static const char* value(const manifold_systems::ConverseRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<manifold_systems::ConverseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d55c807f317134af6b1b0dbdf90b9a40";
  }

  static const char* value(const manifold_systems::ConverseResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<manifold_systems::ConverseResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "manifold_systems/Converse";
  }

  static const char* value(const manifold_systems::ConverseResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // MANIFOLD_SYSTEMS_SERVICE_CONVERSE_H

