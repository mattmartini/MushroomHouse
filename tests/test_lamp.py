"""Tests for: Lamp"""

import platform
import pytest

if platform.system() == 'Linux':
    from RPi import GPIO
else:
    from RPiMock import GPIO


def test_setmode():
    """Test setmode options"""
    mode = GPIO.setmode(GPIO.BCM)
    assert mode == "bcm"
