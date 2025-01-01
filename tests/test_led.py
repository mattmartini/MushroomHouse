"""Tests for: LED"""

import pytest
from mushrooms.led_light import LED


# @pytest.mark.skip
def test_led():
    """Test led"""

    CHANNEL = "D26"
    CYCLE_TIME = 10

    my_led = Led(channel=CHANNEL)
    print(my_led)
    print(repr(my_lamp))
    assert my_led.led.value == False
