# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/beluga/beluga_ble_finalize_transfer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.beluga import beluga_ble_transfer_complete_pb2 as pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__complete__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/beluga/beluga_ble_finalize_transfer.proto',
  package='pogoprotos.data.beluga',
  syntax='proto3',
  serialized_pb=_b('\n9pogoprotos/data/beluga/beluga_ble_finalize_transfer.proto\x12\x16pogoprotos.data.beluga\x1a\x39pogoprotos/data/beluga/beluga_ble_transfer_complete.proto\"\x8a\x01\n\x19\x42\x65lugaBleFinalizeTransfer\x12S\n\x18\x62\x65luga_transfer_complete\x18\x01 \x01(\x0b\x32\x31.pogoprotos.data.beluga.BelugaBleTransferComplete\x12\x18\n\x10server_signature\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__complete__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BELUGABLEFINALIZETRANSFER = _descriptor.Descriptor(
  name='BelugaBleFinalizeTransfer',
  full_name='pogoprotos.data.beluga.BelugaBleFinalizeTransfer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='beluga_transfer_complete', full_name='pogoprotos.data.beluga.BelugaBleFinalizeTransfer.beluga_transfer_complete', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_signature', full_name='pogoprotos.data.beluga.BelugaBleFinalizeTransfer.server_signature', index=1,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=283,
)

_BELUGABLEFINALIZETRANSFER.fields_by_name['beluga_transfer_complete'].message_type = pogoprotos_dot_data_dot_beluga_dot_beluga__ble__transfer__complete__pb2._BELUGABLETRANSFERCOMPLETE
DESCRIPTOR.message_types_by_name['BelugaBleFinalizeTransfer'] = _BELUGABLEFINALIZETRANSFER

BelugaBleFinalizeTransfer = _reflection.GeneratedProtocolMessageType('BelugaBleFinalizeTransfer', (_message.Message,), dict(
  DESCRIPTOR = _BELUGABLEFINALIZETRANSFER,
  __module__ = 'pogoprotos.data.beluga.beluga_ble_finalize_transfer_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.beluga.BelugaBleFinalizeTransfer)
  ))
_sym_db.RegisterMessage(BelugaBleFinalizeTransfer)


# @@protoc_insertion_point(module_scope)
