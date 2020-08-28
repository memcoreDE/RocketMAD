# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_client_bgmode_settings_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.settings import background_mode_client_settings_pb2 as pogoprotos_dot_settings_dot_background__mode__client__settings__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_client_bgmode_settings_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nIpogoprotos/networking/responses/get_client_bgmode_settings_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x39pogoprotos/settings/background_mode_client_settings.proto\"\xf4\x01\n\x1fGetClientBgmodeSettingsResponse\x12W\n\x06status\x18\x01 \x01(\x0e\x32G.pogoprotos.networking.responses.GetClientBgmodeSettingsResponse.Status\x12\x43\n\x08settings\x18\x02 \x01(\x0b\x32\x31.pogoprotos.settings.BackgroundModeClientSettings\"3\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_settings_dot_background__mode__client__settings__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETCLIENTBGMODESETTINGSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.GetClientBgmodeSettingsResponse.Status',
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
      name='ERROR_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=363,
  serialized_end=414,
)
_sym_db.RegisterEnumDescriptor(_GETCLIENTBGMODESETTINGSRESPONSE_STATUS)


_GETCLIENTBGMODESETTINGSRESPONSE = _descriptor.Descriptor(
  name='GetClientBgmodeSettingsResponse',
  full_name='pogoprotos.networking.responses.GetClientBgmodeSettingsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.GetClientBgmodeSettingsResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='settings', full_name='pogoprotos.networking.responses.GetClientBgmodeSettingsResponse.settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETCLIENTBGMODESETTINGSRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=414,
)

_GETCLIENTBGMODESETTINGSRESPONSE.fields_by_name['status'].enum_type = _GETCLIENTBGMODESETTINGSRESPONSE_STATUS
_GETCLIENTBGMODESETTINGSRESPONSE.fields_by_name['settings'].message_type = pogoprotos_dot_settings_dot_background__mode__client__settings__pb2._BACKGROUNDMODECLIENTSETTINGS
_GETCLIENTBGMODESETTINGSRESPONSE_STATUS.containing_type = _GETCLIENTBGMODESETTINGSRESPONSE
DESCRIPTOR.message_types_by_name['GetClientBgmodeSettingsResponse'] = _GETCLIENTBGMODESETTINGSRESPONSE

GetClientBgmodeSettingsResponse = _reflection.GeneratedProtocolMessageType('GetClientBgmodeSettingsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETCLIENTBGMODESETTINGSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_client_bgmode_settings_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetClientBgmodeSettingsResponse)
  ))
_sym_db.RegisterMessage(GetClientBgmodeSettingsResponse)


# @@protoc_insertion_point(module_scope)
