# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/beluga_daily_transfer_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/beluga_daily_transfer_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_pb=_b('\n:pogoprotos/data/logs/beluga_daily_transfer_log_entry.proto\x12\x14pogoprotos.data.logs\x1a\x1fpogoprotos/inventory/loot.proto\"\xdb\x01\n\x1b\x42\x65lugaDailyTransferLogEntry\x12H\n\x06result\x18\x01 \x01(\x0e\x32\x38.pogoprotos.data.logs.BelugaDailyTransferLogEntry.Result\x12\x1d\n\x15includes_weekly_bonus\x18\x02 \x01(\x08\x12\x31\n\ritems_awarded\x18\x03 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BELUGADAILYTRANSFERLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.BelugaDailyTransferLogEntry.Result',
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
  ],
  containing_type=None,
  options=None,
  serialized_start=305,
  serialized_end=337,
)
_sym_db.RegisterEnumDescriptor(_BELUGADAILYTRANSFERLOGENTRY_RESULT)


_BELUGADAILYTRANSFERLOGENTRY = _descriptor.Descriptor(
  name='BelugaDailyTransferLogEntry',
  full_name='pogoprotos.data.logs.BelugaDailyTransferLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.BelugaDailyTransferLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='includes_weekly_bonus', full_name='pogoprotos.data.logs.BelugaDailyTransferLogEntry.includes_weekly_bonus', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items_awarded', full_name='pogoprotos.data.logs.BelugaDailyTransferLogEntry.items_awarded', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BELUGADAILYTRANSFERLOGENTRY_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=337,
)

_BELUGADAILYTRANSFERLOGENTRY.fields_by_name['result'].enum_type = _BELUGADAILYTRANSFERLOGENTRY_RESULT
_BELUGADAILYTRANSFERLOGENTRY.fields_by_name['items_awarded'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_BELUGADAILYTRANSFERLOGENTRY_RESULT.containing_type = _BELUGADAILYTRANSFERLOGENTRY
DESCRIPTOR.message_types_by_name['BelugaDailyTransferLogEntry'] = _BELUGADAILYTRANSFERLOGENTRY

BelugaDailyTransferLogEntry = _reflection.GeneratedProtocolMessageType('BelugaDailyTransferLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _BELUGADAILYTRANSFERLOGENTRY,
  __module__ = 'pogoprotos.data.logs.beluga_daily_transfer_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.BelugaDailyTransferLogEntry)
  ))
_sym_db.RegisterMessage(BelugaDailyTransferLogEntry)


# @@protoc_insertion_point(module_scope)
