# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/platform/requests/redeem_passcode_message.proto

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
  name='pogoprotos/networking/requests/platform/requests/redeem_passcode_message.proto',
  package='pogoprotos.networking.requests.platform.requests',
  syntax='proto3',
  serialized_pb=_b('\nNpogoprotos/networking/requests/platform/requests/redeem_passcode_message.proto\x12\x30pogoprotos.networking.requests.platform.requests\"\'\n\x15RedeemPasscodeMessage\x12\x0e\n\x06qrcode\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REDEEMPASSCODEMESSAGE = _descriptor.Descriptor(
  name='RedeemPasscodeMessage',
  full_name='pogoprotos.networking.requests.platform.requests.RedeemPasscodeMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='qrcode', full_name='pogoprotos.networking.requests.platform.requests.RedeemPasscodeMessage.qrcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=132,
  serialized_end=171,
)

DESCRIPTOR.message_types_by_name['RedeemPasscodeMessage'] = _REDEEMPASSCODEMESSAGE

RedeemPasscodeMessage = _reflection.GeneratedProtocolMessageType('RedeemPasscodeMessage', (_message.Message,), dict(
  DESCRIPTOR = _REDEEMPASSCODEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.platform.requests.redeem_passcode_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.platform.requests.RedeemPasscodeMessage)
  ))
_sym_db.RegisterMessage(RedeemPasscodeMessage)


# @@protoc_insertion_point(module_scope)
