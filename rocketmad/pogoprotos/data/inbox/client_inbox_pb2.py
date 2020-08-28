# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/inbox/client_inbox.proto

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
  name='pogoprotos/data/inbox/client_inbox.proto',
  package='pogoprotos.data.inbox',
  syntax='proto3',
  serialized_pb=_b('\n(pogoprotos/data/inbox/client_inbox.proto\x12\x15pogoprotos.data.inbox\"\x86\x0e\n\x0b\x43lientInbox\x12\x46\n\rnotifications\x18\x01 \x03(\x0b\x32/.pogoprotos.data.inbox.ClientInbox.Notification\x12N\n\x11\x62uiltin_variables\x18\x02 \x03(\x0b\x32\x33.pogoprotos.data.inbox.ClientInbox.TemplateVariable\x1a\xce\x02\n\x0cNotification\x12\x17\n\x0fnotification_id\x18\x01 \x01(\t\x12\x11\n\ttitle_key\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\t\x12\x1b\n\x13\x63reate_timestamp_ms\x18\x04 \x01(\x03\x12\x46\n\tvariables\x18\x05 \x03(\x0b\x32\x33.pogoprotos.data.inbox.ClientInbox.TemplateVariable\x12\x45\n\x06labels\x18\x06 \x03(\x0e\x32\x35.pogoprotos.data.inbox.ClientInbox.Notification.Label\x12\x16\n\x0e\x65xpire_time_ms\x18\x07 \x01(\x03\"<\n\x05Label\x12\x0f\n\x0bUNSET_LABEL\x10\x00\x12\n\n\x06UNREAD\x10\x01\x12\x07\n\x03NEW\x10\x02\x12\r\n\tIMMEDIATE\x10\x03\x1ah\n\x10TemplateVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07literal\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x14\n\x0clookup_table\x18\x04 \x01(\t\x12\x12\n\nbyte_value\x18\x05 \x01(\x0c\"\xa3\t\n\x14NotificationCategory\x12\x08\n\x04NONE\x10\x00\x12\x0f\n\x0bGYM_REMOVAL\x10\x01\x12\x12\n\x0ePOKEMON_HUNGRY\x10\x02\x12\x19\n\x15\x45XCLUSIVE_RAID_INVITE\x10\x03\x12\x1f\n\x1b\x45XCLUSIVE_RAID_CANCELLATION\x10\x04\x12 \n\x1cSHARED_EXCLUSIVE_RAID_INVITE\x10\x05\x12\x14\n\x10GIFTBOX_INCOMING\x10\x06\x12\x15\n\x11GIFTBOX_DELIVERED\x10\x07\x12\x1f\n\x1b\x46RIENDSHIP_MILESTONE_REWARD\x10\x08\x12#\n\x1fGYM_BATTLE_FRIENDSHIP_INCREMENT\x10\t\x12\x14\n\x10\x42GMODE_EGG_HATCH\x10\n\x12\x16\n\x12\x42GMODE_BUDDY_CANDY\x10\x0b\x12 \n\x1c\x42GMODE_WEEKLY_FITNESS_REPORT\x10\x0c\x12\x1f\n\x1b\x42GMODE_OFF_SESSION_DISTANCE\x10\r\x12\x18\n\x14\x42GMODE_POI_PROXIMITY\x10\x0e\x12\x1c\n\x18\x42GMODE_NAMED_BUDDY_CANDY\x10\x0f\x12\x12\n\x0e\x41PP_BADGE_ONLY\x10\x10\x12\x1b\n\x17\x43OMBAT_CHALLENGE_OPENED\x10\x11\x12\x10\n\x0cLUCKY_FRIEND\x10\x12\x12\x10\n\x0c\x42UDDY_HUNGRY\x10\x13\x12\x14\n\x10\x42UDDY_FOUND_GIFT\x10\x14\x12#\n\x1f\x42UDDY_AFFECTION_LEVEL_MILESTONE\x10\x15\x12\x1b\n\x17\x42UDDY_AFFECTION_WALKING\x10\x16\x12\x18\n\x14\x42UDDY_AFFECTION_CARE\x10\x17\x12\x1a\n\x16\x42UDDY_AFFECTION_BATTLE\x10\x18\x12\x19\n\x15\x42UDDY_AFFECTION_PHOTO\x10\x19\x12\x17\n\x13\x42UDDY_AFFECTION_POI\x10\x1a\x12\x18\n\x14\x42UDDY_ATTRACTIVE_POI\x10\x1b\x12\x1a\n\x16\x46RIEND_INVITE_RECEIVED\x10\x1c\x12\x1a\n\x16\x46RIEND_INVITE_ACCEPTED\x10\x1d\x12\x1c\n\x18\x43OMBAT_VS_SEEKER_CHARGED\x10\x1e\x12!\n\x1d\x43OMBAT_COMPETITIVE_SEASON_END\x10\x1f\x12\"\n\x1e\x42UDDY_AFFECTION_ATTRACTIVE_POI\x10 \x12\x19\n\x15POI_PASSCODE_REDEEMED\x10!\x12\x16\n\x12NO_EGGS_INCUBATING\x10\"\x12\x1c\n\x18RETENTION_UNOPENED_GIFTS\x10\'\x12\x17\n\x13RETENTION_STARPIECE\x10(\x12\x15\n\x11RETENTION_INCENSE\x10)\x12\x17\n\x13RETENTION_LUCKY_EGG\x10*\x12\x1d\n\x19RETENTION_ADVSYNC_REWARDS\x10+\x12!\n\x1dRETENTION_EGGS_NOT_INCUBATING\x10,\x12\x18\n\x14RETENTION_POWER_WALK\x10-\x12\x1e\n\x1aRETENTION_FUN_WITH_FRIENDS\x10.b\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CLIENTINBOX_NOTIFICATION_LABEL = _descriptor.EnumDescriptor(
  name='Label',
  full_name='pogoprotos.data.inbox.ClientInbox.Notification.Label',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_LABEL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREAD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMMEDIATE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=510,
  serialized_end=570,
)
_sym_db.RegisterEnumDescriptor(_CLIENTINBOX_NOTIFICATION_LABEL)

