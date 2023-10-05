# Copyright(C) 2023 Anders Logg
# Licensed under the MIT License

import logging as _logging


def _init_logging(name):
    "Internal function for initializing logging"

    # Initialize logger
    format = "%(asctime)s [%(name)s] [%(levelname)s] %(message)s"
    _logging.basicConfig(format=format)
    logger = _logging.getLogger(name)
    logger.setLevel(_logging.INFO)

    # Define error and critical as print + exit
    def error(message):
        logger.error(message)
        exit(1)

    def critical(message):
        logger.critical(message)
        exit(1)

    return (logger.debug, logger.info, logger.warning, error, critical)


debug, info, warning, error, critical = _init_logging("dtcc-common")


def init_logging(name):
    "Initialize logging for given package"
    debug(f"Initializing logging for {name}")
    return _init_logging(name)


def set_log_level(level):
    """Set log level. Valid levels are:

    "DEBUG"
    "INFO"
    "WARNING"
    "ERROR"
    "CRITICAL"

    """
    logger.setLevel(level)
