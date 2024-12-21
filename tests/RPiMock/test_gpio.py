"""GPIO Tests"""

import pytest
from mushrooms import log
from mushrooms.os_options import GPIO

logger = log.get_logger()


def test_setmode():
    """Test setmode options"""
    GPIO.setmode(None)
    mode = GPIO.getmode()
    assert mode is None
    GPIO.setmode(GPIO.BOARD)
    mode = GPIO.getmode()
    assert mode == GPIO.BOARD
    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()
    assert mode == GPIO.BCM


def test_setwarnings():
    """Test warnings"""
    warn = GPIO.setwarnings(False)
    assert warn is False


def test_to_BCM_channel():
    """Test to BCM channel"""
    GPIO.setmode(None)
    logger.debug("mode: %s", GPIO.getmode())
    with pytest.raises(ValueError) as e:
        GPIO.to_BCM_channel(4)
    assert "GPIO set to unknown mode" in str(e.value)

    GPIO.setmode(GPIO.BOARD)
    logger.debug("mode: %s", GPIO.getmode())
    with pytest.raises(KeyError) as e:
        GPIO.to_BCM_channel(4)
    assert "unknown channel" in str(e.value)
    assert GPIO.to_BCM_channel(5) == 3

    GPIO.setmode(GPIO.BCM)
    logger.debug("mode: %s", GPIO.getmode())
    assert GPIO.to_BCM_channel(23) == 23


def test_setup():
    """Test setup"""
    GPIO.setmode(GPIO.BCM)
    with pytest.raises(ValueError) as e:
        GPIO.setup(99, GPIO.MODE_OUT)
    assert "does not exist" in str(e.value)

    GPIO.setup(25, GPIO.MODE_OUT, initial=GPIO.LOW)
    logger.debug("pin: %s", GPIO.pin_by_channel[25])
    assert str(GPIO.pin_by_channel[25]) == "<PIN OUT @ 0>"
    assert repr(GPIO.pin_by_channel[25]) == "PIN(2, 0, 4)"

    with pytest.raises(Exception) as e:
        GPIO.setup(25, GPIO.MODE_OUT, initial=GPIO.HIGH)
    assert "GPIO is already setup" in str(e.value)

    GPIO.setup(22, GPIO.MODE_OUT, initial=GPIO.HIGH)
    logger.debug("pin: %s", GPIO.pin_by_channel[22])
    assert str(GPIO.pin_by_channel[22]) == "<PIN OUT @ 1>"
    assert repr(GPIO.pin_by_channel[22]) == "PIN(2, 1, 4)"

    GPIO.setup(27, GPIO.MODE_IN, initial=GPIO.LOW)
    logger.debug("pin: %s", GPIO.pin_by_channel[27])
    assert str(GPIO.pin_by_channel[27]) == "<PIN IN @ 0>"
    assert repr(GPIO.pin_by_channel[27]) == "PIN(3, 0, 21)"

    GPIO.setup(17, GPIO.MODE_IN, pull_up_down=GPIO.PUD_UP)
    logger.debug("pin: %s", GPIO.pin_by_channel[17])
    assert str(GPIO.pin_by_channel[17]) == "<PIN IN @ 1>"
    assert repr(GPIO.pin_by_channel[17]) == "PIN(3, 1, 22)"

    GPIO.setup(23, GPIO.MODE_IN, pull_up_down=GPIO.PUD_DOWN)
    logger.debug("pin: %s", GPIO.pin_by_channel[23])
    assert str(GPIO.pin_by_channel[23]) == "<PIN IN @ 0>"
    assert repr(GPIO.pin_by_channel[23]) == "PIN(3, 0, 21)"


def test_output():
    """Test output"""
    GPIO.setmode(GPIO.BCM)
    with pytest.raises(Exception) as e:
        GPIO.output(13, GPIO.LOW)
    assert "GPIO must be setup before used" in str(e.value)

    GPIO.setup(26, GPIO.MODE_IN)
    with pytest.raises(Exception) as e:
        GPIO.output(26, GPIO.HIGH)
    assert "GPIO must be setup as OUT" in str(e.value)

    GPIO.setup(16, GPIO.MODE_OUT)
    with pytest.raises(Exception) as e:
        GPIO.output(16, None)
    assert "Output must be set to HIGH/LOW" in str(e.value)

    GPIO.output(16, GPIO.HIGH)
    assert str(GPIO.pin_by_channel[16]) == "<PIN OUT @ 1>"
    assert repr(GPIO.pin_by_channel[16]) == "PIN(2, 1, 4)"

    GPIO.setup(12, GPIO.MODE_OUT)
    GPIO.output(12, GPIO.LOW)
    assert str(GPIO.pin_by_channel[12]) == "<PIN OUT @ 0>"
    assert repr(GPIO.pin_by_channel[12]) == "PIN(2, 0, 4)"

