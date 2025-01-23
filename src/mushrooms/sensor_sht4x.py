"""Temperature Sensor (SHT4X)."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import time
import adafruit_sht4x
import board
from mushrooms import log


class SensorSHT4X:
    """SHT4X Temperature Sensor."""

    def __init__(self, scale="f"):
        """Initialize sensor."""
        self.scale = scale
        self.i2c = board.STEMMA_I2C()  # uses board.SCL and board.SDA
        self.sht_sensor = adafruit_sht4x.SHT4X(self.i2c)
        self.sht_sensor.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
        # Can also set the mode to enable heater
        # sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
        self.logger = log.get_logger()
        self.logger.debug("Initialize SHT4X Sensor")

    def __del__(self):
        """Delete SHT4X Sensor"""
        self.logger.debug("Delete SHT4X Sensor")

    def __repr__(self):
        """SHT4X Sensor repr"""
        string = f"SHT4X({self.scale}, "
        string += f"s/n:{self.sht_sensor.serial_number}, "
        string += f"mode:{self.sht_sensor.Mode.string[self.sht_sensor.mode]}"
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
        self.logger.debug("SHT4X temp: %0.3f C hum: %0.3f %%", temp_c, humidity)
        if self.scale == "f":
            return self.convert_c_to_f(temp_c), humidity
        return temp_c, humidity

    def cleanup(self):
        """Close resources."""
        self.logger.debug("SHT4X Sensor cleanup")
        pass


def test():
    """Read temperature from SHT4X sensor."""

    my_sensor = SensorSHT4X()
    print(my_sensor)
    tempf, humf = my_sensor.read_temp()
    print(f"temp: {tempf:3.3f} F")
    print(f" hum: {humf:3.3f} %")
    my_sensor.cleanup()

    time.sleep(2)

    my_c_sensor = SensorSHT4X(scale="c")
    tempc, humc = my_c_sensor.read_temp()
    print(f"temp: {tempc:3.3f} C")
    print(f" hum: {humc:3.3f} %")
    my_c_sensor.cleanup()


if __name__ == "__main__":
    test()