_CLIENTINBOX_NOTIFICATIONCATEGORY = _descriptor.EnumDescriptor(
  name='NotificationCategory',
  full_name='pogoprotos.data.inbox.ClientInbox.NotificationCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_REMOVAL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_HUNGRY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RAID_INVITE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCLUSIVE_RAID_CANCELLATION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARED_EXCLUSIVE_RAID_INVITE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIFTBOX_INCOMING', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GIFTBOX_DELIVERED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIENDSHIP_MILESTONE_REWARD', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_BATTLE_FRIENDSHIP_INCREMENT', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_EGG_HATCH', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_BUDDY_CANDY', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_WEEKLY_FITNESS_REPORT', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_OFF_SESSION_DISTANCE', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_POI_PROXIMITY', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BGMODE_NAMED_BUDDY_CANDY', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_BADGE_ONLY', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_CHALLENGE_OPENED', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LUCKY_FRIEND', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_HUNGRY', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_FOUND_GIFT', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_LEVEL_MILESTONE', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_WALKING', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_CARE', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_BATTLE', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_PHOTO', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_POI', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_ATTRACTIVE_POI', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIEND_INVITE_RECEIVED', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FRIEND_INVITE_ACCEPTED', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_VS_SEEKER_CHARGED', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMBAT_COMPETITIVE_SEASON_END', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AFFECTION_ATTRACTIVE_POI', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_PASSCODE_REDEEMED', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_EGGS_INCUBATING', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_UNOPENED_GIFTS', index=35, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_STARPIECE', index=36, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_INCENSE', index=37, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_LUCKY_EGG', index=38, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_ADVSYNC_REWARDS', index=39, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_EGGS_NOT_INCUBATING', index=40, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_POWER_WALK', index=41, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETENTION_FUN_WITH_FRIENDS', index=42, number=46,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=679,
  serialized_end=1866,
)
_sym_db.RegisterEnumDescriptor(_CLIENTINBOX_NOTIFICATIONCATEGORY)


