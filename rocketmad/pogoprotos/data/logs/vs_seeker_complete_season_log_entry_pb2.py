# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/vs_seeker_complete_season_log_entry.proto

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
  name='pogoprotos/data/logs/vs_seeker_complete_season_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_pb=_b('\n>pogoprotos/data/logs/vs_seeker_complete_season_log_entry.proto\x12\x14pogoprotos.data.logs\x1a\x1fpogoprotos/inventory/loot.proto\"\xda\x01\n\x1eVsSeekerCompleteSeasonLogEntry\x12K\n\x06result\x18\x01 \x01(\x0e\x32;.pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntry.Result\x12+\n\x07rewards\x18\x02 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12\x0c\n\x04rank\x18\x03 \x01(\x05\x12\x0e\n\x06rating\x18\x04 \x01(\x02\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_VSSEEKERCOMPLETESEASONLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntry.Result',
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
  serialized_start=308,
  serialized_end=340,
)
_sym_db.RegisterEnumDescriptor(_VSSEEKERCOMPLETESEASONLOGENTRY_RESULT)


_VSSEEKERCOMPLETESEASONLOGENTRY = _descriptor.Descriptor(
  name='VsSeekerCompleteSeasonLogEntry',
  full_name='pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntry.rewards', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntry.rank', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rating', full_name='pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntry.rating', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VSSEEKERCOMPLETESEASONLOGENTRY_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=340,
)

_VSSEEKERCOMPLETESEASONLOGENTRY.fields_by_name['result'].enum_type = _VSSEEKERCOMPLETESEASONLOGENTRY_RESULT
_VSSEEKERCOMPLETESEASONLOGENTRY.fields_by_name['rewards'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_VSSEEKERCOMPLETESEASONLOGENTRY_RESULT.containing_type = _VSSEEKERCOMPLETESEASONLOGENTRY
DESCRIPTOR.message_types_by_name['VsSeekerCompleteSeasonLogEntry'] = _VSSEEKERCOMPLETESEASONLOGENTRY

VsSeekerCompleteSeasonLogEntry = _reflection.GeneratedProtocolMessageType('VsSeekerCompleteSeasonLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _VSSEEKERCOMPLETESEASONLOGENTRY,
  __module__ = 'pogoprotos.data.logs.vs_seeker_complete_season_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.VsSeekerCompleteSeasonLogEntry)
  ))
_sym_db.RegisterMessage(VsSeekerCompleteSeasonLogEntry)


# @@protoc_insertion_point(module_scope)
