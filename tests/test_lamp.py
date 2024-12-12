"""Tests for: Lamp"""

import pytest

# from RPi import GPIO
from RPiSim import GPIO


def test_setmode():
    """Test setmode options"""
    mode = GPIO.setmode(GPIO.BCM)
    assert mode == "bcm"
