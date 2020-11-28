# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/convert_candy_to_xl_candy_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/convert_candy_to_xl_candy_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nHpogoprotos/networking/responses/convert_candy_to_xl_candy_response.proto\x12\x1fpogoprotos.networking.responses\"\xd4\x01\n\x1d\x43onvertCandyToXlCandyResponse\x12U\n\x06status\x18\x01 \x01(\x0e\x32\x45.pogoprotos.networking.responses.ConvertCandyToXlCandyResponse.Status\"\\\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x45RROR_NOT_ENOUGH_CANDY\x10\x02\x12\x1e\n\x1a\x45RROR_PLAYER_LEVEL_TOO_LOW\x10\x03\x62\x06proto3')
)



_CONVERTCANDYTOXLCANDYRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.ConvertCandyToXlCandyResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_ENOUGH_CANDY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_LEVEL_TOO_LOW', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=230,
  serialized_end=322,
)
_sym_db.RegisterEnumDescriptor(_CONVERTCANDYTOXLCANDYRESPONSE_STATUS)


_CONVERTCANDYTOXLCANDYRESPONSE = _descriptor.Descriptor(
  name='ConvertCandyToXlCandyResponse',
  full_name='pogoprotos.networking.responses.ConvertCandyToXlCandyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.ConvertCandyToXlCandyResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONVERTCANDYTOXLCANDYRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=322,
)

_CONVERTCANDYTOXLCANDYRESPONSE.fields_by_name['status'].enum_type = _CONVERTCANDYTOXLCANDYRESPONSE_STATUS
_CONVERTCANDYTOXLCANDYRESPONSE_STATUS.containing_type = _CONVERTCANDYTOXLCANDYRESPONSE
DESCRIPTOR.message_types_by_name['ConvertCandyToXlCandyResponse'] = _CONVERTCANDYTOXLCANDYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConvertCandyToXlCandyResponse = _reflection.GeneratedProtocolMessageType('ConvertCandyToXlCandyResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONVERTCANDYTOXLCANDYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.convert_candy_to_xl_candy_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.ConvertCandyToXlCandyResponse)
  ))
_sym_db.RegisterMessage(ConvertCandyToXlCandyResponse)


# @@protoc_insertion_point(module_scope)
