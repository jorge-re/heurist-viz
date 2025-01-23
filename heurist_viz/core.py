import asyncio
from functools import wraps
from inspect import iscoroutinefunction
from typing import Any, Callable, TypeVar, cast

from .ice.trace import enable_trace, trace

T = TypeVar('T', bound=Callable[..., Any])

def visualize(fn: T) -> T:
    """
    Main decorator for visualizing agent operations.
    
    Args:
        fn: The async function to visualize
        
    Returns:
        Wrapped function with visualization enabled
        
    Example:
        @visualize
        async def run_agent():
            agent = CoreAgent()
            return await agent.handle_message("Hello!")
    """
    if not iscoroutinefunction(fn):
        raise TypeError("visualize must be given an async function")

    # Trace all globals in the function's module
    g = fn.__globals__
    for name, value in g.items():
        if getattr(value, "__module__", None) == fn.__module__:
            g[name] = trace(value)

    traced_fn = trace(fn)

    @wraps(fn)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        enable_trace()
        return await traced_fn(*args, **kwargs)

    return cast(T, wrapper)

def get_visualization_context(obj: Any) -> dict:
    """Get visualization context from an object."""
    context = {
        'type': obj.__class__.__name__,
        'id': id(obj),
    }
    
    # Add memory state if available
    if hasattr(obj, 'memory'):
        context['memory'] = obj.memory.get_state()
        
    # Add tools if available
    if hasattr(obj, 'available_tools'):
        context['tools'] = [
            {'name': tool.name, 'description': tool.description}
            for tool in obj.available_tools
        ]
        
    return context 