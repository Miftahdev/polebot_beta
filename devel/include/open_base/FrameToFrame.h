// Generated by gencpp from file open_base/FrameToFrame.msg
// DO NOT EDIT!


#ifndef OPEN_BASE_MESSAGE_FRAMETOFRAME_H
#define OPEN_BASE_MESSAGE_FRAMETOFRAME_H

#include <ros/service_traits.h>


#include <open_base/FrameToFrameRequest.h>
#include <open_base/FrameToFrameResponse.h>


namespace open_base
{

struct FrameToFrame
{

typedef FrameToFrameRequest Request;
typedef FrameToFrameResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct FrameToFrame
} // namespace open_base


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::open_base::FrameToFrame > {
  static const char* value()
  {
    return "405de59229ff9ecc65cfa6d1fe41484d";
  }

  static const char* value(const ::open_base::FrameToFrame&) { return value(); }
};

template<>
struct DataType< ::open_base::FrameToFrame > {
  static const char* value()
  {
    return "open_base/FrameToFrame";
  }

  static const char* value(const ::open_base::FrameToFrame&) { return value(); }
};


// service_traits::MD5Sum< ::open_base::FrameToFrameRequest> should match
// service_traits::MD5Sum< ::open_base::FrameToFrame >
template<>
struct MD5Sum< ::open_base::FrameToFrameRequest>
{
  static const char* value()
  {
    return MD5Sum< ::open_base::FrameToFrame >::value();
  }
  static const char* value(const ::open_base::FrameToFrameRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::open_base::FrameToFrameRequest> should match
// service_traits::DataType< ::open_base::FrameToFrame >
template<>
struct DataType< ::open_base::FrameToFrameRequest>
{
  static const char* value()
  {
    return DataType< ::open_base::FrameToFrame >::value();
  }
  static const char* value(const ::open_base::FrameToFrameRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::open_base::FrameToFrameResponse> should match
// service_traits::MD5Sum< ::open_base::FrameToFrame >
template<>
struct MD5Sum< ::open_base::FrameToFrameResponse>
{
  static const char* value()
  {
    return MD5Sum< ::open_base::FrameToFrame >::value();
  }
  static const char* value(const ::open_base::FrameToFrameResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::open_base::FrameToFrameResponse> should match
// service_traits::DataType< ::open_base::FrameToFrame >
template<>
struct DataType< ::open_base::FrameToFrameResponse>
{
  static const char* value()
  {
    return DataType< ::open_base::FrameToFrame >::value();
  }
  static const char* value(const ::open_base::FrameToFrameResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // OPEN_BASE_MESSAGE_FRAMETOFRAME_H