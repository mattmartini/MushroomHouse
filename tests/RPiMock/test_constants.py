"""Test constants"""

from mushrooms.os_options import GPIO

def test_gpio_constants():
    """Test GPIO Constants"""
    gpio_consts = {
        "IN": 1,
        "OUT": 0,
        "HIGH": 1,
        "LOW": 0,
        "BOARD": 10,
        "BCM": 11,
        "PUD_OFF": 20,
        "PUD_DOWN": 21,
        "PUD_UP": 22,
        "RISING": 31,
        "FALLING": 32,
        "BOTH": 33,
        "SERIAL": 40,
        "SPI": 41,
        "HARD_PWM": 43,
        "UNKNOWN": -1,
        "MODE_OUT": 2,
        "MODE_IN": 3,
        "MODE_PWM": 8,
    }
    # for key, value in gpio_consts.items():
    #     logger.debug("Key: %s  Value: %s", key, value)
    #     assert GPIO.key == value
    assert GPIO.IN == gpio_consts["IN"]
    assert GPIO.OUT == gpio_consts["OUT"]
    assert GPIO.HIGH == gpio_consts["HIGH"]
    assert GPIO.LOW == gpio_consts["LOW"]
    assert GPIO.BOARD == gpio_consts["BOARD"]
    assert GPIO.BCM == gpio_consts["BCM"]
    assert GPIO.PUD_OFF == gpio_consts["PUD_OFF"]
    assert GPIO.PUD_DOWN == gpio_consts["PUD_DOWN"]
    assert GPIO.PUD_UP == gpio_consts["PUD_UP"]
    assert GPIO.RISING == gpio_consts["RISING"]
    assert GPIO.FALLING == gpio_consts["FALLING"]
    assert GPIO.BOTH == gpio_consts["BOTH"]
    assert GPIO.SERIAL == gpio_consts["SERIAL"]
    assert GPIO.SPI == gpio_consts["SPI"]
    assert GPIO.HARD_PWM == gpio_consts["HARD_PWM"]
    assert GPIO.UNKNOWN == gpio_consts["UNKNOWN"]
    assert GPIO.MODE_OUT == gpio_consts["MODE_OUT"]
    assert GPIO.MODE_IN == gpio_consts["MODE_IN"]
    assert GPIO.MODE_PWM == gpio_consts["MODE_PWM"]
