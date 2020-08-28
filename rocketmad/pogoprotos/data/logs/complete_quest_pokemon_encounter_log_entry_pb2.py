# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/complete_quest_pokemon_encounter_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import encounter_type_pb2 as pogoprotos_dot_enums_dot_encounter__type__pb2
from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/complete_quest_pokemon_encounter_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_pb=_b('\nEpogoprotos/data/logs/complete_quest_pokemon_encounter_log_entry.proto\x12\x14pogoprotos.data.logs\x1a%pogoprotos/enums/encounter_type.proto\x1a%pogoprotos/data/pokemon_display.proto\"\xee\x02\n%CompleteQuestPokemonEncounterLogEntry\x12R\n\x06result\x18\x01 \x01(\x0e\x32\x42.pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry.Result\x12\x16\n\x0epokedex_number\x18\x02 \x01(\x05\x12\x15\n\rcombat_points\x18\x03 \x01(\x05\x12\x12\n\npokemon_id\x18\x04 \x01(\x06\x12\x38\n\x0fpokemon_display\x18\x05 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12\x37\n\x0e\x65ncounter_type\x18\x06 \x01(\x0e\x32\x1f.pogoprotos.enums.EncounterType\";\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x14\n\x10POKEMON_CAPTURED\x10\x01\x12\x10\n\x0cPOKEMON_FLED\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_encounter__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_CAPTURED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_FLED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=481,
  serialized_end=540,
)
_sym_db.RegisterEnumDescriptor(_COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY_RESULT)


_COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY = _descriptor.Descriptor(
  name='CompleteQuestPokemonEncounterLogEntry',
  full_name='pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokedex_number', full_name='pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry.pokedex_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_points', full_name='pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry.combat_points', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry.pokemon_id', index=3,
      number=4, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry.pokemon_display', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_type', full_name='pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry.encounter_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=540,
)

_COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY.fields_by_name['result'].enum_type = _COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY_RESULT
_COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY.fields_by_name['encounter_type'].enum_type = pogoprotos_dot_enums_dot_encounter__type__pb2._ENCOUNTERTYPE
_COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY_RESULT.containing_type = _COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY
DESCRIPTOR.message_types_by_name['CompleteQuestPokemonEncounterLogEntry'] = _COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY

CompleteQuestPokemonEncounterLogEntry = _reflection.GeneratedProtocolMessageType('CompleteQuestPokemonEncounterLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _COMPLETEQUESTPOKEMONENCOUNTERLOGENTRY,
  __module__ = 'pogoprotos.data.logs.complete_quest_pokemon_encounter_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.CompleteQuestPokemonEncounterLogEntry)
  ))
_sym_db.RegisterMessage(CompleteQuestPokemonEncounterLogEntry)


# @@protoc_insertion_point(module_scope)
