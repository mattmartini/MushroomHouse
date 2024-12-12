"""Mock GPIO for use during development"""

from mushrooms import log

logger = log.get_logger()


BOARD = "board"
BCM = "bcm"
OUT = "out"
IN = "in"
HIGH = True
LOW = False


def setmode(mode):
    logger.debug("Set GPIO mode: %s", mode)
    print(mode)


def setup(pin, value):
    logger.debug("Set GPIO pin: %s value: %s", pin, value)
    print(pin, ":", value)


def output(pin, value):
    logger.debug("GPIO output pin: %s value: %s", pin, value)
    print(pin, ":", value)


def cleanup():
    logger.debug("GPIO cleanup")
    print("clean-up")


def setwarnings(flag):
    logger.debug("GPIO set warnings to false")
    print("False")
