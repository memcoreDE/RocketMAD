# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/pokemon_condition.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import condition_type_pb2 as pogoprotos_dot_enums_dot_condition__type__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.enums import form_pb2 as pogoprotos_dot_enums_dot_form__pb2
from pogoprotos.data.combat import with_pokemon_cp_limit_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2
from pogoprotos.data.combat import with_pokemon_type_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2
from pogoprotos.data.combat import with_pokemon_category_pb2 as pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/pokemon_condition.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_pb=_b('\n.pogoprotos/data/combat/pokemon_condition.proto\x12\x16pogoprotos.data.combat\x1a%pogoprotos/enums/condition_type.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a\x1bpogoprotos/enums/form.proto\x1a\x32pogoprotos/data/combat/with_pokemon_cp_limit.proto\x1a.pogoprotos/data/combat/with_pokemon_type.proto\x1a\x32pogoprotos/data/combat/with_pokemon_category.proto\"\xc7\x07\n\x10PokemonCondition\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.pogoprotos.enums.ConditionType\x12K\n\x15with_pokemon_cp_limit\x18\x02 \x01(\x0b\x32*.pogoprotos.data.combat.WithPokemonCpLimitH\x00\x12\x44\n\x11with_pokemon_type\x18\x03 \x01(\x0b\x32\'.pogoprotos.data.combat.WithPokemonTypeH\x00\x12L\n\x15with_pokemon_category\x18\x04 \x01(\x0b\x32+.pogoprotos.data.combat.WithPokemonCategoryH\x00\x12V\n\x11pokemon_whitelist\x18\x05 \x01(\x0b\x32\x39.pogoprotos.data.combat.PokemonCondition.PokemonWhitelistH\x00\x12R\n\x0fpokemon_banlist\x18\x06 \x01(\x0b\x32\x37.pogoprotos.data.combat.PokemonCondition.PokemonBanlistH\x00\x12\x63\n\x18pokemon_caught_timestamp\x18\x07 \x01(\x0b\x32?.pogoprotos.data.combat.PokemonCondition.PokemonCaughtTimestampH\x00\x1aK\n\x16PokemonCaughtTimestamp\x12\x17\n\x0f\x61\x66ter_timestamp\x18\x01 \x01(\x03\x12\x18\n\x10\x62\x65\x66ore_timestamp\x18\x02 \x01(\x03\x1ai\n\x0ePokemonBanlist\x12\x0c\n\x04name\x18\x01 \x01(\t\x12I\n\x07pokemon\x18\x02 \x03(\x0b\x32\x38.pogoprotos.data.combat.PokemonCondition.PokemonWithForm\x1ak\n\x10PokemonWhitelist\x12\x0c\n\x04name\x18\x01 \x01(\t\x12I\n\x07pokemon\x18\x02 \x03(\x0b\x32\x38.pogoprotos.data.combat.PokemonCondition.PokemonWithForm\x1a`\n\x0fPokemonWithForm\x12\'\n\x02id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12$\n\x04\x66orm\x18\x02 \x01(\x0e\x32\x16.pogoprotos.enums.FormB\x0b\n\tConditionb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_condition__type__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_form__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POKEMONCONDITION_POKEMONCAUGHTTIMESTAMP = _descriptor.Descriptor(
  name='PokemonCaughtTimestamp',
  full_name='pogoprotos.data.combat.PokemonCondition.PokemonCaughtTimestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='after_timestamp', full_name='pogoprotos.data.combat.PokemonCondition.PokemonCaughtTimestamp.after_timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='before_timestamp', full_name='pogoprotos.data.combat.PokemonCondition.PokemonCaughtTimestamp.before_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  ],
  serialized_start=895,
  serialized_end=970,
)

_POKEMONCONDITION_POKEMONBANLIST = _descriptor.Descriptor(
  name='PokemonBanlist',
  full_name='pogoprotos.data.combat.PokemonCondition.PokemonBanlist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.data.combat.PokemonCondition.PokemonBanlist.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.combat.PokemonCondition.PokemonBanlist.pokemon', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=972,
  serialized_end=1077,
)

