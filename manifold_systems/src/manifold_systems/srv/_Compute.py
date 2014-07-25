"""autogenerated by genpy from manifold_systems/ComputeRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ComputeRequest(genpy.Message):
  _md5sum = "e6da1f4bb463d64b2399f31589512a6f"
  _type = "manifold_systems/ComputeRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 fx
float64 fy
float64 fz
float64 tx
float64 ty
float64 tz

"""
  __slots__ = ['fx','fy','fz','tx','ty','tz']
  _slot_types = ['float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       fx,fy,fz,tx,ty,tz

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ComputeRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.fx is None:
        self.fx = 0.
      if self.fy is None:
        self.fy = 0.
      if self.fz is None:
        self.fz = 0.
      if self.tx is None:
        self.tx = 0.
      if self.ty is None:
        self.ty = 0.
      if self.tz is None:
        self.tz = 0.
    else:
      self.fx = 0.
      self.fy = 0.
      self.fz = 0.
      self.tx = 0.
      self.ty = 0.
      self.tz = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_6d.pack(_x.fx, _x.fy, _x.fz, _x.tx, _x.ty, _x.tz))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 48
      (_x.fx, _x.fy, _x.fz, _x.tx, _x.ty, _x.tz,) = _struct_6d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_6d.pack(_x.fx, _x.fy, _x.fz, _x.tx, _x.ty, _x.tz))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 48
      (_x.fx, _x.fy, _x.fz, _x.tx, _x.ty, _x.tz,) = _struct_6d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6d = struct.Struct("<6d")
"""autogenerated by genpy from manifold_systems/ComputeResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ComputeResponse(genpy.Message):
  _md5sum = "209f516d3eb691f0663e25cb750d67c1"
  _type = "manifold_systems/ComputeResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 x
float64 y


"""
  __slots__ = ['x','y']
  _slot_types = ['float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x,y

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ComputeResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
    else:
      self.x = 0.
      self.y = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_2d.pack(_x.x, _x.y))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.x, _x.y,) = _struct_2d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_2d.pack(_x.x, _x.y))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.x, _x.y,) = _struct_2d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2d = struct.Struct("<2d")
class Compute(object):
  _type          = 'manifold_systems/Compute'
  _md5sum = 'b41c040ce5a6875183b2d3d611a6f73d'
  _request_class  = ComputeRequest
  _response_class = ComputeResponse