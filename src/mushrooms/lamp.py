"""Turn lamp on and off"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.1.0"

import time
from mushrooms.os_options import GPIO
from mushrooms import log

CHANNEL = 26
CYCLE_TIME = 10


class Lamp:
    """Lamp"""

    def __init__(self, pin=CHANNEL, cycle_time=CYCLE_TIME):
        """Initialize lamp."""
        self.pin = pin
        self.cycle_time = cycle_time
        self.logger = log.get_logger()

        # GPIO Setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        # initialize Lamp to off
        GPIO.output(self.pin, GPIO.LOW)
        self.logger.debug("Initialize Lamp")

    def __del__(self):
        """Delete lamp"""
        self.logger.debug("Delete Lamp")

    def __repr__(self):
        """Lamp repr"""
        string = f"Lamp({self.pin:0d}, "
        string += f"{self.cycle_time:0.1f}, "
        string += ")"
        return string

    def __str__(self):
        """Print Lamp."""
        string = "┌──────────────────────────────┐\n"
        string += "│ Lamp:                      │\n"
        string += f"│ Channel={self.pin:0d}           │\n"
        string += f"│ Cycle Time(s)={self.cycle_time:0.1f}           │\n"
        string += "└──────────────────────────────┘"
        return string

    def lamp_on(self):
        """Turn the lamp on."""
        GPIO.output(self.pin, GPIO.HIGH)
        self.logger.debug("Lamp On")

    def lamp_off(self):
        """Turn the lamp off."""
        GPIO.output(self.pin, GPIO.LOW)
        self.logger.debug("Lamp Off")

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


if __name__ == "__main__":

    my_lamp = Lamp()

    for x in range(3):
        my_lamp.lamp_on()
        time.sleep(1.0)
        my_lamp.lamp_off()
        time.sleep(1.0)

    my_lamp.lamp_cycle(20)
    my_lamp.lamp_cycle(80)

    my_lamp.lamp_off()
    GPIO.cleanup()
