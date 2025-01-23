from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from fvalues import F

JSONValue = Union[None, bool, int, float, str, List["JSONValue"], Dict[str, "JSONValue"]]


def to_json_value(x: Any) -> JSONValue:
    """Convert a value to a JSON-serializable value."""
    if isinstance(x, (type(None), bool, int, float, str)):
        return x
    elif isinstance(x, (list, tuple)):
        return [to_json_value(v) for v in x]
    elif isinstance(x, dict):
        return {str(k): to_json_value(v) for k, v in x.items()}
    elif isinstance(x, F):
        return {"value": str(x), "format": "F"}
    elif hasattr(x, "dict"):
        return to_json_value(x.dict())
    else:
        return str(x)
