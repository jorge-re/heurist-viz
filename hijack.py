import inspect
from typing import Any, Callable, Type

import gorilla
from .ice.trace import TracedABC

from .tracers.agent import AgentTracer

VISUALIZER_PATCH_ID = "agent-viz"

def hijack_method(
    cls: Type[Any],
    method_name: str,
    tracer_cls: Type[TracedABC] = AgentTracer
) -> None:
    """
    Hijack a method for visualization.
    
    Args:
        cls: The class containing the method to hijack
        method_name: Name of the method to hijack
        tracer_cls: Tracer class to use (defaults to AgentTracer)
    """
    # Check if method exists
    if not hasattr(cls, method_name):
        raise AttributeError(f"Method {method_name} not found in {cls.__name__}")
    
    original_method = getattr(cls, method_name)
    
    if not inspect.iscoroutinefunction(original_method):
        raise TypeError(f"Method {method_name} must be async")
    
    async def wrapped(self: Any, *args: Any, **kwargs: Any) -> Any:
        tracer = tracer_cls(self, original_method)
        return await tracer.run(*args, **kwargs)
    
    # Apply the patch with settings to handle existing methods
    settings = gorilla.Settings(
        allow_hit=True,  # Allow overwriting existing method
        store_hit=True,  # Store the original method
        store_hit_id=VISUALIZER_PATCH_ID,  # Use our ID for storage
    )
    
    patch = gorilla.Patch(
        destination=cls,
        name=method_name,
        obj=wrapped,
        settings=settings
    )
    
    gorilla.apply(patch)

def get_original_method(cls: Type[Any], method_name: str) -> Callable:
    """Get the original (un-hijacked) method"""
    return gorilla.get_original_attribute(
        cls,
        method_name,
        VISUALIZER_PATCH_ID
    ) 