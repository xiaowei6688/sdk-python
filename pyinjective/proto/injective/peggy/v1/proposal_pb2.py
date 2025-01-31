# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/proposal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/peggy/v1/proposal.proto',
  package='injective.peggy.v1',
  syntax='proto3',
  serialized_options=b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!injective/peggy/v1/proposal.proto\x12\x12injective.peggy.v1\x1a\x14gogoproto/gogo.proto\"o\n\"BlacklistEthereumAddressesProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1b\n\x13\x62lacklist_addresses\x18\x03 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"l\n\x1fRevokeEthereumBlacklistProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1b\n\x13\x62lacklist_addresses\x18\x03 \x03(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\x42MZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_BLACKLISTETHEREUMADDRESSESPROPOSAL = _descriptor.Descriptor(
  name='BlacklistEthereumAddressesProposal',
  full_name='injective.peggy.v1.BlacklistEthereumAddressesProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.peggy.v1.BlacklistEthereumAddressesProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.peggy.v1.BlacklistEthereumAddressesProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blacklist_addresses', full_name='injective.peggy.v1.BlacklistEthereumAddressesProposal.blacklist_addresses', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=190,
)


_REVOKEETHEREUMBLACKLISTPROPOSAL = _descriptor.Descriptor(
  name='RevokeEthereumBlacklistProposal',
  full_name='injective.peggy.v1.RevokeEthereumBlacklistProposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='injective.peggy.v1.RevokeEthereumBlacklistProposal.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='injective.peggy.v1.RevokeEthereumBlacklistProposal.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blacklist_addresses', full_name='injective.peggy.v1.RevokeEthereumBlacklistProposal.blacklist_addresses', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\350\240\037\000\210\240\037\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=300,
)

DESCRIPTOR.message_types_by_name['BlacklistEthereumAddressesProposal'] = _BLACKLISTETHEREUMADDRESSESPROPOSAL
DESCRIPTOR.message_types_by_name['RevokeEthereumBlacklistProposal'] = _REVOKEETHEREUMBLACKLISTPROPOSAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlacklistEthereumAddressesProposal = _reflection.GeneratedProtocolMessageType('BlacklistEthereumAddressesProposal', (_message.Message,), {
  'DESCRIPTOR' : _BLACKLISTETHEREUMADDRESSESPROPOSAL,
  '__module__' : 'injective.peggy.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.BlacklistEthereumAddressesProposal)
  })
_sym_db.RegisterMessage(BlacklistEthereumAddressesProposal)

RevokeEthereumBlacklistProposal = _reflection.GeneratedProtocolMessageType('RevokeEthereumBlacklistProposal', (_message.Message,), {
  'DESCRIPTOR' : _REVOKEETHEREUMBLACKLISTPROPOSAL,
  '__module__' : 'injective.peggy.v1.proposal_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.RevokeEthereumBlacklistProposal)
  })
_sym_db.RegisterMessage(RevokeEthereumBlacklistProposal)


DESCRIPTOR._options = None
_BLACKLISTETHEREUMADDRESSESPROPOSAL._options = None
_REVOKEETHEREUMBLACKLISTPROPOSAL._options = None
# @@protoc_insertion_point(module_scope)