_CLIENTINBOX_NOTIFICATION = _descriptor.Descriptor(
  name='Notification',
  full_name='pogoprotos.data.inbox.ClientInbox.Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_id', full_name='pogoprotos.data.inbox.ClientInbox.Notification.notification_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title_key', full_name='pogoprotos.data.inbox.ClientInbox.Notification.title_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category', full_name='pogoprotos.data.inbox.ClientInbox.Notification.category', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create_timestamp_ms', full_name='pogoprotos.data.inbox.ClientInbox.Notification.create_timestamp_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variables', full_name='pogoprotos.data.inbox.ClientInbox.Notification.variables', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='pogoprotos.data.inbox.ClientInbox.Notification.labels', index=5,
      number=6, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_time_ms', full_name='pogoprotos.data.inbox.ClientInbox.Notification.expire_time_ms', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTINBOX_NOTIFICATION_LABEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=570,
)

_CLIENTINBOX_TEMPLATEVARIABLE = _descriptor.Descriptor(
  name='TemplateVariable',
  full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='literal', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.literal', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lookup_table', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.lookup_table', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='byte_value', full_name='pogoprotos.data.inbox.ClientInbox.TemplateVariable.byte_value', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=572,
  serialized_end=676,
)

_CLIENTINBOX = _descriptor.Descriptor(
  name='ClientInbox',
  full_name='pogoprotos.data.inbox.ClientInbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notifications', full_name='pogoprotos.data.inbox.ClientInbox.notifications', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='builtin_variables', full_name='pogoprotos.data.inbox.ClientInbox.builtin_variables', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTINBOX_NOTIFICATION, _CLIENTINBOX_TEMPLATEVARIABLE, ],
  enum_types=[
    _CLIENTINBOX_NOTIFICATIONCATEGORY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=1866,
)

_CLIENTINBOX_NOTIFICATION.fields_by_name['variables'].message_type = _CLIENTINBOX_TEMPLATEVARIABLE
_CLIENTINBOX_NOTIFICATION.fields_by_name['labels'].enum_type = _CLIENTINBOX_NOTIFICATION_LABEL
_CLIENTINBOX_NOTIFICATION.containing_type = _CLIENTINBOX
_CLIENTINBOX_NOTIFICATION_LABEL.containing_type = _CLIENTINBOX_NOTIFICATION
_CLIENTINBOX_TEMPLATEVARIABLE.containing_type = _CLIENTINBOX
_CLIENTINBOX.fields_by_name['notifications'].message_type = _CLIENTINBOX_NOTIFICATION
_CLIENTINBOX.fields_by_name['builtin_variables'].message_type = _CLIENTINBOX_TEMPLATEVARIABLE
_CLIENTINBOX_NOTIFICATIONCATEGORY.containing_type = _CLIENTINBOX
DESCRIPTOR.message_types_by_name['ClientInbox'] = _CLIENTINBOX

ClientInbox = _reflection.GeneratedProtocolMessageType('ClientInbox', (_message.Message,), dict(

  Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTINBOX_NOTIFICATION,
    __module__ = 'pogoprotos.data.inbox.client_inbox_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.inbox.ClientInbox.Notification)
    ))
  ,

  TemplateVariable = _reflection.GeneratedProtocolMessageType('TemplateVariable', (_message.Message,), dict(
    DESCRIPTOR = _CLIENTINBOX_TEMPLATEVARIABLE,
    __module__ = 'pogoprotos.data.inbox.client_inbox_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.inbox.ClientInbox.TemplateVariable)
    ))
  ,
  DESCRIPTOR = _CLIENTINBOX,
  __module__ = 'pogoprotos.data.inbox.client_inbox_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.inbox.ClientInbox)
  ))
_sym_db.RegisterMessage(ClientInbox)
_sym_db.RegisterMessage(ClientInbox.Notification)
_sym_db.RegisterMessage(ClientInbox.TemplateVariable)


# @@protoc_insertion_point(module_scope)
