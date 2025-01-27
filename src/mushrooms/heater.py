"""Turn heater on and off"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import time
import board
import digitalio
from mushrooms import log


class Heater:
    """Heater with variable power output approximated via time slicing."""

    def __init__(self, channel="D26", sw_channel="D11"):
        """Initialize heater."""
        self.channel = channel
        self.sw_channel = sw_channel
        # self.pin = pin
        # self.sw_pin = sw_pin
        pin = getattr(board, self.channel)
        self.heat = digitalio.DigitalInOut(pin)
        self.heat.direction = digitalio.Direction.OUTPUT
        sw_pin = getattr(board, self.sw_channel)
        self.high = digitalio.DigitalInOut(sw_pin)
        self.high.direction = digitalio.Direction.OUTPUT

        # initialize heater to off
        self.heat.value = False
        self.high.value = False

        self.logger = log.get_logger()
        self.logger.debug("Initialize Heater %s %s", self.channel, self.sw_channel)

        # # GPIO Setup
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.pin, GPIO.OUT)
        # GPIO.setup(self.sw_pin, GPIO.OUT)
        # GPIO.output(self.pin, GPIO.LOW)
        # GPIO.output(self.sw_pin, GPIO.LOW)
        # self.logger = log.get_logger()

        # self.logger.debug("Initialize Heater")

    def __del__(self):
        """Delete Heater"""
        self.logger.debug("Delete Heater %s %s", self.channel, self.sw_channel)

    def __repr__(self):
        """Heater repr"""
        string = f"Heater({self.channel}, "
        string += f"{self.sw_channel}"
        string += ")"
        return string

    def __str__(self):
        """Print Heater."""
        string = "┌──────────────────────────────┐\n"
        string += "│ Heater:                      │\n"
        string += f"│ Channel(BCM pin)={self.channel}         │\n"
        string += f"│ Switch (BCM pin)={self.sw_channel}         │\n"
        string += "└──────────────────────────────┘"
        return string

    def turn_on(self):
        """Turn the heater on."""
        self.heat.value = True
        self.logger.debug("Heater %s on", self.channel)
        # GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        """Turn the heater off."""
        self.heat.value = False
        self.logger.debug("Heater %s off", self.channel)
        # GPIO.output(self.pin, GPIO.LOW)

    def mode_half(self):
        """Switch the heater to Half Power mode."""
        self.high.value = False
        self.logger.debug("Heater Switch %s Low Power", self.sw_channel)
        # GPIO.output(self.sw_pin, GPIO.LOW)

    def mode_full(self):
        """Turn the heater to Full Power mode."""
        self.high.value = True
        self.logger.debug("Heater Switch %s High Power", self.sw_channel)
        # GPIO.output(self.sw_pin, GPIO.HIGH)

    def heater_cycle(self, power, cycle_time=25):
        """
        Use percentage of time cycle to approximate variable power.
        New heater has two power modes Half (750W) and Full (1500W)
        In order to have a more natural response we use a second relay
        to control which mode the heat utilizes. For computed power
        less than 50%, Half power mode for twice the duration and
        more than 50%, Full power mode for normal duration.
        So Half power for 100% cycle is the transition to Full power
        for 50% cycle.
        """
        if power < 0:
            power = 0
        elif power > 100:
            power = 100

        if power < 50:
            self.mode_half()
            power = power * 2
        else:
            self.mode_full()

        on_time = cycle_time * power / 100
        off_time = cycle_time * (100 - power) / 100

        if power > 0:
            self.turn_on()
            time.sleep(on_time)
        if power < 100:
            self.turn_off()
            time.sleep(off_time)

    def cleanup(self):
        """Close resources."""
        self.turn_off()
        self.mode_half()
        # GPIO.cleanup()
        self.heat.deinit()
        self.high.deinit()
        self.logger.debug("Cleanup Heater %s", self.channel)


def test():
    """Test heater."""

    my_heater = Heater()
    print(my_heater)
    # for _ in range(3):
    #     my_heater.turn_on()
    #     time.sleep(5.0)
    #     my_heater.turn_off()
    #     time.sleep(2.0)

    my_heater.heater_cycle(30, cycle_time=20)
    my_heater.heater_cycle(80, cycle_time=20)
    my_heater.heater_cycle(20, cycle_time=20)

    my_heater.cleanup()


if __name__ == "__main__":
    test()
