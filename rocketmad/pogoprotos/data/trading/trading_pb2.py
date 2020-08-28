# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/trading/trading.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.trading import trading_player_pb2 as pogoprotos_dot_data_dot_trading_dot_trading__player__pb2
from pogoprotos.data.friends import friendship_level_data_pb2 as pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/trading/trading.proto',
  package='pogoprotos.data.trading',
  syntax='proto3',
  serialized_pb=_b('\n%pogoprotos/data/trading/trading.proto\x12\x17pogoprotos.data.trading\x1a,pogoprotos/data/trading/trading_player.proto\x1a\x33pogoprotos/data/friends/friendship_level_data.proto\"\x9e\x04\n\x07Trading\x12<\n\x05state\x18\x01 \x01(\x0e\x32-.pogoprotos.data.trading.Trading.TradingState\x12\x15\n\rexpiration_ms\x18\x02 \x01(\x04\x12\x36\n\x06player\x18\x03 \x01(\x0b\x32&.pogoprotos.data.trading.TradingPlayer\x12\x36\n\x06\x66riend\x18\x04 \x01(\x0b\x32&.pogoprotos.data.trading.TradingPlayer\x12\x1a\n\x12trading_s2_cell_id\x18\x05 \x01(\x03\x12\x17\n\x0ftransaction_log\x18\x06 \x01(\t\x12K\n\x15\x66riendship_level_data\x18\x07 \x01(\x0b\x32,.pogoprotos.data.friends.FriendshipLevelData\x12\x1a\n\x12is_special_trading\x18\x08 \x01(\x08\x12R\n\x1cpre_trading_friendship_level\x18\t \x01(\x0b\x32,.pogoprotos.data.friends.FriendshipLevelData\"\\\n\x0cTradingState\x12\t\n\x05UNSET\x10\x00\x12\x0e\n\nPRIMORDIAL\x10\x01\x12\x08\n\x04WAIT\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\x12\r\n\tCONFIRMED\x10\x04\x12\x0c\n\x08\x46INISHED\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_trading_dot_trading__player__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TRADING_TRADINGSTATE = _descriptor.EnumDescriptor(
  name='TradingState',
  full_name='pogoprotos.data.trading.Trading.TradingState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIMORDIAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WAIT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRMED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISHED', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=616,
  serialized_end=708,
)
_sym_db.RegisterEnumDescriptor(_TRADING_TRADINGSTATE)


_TRADING = _descriptor.Descriptor(
  name='Trading',
  full_name='pogoprotos.data.trading.Trading',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='pogoprotos.data.trading.Trading.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration_ms', full_name='pogoprotos.data.trading.Trading.expiration_ms', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player', full_name='pogoprotos.data.trading.Trading.player', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend', full_name='pogoprotos.data.trading.Trading.friend', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trading_s2_cell_id', full_name='pogoprotos.data.trading.Trading.trading_s2_cell_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_log', full_name='pogoprotos.data.trading.Trading.transaction_log', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friendship_level_data', full_name='pogoprotos.data.trading.Trading.friendship_level_data', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_special_trading', full_name='pogoprotos.data.trading.Trading.is_special_trading', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_trading_friendship_level', full_name='pogoprotos.data.trading.Trading.pre_trading_friendship_level', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRADING_TRADINGSTATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=708,
)

_TRADING.fields_by_name['state'].enum_type = _TRADING_TRADINGSTATE
_TRADING.fields_by_name['player'].message_type = pogoprotos_dot_data_dot_trading_dot_trading__player__pb2._TRADINGPLAYER
_TRADING.fields_by_name['friend'].message_type = pogoprotos_dot_data_dot_trading_dot_trading__player__pb2._TRADINGPLAYER
_TRADING.fields_by_name['friendship_level_data'].message_type = pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2._FRIENDSHIPLEVELDATA
_TRADING.fields_by_name['pre_trading_friendship_level'].message_type = pogoprotos_dot_data_dot_friends_dot_friendship__level__data__pb2._FRIENDSHIPLEVELDATA
_TRADING_TRADINGSTATE.containing_type = _TRADING
DESCRIPTOR.message_types_by_name['Trading'] = _TRADING

Trading = _reflection.GeneratedProtocolMessageType('Trading', (_message.Message,), dict(
  DESCRIPTOR = _TRADING,
  __module__ = 'pogoprotos.data.trading.trading_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.trading.Trading)
  ))
_sym_db.RegisterMessage(Trading)


# @@protoc_insertion_point(module_scope)
