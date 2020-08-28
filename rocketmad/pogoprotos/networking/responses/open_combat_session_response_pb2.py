# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/open_combat_session_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.combat import combat_pb2 as pogoprotos_dot_data_dot_combat_dot_combat__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/open_combat_session_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nBpogoprotos/networking/responses/open_combat_session_response.proto\x12\x1fpogoprotos.networking.responses\x1a#pogoprotos/data/combat/combat.proto\"\xd0\x04\n\x19OpenCombatSessionResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.pogoprotos.networking.responses.OpenCombatSessionResponse.Result\x12.\n\x06\x63ombat\x18\x02 \x01(\x0b\x32\x1e.pogoprotos.data.combat.Combat\x12\x18\n\x10should_debug_log\x18\x03 \x01(\x08\"\x95\x03\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1e\n\x1a\x45RROR_INVALID_COMBAT_STATE\x10\x02\x12\x1d\n\x19\x45RROR_COMBAT_SESSION_FULL\x10\x03\x12\"\n\x1e\x45RROR_POKEMON_NOT_IN_INVENTORY\x10\x04\x12\x1f\n\x1b\x45RROR_OPPONENT_NOT_IN_RANGE\x10\x05\x12\x1b\n\x17\x45RROR_CHALLENGE_EXPIRED\x10\x06\x12$\n ERROR_PLAYER_BELOW_MINIMUM_LEVEL\x10\x07\x12\x17\n\x13\x45RROR_OPPONENT_QUIT\x10\x08\x12.\n*ERROR_POKEMON_LINEUP_INELIGIBLE_FOR_LEAGUE\x10\t\x12#\n\x1f\x45RROR_COMBAT_LEAGUE_UNSPECIFIED\x10\n\x12\x17\n\x13\x45RROR_ACCESS_DENIED\x10\x0b\x12%\n!ERROR_PLAYER_HAS_NO_BATTLE_PASSES\x10\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_combat_dot_combat__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OPENCOMBATSESSIONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.OpenCombatSessionResponse.Result',
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
      name='ERROR_INVALID_COMBAT_STATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_COMBAT_SESSION_FULL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_IN_INVENTORY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_OPPONENT_NOT_IN_RANGE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CHALLENGE_EXPIRED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_BELOW_MINIMUM_LEVEL', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_OPPONENT_QUIT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_LINEUP_INELIGIBLE_FOR_LEAGUE', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_COMBAT_LEAGUE_UNSPECIFIED', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ACCESS_DENIED', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_HAS_NO_BATTLE_PASSES', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=328,
  serialized_end=733,
)
_sym_db.RegisterEnumDescriptor(_OPENCOMBATSESSIONRESPONSE_RESULT)


_OPENCOMBATSESSIONRESPONSE = _descriptor.Descriptor(
  name='OpenCombatSessionResponse',
  full_name='pogoprotos.networking.responses.OpenCombatSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.OpenCombatSessionResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat', full_name='pogoprotos.networking.responses.OpenCombatSessionResponse.combat', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='should_debug_log', full_name='pogoprotos.networking.responses.OpenCombatSessionResponse.should_debug_log', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OPENCOMBATSESSIONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=733,
)

_OPENCOMBATSESSIONRESPONSE.fields_by_name['result'].enum_type = _OPENCOMBATSESSIONRESPONSE_RESULT
_OPENCOMBATSESSIONRESPONSE.fields_by_name['combat'].message_type = pogoprotos_dot_data_dot_combat_dot_combat__pb2._COMBAT
_OPENCOMBATSESSIONRESPONSE_RESULT.containing_type = _OPENCOMBATSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['OpenCombatSessionResponse'] = _OPENCOMBATSESSIONRESPONSE

OpenCombatSessionResponse = _reflection.GeneratedProtocolMessageType('OpenCombatSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPENCOMBATSESSIONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.open_combat_session_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.OpenCombatSessionResponse)
  ))
_sym_db.RegisterMessage(OpenCombatSessionResponse)


# @@protoc_insertion_point(module_scope)
