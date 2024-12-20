"""Tests for: Lamp"""

import pytest
from mushrooms.os_options import GPIO


def test_setmode():
    """Test setmode options"""
    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()
    assert mode == "bcm"

