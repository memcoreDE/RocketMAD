# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gamenotification/game_notification_action_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.requests.game.gamenotification import game_notification_action_pb2 as pogoprotos_dot_networking_dot_requests_dot_game_dot_gamenotification_dot_game__notification__action__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gamenotification/game_notification_action_request.proto',
  package='pogoprotos.networking.requests.game.gamenotification',
  syntax='proto3',
  serialized_pb=_b('\n[pogoprotos/networking/requests/game/gamenotification/game_notification_action_request.proto\x12\x34pogoprotos.networking.requests.game.gamenotification\x1aSpogoprotos/networking/requests/game/gamenotification/game_notification_action.proto\"\x9c\x01\n\x1dGameNotificationActionRequest\x12\x62\n\x0crequest_type\x18\x01 \x01(\x0e\x32L.pogoprotos.networking.requests.game.gamenotification.GameNotificationAction\x12\x17\n\x0frequest_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_requests_dot_game_dot_gamenotification_dot_game__notification__action__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GAMENOTIFICATIONACTIONREQUEST = _descriptor.Descriptor(
  name='GameNotificationActionRequest',
  full_name='pogoprotos.networking.requests.game.gamenotification.GameNotificationActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_type', full_name='pogoprotos.networking.requests.game.gamenotification.GameNotificationActionRequest.request_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_message', full_name='pogoprotos.networking.requests.game.gamenotification.GameNotificationActionRequest.request_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=235,
  serialized_end=391,
)

_GAMENOTIFICATIONACTIONREQUEST.fields_by_name['request_type'].enum_type = pogoprotos_dot_networking_dot_requests_dot_game_dot_gamenotification_dot_game__notification__action__pb2._GAMENOTIFICATIONACTION
DESCRIPTOR.message_types_by_name['GameNotificationActionRequest'] = _GAMENOTIFICATIONACTIONREQUEST

GameNotificationActionRequest = _reflection.GeneratedProtocolMessageType('GameNotificationActionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GAMENOTIFICATIONACTIONREQUEST,
  __module__ = 'pogoprotos.networking.requests.game.gamenotification.game_notification_action_request_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gamenotification.GameNotificationActionRequest)
  ))
_sym_db.RegisterMessage(GameNotificationActionRequest)


# @@protoc_insertion_point(module_scope)
