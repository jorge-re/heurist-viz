import logging
import os
import sys
import threading
from typing import Optional

import structlog
from structlog import get_logger
from structlog.stdlib import BoundLogger
from structlog.stdlib import LoggerFactory

# Prevent logging the warning 'None of PyTorch...' at the end of transformers/__init__.py.
# This depends on this being the first place that transformers is imported.
# It also assumes that transformers will be imported eventually
# so eagerly importing it now doesn't have an extra cost.
previous_verbosity = os.environ.get("TRANSFORMERS_VERBOSITY", None)
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
import transformers  # noqa

# Allow using the TRANSFORMERS_VERBOSITY env var normally to still work,
# and avoid suppressing other warnings.
if previous_verbosity:  # Setting to None raises an error
    os.environ["TRANSFORMERS_VERBOSITY"] = previous_verbosity

# Used to prevent interleaved logging from multiple threads. See [Settings.__get_and_store].
log_lock = threading.Lock()


def init_logging(level: Optional[str] = None):
    if level:
        level = getattr(logging, level.upper())
    else:
        level = logging.INFO

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stderr,
        level=level,
    )

    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.dev.ConsoleRenderer(),
        ],
        context_class=dict,
        logger_factory=LoggerFactory(),
        wrapper_class=BoundLogger,
        cache_logger_on_first_use=True,
    )

    log = get_logger()
    log.debug("Logging initialized")
