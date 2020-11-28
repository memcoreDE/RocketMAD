# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/tutorial_state.proto

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
  name='pogoprotos/enums/tutorial_state.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%pogoprotos/enums/tutorial_state.proto\x12\x10pogoprotos.enums*\xc7\n\n\rTutorialState\x12\x10\n\x0cLEGAL_SCREEN\x10\x00\x12\x14\n\x10\x41VATAR_SELECTION\x10\x01\x12\x14\n\x10\x41\x43\x43OUNT_CREATION\x10\x02\x12\x13\n\x0fPOKEMON_CAPTURE\x10\x03\x12\x12\n\x0eNAME_SELECTION\x10\x04\x12\x11\n\rPOKEMON_BERRY\x10\x05\x12\x1b\n\x17USE_ITEM_TUTORIAL_STATE\x10\x06\x12\"\n\x1e\x46IRST_TIME_EXPERIENCE_COMPLETE\x10\x07\x12\x15\n\x11POKESTOP_TUTORIAL\x10\x08\x12\x10\n\x0cGYM_TUTORIAL\x10\t\x12\x1c\n\x18\x43HALLENGE_QUEST_TUTORIAL\x10\n\x12\x1f\n\x1bPRIVACY_POLICY_CONFIRMATION\x10\x0b\x12\x14\n\x10TRADING_TUTORIAL\x10\x0c\x12\x1b\n\x17POI_SUBMISSION_TUTORIAL\x10\r\x12\x15\n\x11V1_START_TUTORIAL\x10\x0e\x12\x15\n\x11V2_START_TUTORIAL\x10\x0f\x12\x18\n\x14V2_CUSTOMIZED_AVATAR\x10\x10\x12\x18\n\x14V2_CAUGHT_FIRST_WILD\x10\x11\x12 \n\x1cV2_FINISHED_TUTORIAL_CATCHES\x10\x12\x12\x15\n\x11V2_NAME_SELECTION\x10\x13\x12\x10\n\x0cV2_EGG_GIVEN\x10\x14\x12\x19\n\x15V2_START_EGG_TUTORIAL\x10\x15\x12\x1d\n\x19V2_COMPLETED_EGG_TUTORIAL\x10\x16\x12\x15\n\x11\x41R_PHOTO_TUTORIAL\x10\x17\x12\x1c\n\x18STARTER_POKEMON_CAPTURED\x10\x18\x12\x1e\n\x1a\x41R_PHOTO_FIRST_TIME_DIALOG\x10\x19\x12\x1d\n\x19\x41R_CLASSIC_PHOTO_TUTORIAL\x10\x1a\x12\x1a\n\x16\x41R_PLUS_PHOTO_TUTORIAL\x10\x1b\x12 \n\x1cINVASION_INTRODUCTION_DIALOG\x10\x1d\x12\x1d\n\x19INVASION_ENCOUNTER_DIALOG\x10\x1e\x12\"\n\x1eINVASION_SHADOW_POKEMON_DIALOG\x10\x1f\x12 \n\x1cINVASION_MAP_FRAGMENT_DIALOG\x10!\x12 \n\x1cINVASION_MAP_RECEIVED_DIALOG\x10\"\x12\"\n\x1eINVASION_MAP_2_RECEIVED_DIALOG\x10#\x12\x18\n\x14\x42UDDY_WELCOME_PROMPT\x10$\x12\x1a\n\x16\x42UDDY_AR_PLUS_TUTORIAL\x10%\x12\x17\n\x13\x42UDDY_FEED_TUTORIAL\x10&\x12\x17\n\x13\x42UDDY_ON_MAP_PROMPT\x10\'\x12\x1f\n\x1b\x42\x41TTLE_LEAGUE_HELP_TUTORIAL\x10(\x12\x19\n\x15\x41RMP_TOS_CONFIRMATION\x10)\x12\x1e\n\x1a\x42UDDY_REMOTE_GIFT_TUTORIAL\x10*\x12\x15\n\x11XL_CANDY_TUTORIAL\x10+\x12\x1a\n\x16LEVEL_UP_PAGE_TUTORIAL\x10,\x12\"\n\x1e\x44\x41ILY_BONUS_ENCOUNTER_TUTORIAL\x10-\x12\x1b\n\x17SPONSORED_GIFT_TUTORIAL\x10.\x12\x1b\n\x17XGS_ONLINE_CONSENT_NOTE\x10/\x12(\n$APP_TRACKING_OPTIN_REQUIRED_TUTORIAL\x10\x30\x12\x1d\n\x19\x41PP_TRACKING_OPTIN_DIALOG\x10\x31\x62\x06proto3')
)

