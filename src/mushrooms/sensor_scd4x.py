"""Temperature Sensor (SCD4X)."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.4.0"

import time
import board
import adafruit_scd4x
from mushrooms import log


class SensorSCD4X:
    """SCD4X Temperature Sensor."""

    def __init__(self, scale="f"):
        """Initialize sensor."""
        self.scale = scale
        self.i2c = board.I2C()  # uses board.SCL and board.SDA
        self.scd4x_sensor = adafruit_scd4x.SCD4X(self.i2c)
        # The default I2C device address for the sensor is 0x62

        self.logger = log.get_logger()
        self.logger.debug("Initialize SCD4X Sensor")

        self.scd4x_sensor.start_periodic_measurement()
        self.logger.debug("SCD4X Sensor waiting for first measurement")
        while self.scd4x_sensor.data_ready is not True:
            time.sleep(1.0)
        self.logger.debug("SCD4X Sensor made first measurement")

    def __del__(self):
        """Delete SCD4X Sensor"""
        self.logger.debug("Delete SCD4X Sensor")

    def __repr__(self):
        """SCD4X Sensor repr"""
        string = f"SCD4X({self.scale}"
        string += ")"
        return string

    def convert_c_to_f(self, temp_c):
        """Convert temperature from C to F"""
        return temp_c * 9.0 / 5.0 + 32.0

    def read_CO2(self):
        """Read CO2 concentration with retry."""
        if self.scd4x_sensor.data_ready is not True:
            self.logger.warning("SCD4X Sensor: data not ready")
        for _ in range(5):
            try:
                co2 = self.scd4x_sensor.CO2
                break
            except RuntimeError:
                self.logger.warning("SCD4X Sensor: no data available")
                time.sleep(0.5)
                continue
        self.logger.debug(
            "SCD4X co2(ppm): %d", co2
        )
        return co2

    def read_temp(self):
        """Read temperature with retry."""
        if self.scd4x_sensor.data_ready is not True:
            self.logger.warning("SCD4X Sensor: data not ready")
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
        self.logger.debug(
            "SCD4X co2(ppm): %d temp: %0.3f C hum: %0.3f %%", co2, temp_c, humidity
        )
        if self.scale == "f":
            return co2, self.convert_c_to_f(temp_c), humidity
        return co2, temp_c, humidity

    def cleanup(self):
        """Close resources."""
        self.scd4x_sensor.stop_periodic_measurement()
        self.logger.debug("SCD4X Sensor cleanup")


def test():
    """Read temperature from SCD4X sensor."""

    my_sensor = SensorSCD4X()
    print(my_sensor)
    co2, tempf, humf = my_sensor.read_temp()
    print(f" co2: {co2:d} ppm")
    print(f"temp: {tempf:0.3f} °F")
    print(f" hum: {humf:0.3f} %")
    my_sensor.cleanup()

    time.sleep(2)

    my_c_sensor = SensorSCD4X(scale="c")
    print(my_c_sensor)
    co2, tempc, humc = my_c_sensor.read_temp()
    print(f" co2: {co2:d} ppm")
    print(f"temp: {tempc:0.3f} °C")
    print(f" hum: {humc:0.3f} %")
    my_c_sensor.cleanup()

    time.sleep(2)

    my_co2_sensor = SensorSCD4X()
    print(my_co2_sensor)
    co2 = my_sensor.read_CO2()
    print(f" co2: {co2:d} ppm")
    my_sensor.cleanup()


if __name__ == "__main__":
    test()
