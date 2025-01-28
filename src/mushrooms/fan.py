"""Turn Fan on and off."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.4.0"

import time
import board
import digitalio
from mushrooms import log


class Fan:
    """Class for a Fan controlled by relay."""

    def __init__(self, channel="D25"):
        """Initialize Fan."""
        self.channel = channel
        pin = getattr(board, channel)
        self.fan = digitalio.DigitalInOut(pin)
        self.fan.direction = digitalio.Direction.OUTPUT
        self.logger = log.get_logger()
        self.logger.debug("Initialize Fan %s", self.channel)

    def __del__(self):
        """Delete Fan"""
        self.logger.debug("Delete Fan %s", self.channel)

    def __repr__(self):
        """Fan repr"""
        string = f"Fan({self.channel}"
        string += ")"
        return string

    def __str__(self):
        """Print Fan"""
        string = "┌────────────────┐\n"
        string += "│ Fan:           │\n"
        string += f"│ Pin={self.channel}        │\n"
        string += f"│ Value={self.fan.value}    │\n"
        string += "└────────────────┘"
        return string

    def turn_on(self):
        """Turn the Fan on."""
        self.fan.value = True
        self.logger.debug("Fan %s on", self.channel)

    def turn_off(self):
        """Turn the Fan off."""
        self.fan.value = False
        self.logger.debug("Fan %s off", self.channel)

    def cleanup(self):
        """Close resources."""
        self.turn_off()
        self.logger.debug("Fan %s cleanup", self.channel)
        self.fan.deinit()


def test():
    """Test Fan blink."""
    my_fan = Fan(channel="D25")
    print(my_fan)

    for _ in range(2):
        my_fan.turn_on()
        time.sleep(150.0)
        my_fan.turn_off()
        time.sleep(30.0)

    my_fan.cleanup()


if __name__ == "__main__":
    test()