_POKEMONCONDITION_POKEMONWHITELIST = _descriptor.Descriptor(
  name='PokemonWhitelist',
  full_name='pogoprotos.data.combat.PokemonCondition.PokemonWhitelist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.data.combat.PokemonCondition.PokemonWhitelist.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.data.combat.PokemonCondition.PokemonWhitelist.pokemon', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1079,
  serialized_end=1186,
)

_POKEMONCONDITION_POKEMONWITHFORM = _descriptor.Descriptor(
  name='PokemonWithForm',
  full_name='pogoprotos.data.combat.PokemonCondition.PokemonWithForm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.data.combat.PokemonCondition.PokemonWithForm.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='form', full_name='pogoprotos.data.combat.PokemonCondition.PokemonWithForm.form', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  ],
  serialized_start=1188,
  serialized_end=1284,
)

_POKEMONCONDITION = _descriptor.Descriptor(
  name='PokemonCondition',
  full_name='pogoprotos.data.combat.PokemonCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.data.combat.PokemonCondition.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_cp_limit', full_name='pogoprotos.data.combat.PokemonCondition.with_pokemon_cp_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_type', full_name='pogoprotos.data.combat.PokemonCondition.with_pokemon_type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='with_pokemon_category', full_name='pogoprotos.data.combat.PokemonCondition.with_pokemon_category', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_whitelist', full_name='pogoprotos.data.combat.PokemonCondition.pokemon_whitelist', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_banlist', full_name='pogoprotos.data.combat.PokemonCondition.pokemon_banlist', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_caught_timestamp', full_name='pogoprotos.data.combat.PokemonCondition.pokemon_caught_timestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_POKEMONCONDITION_POKEMONCAUGHTTIMESTAMP, _POKEMONCONDITION_POKEMONBANLIST, _POKEMONCONDITION_POKEMONWHITELIST, _POKEMONCONDITION_POKEMONWITHFORM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Condition', full_name='pogoprotos.data.combat.PokemonCondition.Condition',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=330,
  serialized_end=1297,
)

