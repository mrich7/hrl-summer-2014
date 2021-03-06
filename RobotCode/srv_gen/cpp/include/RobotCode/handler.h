/* Auto-generated by genmsg_cpp for file /home/dave/git/hrl-summer-2014/RobotCode/srv/handler.srv */
#ifndef ROBOTCODE_SERVICE_HANDLER_H
#define ROBOTCODE_SERVICE_HANDLER_H
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




namespace RobotCode
{
template <class ContainerAllocator>
struct handlerRequest_ {
  typedef handlerRequest_<ContainerAllocator> Type;

  handlerRequest_()
  : x(0)
  {
  }

  handlerRequest_(const ContainerAllocator& _alloc)
  : x(0)
  {
  }

  typedef int64_t _x_type;
  int64_t x;


  typedef boost::shared_ptr< ::RobotCode::handlerRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::RobotCode::handlerRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct handlerRequest
typedef  ::RobotCode::handlerRequest_<std::allocator<void> > handlerRequest;

typedef boost::shared_ptr< ::RobotCode::handlerRequest> handlerRequestPtr;
typedef boost::shared_ptr< ::RobotCode::handlerRequest const> handlerRequestConstPtr;


template <class ContainerAllocator>
struct handlerResponse_ {
  typedef handlerResponse_<ContainerAllocator> Type;

  handlerResponse_()
  {
  }

  handlerResponse_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::RobotCode::handlerResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::RobotCode::handlerResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct handlerResponse
typedef  ::RobotCode::handlerResponse_<std::allocator<void> > handlerResponse;

typedef boost::shared_ptr< ::RobotCode::handlerResponse> handlerResponsePtr;
typedef boost::shared_ptr< ::RobotCode::handlerResponse const> handlerResponseConstPtr;

struct handler
{

typedef handlerRequest Request;
typedef handlerResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct handler
} // namespace RobotCode

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::RobotCode::handlerRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::RobotCode::handlerRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::RobotCode::handlerRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b429044e1360891965aa67e074722c0e";
  }

  static const char* value(const  ::RobotCode::handlerRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb429044e13608919ULL;
  static const uint64_t static_value2 = 0x65aa67e074722c0eULL;
};

template<class ContainerAllocator>
struct DataType< ::RobotCode::handlerRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RobotCode/handlerRequest";
  }

  static const char* value(const  ::RobotCode::handlerRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::RobotCode::handlerRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "int64 x\n\
\n\
";
  }

  static const char* value(const  ::RobotCode::handlerRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::RobotCode::handlerRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::RobotCode::handlerResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::RobotCode::handlerResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::RobotCode::handlerResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::RobotCode::handlerResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::RobotCode::handlerResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RobotCode/handlerResponse";
  }

  static const char* value(const  ::RobotCode::handlerResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::RobotCode::handlerResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
\n\
";
  }

  static const char* value(const  ::RobotCode::handlerResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::RobotCode::handlerResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::RobotCode::handlerRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.x);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct handlerRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::RobotCode::handlerResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct handlerResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<RobotCode::handler> {
  static const char* value() 
  {
    return "b429044e1360891965aa67e074722c0e";
  }

  static const char* value(const RobotCode::handler&) { return value(); } 
};

template<>
struct DataType<RobotCode::handler> {
  static const char* value() 
  {
    return "RobotCode/handler";
  }

  static const char* value(const RobotCode::handler&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<RobotCode::handlerRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b429044e1360891965aa67e074722c0e";
  }

  static const char* value(const RobotCode::handlerRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<RobotCode::handlerRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RobotCode/handler";
  }

  static const char* value(const RobotCode::handlerRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<RobotCode::handlerResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b429044e1360891965aa67e074722c0e";
  }

  static const char* value(const RobotCode::handlerResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<RobotCode::handlerResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RobotCode/handler";
  }

  static const char* value(const RobotCode::handlerResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // ROBOTCODE_SERVICE_HANDLER_H

