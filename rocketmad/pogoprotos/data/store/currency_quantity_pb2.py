# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/store/currency_quantity.proto

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
  name='pogoprotos/data/store/currency_quantity.proto',
  package='pogoprotos.data.store',
  syntax='proto3',
  serialized_pb=_b('\n-pogoprotos/data/store/currency_quantity.proto\x12\x15pogoprotos.data.store\";\n\x10\x43urrencyQuantity\x12\x15\n\rcurrency_type\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CURRENCYQUANTITY = _descriptor.Descriptor(
  name='CurrencyQuantity',
  full_name='pogoprotos.data.store.CurrencyQuantity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency_type', full_name='pogoprotos.data.store.CurrencyQuantity.currency_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='pogoprotos.data.store.CurrencyQuantity.quantity', index=1,
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
  serialized_start=72,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['CurrencyQuantity'] = _CURRENCYQUANTITY

CurrencyQuantity = _reflection.GeneratedProtocolMessageType('CurrencyQuantity', (_message.Message,), dict(
  DESCRIPTOR = _CURRENCYQUANTITY,
  __module__ = 'pogoprotos.data.store.currency_quantity_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.store.CurrencyQuantity)
  ))
_sym_db.RegisterMessage(CurrencyQuantity)


# @@protoc_insertion_point(module_scope)
