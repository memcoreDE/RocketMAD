# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_npc_combat_rewards_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import combat_player_finish_state_pb2 as pogoprotos_dot_enums_dot_combat__player__finish__state__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/get_npc_combat_rewards_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nLpogoprotos/networking/requests/messages/get_npc_combat_rewards_message.proto\x12\'pogoprotos.networking.requests.messages\x1a\x31pogoprotos/enums/combat_player_finish_state.proto\"\xb6\x01\n\x1aGetNpcCombatRewardsMessage\x12&\n\x1e\x63ombat_npc_trainer_template_id\x18\x01 \x01(\t\x12?\n\x0c\x66inish_state\x18\x02 \x01(\x0e\x32).pogoprotos.enums.CombatPlayerFinishState\x12\x1c\n\x14\x61ttacking_pokemon_id\x18\x03 \x03(\x06\x12\x11\n\tcombat_id\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_combat__player__finish__state__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETNPCCOMBATREWARDSMESSAGE = _descriptor.Descriptor(
  name='GetNpcCombatRewardsMessage',
  full_name='pogoprotos.networking.requests.messages.GetNpcCombatRewardsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='combat_npc_trainer_template_id', full_name='pogoprotos.networking.requests.messages.GetNpcCombatRewardsMessage.combat_npc_trainer_template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish_state', full_name='pogoprotos.networking.requests.messages.GetNpcCombatRewardsMessage.finish_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attacking_pokemon_id', full_name='pogoprotos.networking.requests.messages.GetNpcCombatRewardsMessage.attacking_pokemon_id', index=2,
      number=3, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combat_id', full_name='pogoprotos.networking.requests.messages.GetNpcCombatRewardsMessage.combat_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=173,
  serialized_end=355,
)

_GETNPCCOMBATREWARDSMESSAGE.fields_by_name['finish_state'].enum_type = pogoprotos_dot_enums_dot_combat__player__finish__state__pb2._COMBATPLAYERFINISHSTATE
DESCRIPTOR.message_types_by_name['GetNpcCombatRewardsMessage'] = _GETNPCCOMBATREWARDSMESSAGE

GetNpcCombatRewardsMessage = _reflection.GeneratedProtocolMessageType('GetNpcCombatRewardsMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETNPCCOMBATREWARDSMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.get_npc_combat_rewards_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetNpcCombatRewardsMessage)
  ))
_sym_db.RegisterMessage(GetNpcCombatRewardsMessage)


# @@protoc_insertion_point(module_scope)
