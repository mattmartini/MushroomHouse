"""Mock GPIO for use during development"""

from mushrooms import log
from RPiMock.PIN import PIN
from RPiMock.constants import (
    IN, OUT, HIGH, LOW, BOARD, BCM, PUD_OFF, PUD_DOWN, PUD_UP, RISING, FALLING,
    BOTH, SERIAL, SPI, HARD_PWM, UNKNOWN, MODE_OUT, MODE_IN, MODE_PWM,
    PHYS_TO_BCM_MAP, GPIONames,
)

logger = log.get_logger()

# GPIO state, it is a module_wide singleton because that's how the hardware works
_mode = None
pin_by_channel = {}


def setmode(mode):
    """GPIO Set Mode"""
    global _mode
    _mode = mode
    logger.debug("Set GPIO mode: %s", _mode)


def getmode():
    """GPIO Get Mode"""
    global _mode
    mode = _mode
    logger.debug("Get GPIO mode: %s", _mode)
    return mode


def setup(channel, state, initial=None, pull_up_down=None):
    """GPIO setup"""

    logger.debug(
        "Set GPIO channel: %s state: %s initial: %s pull_up_down: %s",
        channel, state, initial, pull_up_down,)
    channel = to_BCM_channel(channel)

    if channel not in GPIONames:
        raise ValueError(f"GPIO {channel} does not exist")

    # check if channel is already setup
    if channel in pin_by_channel:
        raise Exception("GPIO is already setup")

    if state == MODE_OUT:
        # GPIO is set as output, default OUT 0
        pin = PIN(MODE_OUT)
        if initial == HIGH:
            pin.value = 1

        pin_by_channel[channel] = pin

    elif state == MODE_IN:
        # set input
        pin = PIN(MODE_IN)
        if pull_up_down is None or pull_up_down == PUD_DOWN:
            pin.pull_up_down = PUD_DOWN
            pin.value = 0
        elif pull_up_down == PUD_UP:
            pin.pull_up_down = PUD_UP
            pin.value = 1

        pin_by_channel[channel] = pin


def output(channel, value):
    """GPIO Output"""

    logger.debug("GPIO output channel: %s value: %s", channel, value)

    channel = to_BCM_channel(channel)

    if channel not in pin_by_channel:
        # if channel is not set up
        raise Exception(f"GPIO must be setup before used (channel {channel})")
    else:
        pin = pin_by_channel[channel]
        if pin.mode == MODE_IN:
            # if channel is set up as IN and used as an OUTPUT
            raise Exception(f"GPIO must be setup as OUT (channel {channel})")

    if value not in {LOW, HIGH}:
        raise Exception(
            f"Output must be set to HIGH/LOW (channel {channel}), was set to {value}"
        )

    pin = pin_by_channel[channel]
    if value == LOW:
        pin.value = 0
    elif value == HIGH:
        pin.value = 1


def cleanup():
    """GPIO Cleanup"""
    logger.debug("GPIO cleanup")


def setwarnings(flag):
    """GPIO Set Warnings"""
    logger.debug("GPIO set warnings to false")
    return False


def to_BCM_channel(channel):
    """
    Make sure `channel` is a GPIO channel number, even if mode is set to BOARD.
    """
    if _mode == BOARD:
        if channel not in PHYS_TO_BCM_MAP:
            raise KeyError('unknown channel "{}"'.format(channel))
        return PHYS_TO_BCM_MAP[channel]
    elif _mode == BCM:
        return channel
    else:
        raise ValueError("GPIO set to unknown mode")
