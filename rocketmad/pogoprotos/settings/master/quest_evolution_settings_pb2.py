# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/quest_evolution_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/quest_evolution_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9pogoprotos/settings/master/quest_evolution_settings.proto\x12\x1apogoprotos.settings.master\"b\n\x16QuestEvolutionSettings\x12\x1f\n\x17\x65nable_quest_evolutions\x18\x01 \x01(\x08\x12\'\n\x1f\x65nable_walking_quest_evolutions\x18\x02 \x01(\x08\x62\x06proto3')
)




_QUESTEVOLUTIONSETTINGS = _descriptor.Descriptor(
  name='QuestEvolutionSettings',
  full_name='pogoprotos.settings.master.QuestEvolutionSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_quest_evolutions', full_name='pogoprotos.settings.master.QuestEvolutionSettings.enable_quest_evolutions', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_walking_quest_evolutions', full_name='pogoprotos.settings.master.QuestEvolutionSettings.enable_walking_quest_evolutions', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['QuestEvolutionSettings'] = _QUESTEVOLUTIONSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestEvolutionSettings = _reflection.GeneratedProtocolMessageType('QuestEvolutionSettings', (_message.Message,), dict(
  DESCRIPTOR = _QUESTEVOLUTIONSETTINGS,
  __module__ = 'pogoprotos.settings.master.quest_evolution_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.QuestEvolutionSettings)
  ))
_sym_db.RegisterMessage(QuestEvolutionSettings)


# @@protoc_insertion_point(module_scope)
