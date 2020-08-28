# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gamefitness/game_fitness_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gamefitness/game_fitness_action.proto',
  package='pogoprotos.networking.requests.game.gamefitness',
  syntax='proto3',
  serialized_pb=_b('\nIpogoprotos/networking/requests/game/gamefitness/game_fitness_action.proto\x12/pogoprotos.networking.requests.game.gamefitness*\x83\x02\n\x11GameFitnessAction\x12\x1f\n\x1bUNKNOWN_GAME_FITNESS_ACTION\x10\x00\x12\x1c\n\x16UPDATE_FITNESS_METRICS\x10\x80\x88\'\x12\x18\n\x12GET_FITNESS_REPORT\x10\x81\x88\'\x12!\n\x1bGET_ADVENTURE_SYNC_SETTINGS\x10\x82\x88\'\x12$\n\x1eUPDATE_ADVENTURE_SYNC_SETTINGS\x10\x83\x88\'\x12#\n\x1dUPDATE_ADVENTURE_SYNC_FITNESS\x10\x84\x88\'\x12\'\n!GET_ADVENTURE_SYNC_FITNESS_REPORT\x10\x85\x88\'b\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GAMEFITNESSACTION = _descriptor.EnumDescriptor(
  name='GameFitnessAction',
  full_name='pogoprotos.networking.requests.game.gamefitness.GameFitnessAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_GAME_FITNESS_ACTION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_FITNESS_METRICS', index=1, number=640000,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FITNESS_REPORT', index=2, number=640001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_ADVENTURE_SYNC_SETTINGS', index=3, number=640002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_ADVENTURE_SYNC_SETTINGS', index=4, number=640003,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_ADVENTURE_SYNC_FITNESS', index=5, number=640004,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_ADVENTURE_SYNC_FITNESS_REPORT', index=6, number=640005,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=127,
  serialized_end=386,
)
_sym_db.RegisterEnumDescriptor(_GAMEFITNESSACTION)

GameFitnessAction = enum_type_wrapper.EnumTypeWrapper(_GAMEFITNESSACTION)
UNKNOWN_GAME_FITNESS_ACTION = 0
UPDATE_FITNESS_METRICS = 640000
GET_FITNESS_REPORT = 640001
GET_ADVENTURE_SYNC_SETTINGS = 640002
UPDATE_ADVENTURE_SYNC_SETTINGS = 640003
UPDATE_ADVENTURE_SYNC_FITNESS = 640004
GET_ADVENTURE_SYNC_FITNESS_REPORT = 640005


DESCRIPTOR.enum_types_by_name['GameFitnessAction'] = _GAMEFITNESSACTION


# @@protoc_insertion_point(module_scope)
