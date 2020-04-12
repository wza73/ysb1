#! coding: utf-8
import logging
from logging.handlers import RotatingFileHandler

LOGGER = logging.getLogger("ThirdPlugin")
def set_logger():
    handler = RotatingFileHandler("/var/log/third_plugin.log",
                                  maxBytes=2*1024*1024, backupCount=5, mode="a")
    formatter = logging.Formatter("%(asctime)s %(name)-6s %(levelname)-4s %(message)s")
    handler.setFormatter(formatter)

    LOGGER.addHandler(handler)
    LOGGER.setLevel(logging.INFO)
set_logger()

def get_logger():
    return LOGGER



