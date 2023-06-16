# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

# Set up default logger
import logging as _logging

_format = "%(asctime)s [%(name)s] [%(levelname)s] %(message)s"
_logging.basicConfig(format=_format)
_logger = _logging.getLogger("dtcc-common")
_logger.setLevel(_logging.INFO)

# Expose logging functions
debug = _logger.debug
info = _logger.info
warning = _logger.warning
error = _logger.error
critical = _logger.critical


def init_logging(name):
    "Initialize logging with given name"
    _logger.name = name


def set_log_level(level):
    """Set log level. Valid levels are:

    "DEBUG"
    "INFO"
    "WARNING"
    "ERROR"
    "CRITICAL"

    """
    logger.setLevel(level)
