# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/decline_ex_raid_pass_log_entry.proto

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
  name='pogoprotos/data/logs/decline_ex_raid_pass_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_pb=_b('\n9pogoprotos/data/logs/decline_ex_raid_pass_log_entry.proto\x12\x14pogoprotos.data.logs\"\x9e\x01\n\x19\x44\x65\x63lineExRaidPassLogEntry\x12\x46\n\x06result\x18\x01 \x01(\x0e\x32\x36.pogoprotos.data.logs.DeclineExRaidPassLogEntry.Result\x12\x17\n\x0f\x66riend_codename\x18\x02 \x01(\t\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DECLINEEXRAIDPASSLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.DeclineExRaidPassLogEntry.Result',
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
  serialized_start=210,
  serialized_end=242,
)
_sym_db.RegisterEnumDescriptor(_DECLINEEXRAIDPASSLOGENTRY_RESULT)


_DECLINEEXRAIDPASSLOGENTRY = _descriptor.Descriptor(
  name='DeclineExRaidPassLogEntry',
  full_name='pogoprotos.data.logs.DeclineExRaidPassLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.DeclineExRaidPassLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_codename', full_name='pogoprotos.data.logs.DeclineExRaidPassLogEntry.friend_codename', index=1,
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
    _DECLINEEXRAIDPASSLOGENTRY_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=242,
)

_DECLINEEXRAIDPASSLOGENTRY.fields_by_name['result'].enum_type = _DECLINEEXRAIDPASSLOGENTRY_RESULT
_DECLINEEXRAIDPASSLOGENTRY_RESULT.containing_type = _DECLINEEXRAIDPASSLOGENTRY
DESCRIPTOR.message_types_by_name['DeclineExRaidPassLogEntry'] = _DECLINEEXRAIDPASSLOGENTRY

DeclineExRaidPassLogEntry = _reflection.GeneratedProtocolMessageType('DeclineExRaidPassLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _DECLINEEXRAIDPASSLOGENTRY,
  __module__ = 'pogoprotos.data.logs.decline_ex_raid_pass_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.DeclineExRaidPassLogEntry)
  ))
_sym_db.RegisterMessage(DeclineExRaidPassLogEntry)


# @@protoc_insertion_point(module_scope)
