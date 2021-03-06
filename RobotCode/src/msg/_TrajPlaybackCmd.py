"""autogenerated by genpy from hrl_pr2_traj_playback/TrajPlaybackCmd.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TrajPlaybackCmd(genpy.Message):
  _md5sum = "288f4134e129633c0e508e5a773294ba"
  _type = "hrl_pr2_traj_playback/TrajPlaybackCmd"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8 START=0
int8 STOP=1
int8 RESET=2

int8 type
string traj_name
bool is_trajectory
bool is_forward
bool is_setup

"""
  # Pseudo-constants
  START = 0
  STOP = 1
  RESET = 2

  __slots__ = ['type','traj_name','is_trajectory','is_forward','is_setup']
  _slot_types = ['int8','string','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       type,traj_name,is_trajectory,is_forward,is_setup

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TrajPlaybackCmd, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.type is None:
        self.type = 0
      if self.traj_name is None:
        self.traj_name = ''
      if self.is_trajectory is None:
        self.is_trajectory = False
      if self.is_forward is None:
        self.is_forward = False
      if self.is_setup is None:
        self.is_setup = False
    else:
      self.type = 0
      self.traj_name = ''
      self.is_trajectory = False
      self.is_forward = False
      self.is_setup = False

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
      buff.write(_struct_b.pack(self.type))
      _x = self.traj_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3B.pack(_x.is_trajectory, _x.is_forward, _x.is_setup))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.type,) = _struct_b.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.traj_name = str[start:end].decode('utf-8')
      else:
        self.traj_name = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.is_trajectory, _x.is_forward, _x.is_setup,) = _struct_3B.unpack(str[start:end])
      self.is_trajectory = bool(self.is_trajectory)
      self.is_forward = bool(self.is_forward)
      self.is_setup = bool(self.is_setup)
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
      buff.write(_struct_b.pack(self.type))
      _x = self.traj_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3B.pack(_x.is_trajectory, _x.is_forward, _x.is_setup))
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
      start = end
      end += 1
      (self.type,) = _struct_b.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.traj_name = str[start:end].decode('utf-8')
      else:
        self.traj_name = str[start:end]
      _x = self
      start = end
      end += 3
      (_x.is_trajectory, _x.is_forward, _x.is_setup,) = _struct_3B.unpack(str[start:end])
      self.is_trajectory = bool(self.is_trajectory)
      self.is_forward = bool(self.is_forward)
      self.is_setup = bool(self.is_setup)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3B = struct.Struct("<3B")
_struct_b = struct.Struct("<b")
