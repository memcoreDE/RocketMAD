# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/feature_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/feature_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#pogoprotos/enums/feature_type.proto\x12\x10pogoprotos.enums*\x86\x01\n\x0b\x46\x65\x61tureType\x12\x16\n\x12\x46\x45\x41TURE_TYPE_UNSET\x10\x00\x12\x1e\n\x1a\x46\x45\x41TURE_TYPE_ONLINE_STATUS\x10\x01\x12 \n\x1c\x46\x45\x41TURE_TYPE_NIANTIC_PROFILE\x10\x02\x12\x1d\n\x19\x46\x45\x41TURE_TYPE_FRIENDS_LIST\x10\x03\x62\x06proto3')
)

_FEATURETYPE = _descriptor.EnumDescriptor(
  name='FeatureType',
  full_name='pogoprotos.enums.FeatureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FEATURE_TYPE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURE_TYPE_ONLINE_STATUS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURE_TYPE_NIANTIC_PROFILE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURE_TYPE_FRIENDS_LIST', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=58,
  serialized_end=192,
)
_sym_db.RegisterEnumDescriptor(_FEATURETYPE)

FeatureType = enum_type_wrapper.EnumTypeWrapper(_FEATURETYPE)
FEATURE_TYPE_UNSET = 0
FEATURE_TYPE_ONLINE_STATUS = 1
FEATURE_TYPE_NIANTIC_PROFILE = 2
FEATURE_TYPE_FRIENDS_LIST = 3


DESCRIPTOR.enum_types_by_name['FeatureType'] = _FEATURETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
