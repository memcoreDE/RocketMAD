# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/sku_data.proto

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
  name='pogoprotos/data/sku_data.proto',
  package='pogoprotos.data',
  syntax='proto3',
  serialized_pb=_b('\n\x1epogoprotos/data/sku_data.proto\x12\x0fpogoprotos.data\"\xe9\x04\n\x07SkuData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nis_enabled\x18\x02 \x01(\x08\x12\x34\n\x07\x63ontent\x18\x03 \x03(\x0b\x32#.pogoprotos.data.SkuData.SkuContent\x12\x30\n\x05price\x18\x04 \x03(\x0b\x32!.pogoprotos.data.SkuData.SkuPrice\x12=\n\x0cpayment_type\x18\x05 \x01(\x0e\x32\'.pogoprotos.data.SkuData.SkuPaymentType\x12\"\n\x1alast_modified_timestamp_ms\x18\x06 \x01(\x03\x12G\n\x11presentation_data\x18\x07 \x03(\x0b\x32,.pogoprotos.data.SkuData.SkuPresentationData\x12\x1f\n\x17\x65nabled_window_start_ms\x18\x08 \x01(\x03\x12\x1d\n\x15\x65nabled_window_end_ms\x18\t \x01(\x03\x12\x17\n\x0fsubscription_id\x18\n \x01(\t\x1a\x31\n\nSkuContent\x12\x11\n\titem_type\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x1a\x30\n\x08SkuPrice\x12\x15\n\rcurrency_type\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x05\x1a\x31\n\x13SkuPresentationData\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"9\n\x0eSkuPaymentType\x12\t\n\x05UNSET\x10\x00\x12\x0f\n\x0bTHIRD_PARTY\x10\x01\x12\x0b\n\x07IN_GAME\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SKUDATA_SKUPAYMENTTYPE = _descriptor.EnumDescriptor(
  name='SkuPaymentType',
  full_name='pogoprotos.data.SkuData.SkuPaymentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THIRD_PARTY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_GAME', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=612,
  serialized_end=669,
)
_sym_db.RegisterEnumDescriptor(_SKUDATA_SKUPAYMENTTYPE)


_SKUDATA_SKUCONTENT = _descriptor.Descriptor(
  name='SkuContent',
  full_name='pogoprotos.data.SkuData.SkuContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_type', full_name='pogoprotos.data.SkuData.SkuContent.item_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='pogoprotos.data.SkuData.SkuContent.quantity', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=460,
  serialized_end=509,
)

_SKUDATA_SKUPRICE = _descriptor.Descriptor(
  name='SkuPrice',
  full_name='pogoprotos.data.SkuData.SkuPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency_type', full_name='pogoprotos.data.SkuData.SkuPrice.currency_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='pogoprotos.data.SkuData.SkuPrice.price', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=511,
  serialized_end=559,
)

_SKUDATA_SKUPRESENTATIONDATA = _descriptor.Descriptor(
  name='SkuPresentationData',
  full_name='pogoprotos.data.SkuData.SkuPresentationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pogoprotos.data.SkuData.SkuPresentationData.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='pogoprotos.data.SkuData.SkuPresentationData.value', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=610,
)

_SKUDATA = _descriptor.Descriptor(
  name='SkuData',
  full_name='pogoprotos.data.SkuData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pogoprotos.data.SkuData.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_enabled', full_name='pogoprotos.data.SkuData.is_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='pogoprotos.data.SkuData.content', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='pogoprotos.data.SkuData.price', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type', full_name='pogoprotos.data.SkuData.payment_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified_timestamp_ms', full_name='pogoprotos.data.SkuData.last_modified_timestamp_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='presentation_data', full_name='pogoprotos.data.SkuData.presentation_data', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enabled_window_start_ms', full_name='pogoprotos.data.SkuData.enabled_window_start_ms', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enabled_window_end_ms', full_name='pogoprotos.data.SkuData.enabled_window_end_ms', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subscription_id', full_name='pogoprotos.data.SkuData.subscription_id', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SKUDATA_SKUCONTENT, _SKUDATA_SKUPRICE, _SKUDATA_SKUPRESENTATIONDATA, ],
  enum_types=[
    _SKUDATA_SKUPAYMENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=669,
)

_SKUDATA_SKUCONTENT.containing_type = _SKUDATA
_SKUDATA_SKUPRICE.containing_type = _SKUDATA
_SKUDATA_SKUPRESENTATIONDATA.containing_type = _SKUDATA
_SKUDATA.fields_by_name['content'].message_type = _SKUDATA_SKUCONTENT
_SKUDATA.fields_by_name['price'].message_type = _SKUDATA_SKUPRICE
_SKUDATA.fields_by_name['payment_type'].enum_type = _SKUDATA_SKUPAYMENTTYPE
_SKUDATA.fields_by_name['presentation_data'].message_type = _SKUDATA_SKUPRESENTATIONDATA
_SKUDATA_SKUPAYMENTTYPE.containing_type = _SKUDATA
DESCRIPTOR.message_types_by_name['SkuData'] = _SKUDATA

SkuData = _reflection.GeneratedProtocolMessageType('SkuData', (_message.Message,), dict(

  SkuContent = _reflection.GeneratedProtocolMessageType('SkuContent', (_message.Message,), dict(
    DESCRIPTOR = _SKUDATA_SKUCONTENT,
    __module__ = 'pogoprotos.data.sku_data_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.SkuData.SkuContent)
    ))
  ,

  SkuPrice = _reflection.GeneratedProtocolMessageType('SkuPrice', (_message.Message,), dict(
    DESCRIPTOR = _SKUDATA_SKUPRICE,
    __module__ = 'pogoprotos.data.sku_data_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.SkuData.SkuPrice)
    ))
  ,

  SkuPresentationData = _reflection.GeneratedProtocolMessageType('SkuPresentationData', (_message.Message,), dict(
    DESCRIPTOR = _SKUDATA_SKUPRESENTATIONDATA,
    __module__ = 'pogoprotos.data.sku_data_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.SkuData.SkuPresentationData)
    ))
  ,
  DESCRIPTOR = _SKUDATA,
  __module__ = 'pogoprotos.data.sku_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.SkuData)
  ))
_sym_db.RegisterMessage(SkuData)
_sym_db.RegisterMessage(SkuData.SkuContent)
_sym_db.RegisterMessage(SkuData.SkuPrice)
_sym_db.RegisterMessage(SkuData.SkuPresentationData)


# @@protoc_insertion_point(module_scope)
