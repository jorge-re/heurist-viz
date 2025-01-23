from typing import Any, Callable

from ..ice.trace import TracedABC, trace

from ..ice.environment import env

from ..core import get_visualization_context

class AgentTracer(TracedABC):
    """Tracer for agent operations."""
    
    def __init__(self, agent_obj: Any, method: Callable):
        self.agent = agent_obj
        self.method = method
        self._environment = env()
        
    async def run(self, *args: Any, **kwargs: Any) -> Any:
        """Execute and trace the agent method"""
        try:
            result = await self.method(self.agent, *args, **kwargs)
            
            # For handle_message, we want to show the interaction
            if self.method.__name__ == 'handle_message':
                self._environment.print({
                    "input": args[0] if args else kwargs.get('message', ''),
                    "output": result
                })
            
            return result
            
        except Exception as e:
            self._environment.print({"error": str(e)})
            raise 