# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/vsseeker/vs_seeker_loot.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.vsseeker import vs_seeker_reward_track_pb2 as pogoprotos_dot_data_dot_vsseeker_dot_vs__seeker__reward__track__pb2
from pogoprotos.inventory import loot_item_pb2 as pogoprotos_dot_inventory_dot_loot__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/vsseeker/vs_seeker_loot.proto',
  package='pogoprotos.data.vsseeker',
  syntax='proto3',
  serialized_pb=_b('\n-pogoprotos/data/vsseeker/vs_seeker_loot.proto\x12\x18pogoprotos.data.vsseeker\x1a\x35pogoprotos/data/vsseeker/vs_seeker_reward_track.proto\x1a$pogoprotos/inventory/loot_item.proto\"\xee\x02\n\x0cVsSeekerLoot\x12\x12\n\nrank_level\x18\x01 \x01(\x05\x12=\n\x06reward\x18\x02 \x03(\x0b\x32-.pogoprotos.data.vsseeker.VsSeekerLoot.Reward\x12\x43\n\x0creward_track\x18\x03 \x01(\x0e\x32-.pogoprotos.data.vsseeker.VsSeekerRewardTrack\x1a\xc5\x01\n\x06Reward\x12.\n\x04item\x18\x01 \x01(\x0b\x32\x1e.pogoprotos.inventory.LootItemH\x00\x12\x18\n\x0epokemon_reward\x18\x02 \x01(\x08H\x00\x12\x19\n\x0fitem_loot_table\x18\x03 \x01(\x08H\x00\x12\x1f\n\x15item_loot_table_count\x18\x04 \x01(\x05H\x00\x12\'\n\x1ditem_ranking_loot_table_count\x18\x05 \x01(\x05H\x00\x42\x0c\n\nRewardTypeb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_vsseeker_dot_vs__seeker__reward__track__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_loot__item__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VSSEEKERLOOT_REWARD = _descriptor.Descriptor(
  name='Reward',
  full_name='pogoprotos.data.vsseeker.VsSeekerLoot.Reward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.Reward.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_reward', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.Reward.pokemon_reward', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_loot_table', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.Reward.item_loot_table', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_loot_table_count', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.Reward.item_loot_table_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_ranking_loot_table_count', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.Reward.item_ranking_loot_table_count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='RewardType', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.Reward.RewardType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=338,
  serialized_end=535,
)

_VSSEEKERLOOT = _descriptor.Descriptor(
  name='VsSeekerLoot',
  full_name='pogoprotos.data.vsseeker.VsSeekerLoot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank_level', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.rank_level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.reward', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_track', full_name='pogoprotos.data.vsseeker.VsSeekerLoot.reward_track', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VSSEEKERLOOT_REWARD, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=535,
)

_VSSEEKERLOOT_REWARD.fields_by_name['item'].message_type = pogoprotos_dot_inventory_dot_loot__item__pb2._LOOTITEM
_VSSEEKERLOOT_REWARD.containing_type = _VSSEEKERLOOT
_VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType'].fields.append(
  _VSSEEKERLOOT_REWARD.fields_by_name['item'])
_VSSEEKERLOOT_REWARD.fields_by_name['item'].containing_oneof = _VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType']
_VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType'].fields.append(
  _VSSEEKERLOOT_REWARD.fields_by_name['pokemon_reward'])
_VSSEEKERLOOT_REWARD.fields_by_name['pokemon_reward'].containing_oneof = _VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType']
_VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType'].fields.append(
  _VSSEEKERLOOT_REWARD.fields_by_name['item_loot_table'])
_VSSEEKERLOOT_REWARD.fields_by_name['item_loot_table'].containing_oneof = _VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType']
_VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType'].fields.append(
  _VSSEEKERLOOT_REWARD.fields_by_name['item_loot_table_count'])
_VSSEEKERLOOT_REWARD.fields_by_name['item_loot_table_count'].containing_oneof = _VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType']
_VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType'].fields.append(
  _VSSEEKERLOOT_REWARD.fields_by_name['item_ranking_loot_table_count'])
_VSSEEKERLOOT_REWARD.fields_by_name['item_ranking_loot_table_count'].containing_oneof = _VSSEEKERLOOT_REWARD.oneofs_by_name['RewardType']
_VSSEEKERLOOT.fields_by_name['reward'].message_type = _VSSEEKERLOOT_REWARD
_VSSEEKERLOOT.fields_by_name['reward_track'].enum_type = pogoprotos_dot_data_dot_vsseeker_dot_vs__seeker__reward__track__pb2._VSSEEKERREWARDTRACK
DESCRIPTOR.message_types_by_name['VsSeekerLoot'] = _VSSEEKERLOOT

VsSeekerLoot = _reflection.GeneratedProtocolMessageType('VsSeekerLoot', (_message.Message,), dict(

  Reward = _reflection.GeneratedProtocolMessageType('Reward', (_message.Message,), dict(
    DESCRIPTOR = _VSSEEKERLOOT_REWARD,
    __module__ = 'pogoprotos.data.vsseeker.vs_seeker_loot_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.vsseeker.VsSeekerLoot.Reward)
    ))
  ,
  DESCRIPTOR = _VSSEEKERLOOT,
  __module__ = 'pogoprotos.data.vsseeker.vs_seeker_loot_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.vsseeker.VsSeekerLoot)
  ))
_sym_db.RegisterMessage(VsSeekerLoot)
_sym_db.RegisterMessage(VsSeekerLoot.Reward)


# @@protoc_insertion_point(module_scope)
