"""Tests for: Lamp"""

import pytest
from mushrooms.os_options import GPIO
from mushrooms import lamp


# @pytest.mark.skip
def test_lamp():
    """Test lamp"""

    CHANNEL = 26
    for x in range(3):
        lamp_on(CHANNEL)
        time.sleep(1.0)
        lamp_off(CHANNEL)
        time.sleep(1.0)

    lamp_cycle(20)
    lamp_cycle(80)

    lamp_off(CHANNEL)
    GPIO.cleanup()
