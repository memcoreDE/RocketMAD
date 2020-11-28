# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/edit_pokemon_tag_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_tag_color_pb2 as pogoprotos_dot_enums_dot_pokemon__tag__color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/edit_pokemon_tag_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nFpogoprotos/networking/requests/messages/edit_pokemon_tag_message.proto\x12\'pogoprotos.networking.requests.messages\x1a(pogoprotos/enums/pokemon_tag_color.proto\"\xe5\x01\n\x15\x45\x64itPokemonTagMessage\x12^\n\x0btag_to_edit\x18\x02 \x03(\x0b\x32I.pogoprotos.networking.requests.messages.EditPokemonTagMessage.PokemonTag\x1al\n\nPokemonTag\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x30\n\x05\x63olor\x18\x03 \x01(\x0e\x32!.pogoprotos.enums.PokemonTagColor\x12\x12\n\nsort_index\x18\x04 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__tag__color__pb2.DESCRIPTOR,])




_EDITPOKEMONTAGMESSAGE_POKEMONTAG = _descriptor.Descriptor(
  name='PokemonTag',
  full_name='pogoprotos.networking.requests.messages.EditPokemonTagMessage.PokemonTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.networking.requests.messages.EditPokemonTagMessage.PokemonTag.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='pogoprotos.networking.requests.messages.EditPokemonTagMessage.PokemonTag.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='pogoprotos.networking.requests.messages.EditPokemonTagMessage.PokemonTag.color', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort_index', full_name='pogoprotos.networking.requests.messages.EditPokemonTagMessage.PokemonTag.sort_index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=279,
  serialized_end=387,
)

_EDITPOKEMONTAGMESSAGE = _descriptor.Descriptor(
  name='EditPokemonTagMessage',
  full_name='pogoprotos.networking.requests.messages.EditPokemonTagMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag_to_edit', full_name='pogoprotos.networking.requests.messages.EditPokemonTagMessage.tag_to_edit', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EDITPOKEMONTAGMESSAGE_POKEMONTAG, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=387,
)

_EDITPOKEMONTAGMESSAGE_POKEMONTAG.fields_by_name['color'].enum_type = pogoprotos_dot_enums_dot_pokemon__tag__color__pb2._POKEMONTAGCOLOR
_EDITPOKEMONTAGMESSAGE_POKEMONTAG.containing_type = _EDITPOKEMONTAGMESSAGE
_EDITPOKEMONTAGMESSAGE.fields_by_name['tag_to_edit'].message_type = _EDITPOKEMONTAGMESSAGE_POKEMONTAG
DESCRIPTOR.message_types_by_name['EditPokemonTagMessage'] = _EDITPOKEMONTAGMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EditPokemonTagMessage = _reflection.GeneratedProtocolMessageType('EditPokemonTagMessage', (_message.Message,), dict(

  PokemonTag = _reflection.GeneratedProtocolMessageType('PokemonTag', (_message.Message,), dict(
    DESCRIPTOR = _EDITPOKEMONTAGMESSAGE_POKEMONTAG,
    __module__ = 'pogoprotos.networking.requests.messages.edit_pokemon_tag_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.EditPokemonTagMessage.PokemonTag)
    ))
  ,
  DESCRIPTOR = _EDITPOKEMONTAGMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.edit_pokemon_tag_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.EditPokemonTagMessage)
  ))
_sym_db.RegisterMessage(EditPokemonTagMessage)
_sym_db.RegisterMessage(EditPokemonTagMessage.PokemonTag)


# @@protoc_insertion_point(module_scope)
