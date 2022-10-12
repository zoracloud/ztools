"""Utils for TFX component types. Intended for internal usage only."""

from typing import Any, Callable, Dict, Optional, Type

from ztl import types
from ztl.dsl.components.base import base_component
from ztl.dsl.components.base import executor_spec as base_executor_spec
from ztl.types import component_spec
from ztl.types.system_executions import SystemExecution


def create_tfx_component_class(
    name: str,
    tfx_executor_spec: base_executor_spec.ExecutorSpec,
    input_channel_parameters: Optional[Dict[
        str, component_spec.ChannelParameter]] = None,
    output_channel_parameters: Optional[Dict[
        str, component_spec.ChannelParameter]] = None,
    execution_parameters: Optional[Dict[
        str, component_spec.ExecutionParameter]] = None,
    type_annotation: Optional[Type[SystemExecution]] = None,
    default_init_args: Optional[Dict[str, Any]] = None,
    base_class: Type[
        base_component.BaseComponent] = base_component.BaseComponent,
) -> Callable[..., base_component.BaseComponent]:
  """Creates a TFX component class dynamically."""
  tfx_component_spec_class = type(
      str(name) + 'Spec',
      (component_spec.ComponentSpec,),
      dict(
          PARAMETERS=execution_parameters or {},
          INPUTS=input_channel_parameters or {},
          OUTPUTS=output_channel_parameters or {},
          TYPE_ANNOTATION=type_annotation,
      ),
  )

  def tfx_component_class_init(self, **kwargs):
    arguments = {}
    arguments.update(kwargs)
    arguments.update(default_init_args or {})

    # Provide default values for output channels.
    output_channel_params = output_channel_parameters or {}
    for output_key, output_channel_param in output_channel_params.items():
      if output_key not in arguments:
        arguments[output_key] = types.Channel(type=output_channel_param.type)

    base_class.__init__(
        self,
        # Generate spec by wiring up the input/output channel.
        spec=self.__class__.SPEC_CLASS(**arguments))
    # Set class name as the default id. It can be overwritten by the user.
    if not self.id:
      base_class.with_id(self, self.__class__.__name__)

  tfx_component_class = type(
      str(name),
      (base_class,),
      dict(
          SPEC_CLASS=tfx_component_spec_class,
          EXECUTOR_SPEC=tfx_executor_spec,
          __init__=tfx_component_class_init,
      ),
  )
  return tfx_component_class