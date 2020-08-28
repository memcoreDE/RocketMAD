# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/open_gift_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/open_gift_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/data/logs/open_gift_log_entry.proto\x12\x14pogoprotos.data.logs\x1a\"pogoprotos/data/pokemon_data.proto\x1a\x1fpogoprotos/inventory/loot.proto\"\xeb\x01\n\x10OpenGiftLogEntry\x12=\n\x06result\x18\x01 \x01(\x0e\x32-.pogoprotos.data.logs.OpenGiftLogEntry.Result\x12\x17\n\x0f\x66riend_codename\x18\x02 \x01(\t\x12)\n\x05items\x18\x03 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12\x32\n\x0cpokemon_eggs\x18\x04 \x03(\x0b\x32\x1c.pogoprotos.data.PokemonData\" \n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OPENGIFTLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.OpenGiftLogEntry.Result',
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
  serialized_start=345,
  serialized_end=377,
)
_sym_db.RegisterEnumDescriptor(_OPENGIFTLOGENTRY_RESULT)


_OPENGIFTLOGENTRY = _descriptor.Descriptor(
  name='OpenGiftLogEntry',
  full_name='pogoprotos.data.logs.OpenGiftLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.OpenGiftLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_codename', full_name='pogoprotos.data.logs.OpenGiftLogEntry.friend_codename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='pogoprotos.data.logs.OpenGiftLogEntry.items', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_eggs', full_name='pogoprotos.data.logs.OpenGiftLogEntry.pokemon_eggs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPENGIFTLOGENTRY_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=377,
)

_OPENGIFTLOGENTRY.fields_by_name['result'].enum_type = _OPENGIFTLOGENTRY_RESULT
_OPENGIFTLOGENTRY.fields_by_name['items'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_OPENGIFTLOGENTRY.fields_by_name['pokemon_eggs'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_OPENGIFTLOGENTRY_RESULT.containing_type = _OPENGIFTLOGENTRY
DESCRIPTOR.message_types_by_name['OpenGiftLogEntry'] = _OPENGIFTLOGENTRY

OpenGiftLogEntry = _reflection.GeneratedProtocolMessageType('OpenGiftLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _OPENGIFTLOGENTRY,
  __module__ = 'pogoprotos.data.logs.open_gift_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.OpenGiftLogEntry)
  ))
_sym_db.RegisterMessage(OpenGiftLogEntry)


# @@protoc_insertion_point(module_scope)
