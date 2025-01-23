import os
import sys

# Add the ice directory itself to PYTHONPATH so 'ice.*' imports work
ice_dir = os.path.dirname(__file__)
if ice_dir not in sys.path:
    sys.path.insert(0, ice_dir)

from .logging import init_logging

init_logging()

try:
    from .version import __version__
except ImportError:
    # version.py is auto-generated with the git tag when building
    __version__ = ""