_POKEMONCONDITION_POKEMONCAUGHTTIMESTAMP.containing_type = _POKEMONCONDITION
_POKEMONCONDITION_POKEMONBANLIST.fields_by_name['pokemon'].message_type = _POKEMONCONDITION_POKEMONWITHFORM
_POKEMONCONDITION_POKEMONBANLIST.containing_type = _POKEMONCONDITION
_POKEMONCONDITION_POKEMONWHITELIST.fields_by_name['pokemon'].message_type = _POKEMONCONDITION_POKEMONWITHFORM
_POKEMONCONDITION_POKEMONWHITELIST.containing_type = _POKEMONCONDITION
_POKEMONCONDITION_POKEMONWITHFORM.fields_by_name['id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_POKEMONCONDITION_POKEMONWITHFORM.fields_by_name['form'].enum_type = pogoprotos_dot_enums_dot_form__pb2._FORM
_POKEMONCONDITION_POKEMONWITHFORM.containing_type = _POKEMONCONDITION
_POKEMONCONDITION.fields_by_name['type'].enum_type = pogoprotos_dot_enums_dot_condition__type__pb2._CONDITIONTYPE
_POKEMONCONDITION.fields_by_name['with_pokemon_cp_limit'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__cp__limit__pb2._WITHPOKEMONCPLIMIT
_POKEMONCONDITION.fields_by_name['with_pokemon_type'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__type__pb2._WITHPOKEMONTYPE
_POKEMONCONDITION.fields_by_name['with_pokemon_category'].message_type = pogoprotos_dot_data_dot_combat_dot_with__pokemon__category__pb2._WITHPOKEMONCATEGORY
_POKEMONCONDITION.fields_by_name['pokemon_whitelist'].message_type = _POKEMONCONDITION_POKEMONWHITELIST
_POKEMONCONDITION.fields_by_name['pokemon_banlist'].message_type = _POKEMONCONDITION_POKEMONBANLIST
_POKEMONCONDITION.fields_by_name['pokemon_caught_timestamp'].message_type = _POKEMONCONDITION_POKEMONCAUGHTTIMESTAMP
_POKEMONCONDITION.oneofs_by_name['Condition'].fields.append(
  _POKEMONCONDITION.fields_by_name['with_pokemon_cp_limit'])
_POKEMONCONDITION.fields_by_name['with_pokemon_cp_limit'].containing_oneof = _POKEMONCONDITION.oneofs_by_name['Condition']
_POKEMONCONDITION.oneofs_by_name['Condition'].fields.append(
  _POKEMONCONDITION.fields_by_name['with_pokemon_type'])
_POKEMONCONDITION.fields_by_name['with_pokemon_type'].containing_oneof = _POKEMONCONDITION.oneofs_by_name['Condition']
_POKEMONCONDITION.oneofs_by_name['Condition'].fields.append(
  _POKEMONCONDITION.fields_by_name['with_pokemon_category'])
_POKEMONCONDITION.fields_by_name['with_pokemon_category'].containing_oneof = _POKEMONCONDITION.oneofs_by_name['Condition']
_POKEMONCONDITION.oneofs_by_name['Condition'].fields.append(
  _POKEMONCONDITION.fields_by_name['pokemon_whitelist'])
_POKEMONCONDITION.fields_by_name['pokemon_whitelist'].containing_oneof = _POKEMONCONDITION.oneofs_by_name['Condition']
_POKEMONCONDITION.oneofs_by_name['Condition'].fields.append(
  _POKEMONCONDITION.fields_by_name['pokemon_banlist'])
_POKEMONCONDITION.fields_by_name['pokemon_banlist'].containing_oneof = _POKEMONCONDITION.oneofs_by_name['Condition']
_POKEMONCONDITION.oneofs_by_name['Condition'].fields.append(
  _POKEMONCONDITION.fields_by_name['pokemon_caught_timestamp'])
_POKEMONCONDITION.fields_by_name['pokemon_caught_timestamp'].containing_oneof = _POKEMONCONDITION.oneofs_by_name['Condition']
DESCRIPTOR.message_types_by_name['PokemonCondition'] = _POKEMONCONDITION

PokemonCondition = _reflection.GeneratedProtocolMessageType('PokemonCondition', (_message.Message,), dict(

  PokemonCaughtTimestamp = _reflection.GeneratedProtocolMessageType('PokemonCaughtTimestamp', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONCONDITION_POKEMONCAUGHTTIMESTAMP,
    __module__ = 'pogoprotos.data.combat.pokemon_condition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.PokemonCondition.PokemonCaughtTimestamp)
    ))
  ,

  PokemonBanlist = _reflection.GeneratedProtocolMessageType('PokemonBanlist', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONCONDITION_POKEMONBANLIST,
    __module__ = 'pogoprotos.data.combat.pokemon_condition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.PokemonCondition.PokemonBanlist)
    ))
  ,

  PokemonWhitelist = _reflection.GeneratedProtocolMessageType('PokemonWhitelist', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONCONDITION_POKEMONWHITELIST,
    __module__ = 'pogoprotos.data.combat.pokemon_condition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.PokemonCondition.PokemonWhitelist)
    ))
  ,

  PokemonWithForm = _reflection.GeneratedProtocolMessageType('PokemonWithForm', (_message.Message,), dict(
    DESCRIPTOR = _POKEMONCONDITION_POKEMONWITHFORM,
    __module__ = 'pogoprotos.data.combat.pokemon_condition_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.PokemonCondition.PokemonWithForm)
    ))
  ,
  DESCRIPTOR = _POKEMONCONDITION,
  __module__ = 'pogoprotos.data.combat.pokemon_condition_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.PokemonCondition)
  ))
_sym_db.RegisterMessage(PokemonCondition)
_sym_db.RegisterMessage(PokemonCondition.PokemonCaughtTimestamp)
_sym_db.RegisterMessage(PokemonCondition.PokemonBanlist)
_sym_db.RegisterMessage(PokemonCondition.PokemonWhitelist)
_sym_db.RegisterMessage(PokemonCondition.PokemonWithForm)


# @@protoc_insertion_point(module_scope)
