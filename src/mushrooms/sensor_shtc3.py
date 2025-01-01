"""Temperature Sensor (SHTC3)."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.0"

import time
import adafruit_shtc3
import board
from mushrooms import log


class SensorSHTC3:
    """SHTC3 Temperature Sensor."""

    def __init__(self, scale="f"):
        """Initialize sensor."""
        self.scale = scale
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.sht_sensor = adafruit_shtc3.SHTC3(self.i2c)
        self.logger = log.get_logger()
        self.logger.debug("Initialize SHTC3 Sensor")

    def __del__(self):
        """Delete SHTC3 Sensor"""
        self.logger.debug("Delete SHTC3 Sensor")

    def __repr__(self):
        """SHTC3 Sensor repr"""
        string = f"SHTC3({self.scale}"
        string += ")"
        return string

    def convert_c_to_f(self, temp_c):
        """Convert temperature from C to F"""
        return temp_c * 9.0 / 5.0 + 32.0

    def read_temp(self):
        """Read temperature with retry."""
        for _ in range(5):
            try:
                temp_c, humidity = self.sht_sensor.measurements
                break
            except RuntimeError:
                time.sleep(0.5)
                continue
        self.logger.debug("SHTC3 temp: %0.3f C hum: %0.3f %%", temp_c, humidity)
        if self.scale == "f":
            return self.convert_c_to_f(temp_c), humidity
        return temp_c, humidity

    def cleanup(self):
        """Close resources."""
        self.logger.debug("SHTC3 Sensor cleanup")
        pass


def test():
    """Read temperature from SHTC3 sensor."""

    my_sensor = SensorSHTC3()
    tempf, humf = my_sensor.read_temp()
    print(f"temp: {tempf:3.3f} F")
    print(f" hum: {humf:3.3f} %")
    my_sensor.cleanup()

    time.sleep(2)

    my_c_sensor = SensorSHTC3(scale="c")
    tempc, humc = my_c_sensor.read_temp()
    print(f"temp: {tempc:3.3f} C")
    print(f" hum: {humc:3.3f} %")
    my_c_sensor.cleanup()


if __name__ == "__main__":
    test()
