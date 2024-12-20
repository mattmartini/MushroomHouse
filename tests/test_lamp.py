"""Tests for: Lamp"""

import pytest
from mushrooms import os_options


def test_setmode():
    """Test setmode options"""
    mode = GPIO.setmode(GPIO.BCM)
    assert mode == "bcm"
