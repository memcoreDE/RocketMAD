# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/game/gameaccountregistry/responses/remove_login_action_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.login import login_detail_pb2 as pogoprotos_dot_data_dot_login_dot_login__detail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/game/gameaccountregistry/responses/remove_login_action_response.proto',
  package='pogoprotos.networking.responses.game.gameaccountregistry.responses',
  syntax='proto3',
  serialized_pb=_b('\nepogoprotos/networking/responses/game/gameaccountregistry/responses/remove_login_action_response.proto\x12\x42pogoprotos.networking.responses.game.gameaccountregistry.responses\x1a(pogoprotos/data/login/login_detail.proto\"\x8a\x02\n\x19RemoveLoginActionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x38\n\x0clogin_detail\x18\x02 \x03(\x0b\x32\".pogoprotos.data.login.LoginDetail\x12t\n\x06status\x18\x03 \x01(\x0e\x32\x64.pogoprotos.networking.responses.game.gameaccountregistry.responses.RemoveLoginActionResponse.Status\",\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x17\n\x13LOGIN_NOT_REMOVABLE\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_login_dot_login__detail__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REMOVELOGINACTIONRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.game.gameaccountregistry.responses.RemoveLoginActionResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGIN_NOT_REMOVABLE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=438,
  serialized_end=482,
)
_sym_db.RegisterEnumDescriptor(_REMOVELOGINACTIONRESPONSE_STATUS)


_REMOVELOGINACTIONRESPONSE = _descriptor.Descriptor(
  name='RemoveLoginActionResponse',
  full_name='pogoprotos.networking.responses.game.gameaccountregistry.responses.RemoveLoginActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.networking.responses.game.gameaccountregistry.responses.RemoveLoginActionResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='login_detail', full_name='pogoprotos.networking.responses.game.gameaccountregistry.responses.RemoveLoginActionResponse.login_detail', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.game.gameaccountregistry.responses.RemoveLoginActionResponse.status', index=2,
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
    _REMOVELOGINACTIONRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=482,
)

_REMOVELOGINACTIONRESPONSE.fields_by_name['login_detail'].message_type = pogoprotos_dot_data_dot_login_dot_login__detail__pb2._LOGINDETAIL
_REMOVELOGINACTIONRESPONSE.fields_by_name['status'].enum_type = _REMOVELOGINACTIONRESPONSE_STATUS
_REMOVELOGINACTIONRESPONSE_STATUS.containing_type = _REMOVELOGINACTIONRESPONSE
DESCRIPTOR.message_types_by_name['RemoveLoginActionResponse'] = _REMOVELOGINACTIONRESPONSE

RemoveLoginActionResponse = _reflection.GeneratedProtocolMessageType('RemoveLoginActionResponse', (_message.Message,), dict(
  DESCRIPTOR = _REMOVELOGINACTIONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.game.gameaccountregistry.responses.remove_login_action_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.game.gameaccountregistry.responses.RemoveLoginActionResponse)
  ))
_sym_db.RegisterMessage(RemoveLoginActionResponse)


# @@protoc_insertion_point(module_scope)
