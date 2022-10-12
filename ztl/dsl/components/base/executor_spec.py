"""Executor specifications for defining what to to execute."""

import copy
from typing import cast, Iterable, List, Optional, Type

from ztl import types
from ztl.dsl.components.base import base_executor
from ztl.proto.orchestration.compiled_proto import executable_spec_pb2
from ztl.utils import import_utils
from ztl.utils import json_utils
from ztl.utils import name_utils

from google.protobuf import message


class ExecutorSpec(json_utils.Jsonable):
  """A specification for a component executor.
  An instance of ExecutorSpec describes the implementation of a component.
  """

  def encode(
      self,
      component_spec: Optional[types.ComponentSpec] = None) -> message.Message:
    """Encodes ExecutorSpec into an IR proto for compiling.
    This method will be used by DSL compiler to generate the corresponding IR.
    Args:
      component_spec: Optional. The ComponentSpec to help with the encoding.
    Returns:
      An executor spec proto.
    """
    # TODO(b/158712976, b/161286496): Serialize executor specs for different
    # platforms.
    raise NotImplementedError('{} does not support encoding into IR.'.format(
        name_utils.get_full_name(self.__class__)))

  def copy(self) -> 'ExecutorSpec':
    """Makes a copy of the ExecutorSpec.
    An abstract method to implement to make a copy of the ExecutorSpec instance.
    Deepcopy is preferred in the implementation. But if for any reason a
    deepcopy is not able to be made because of some fields are not deepcopyable,
    it is OK to make a shallow copy as long as the subfield is consider
    globally immutable.
    Returns:
      A copy of ExecutorSpec.
    """
    return cast('ExecutorSpec', copy.deepcopy(self))


class ExecutorClassSpec(ExecutorSpec):
  """A specification of executor class.
  Attributes:
    executor_class: a subclass of base_executor.BaseExecutor used to execute
      this component (required).
    extra_flags: extra flags to be set in the Python base executor.
  """

  def __init__(self, executor_class: Type[base_executor.BaseExecutor]):
    if not executor_class:
      raise ValueError('executor_class is required')
    self.executor_class = executor_class
    self._class_path = None
    self.extra_flags = []
    super().__init__()

  def __reduce__(self):
    # When executing on the Beam DAG runner, the ExecutorClassSpec instance
    # is pickled using the "dill" library. To make sure that the executor code
    # itself is not pickled, we save the class path which will be reimported
    # by the worker in this custom __reduce__ function.
    #
    # See https://docs.python.org/3/library/pickle.html#object.__reduce__ for
    # more details.
    return (ExecutorClassSpec._reconstruct_from_executor_class_path,
            (self.class_path,))

  def _set_class_path(self):
    if self._class_path is None:
      self._class_path = name_utils.get_full_name(self.executor_class)

  @property
  def class_path(self):
    """Fully qualified class name for the executor class.
    <executor_class_module>.<executor_class_name>
    Returns:
      Fully qualified class name for the executor class.
    """
    self._set_class_path()
    return self._class_path

  @staticmethod
  def _reconstruct_from_executor_class_path(executor_class_path):
    executor_class = import_utils.import_class_by_path(executor_class_path)
    return ExecutorClassSpec(executor_class)

  def encode(
      self,
      component_spec: Optional[types.ComponentSpec] = None) -> message.Message:
    result = executable_spec_pb2.PythonClassExecutableSpec()
    result.class_path = self.class_path
    result.extra_flags.extend(self.extra_flags)
    return result

  def add_extra_flags(self, extra_flags: Iterable[str]) -> None:
    self.extra_flags.extend(extra_flags)

  def copy(self) -> 'ExecutorClassSpec':
    # The __reduce__() method is customized and the function
    # import_class_by_path() is used in it. import_class_by_path() doesn't work
    # with nested class which is very common in tests. copy.deepcopy(self)
    # desn't work.
    # So in this implementation, a new
    # ExecutorClassSpec is created and every field in the old instance is
    # deepcopied to the new instance.
    cls = self.__class__
    result = cls.__new__(cls)
    for k, v in self.__dict__.items():
      setattr(result, k, copy.deepcopy(v))
    return result


class BeamExecutorSpec(ExecutorClassSpec):
  """A specification of Beam executor.
  Attributes:
    executor_class: a subclass of base_executor.BaseExecutor used to execute
      this component (required).
    extra_flags: extra flags to be set in the Python base executor.
    beam_pipeline_args: arguments for Beam powered Components.
  """

  def __init__(self, executor_class: Type[base_executor.BaseExecutor]):
    super().__init__(executor_class=executor_class)
    self.beam_pipeline_args = []

  def encode(
      self,
      component_spec: Optional[types.ComponentSpec] = None) -> message.Message:
    result = executable_spec_pb2.BeamExecutableSpec()
    result.python_executor_spec.CopyFrom(
        super().encode(component_spec=component_spec))
    result.beam_pipeline_args.extend(self.beam_pipeline_args)
    return result

  def add_beam_pipeline_args(self, beam_pipeline_args: Iterable[str]) -> None:
    self.beam_pipeline_args.extend(beam_pipeline_args)

  def copy(self) -> 'BeamExecutorSpec':
    return cast(self.__class__, super().copy())


class ExecutorContainerSpec(ExecutorSpec):
  """A specification of a container.
  The spec includes image, command line entrypoint and arguments for a
  container. For example:
  spec = ExecutorContainerSpec(
    image='docker/whalesay',
    command=['cowsay'],
    args=['hello wolrd'])
  Attributes:
    image: Container image that has executor application. Assumption is that
      this container image is separately release-managed, and tagged/versioned
      accordingly.
    command: Container entrypoint array. Not executed within a shell. The docker
      image's ENTRYPOINT is used if this is not provided. The Jinja templating
      mechanism is used for constructing a user-specified command-line
      invocation based on input and output metadata at runtime.
    args: Arguments to the container entrypoint. The docker image's CMD is used
      if this is not provided. The Jinja templating mechanism is used for
      constructing a user-specified command-line invocation based on input and
      output metadata at runtime.
  """

  def __init__(self,
               image: str,
               command: Optional[List[str]] = None,
               args: Optional[List[str]] = None):
    if not image:
      raise ValueError('image cannot be None or empty.')
    self.image = image
    self.command = command
    self.args = args
    super().__init__()