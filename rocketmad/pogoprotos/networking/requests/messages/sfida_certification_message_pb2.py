# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/sfida_certification_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/sfida_certification_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nIpogoprotos/networking/requests/messages/sfida_certification_message.proto\x12\'pogoprotos.networking.requests.messages\"\xe1\x01\n\x19SfidaCertificationMessage\x12i\n\x05stage\x18\x01 \x01(\x0e\x32Z.pogoprotos.networking.requests.messages.SfidaCertificationMessage.SfidaCertificationStage\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"H\n\x17SfidaCertificationStage\x12\t\n\x05UNSET\x10\x00\x12\n\n\x06STAGE1\x10\x01\x12\n\n\x06STAGE2\x10\x02\x12\n\n\x06STAGE3\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SFIDACERTIFICATIONMESSAGE_SFIDACERTIFICATIONSTAGE = _descriptor.EnumDescriptor(
  name='SfidaCertificationStage',
  full_name='pogoprotos.networking.requests.messages.SfidaCertificationMessage.SfidaCertificationStage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE2', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE3', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=272,
  serialized_end=344,
)
_sym_db.RegisterEnumDescriptor(_SFIDACERTIFICATIONMESSAGE_SFIDACERTIFICATIONSTAGE)


_SFIDACERTIFICATIONMESSAGE = _descriptor.Descriptor(
  name='SfidaCertificationMessage',
  full_name='pogoprotos.networking.requests.messages.SfidaCertificationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage', full_name='pogoprotos.networking.requests.messages.SfidaCertificationMessage.stage', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='pogoprotos.networking.requests.messages.SfidaCertificationMessage.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SFIDACERTIFICATIONMESSAGE_SFIDACERTIFICATIONSTAGE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=344,
)

_SFIDACERTIFICATIONMESSAGE.fields_by_name['stage'].enum_type = _SFIDACERTIFICATIONMESSAGE_SFIDACERTIFICATIONSTAGE
_SFIDACERTIFICATIONMESSAGE_SFIDACERTIFICATIONSTAGE.containing_type = _SFIDACERTIFICATIONMESSAGE
DESCRIPTOR.message_types_by_name['SfidaCertificationMessage'] = _SFIDACERTIFICATIONMESSAGE

SfidaCertificationMessage = _reflection.GeneratedProtocolMessageType('SfidaCertificationMessage', (_message.Message,), dict(
  DESCRIPTOR = _SFIDACERTIFICATIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.sfida_certification_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SfidaCertificationMessage)
  ))
_sym_db.RegisterMessage(SfidaCertificationMessage)


# @@protoc_insertion_point(module_scope)
