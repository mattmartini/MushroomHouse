"""Tests for: Lamp"""

import pytest
from mushrooms.os_options import GPIO


@pytest.mark.skip
def test_setmode():
    """Test setmode options"""
    GPIO.setmode(GPIO.BCM)
    # mode = GPIO.getmode()
    # assert mode == GPIO.BCM

