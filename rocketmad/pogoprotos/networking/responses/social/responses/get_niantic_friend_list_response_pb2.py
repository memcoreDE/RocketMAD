# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/social/responses/get_niantic_friend_list_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.social import social_pb2 as pogoprotos_dot_data_dot_social_dot_social__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/social/responses/get_niantic_friend_list_response.proto',
  package='pogoprotos.networking.responses.social.responses',
  syntax='proto3',
  serialized_pb=_b('\nWpogoprotos/networking/responses/social/responses/get_niantic_friend_list_response.proto\x12\x30pogoprotos.networking.responses.social.responses\x1a#pogoprotos/data/social/social.proto\"\xdc\x05\n\x1cGetNianticFriendListResponse\x12\x65\n\x06result\x18\x01 \x01(\x0e\x32U.pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.Result\x12t\n\x0eniantic_friend\x18\x02 \x03(\x0b\x32\\.pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend\x1a\x9d\x02\n\rNianticFriend\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12\x8b\x01\n\x13niantic_friend_info\x18\x02 \x03(\x0b\x32n.pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend.NianticFriendInfo\x1ak\n\x11NianticFriendInfo\x12\x10\n\x08\x63odename\x18\x01 \x01(\t\x12\x0c\n\x04team\x18\x02 \x01(\t\x12\x36\n\x07\x61pp_key\x18\x03 \x01(\x0e\x32%.pogoprotos.data.social.Social.AppKey\x1ak\n\x11NianticFriendInfo\x12\x10\n\x08\x63odename\x18\x01 \x01(\t\x12\x0c\n\x04team\x18\x02 \x01(\t\x12\x36\n\x07\x61pp_key\x18\x03 \x01(\x0e\x32%.pogoprotos.data.social.Social.AppKey\"R\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12%\n!ERROR_SOCIAL_GRAPH_IMPORT_OPT_OUT\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_social_dot_social__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETNIANTICFRIENDLISTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_SOCIAL_GRAPH_IMPORT_OPT_OUT', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=829,
  serialized_end=911,
)
_sym_db.RegisterEnumDescriptor(_GETNIANTICFRIENDLISTRESPONSE_RESULT)


_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND_NIANTICFRIENDINFO = _descriptor.Descriptor(
  name='NianticFriendInfo',
  full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend.NianticFriendInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codename', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend.NianticFriendInfo.codename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend.NianticFriendInfo.team', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_key', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend.NianticFriendInfo.app_key', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=718,
)

_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND = _descriptor.Descriptor(
  name='NianticFriend',
  full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='niantic_friend_info', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend.niantic_friend_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND_NIANTICFRIENDINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=433,
  serialized_end=718,
)

_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIENDINFO = _descriptor.Descriptor(
  name='NianticFriendInfo',
  full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriendInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codename', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriendInfo.codename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriendInfo.team', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_key', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriendInfo.app_key', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=718,
)

_GETNIANTICFRIENDLISTRESPONSE = _descriptor.Descriptor(
  name='GetNianticFriendListResponse',
  full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='niantic_friend', full_name='pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.niantic_friend', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND, _GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIENDINFO, ],
  enum_types=[
    _GETNIANTICFRIENDLISTRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=911,
)

_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND_NIANTICFRIENDINFO.fields_by_name['app_key'].enum_type = pogoprotos_dot_data_dot_social_dot_social__pb2._SOCIAL_APPKEY
_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND_NIANTICFRIENDINFO.containing_type = _GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND
_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND.fields_by_name['niantic_friend_info'].message_type = _GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND_NIANTICFRIENDINFO
_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND.containing_type = _GETNIANTICFRIENDLISTRESPONSE
_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIENDINFO.fields_by_name['app_key'].enum_type = pogoprotos_dot_data_dot_social_dot_social__pb2._SOCIAL_APPKEY
_GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIENDINFO.containing_type = _GETNIANTICFRIENDLISTRESPONSE
_GETNIANTICFRIENDLISTRESPONSE.fields_by_name['result'].enum_type = _GETNIANTICFRIENDLISTRESPONSE_RESULT
_GETNIANTICFRIENDLISTRESPONSE.fields_by_name['niantic_friend'].message_type = _GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND
_GETNIANTICFRIENDLISTRESPONSE_RESULT.containing_type = _GETNIANTICFRIENDLISTRESPONSE
DESCRIPTOR.message_types_by_name['GetNianticFriendListResponse'] = _GETNIANTICFRIENDLISTRESPONSE

GetNianticFriendListResponse = _reflection.GeneratedProtocolMessageType('GetNianticFriendListResponse', (_message.Message,), dict(

  NianticFriend = _reflection.GeneratedProtocolMessageType('NianticFriend', (_message.Message,), dict(

    NianticFriendInfo = _reflection.GeneratedProtocolMessageType('NianticFriendInfo', (_message.Message,), dict(
      DESCRIPTOR = _GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND_NIANTICFRIENDINFO,
      __module__ = 'pogoprotos.networking.responses.social.responses.get_niantic_friend_list_response_pb2'
      # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend.NianticFriendInfo)
      ))
    ,
    DESCRIPTOR = _GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIEND,
    __module__ = 'pogoprotos.networking.responses.social.responses.get_niantic_friend_list_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriend)
    ))
  ,

  NianticFriendInfo = _reflection.GeneratedProtocolMessageType('NianticFriendInfo', (_message.Message,), dict(
    DESCRIPTOR = _GETNIANTICFRIENDLISTRESPONSE_NIANTICFRIENDINFO,
    __module__ = 'pogoprotos.networking.responses.social.responses.get_niantic_friend_list_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse.NianticFriendInfo)
    ))
  ,
  DESCRIPTOR = _GETNIANTICFRIENDLISTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.social.responses.get_niantic_friend_list_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.social.responses.GetNianticFriendListResponse)
  ))
_sym_db.RegisterMessage(GetNianticFriendListResponse)
_sym_db.RegisterMessage(GetNianticFriendListResponse.NianticFriend)
_sym_db.RegisterMessage(GetNianticFriendListResponse.NianticFriend.NianticFriendInfo)
_sym_db.RegisterMessage(GetNianticFriendListResponse.NianticFriendInfo)


# @@protoc_insertion_point(module_scope)
