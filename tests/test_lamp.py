"""Tests for: Lamp"""

import pytest
from mushrooms.os_options import GPIO


def test_setmode():
    """Test setmode options"""
    mode = GPIO.setmode(GPIO.BCM)
    assert mode == "bcm"
