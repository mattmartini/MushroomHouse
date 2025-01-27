"""Turn lamp on and off"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import time
import board
import digitalio
from mushrooms import log


class Lamp:
    """Lamp"""

    def __init__(self, channel="D26", cycle_time=10):
        """Initialize lamp."""
        self.channel = channel
        self.cycle_time = cycle_time

        pin = getattr(board, self.channel)
        self.light = digitalio.DigitalInOut(pin)
        self.light.direction = digitalio.Direction.OUTPUT
        # initialize Lamp to off
        self.light.value = False

        self.logger = log.get_logger()
        self.logger.debug("Initialize Lamp %s", self.channel)

        # # GPIO Setup
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.pin, GPIO.OUT)
        # GPIO.output(self.pin, GPIO.LOW)
        # self.logger.debug("Initialize Lamp")

    def __del__(self):
        """Delete lamp"""
        self.logger.debug("Delete Lamp %s", self.channel)

    def __repr__(self):
        """Lamp repr"""
        string = f"Lamp({self.channel}, "
        string += f"{self.cycle_time:0.1f}"
        string += ")"
        return string

    def __str__(self):
        """Print Lamp."""
        string = "┌─────────────────────────┐\n"
        string += "│ Lamp:                   │\n"
        string += f"│ Channel(BCM pin)={self.channel}    │\n"
        string += f"│ Cycle Time(s)={self.cycle_time:0.1f}      │\n"
        string += "└─────────────────────────┘"
        return string

    def lamp_on(self):
        """Turn the lamp on."""
        self.light.value = True
        self.logger.debug("Lamp %s on", self.channel)
        # GPIO.output(self.pin, GPIO.HIGH)
        # self.logger.debug("Lamp On")

    def lamp_off(self):
        """Turn the lamp off."""
        # GPIO.output(self.pin, GPIO.LOW)
        # self.logger.debug("Lamp Off")
        self.light.value = False
        self.logger.debug("Lamp %s off", self.channel)

    def lamp_cycle(self, power):
        """use percentage of time cycle to approximate variable power"""
        self.logger.debug("Lamp Cycle: %d", power)
        if (power < 0) or (power > 100):
            power = 0

        on_time = self.cycle_time * power / 100
        off_time = self.cycle_time * (100 - power) / 100

        if power > 0:
            self.lamp_on()
            time.sleep(on_time)
        if power < 100:
            self.lamp_off()
            time.sleep(off_time)

    def cleanup(self):
        """Close resources."""
        self.lamp_off()
        self.logger.debug("Lamp %s cleanup", self.channel)
        self.light.deinit()


def test():
    """Test Lamp blink."""
    my_lamp = Lamp(channel="D26")
    print(my_lamp)
    print(repr(my_lamp))

    for x in range(2):
        my_lamp.lamp_on()
        time.sleep(1.0)
        my_lamp.lamp_off()
        time.sleep(1.0)

    my_lamp.lamp_cycle(20)
    my_lamp.lamp_cycle(80)

    my_lamp.cleanup()


if __name__ == "__main__":
    test()
