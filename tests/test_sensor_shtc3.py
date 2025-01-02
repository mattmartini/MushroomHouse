"""Tests for: Sensor SHTC3"""

import pytest
from mushrooms.sensor_shtc3 import SensorSHTC3


# @pytest.mark.skip
def test_sensor_shtc3():
    """Test sensor shtc3"""

    my_sensor = SensorSHTC3()
    print(my_sensor)
    print(repr(my_sensor))
    tempf, humf = my_sensor.read_temp()


    assert repr(my_sensor) == "SHTC3(D26)"


