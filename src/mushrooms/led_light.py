"""Turn LED on and off."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.1.0"

import time
import board
import digitalio
from mushrooms import log


class LED:
    """Class for a LED light."""

    def __init__(self, channel="D26"):
        """Initialize LED light."""
        self.channel = channel
        pin = getattr(board, channel)
        self.led = digitalio.DigitalInOut(pin)
        self.led.direction = digitalio.Direction.OUTPUT
        self.logger = log.get_logger()
        self.logger.debug("Initialize LED")

    def __del__(self):
        """Delete LED"""
        self.cleanup()
        self.logger.debug("Delete LED")

    def __repr__(self):
        """LED repr"""
        string = f"LED({self.channel}, "
        string += ")"
        return string

    def __str__(self):
        """Print LED"""
        string = "┌────────────────┐\n"
        string += "│ LED:           │\n"
        string += f"│ Pin={self.channel}     │\n"
        string += f"│ val={self.led.value}   │\n"
        string += "└────────────────┘"
        return string

    def turn_on(self):
        """Turn the LED on."""
        self.led.value = True
        self.logger.debug("LED on")

    def turn_off(self):
        """Turn the LED off."""
        self.led.value = False
        self.logger.debug("LED off")

    def cleanup(self):
        """Close resources."""
        self.turn_off()
        self.led.deinit()
        self.logger.debug("LED cleanup")


def test():
    """Test LED blink."""
    my_led = LED(channel="D26")

    for _ in range(10):
        my_led.turn_on()
        time.sleep(1.0)
        my_led.turn_off()
        time.sleep(1.0)

    my_led.cleanup()


if __name__ == "__main__":
    test()
