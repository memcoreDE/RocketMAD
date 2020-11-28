# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/unlink_nintendo_account_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/unlink_nintendo_account_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFpogoprotos/networking/responses/unlink_nintendo_account_response.proto\x12\x1fpogoprotos.networking.responses\"\xf4\x01\n\x1dUnlinkNintendoAccountResponse\x12U\n\x06status\x18\x01 \x01(\x0e\x32\x45.pogoprotos.networking.responses.UnlinkNintendoAccountResponse.Status\"|\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1e\n\x1a\x45RROR_PLAYER_LEVEL_TOO_LOW\x10\x02\x12\x18\n\x14\x45RROR_NO_LINKED_NAID\x10\x03\x12\x1e\n\x1a\x45RROR_TRANSFER_IN_PROGRESS\x10\x04\x62\x06proto3')
)



_UNLINKNINTENDOACCOUNTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.UnlinkNintendoAccountResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_LEVEL_TOO_LOW', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_LINKED_NAID', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_TRANSFER_IN_PROGRESS', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=228,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_UNLINKNINTENDOACCOUNTRESPONSE_STATUS)


_UNLINKNINTENDOACCOUNTRESPONSE = _descriptor.Descriptor(
  name='UnlinkNintendoAccountResponse',
  full_name='pogoprotos.networking.responses.UnlinkNintendoAccountResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.UnlinkNintendoAccountResponse.status', index=0,
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
    _UNLINKNINTENDOACCOUNTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=352,
)

_UNLINKNINTENDOACCOUNTRESPONSE.fields_by_name['status'].enum_type = _UNLINKNINTENDOACCOUNTRESPONSE_STATUS
_UNLINKNINTENDOACCOUNTRESPONSE_STATUS.containing_type = _UNLINKNINTENDOACCOUNTRESPONSE
DESCRIPTOR.message_types_by_name['UnlinkNintendoAccountResponse'] = _UNLINKNINTENDOACCOUNTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnlinkNintendoAccountResponse = _reflection.GeneratedProtocolMessageType('UnlinkNintendoAccountResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNLINKNINTENDOACCOUNTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.unlink_nintendo_account_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UnlinkNintendoAccountResponse)
  ))
_sym_db.RegisterMessage(UnlinkNintendoAccountResponse)


# @@protoc_insertion_point(module_scope)
