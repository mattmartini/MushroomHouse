"""Tests for: Sensor DHT22"""

import pytest
from mushrooms.sensor_dht22 import SensorDHT22


# @pytest.mark.skip
def test_sensor_dht22():
    """Test sensor dht22"""

    my_sensor = SensorDHT22()
    print(my_sensor)
    print(repr(my_sensor))
    tempf, humf = my_sensor.read_temp()


    assert repr(my_sensor) == "DHT22(pin: D18 scale: f)"


