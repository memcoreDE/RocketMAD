# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gamepoi/requests/add_new_poi_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.player import player_reputation_pb2 as pogoprotos_dot_data_dot_player_dot_player__reputation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gamepoi/requests/add_new_poi_message.proto',
  package='pogoprotos.networking.requests.game.gamepoi.requests',
  syntax='proto3',
  serialized_pb=_b('\nNpogoprotos/networking/requests/game/gamepoi/requests/add_new_poi_message.proto\x12\x34pogoprotos.networking.requests.game.gamepoi.requests\x1a.pogoprotos/data/player/player_reputation.proto\"\xa9\x02\n\x10\x41\x64\x64NewPoiMessage\x12\r\n\x05title\x18\x01 \x01(\t\x12\x18\n\x10long_description\x18\x02 \x01(\t\x12\x1a\n\x12image_gs_file_path\x18\x03 \x01(\t\x12\x0e\n\x06lat_e6\x18\x04 \x01(\x05\x12\x0e\n\x06lng_e6\x18\x05 \x01(\x05\x12\x19\n\x11image_serving_url\x18\x06 \x01(\t\x12\x0f\n\x07user_id\x18\x07 \x01(\t\x12\x17\n\x0fplayer_language\x18\x08 \x01(\t\x12\x16\n\x0egame_unique_id\x18\t \x01(\t\x12\x0e\n\x06\x61pp_id\x18\n \x01(\t\x12\x43\n\x11player_reputation\x18\x0b \x01(\x0b\x32(.pogoprotos.data.player.PlayerReputationb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player_dot_player__reputation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ADDNEWPOIMESSAGE = _descriptor.Descriptor(
  name='AddNewPoiMessage',
  full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long_description', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.long_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_gs_file_path', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.image_gs_file_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat_e6', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.lat_e6', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lng_e6', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.lng_e6', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_serving_url', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.image_serving_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.user_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_language', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.player_language', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_unique_id', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.game_unique_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.app_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_reputation', full_name='pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage.player_reputation', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=185,
  serialized_end=482,
)

_ADDNEWPOIMESSAGE.fields_by_name['player_reputation'].message_type = pogoprotos_dot_data_dot_player_dot_player__reputation__pb2._PLAYERREPUTATION
DESCRIPTOR.message_types_by_name['AddNewPoiMessage'] = _ADDNEWPOIMESSAGE

AddNewPoiMessage = _reflection.GeneratedProtocolMessageType('AddNewPoiMessage', (_message.Message,), dict(
  DESCRIPTOR = _ADDNEWPOIMESSAGE,
  __module__ = 'pogoprotos.networking.requests.game.gamepoi.requests.add_new_poi_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gamepoi.requests.AddNewPoiMessage)
  ))
_sym_db.RegisterMessage(AddNewPoiMessage)


# @@protoc_insertion_point(module_scope)
