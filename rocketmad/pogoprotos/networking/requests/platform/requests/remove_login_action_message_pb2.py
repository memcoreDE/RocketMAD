# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/platform/requests/remove_login_action_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import identity_provider_pb2 as pogoprotos_dot_enums_dot_identity__provider__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/platform/requests/remove_login_action_message.proto',
  package='pogoprotos.networking.requests.platform.requests',
  syntax='proto3',
  serialized_pb=_b('\nRpogoprotos/networking/requests/platform/requests/remove_login_action_message.proto\x12\x30pogoprotos.networking.requests.platform.requests\x1a(pogoprotos/enums/identity_provider.proto\"s\n\x18RemoveLoginActionMessage\x12=\n\x11identity_provider\x18\x01 \x01(\x0e\x32\".pogoprotos.enums.IdentityProvider\x12\x18\n\x10\x61uth_provider_id\x18\x02 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_identity__provider__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REMOVELOGINACTIONMESSAGE = _descriptor.Descriptor(
  name='RemoveLoginActionMessage',
  full_name='pogoprotos.networking.requests.platform.requests.RemoveLoginActionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity_provider', full_name='pogoprotos.networking.requests.platform.requests.RemoveLoginActionMessage.identity_provider', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_provider_id', full_name='pogoprotos.networking.requests.platform.requests.RemoveLoginActionMessage.auth_provider_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=178,
  serialized_end=293,
)

_REMOVELOGINACTIONMESSAGE.fields_by_name['identity_provider'].enum_type = pogoprotos_dot_enums_dot_identity__provider__pb2._IDENTITYPROVIDER
DESCRIPTOR.message_types_by_name['RemoveLoginActionMessage'] = _REMOVELOGINACTIONMESSAGE

RemoveLoginActionMessage = _reflection.GeneratedProtocolMessageType('RemoveLoginActionMessage', (_message.Message,), dict(
  DESCRIPTOR = _REMOVELOGINACTIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.platform.requests.remove_login_action_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.platform.requests.RemoveLoginActionMessage)
  ))
_sym_db.RegisterMessage(RemoveLoginActionMessage)


# @@protoc_insertion_point(module_scope)
