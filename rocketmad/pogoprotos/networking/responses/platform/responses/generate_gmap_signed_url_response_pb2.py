# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/platform/responses/generate_gmap_signed_url_response.proto

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
  name='pogoprotos/networking/responses/platform/responses/generate_gmap_signed_url_response.proto',
  package='pogoprotos.networking.responses.platform.responses',
  syntax='proto3',
  serialized_pb=_b('\nZpogoprotos/networking/responses/platform/responses/generate_gmap_signed_url_response.proto\x12\x32pogoprotos.networking.responses.platform.responses\"\xa0\x02\n\x1dGenerateGmapSignedUrlResponse\x12h\n\x06result\x18\x01 \x01(\x0e\x32X.pogoprotos.networking.responses.platform.responses.GenerateGmapSignedUrlResponse.Result\x12\x12\n\nsigned_url\x18\x02 \x01(\t\"\x80\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1a\n\x16\x45RROR_PLAYER_NOT_VALID\x10\x02\x12\x16\n\x12\x45RROR_RATE_LIMITED\x10\x03\x12\x17\n\x13\x45RROR_MISSING_INPUT\x10\x04\x12\x11\n\rERROR_UNKNOWN\x10\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GENERATEGMAPSIGNEDURLRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.platform.responses.GenerateGmapSignedUrlResponse.Result',
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
      name='ERROR_PLAYER_NOT_VALID', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_RATE_LIMITED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MISSING_INPUT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UNKNOWN', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=307,
  serialized_end=435,
)
_sym_db.RegisterEnumDescriptor(_GENERATEGMAPSIGNEDURLRESPONSE_RESULT)


_GENERATEGMAPSIGNEDURLRESPONSE = _descriptor.Descriptor(
  name='GenerateGmapSignedUrlResponse',
  full_name='pogoprotos.networking.responses.platform.responses.GenerateGmapSignedUrlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.platform.responses.GenerateGmapSignedUrlResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signed_url', full_name='pogoprotos.networking.responses.platform.responses.GenerateGmapSignedUrlResponse.signed_url', index=1,
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
    _GENERATEGMAPSIGNEDURLRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=435,
)

_GENERATEGMAPSIGNEDURLRESPONSE.fields_by_name['result'].enum_type = _GENERATEGMAPSIGNEDURLRESPONSE_RESULT
_GENERATEGMAPSIGNEDURLRESPONSE_RESULT.containing_type = _GENERATEGMAPSIGNEDURLRESPONSE
DESCRIPTOR.message_types_by_name['GenerateGmapSignedUrlResponse'] = _GENERATEGMAPSIGNEDURLRESPONSE

GenerateGmapSignedUrlResponse = _reflection.GeneratedProtocolMessageType('GenerateGmapSignedUrlResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENERATEGMAPSIGNEDURLRESPONSE,
  __module__ = 'pogoprotos.networking.responses.platform.responses.generate_gmap_signed_url_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.platform.responses.GenerateGmapSignedUrlResponse)
  ))
_sym_db.RegisterMessage(GenerateGmapSignedUrlResponse)


# @@protoc_insertion_point(module_scope)
