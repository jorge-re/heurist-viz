import asyncio
from functools import wraps
from inspect import iscoroutinefunction
from typing import Any, Callable, TypeVar, cast, Optional

from .ice.trace import enable_trace, trace

# from visualizer.ui.server import get_server
# from visualizer.core import get_visualization_context

from .ice.environment import env
from .ice.mode import Mode
from .ice.recipe import FunctionBasedRecipe, recipe
from merge_args import merge_args

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

    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Trace all globals in the module
        g = fn.__globals__
        for name, value in g.items():
            if getattr(value, "__module__", None) == fn.__module__:
                g[name] = trace(value)

        traced_fn = trace(fn)
        recipe.all_recipes.append(traced_fn)

        async def run_traced():
            enable_trace()
            return await traced_fn(*args, **kwargs)

        return asyncio.run(run_traced())

    return wrapper

def visualize_object(obj: Any) -> None:
    """
    Visualize an object's current state.
    
    Args:
        obj: The object to visualize
    """
    # Convert object to a simple dict representation for visualization
    state = {
        "type": obj.__class__.__name__,
        "attributes": {
            name: str(value) for name, value in vars(obj).items() 
            if not name.startswith('_')
        }
    }
    env().print(state) 