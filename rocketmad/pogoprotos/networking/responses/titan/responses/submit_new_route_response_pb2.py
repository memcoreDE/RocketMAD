# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/titan/responses/submit_new_route_response.proto

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
  name='pogoprotos/networking/responses/titan/responses/submit_new_route_response.proto',
  package='pogoprotos.networking.responses.titan.responses',
  syntax='proto3',
  serialized_pb=_b('\nOpogoprotos/networking/responses/titan/responses/submit_new_route_response.proto\x12/pogoprotos.networking.responses.titan.responses\"\x85\x03\n\x16SubmitNewRouteResponse\x12^\n\x06status\x18\x01 \x01(\x0e\x32N.pogoprotos.networking.responses.titan.responses.SubmitNewRouteResponse.Status\"\x8a\x02\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x1f\n\x1bTOO_MANY_RECENT_SUBMISSIONS\x10\x03\x12\t\n\x05MINOR\x10\x04\x12\x11\n\rNOT_AVAILABLE\x10\x05\x12\x11\n\rINVALID_INPUT\x10\x06\x12\x11\n\rMISSING_IMAGE\x10\x07\x12\x16\n\x12INVALID_CHECKPOINT\x10\x08\x12\x18\n\x14INVALID_ROUTE_LENGTH\x10\t\x12\x19\n\x15\x44UPLICATE_CHECKPOINTS\x10\n\x12\x15\n\x11\x41LREADY_SUBMITTED\x10\x0b\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SUBMITNEWROUTERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.titan.responses.SubmitNewRouteResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_RECENT_SUBMISSIONS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINOR', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_AVAILABLE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_INPUT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_IMAGE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CHECKPOINT', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ROUTE_LENGTH', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_CHECKPOINTS', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_SUBMITTED', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=256,
  serialized_end=522,
)
_sym_db.RegisterEnumDescriptor(_SUBMITNEWROUTERESPONSE_STATUS)


_SUBMITNEWROUTERESPONSE = _descriptor.Descriptor(
  name='SubmitNewRouteResponse',
  full_name='pogoprotos.networking.responses.titan.responses.SubmitNewRouteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.titan.responses.SubmitNewRouteResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SUBMITNEWROUTERESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=522,
)

_SUBMITNEWROUTERESPONSE.fields_by_name['status'].enum_type = _SUBMITNEWROUTERESPONSE_STATUS
_SUBMITNEWROUTERESPONSE_STATUS.containing_type = _SUBMITNEWROUTERESPONSE
DESCRIPTOR.message_types_by_name['SubmitNewRouteResponse'] = _SUBMITNEWROUTERESPONSE

SubmitNewRouteResponse = _reflection.GeneratedProtocolMessageType('SubmitNewRouteResponse', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITNEWROUTERESPONSE,
  __module__ = 'pogoprotos.networking.responses.titan.responses.submit_new_route_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.titan.responses.SubmitNewRouteResponse)
  ))
_sym_db.RegisterMessage(SubmitNewRouteResponse)


# @@protoc_insertion_point(module_scope)
