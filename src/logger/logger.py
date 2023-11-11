import logging

from config.logging import logging_settings


def get_logger(name):
    logging.basicConfig(
        format=logging_settings.format,
        datefmt=logging_settings.datefmt,
        level=logging_settings.level.upper(),
    )

    logger = logging.getLogger(name)

    return logger
