import logging


def get_module_logger(module_name: str) -> logging.Logger:
    """Instantiates a logger object on stdout
    Args:
        module_name (str): Name of the module outputting the logs
    Returns:
        logger (Logging.logger): A logger object
    """
    logger = logging.getLogger(module_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
