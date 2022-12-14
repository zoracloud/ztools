# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: garbage_collection_policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='garbage_collection_policy.proto',
  package='orchestration',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fgarbage_collection_policy.proto\x12\rorchestration\"\xc1\x01\n\x17GarbageCollectionPolicy\x12h\n\x1ckeep_most_recently_published\x18\x01 \x01(\x0b\x32@.orchestration.GarbageCollectionPolicy.KeepMostRecentlyPublishedH\x00\x1a\x32\n\x19KeepMostRecentlyPublished\x12\x15\n\rnum_artifacts\x18\x01 \x01(\x05\x42\x08\n\x06policyb\x06proto3'
)




_GARBAGECOLLECTIONPOLICY_KEEPMOSTRECENTLYPUBLISHED = _descriptor.Descriptor(
  name='KeepMostRecentlyPublished',
  full_name='orchestration.GarbageCollectionPolicy.KeepMostRecentlyPublished',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_artifacts', full_name='orchestration.GarbageCollectionPolicy.KeepMostRecentlyPublished.num_artifacts', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=184,
  serialized_end=234,
)

_GARBAGECOLLECTIONPOLICY = _descriptor.Descriptor(
  name='GarbageCollectionPolicy',
  full_name='orchestration.GarbageCollectionPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keep_most_recently_published', full_name='orchestration.GarbageCollectionPolicy.keep_most_recently_published', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GARBAGECOLLECTIONPOLICY_KEEPMOSTRECENTLYPUBLISHED, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='policy', full_name='orchestration.GarbageCollectionPolicy.policy',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=51,
  serialized_end=244,
)

_GARBAGECOLLECTIONPOLICY_KEEPMOSTRECENTLYPUBLISHED.containing_type = _GARBAGECOLLECTIONPOLICY
_GARBAGECOLLECTIONPOLICY.fields_by_name['keep_most_recently_published'].message_type = _GARBAGECOLLECTIONPOLICY_KEEPMOSTRECENTLYPUBLISHED
_GARBAGECOLLECTIONPOLICY.oneofs_by_name['policy'].fields.append(
  _GARBAGECOLLECTIONPOLICY.fields_by_name['keep_most_recently_published'])
_GARBAGECOLLECTIONPOLICY.fields_by_name['keep_most_recently_published'].containing_oneof = _GARBAGECOLLECTIONPOLICY.oneofs_by_name['policy']
DESCRIPTOR.message_types_by_name['GarbageCollectionPolicy'] = _GARBAGECOLLECTIONPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GarbageCollectionPolicy = _reflection.GeneratedProtocolMessageType('GarbageCollectionPolicy', (_message.Message,), {

  'KeepMostRecentlyPublished' : _reflection.GeneratedProtocolMessageType('KeepMostRecentlyPublished', (_message.Message,), {
    'DESCRIPTOR' : _GARBAGECOLLECTIONPOLICY_KEEPMOSTRECENTLYPUBLISHED,
    '__module__' : 'garbage_collection_policy_pb2'
    # @@protoc_insertion_point(class_scope:orchestration.GarbageCollectionPolicy.KeepMostRecentlyPublished)
    })
  ,
  'DESCRIPTOR' : _GARBAGECOLLECTIONPOLICY,
  '__module__' : 'garbage_collection_policy_pb2'
  # @@protoc_insertion_point(class_scope:orchestration.GarbageCollectionPolicy)
  })
_sym_db.RegisterMessage(GarbageCollectionPolicy)
_sym_db.RegisterMessage(GarbageCollectionPolicy.KeepMostRecentlyPublished)


# @@protoc_insertion_point(module_scope)
