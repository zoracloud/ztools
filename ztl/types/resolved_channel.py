"""Module for ResolvedChannel.
The main purpose of this module is to break the cyclic import dependency.
"""

from typing import Optional, Type

from ztl.dsl.control_flow import for_each_internal
from ztl.dsl.input_resolution import resolver_op
from ztl.types import artifact
from ztl.types import channel
from ztl.utils import doc_controls


@doc_controls.do_not_generate_docs
class ResolvedChannel(channel.BaseChannel):
  """A BaseChannel that refers to the resolver function's output.
  For example:
      trainer_inputs = trainer_resolver_function(
          examples=example_gen.outputs['examples'])
      trainer = Trainer(examples=trainer_inputs['examples'])
  then the `trainer_inputs['examples']` is a ResolvedChannel instance.
  """

  def __init__(
      self,
      artifact_type: Type[artifact.Artifact],
      output_node: resolver_op.Node,
      output_key: Optional[str] = None,
      for_each_context: Optional[for_each_internal.ForEachContext] = None):
    super().__init__(artifact_type)
    self._output_node = output_node
    self._output_key = output_key
    self._for_each_context = for_each_context

  @property
  def output_node(self) -> resolver_op.Node:
    return self._output_node

  @property
  def output_key(self) -> Optional[str]:
    return self._output_key

  @property
  def for_each_context(self) -> Optional[for_each_internal.ForEachContext]:
    return self._for_each_context