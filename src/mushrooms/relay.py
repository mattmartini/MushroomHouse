"""Turn Relay on and off."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import time
import board
import digitalio
from mushrooms import log


class Relay:
    """Class for a Relay light."""

    def __init__(self, channel="D25"):
        """Initialize Relay light."""
        self.channel = channel
        pin = getattr(board, channel)
        self.relay = digitalio.DigitalInOut(pin)
        self.relay.direction = digitalio.Direction.OUTPUT
        self.logger = log.get_logger()
        self.logger.debug("Initialize Relay %s", self.channel)

    def __del__(self):
        """Delete Relay"""
        self.logger.debug("Delete Relay %s", self.channel)

    def __repr__(self):
        """Relay repr"""
        string = f"Relay({self.channel}"
        string += ")"
        return string

    def __str__(self):
        """Print Relay"""
        string = "┌────────────────┐\n"
        string += "│ Relay:         │\n"
        string += f"│ Pin={self.channel}        │\n"
        string += f"│ Value={self.relay.value}    │\n"
        string += "└────────────────┘"
        return string

    def turn_on(self):
        """Turn the Relay on."""
        self.relay.value = True
        self.logger.debug("Relay %s on", self.channel)

    def turn_off(self):
        """Turn the Relay off."""
        self.relay.value = False
        self.logger.debug("Relay %s off", self.channel)

    def cleanup(self):
        """Close resources."""
        self.turn_off()
        self.logger.debug("Relay %s cleanup", self.channel)
        self.relay.deinit()


def test():
    """Test Relay blink."""
    my_relay = Relay(channel="D25")
    print(my_relay)

    for _ in range(5):
        my_relay.turn_on()
        time.sleep(1.0)
        my_relay.turn_off()
        time.sleep(1.0)

    my_relay.cleanup()


if __name__ == "__main__":
    test()
