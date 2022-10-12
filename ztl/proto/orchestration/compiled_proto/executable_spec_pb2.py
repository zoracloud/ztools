# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: executable_spec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import placeholder_pb2 as placeholder__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='executable_spec.proto',
  package='orchestration',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x65xecutable_spec.proto\x12\rorchestration\x1a\x11placeholder.proto\"D\n\x19PythonClassExecutableSpec\x12\x12\n\nclass_path\x18\x01 \x01(\t\x12\x13\n\x0b\x65xtra_flags\x18\x02 \x03(\t\"x\n\x12\x42\x65\x61mExecutableSpec\x12\x46\n\x14python_executor_spec\x18\x01 \x01(\x0b\x32(.orchestration.PythonClassExecutableSpec\x12\x1a\n\x12\x62\x65\x61m_pipeline_args\x18\x02 \x03(\t\"\x94\x01\n\x17\x43ontainerExecutableSpec\x12\r\n\x05image\x18\x01 \x01(\t\x12\x36\n\x08\x63ommands\x18\x02 \x03(\x0b\x32$.orchestration.PlaceholderExpression\x12\x32\n\x04\x61rgs\x18\x03 \x03(\x0b\x32$.orchestration.PlaceholderExpressionb\x06proto3'
  ,
  dependencies=[placeholder__pb2.DESCRIPTOR,])




_PYTHONCLASSEXECUTABLESPEC = _descriptor.Descriptor(
  name='PythonClassExecutableSpec',
  full_name='orchestration.PythonClassExecutableSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_path', full_name='orchestration.PythonClassExecutableSpec.class_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_flags', full_name='orchestration.PythonClassExecutableSpec.extra_flags', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=127,
)


_BEAMEXECUTABLESPEC = _descriptor.Descriptor(
  name='BeamExecutableSpec',
  full_name='orchestration.BeamExecutableSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='python_executor_spec', full_name='orchestration.BeamExecutableSpec.python_executor_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='beam_pipeline_args', full_name='orchestration.BeamExecutableSpec.beam_pipeline_args', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=249,
)


_CONTAINEREXECUTABLESPEC = _descriptor.Descriptor(
  name='ContainerExecutableSpec',
  full_name='orchestration.ContainerExecutableSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='orchestration.ContainerExecutableSpec.image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commands', full_name='orchestration.ContainerExecutableSpec.commands', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args', full_name='orchestration.ContainerExecutableSpec.args', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=400,
)

_BEAMEXECUTABLESPEC.fields_by_name['python_executor_spec'].message_type = _PYTHONCLASSEXECUTABLESPEC
_CONTAINEREXECUTABLESPEC.fields_by_name['commands'].message_type = placeholder__pb2._PLACEHOLDEREXPRESSION
_CONTAINEREXECUTABLESPEC.fields_by_name['args'].message_type = placeholder__pb2._PLACEHOLDEREXPRESSION
DESCRIPTOR.message_types_by_name['PythonClassExecutableSpec'] = _PYTHONCLASSEXECUTABLESPEC
DESCRIPTOR.message_types_by_name['BeamExecutableSpec'] = _BEAMEXECUTABLESPEC
DESCRIPTOR.message_types_by_name['ContainerExecutableSpec'] = _CONTAINEREXECUTABLESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PythonClassExecutableSpec = _reflection.GeneratedProtocolMessageType('PythonClassExecutableSpec', (_message.Message,), {
  'DESCRIPTOR' : _PYTHONCLASSEXECUTABLESPEC,
  '__module__' : 'executable_spec_pb2'
  # @@protoc_insertion_point(class_scope:orchestration.PythonClassExecutableSpec)
  })
_sym_db.RegisterMessage(PythonClassExecutableSpec)

BeamExecutableSpec = _reflection.GeneratedProtocolMessageType('BeamExecutableSpec', (_message.Message,), {
  'DESCRIPTOR' : _BEAMEXECUTABLESPEC,
  '__module__' : 'executable_spec_pb2'
  # @@protoc_insertion_point(class_scope:orchestration.BeamExecutableSpec)
  })
_sym_db.RegisterMessage(BeamExecutableSpec)

ContainerExecutableSpec = _reflection.GeneratedProtocolMessageType('ContainerExecutableSpec', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINEREXECUTABLESPEC,
  '__module__' : 'executable_spec_pb2'
  # @@protoc_insertion_point(class_scope:orchestration.ContainerExecutableSpec)
  })
_sym_db.RegisterMessage(ContainerExecutableSpec)


# @@protoc_insertion_point(module_scope)