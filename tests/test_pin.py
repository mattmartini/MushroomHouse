"""Tests for: PIN"""

import pytest
from RPiMock.PIN import PIN
from RPiMock.constants import (
    IN, OUT, HIGH, LOW, BOARD, BCM, PUD_OFF, PUD_DOWN, PUD_UP, RISING, FALLING,
    BOTH, SERIAL, SPI, HARD_PWM, UNKNOWN, MODE_OUT, MODE_IN, MODE_PWM,
    PHYS_TO_BCM_MAP, GPIONames,
)


def test_initial_repr():
    """Test initial repr"""
    pin = PIN(MODE_IN)
    assert repr(pin) == "PIN(3, 0, 4)"
    pin = PIN(MODE_OUT)
    assert repr(pin) == "PIN(2, 0, 4)"

def test_initial_str():
    """Test initial repr"""
    pin = PIN(MODE_IN)
    assert str(pin) == "<PIN IN @ 0>"
    pin = PIN(MODE_OUT)
    assert str(pin) == "<PIN OUT @ 0>"

def test_pin_value():
    """Test pin value"""
    pin = PIN(MODE_IN, value=HIGH)
    assert repr(pin) == "PIN(3, 1, 4)"
    pin = PIN(MODE_IN, value=LOW)
    assert repr(pin) == "PIN(3, 0, 4)"

    pin = PIN(MODE_OUT, value=HIGH)
    assert repr(pin) == "PIN(2, 1, 4)"
    pin = PIN(MODE_OUT, value=LOW)
    assert repr(pin) == "PIN(2, 0, 4)"

def test_pin_pull_up_down():
    """Test pin pull up down"""
    pin = PIN(MODE_IN, pull_up_down=PUD_UP)
    assert repr(pin) == "PIN(3, 0, 22)"
    pin = PIN(MODE_IN, pull_up_down=PUD_DOWN)
    assert repr(pin) == "PIN(3, 0, 21)"

    pin = PIN(MODE_OUT, pull_up_down=PUD_UP)
    assert repr(pin) == "PIN(2, 0, 22)"
    pin = PIN(MODE_OUT, pull_up_down=PUD_DOWN)
    assert repr(pin) == "PIN(2, 0, 21)"

# def test_initial_input(new_buffer):
#     """Test initial input"""
#     assert new_buffer.input["prev"] is None
#     assert new_buffer.input["next"] is None
