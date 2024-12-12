"""Turn lamp on and off"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.1.0"

import time
# from RPi import GPIO
# from RPiMock import GPIO
from RPiSim import GPIO

CHANNEL = 26
CYCLE_TIME = 10

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL, GPIO.OUT)


def lamp_on(pin):
    """turn the lamp on"""
    GPIO.output(pin, GPIO.HIGH)  # Turn lamp on


def lamp_off(pin):
    """turn the lamp off"""
    GPIO.output(pin, GPIO.LOW)  # Turn lamp off


def lamp_cycle(power):
    """use percentage of time cycle to approximate variable power"""
    if (power < 0) or (power > 100):
        power = 0

    on_time = CYCLE_TIME * power / 100
    off_time = CYCLE_TIME * (100 - power) / 100

    if power > 0:
        lamp_on(CHANNEL)
        time.sleep(on_time)
    if power < 100:
        lamp_off(CHANNEL)
        time.sleep(off_time)


if __name__ == "__main__":

    for x in range(3):
        lamp_on(CHANNEL)
        time.sleep(1.0)
        lamp_off(CHANNEL)
        time.sleep(1.0)

    lamp_cycle(20)
    lamp_cycle(80)

    lamp_off(CHANNEL)
    GPIO.cleanup()
