from .core import get_visualization_context
from .hijack import hijack_method, get_original_method
from .tracers.agent import AgentTracer
from .visualize import visualize, visualize_object
import inspect
import sys
from .ice.trace import enable_trace, trace

def setup_agent_visualization():
    """Set up visualization for any agent-like class with specific methods."""
    # Methods to visualize
    target_methods = ["handle_message", "agent_cot", "call_llm"]
    
    try:
        # Look through all loaded modules
        for module_name, module in sys.modules.items():
            if not module or not hasattr(module, '__dict__'):
                continue
                
            # Find all classes in the module
            for name, obj in module.__dict__.items():
                if not inspect.isclass(obj):
                    continue
                    
                # Check if class has any of our target methods
                for method in target_methods:
                    if hasattr(obj, method):
                        try:
                            hijack_method(obj, method)
                            print(f"Visualizing {method} for {obj.__name__}")
                        except Exception as e:
                            print(f"Warning: Could not hijack {method} for {obj.__name__}: {str(e)}")
                            
    except Exception as e:
        print(f"Warning: Error setting up agent visualization: {str(e)}")

# Set up visualization when module is imported
setup_agent_visualization()

# Expose the visualize decorator
def visualize(fn):
    enable_trace()  # Enable tracing when the decorator is used
    return trace(fn)

__all__ = [
    "visualize",
    "visualize_object",
    "hijack_method",
    "get_original_method",
    "AgentTracer",
    "get_visualization_context",
    "get_server"
] 