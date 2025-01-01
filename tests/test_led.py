"""Tests for: LED"""

import pytest
from mushrooms.led_light import LED


# @pytest.mark.skip
def test_led():
    """Test led"""

    CHANNEL = "D26"
    CYCLE_TIME = 10

    my_led = LED()
    print(my_led)
    print(repr(my_led))

    assert repr(my_led) == "LED(D26)"

    assert my_led.led.value == False

    my_led.turn_on()
    assert my_led.led.value == True

    my_led.turn_off()
    assert my_led.led.value == False

