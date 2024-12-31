"""Tests for: Lamp"""

import pytest
from mushrooms.lamp import Lamp
from mushrooms.os_options import GPIO

# @pytest.mark.skip
def test_lamp():
    """Test lamp"""

    CHANNEL = 26
    CYCLE_TIME = 10

    my_lamp = Lamp(pin=CHANNEL, cycle_time=CYCLE_TIME)
    print(my_lamp)
    print(repr(my_lamp))

    for x in range(3):
        my_lamp.lamp_on()
        time.sleep(1.0)
        my_lamp.lamp_off()
        time.sleep(1.0)

    my_lamp.lamp_cycle(20)
    my_lamp.lamp_cycle(80)

    my_lamp.lamp_off()
    GPIO.cleanup()
