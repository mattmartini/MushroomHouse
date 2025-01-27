"""Temperature Sensor (SCD4X)."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import time
import adafruit_scd4x
import board
from mushrooms import log


class SensorSCD4X:
    """SCD4X Temperature Sensor."""

    def __init__(self, scale="f"):
        """Initialize sensor."""
        self.scale = scale
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.scd4x_sensor = adafruit_scd4x.SCD4X(self.i2c)
        self.logger = log.get_logger()
        self.logger.debug("Initialize SCD4X Sensor")
        self.scd4x_sensor.start_periodic_measurement()
        self.logger.debug("SCD4X Sensor waiting for first measurment")

    def __del__(self):
        """Delete SCD4X Sensor"""
        self.logger.debug("Delete SCD4X Sensor")

    def __repr__(self):
        """SCD4X Sensor repr"""
        string = f"SCD4X({self.scale}, "
        # string += f"s/n:{[hex(i) for i in self.scd4x_sensor.serial_number]}, "
        string += ")"
        return string

    def convert_c_to_f(self, temp_c):
        """Convert temperature from C to F"""
        return temp_c * 9.0 / 5.0 + 32.0

    def read_temp(self):
        """Read temperature with retry."""
        for _ in range(5):
            try:
                co2 = self.scd4x_sensor.CO2
                temp_c = self.scd4x_sensor.temperature
                humidity = self.scd4x_sensor.relative_humidity
                break
            except RuntimeError:
                self.logger.warning("SCD4X Sensor: no data available")
                time.sleep(0.5)
                continue
        self.logger.debug("SCD4X co2: %0.3f temp: %0.3f C hum: %0.3f %%", co2, temp_c, humidity)
        if self.scale == "f":
            return self.convert_c_to_f(temp_c), humidity
        return co2, temp_c, humidity

    def cleanup(self):
        """Close resources."""
        self.logger.debug("SCD4X Sensor cleanup")
        pass


def test():
    """Read temperature from SCD4X sensor."""

    my_sensor = SensorSCD4X()
    print(my_sensor)
    co2, tempf, humf = my_sensor.read_temp()
    print(f" co2: {co2:3.3f} ppm")
    print(f"temp: {tempf:3.3f} °F")
    print(f" hum: {humf:3.3f} %")
    my_sensor.cleanup()

    time.sleep(2)

    my_c_sensor = SensorSCD4X(scale="c")
    co2, tempc, humc = my_c_sensor.read_temp()
    print(f" co2: {co2:3.3f} ppm")
    print(f"temp: {tempc:3.3f} °C")
    print(f" hum: {humc:3.3f} %")
    my_c_sensor.cleanup()


if __name__ == "__main__":
    test()
