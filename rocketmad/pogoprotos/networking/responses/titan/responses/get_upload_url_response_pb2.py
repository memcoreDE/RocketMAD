# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/titan/responses/get_upload_url_response.proto

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
  name='pogoprotos/networking/responses/titan/responses/get_upload_url_response.proto',
  package='pogoprotos.networking.responses.titan.responses',
  syntax='proto3',
  serialized_pb=_b('\nMpogoprotos/networking/responses/titan/responses/get_upload_url_response.proto\x12/pogoprotos.networking.responses.titan.responses\"\xcc\x03\n\x14GetUploadUrlResponse\x12\\\n\x06status\x18\x01 \x01(\x0e\x32L.pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.Status\x12\x12\n\nsigned_url\x18\x02 \x01(\t\x12#\n\x1bsupporting_image_signed_url\x18\x03 \x01(\t\x12y\n\x13\x63ontext_signed_urls\x18\x04 \x03(\x0b\x32\\.pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.ContextSignedUrlsEntry\x1a\x38\n\x16\x43ontextSignedUrlsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"h\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08\x46\x41ILURES\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x12\x1a\n\x16MISSING_IMAGE_CONTEXTS\x10\x03\x12\x1c\n\x18\x44UPLICATE_IMAGE_CONTEXTS\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETUPLOADURLRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURES', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_IMAGE_CONTEXTS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_IMAGE_CONTEXTS', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=487,
  serialized_end=591,
)
_sym_db.RegisterEnumDescriptor(_GETUPLOADURLRESPONSE_STATUS)


_GETUPLOADURLRESPONSE_CONTEXTSIGNEDURLSENTRY = _descriptor.Descriptor(
  name='ContextSignedUrlsEntry',
  full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.ContextSignedUrlsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.ContextSignedUrlsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.ContextSignedUrlsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=429,
  serialized_end=485,
)

_GETUPLOADURLRESPONSE = _descriptor.Descriptor(
  name='GetUploadUrlResponse',
  full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signed_url', full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.signed_url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supporting_image_signed_url', full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.supporting_image_signed_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context_signed_urls', full_name='pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.context_signed_urls', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETUPLOADURLRESPONSE_CONTEXTSIGNEDURLSENTRY, ],
  enum_types=[
    _GETUPLOADURLRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=591,
)

_GETUPLOADURLRESPONSE_CONTEXTSIGNEDURLSENTRY.containing_type = _GETUPLOADURLRESPONSE
_GETUPLOADURLRESPONSE.fields_by_name['status'].enum_type = _GETUPLOADURLRESPONSE_STATUS
_GETUPLOADURLRESPONSE.fields_by_name['context_signed_urls'].message_type = _GETUPLOADURLRESPONSE_CONTEXTSIGNEDURLSENTRY
_GETUPLOADURLRESPONSE_STATUS.containing_type = _GETUPLOADURLRESPONSE
DESCRIPTOR.message_types_by_name['GetUploadUrlResponse'] = _GETUPLOADURLRESPONSE

GetUploadUrlResponse = _reflection.GeneratedProtocolMessageType('GetUploadUrlResponse', (_message.Message,), dict(

  ContextSignedUrlsEntry = _reflection.GeneratedProtocolMessageType('ContextSignedUrlsEntry', (_message.Message,), dict(
    DESCRIPTOR = _GETUPLOADURLRESPONSE_CONTEXTSIGNEDURLSENTRY,
    __module__ = 'pogoprotos.networking.responses.titan.responses.get_upload_url_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse.ContextSignedUrlsEntry)
    ))
  ,
  DESCRIPTOR = _GETUPLOADURLRESPONSE,
  __module__ = 'pogoprotos.networking.responses.titan.responses.get_upload_url_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.titan.responses.GetUploadUrlResponse)
  ))
_sym_db.RegisterMessage(GetUploadUrlResponse)
_sym_db.RegisterMessage(GetUploadUrlResponse.ContextSignedUrlsEntry)


_GETUPLOADURLRESPONSE_CONTEXTSIGNEDURLSENTRY.has_options = True
_GETUPLOADURLRESPONSE_CONTEXTSIGNEDURLSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