_TUTORIALSTATE = _descriptor.EnumDescriptor(
  name='TutorialState',
  full_name='pogoprotos.enums.TutorialState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEGAL_SCREEN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_SELECTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_CREATION', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_CAPTURE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_SELECTION', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_BERRY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USE_ITEM_TUTORIAL_STATE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST_TIME_EXPERIENCE_COMPLETE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKESTOP_TUTORIAL', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GYM_TUTORIAL', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_QUEST_TUTORIAL', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVACY_POLICY_CONFIRMATION', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADING_TUTORIAL', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_SUBMISSION_TUTORIAL', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V1_START_TUTORIAL', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_START_TUTORIAL', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_CUSTOMIZED_AVATAR', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_CAUGHT_FIRST_WILD', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_FINISHED_TUTORIAL_CATCHES', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_NAME_SELECTION', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_EGG_GIVEN', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_START_EGG_TUTORIAL', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2_COMPLETED_EGG_TUTORIAL', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_PHOTO_TUTORIAL', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARTER_POKEMON_CAPTURED', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_PHOTO_FIRST_TIME_DIALOG', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_CLASSIC_PHOTO_TUTORIAL', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AR_PLUS_PHOTO_TUTORIAL', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_INTRODUCTION_DIALOG', index=28, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_ENCOUNTER_DIALOG', index=29, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_SHADOW_POKEMON_DIALOG', index=30, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_MAP_FRAGMENT_DIALOG', index=31, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_MAP_RECEIVED_DIALOG', index=32, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVASION_MAP_2_RECEIVED_DIALOG', index=33, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_WELCOME_PROMPT', index=34, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_AR_PLUS_TUTORIAL', index=35, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_FEED_TUTORIAL', index=36, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_ON_MAP_PROMPT', index=37, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATTLE_LEAGUE_HELP_TUTORIAL', index=38, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARMP_TOS_CONFIRMATION', index=39, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDDY_REMOTE_GIFT_TUTORIAL', index=40, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XL_CANDY_TUTORIAL', index=41, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL_UP_PAGE_TUTORIAL', index=42, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAILY_BONUS_ENCOUNTER_TUTORIAL', index=43, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPONSORED_GIFT_TUTORIAL', index=44, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XGS_ONLINE_CONSENT_NOTE', index=45, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_TRACKING_OPTIN_REQUIRED_TUTORIAL', index=46, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_TRACKING_OPTIN_DIALOG', index=47, number=49,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=60,
  serialized_end=1411,
)
_sym_db.RegisterEnumDescriptor(_TUTORIALSTATE)

TutorialState = enum_type_wrapper.EnumTypeWrapper(_TUTORIALSTATE)
LEGAL_SCREEN = 0
AVATAR_SELECTION = 1
ACCOUNT_CREATION = 2
POKEMON_CAPTURE = 3
NAME_SELECTION = 4
POKEMON_BERRY = 5
USE_ITEM_TUTORIAL_STATE = 6
FIRST_TIME_EXPERIENCE_COMPLETE = 7
POKESTOP_TUTORIAL = 8
GYM_TUTORIAL = 9
CHALLENGE_QUEST_TUTORIAL = 10
PRIVACY_POLICY_CONFIRMATION = 11
TRADING_TUTORIAL = 12
POI_SUBMISSION_TUTORIAL = 13
V1_START_TUTORIAL = 14
V2_START_TUTORIAL = 15
V2_CUSTOMIZED_AVATAR = 16
V2_CAUGHT_FIRST_WILD = 17
V2_FINISHED_TUTORIAL_CATCHES = 18
V2_NAME_SELECTION = 19
V2_EGG_GIVEN = 20
V2_START_EGG_TUTORIAL = 21
V2_COMPLETED_EGG_TUTORIAL = 22
AR_PHOTO_TUTORIAL = 23
STARTER_POKEMON_CAPTURED = 24
AR_PHOTO_FIRST_TIME_DIALOG = 25
AR_CLASSIC_PHOTO_TUTORIAL = 26
AR_PLUS_PHOTO_TUTORIAL = 27
INVASION_INTRODUCTION_DIALOG = 29
INVASION_ENCOUNTER_DIALOG = 30
INVASION_SHADOW_POKEMON_DIALOG = 31
INVASION_MAP_FRAGMENT_DIALOG = 33
INVASION_MAP_RECEIVED_DIALOG = 34
INVASION_MAP_2_RECEIVED_DIALOG = 35
BUDDY_WELCOME_PROMPT = 36
BUDDY_AR_PLUS_TUTORIAL = 37
BUDDY_FEED_TUTORIAL = 38
BUDDY_ON_MAP_PROMPT = 39
BATTLE_LEAGUE_HELP_TUTORIAL = 40
ARMP_TOS_CONFIRMATION = 41
BUDDY_REMOTE_GIFT_TUTORIAL = 42
XL_CANDY_TUTORIAL = 43
LEVEL_UP_PAGE_TUTORIAL = 44
DAILY_BONUS_ENCOUNTER_TUTORIAL = 45
SPONSORED_GIFT_TUTORIAL = 46
XGS_ONLINE_CONSENT_NOTE = 47
APP_TRACKING_OPTIN_REQUIRED_TUTORIAL = 48
APP_TRACKING_OPTIN_DIALOG = 49


DESCRIPTOR.enum_types_by_name['TutorialState'] = _TUTORIALSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
