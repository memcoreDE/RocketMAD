# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/report_ad_feedback_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/report_ad_feedback_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nApogoprotos/networking/responses/report_ad_feedback_response.proto\x12\x1fpogoprotos.networking.responses\"\x1a\n\x18ReportAdFeedbackResponseb\x06proto3')
)




_REPORTADFEEDBACKRESPONSE = _descriptor.Descriptor(
  name='ReportAdFeedbackResponse',
  full_name='pogoprotos.networking.responses.ReportAdFeedbackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=102,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['ReportAdFeedbackResponse'] = _REPORTADFEEDBACKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportAdFeedbackResponse = _reflection.GeneratedProtocolMessageType('ReportAdFeedbackResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPORTADFEEDBACKRESPONSE,
  __module__ = 'pogoprotos.networking.responses.report_ad_feedback_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.ReportAdFeedbackResponse)
  ))
_sym_db.RegisterMessage(ReportAdFeedbackResponse)


# @@protoc_insertion_point(module_scope)
