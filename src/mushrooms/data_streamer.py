"""Stream temperature data to initialstate.com for graphing."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import os
from ISStreamer.Streamer import Streamer


SENSOR_LOCATION_NAME = "Hothouse"
BUCKET_NAME = os.environ.get("BUCKET_NAME")
BUCKET_KEY = os.environ.get("BUCKET_KEY")
ACCESS_KEY = os.environ.get("ACCESS_KEY")


class DataStreamer:
    """Initial State Streamer"""

    def __init__(self, temp, goal_temp=40.0, out_temp=0, hum=0, pwr=0):
        """Initialize streamer."""
        self.temp = format(temp, ".2f")
        self.goal_temp = format(goal_temp, ".2f")
        self.out_temp = format(out_temp, ".2f")
        self.hum = format(hum, ".2f")
        self.pwr = format(pwr, ".2f")
        self.streamer = Streamer(
            bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY
        )

    def __del__(self):
        """Delete DataStreamer"""
        # self.logger.debug("Delete Streamer")

    def __repr__(self):
        """DataStreamer repr"""
        string = f"DataStreamer({self.temp:0.2f}, "
        string += f"{self.goal_temp:0.2f}, "
        string += f"{self.out_temp:0.2f}, "
        string += f"{self.hum:0.2f}, "
        string += f"{self.pwr:0.2f}"
        string += ")"
        return string

    def __str__(self):
        """Print DataStreamer."""
        string =   "┌──────────────────────────────────┐\n"
        string +=  "│ Temperature Data:                │\n"
        string += f"│ MushroomHouse Temperature: {self.temp} │\n"
        string += f"│ Outside Temperature: {self.out_temp}       │\n"
        string += f"│ Goal Temperature: {self.goal_temp}          │\n"
        string += f"│ Humidity: {self.hum}                  │\n"
        string += f"│ Power: {self.pwr}                      │\n"
        string +=  "└──────────────────────────────────┘"
        return string

    def load_data(self, temp, goal_temp, out_temp, hum, pwr):
        """Load next data samples"""
        self.temp = format(temp, ".2f")
        self.goal_temp = format(goal_temp, ".2f")
        self.out_temp = format(out_temp, ".2f")
        self.hum = format(hum, ".2f")
        self.pwr = format(pwr, ".2f")

    def send_data(self):
        """Send data samples"""
        self.streamer.log(SENSOR_LOCATION_NAME + " Temperature(F)", self.temp)
        self.streamer.log(SENSOR_LOCATION_NAME + " GoalTemperature(F)", self.goal_temp)
        self.streamer.log(SENSOR_LOCATION_NAME + " Humidity(%)", self.hum)
        self.streamer.log(SENSOR_LOCATION_NAME + " Power(%)", self.pwr)
        self.streamer.log(
            SENSOR_LOCATION_NAME + " OutsideTemperature(F)", self.out_temp
        )
        self.streamer.flush()

    def cleanup(self):
        """Close resources."""
        self.streamer.flush()


def test():
    """Read temperature from DHT22 sensor."""

    import time

    my_streamer = DataStreamer(
        temp=47.0, goal_temp=60.0, out_temp=45.0, hum=90.0, pwr=0
    )
    my_streamer.send_data()
    time.sleep(15)
    my_streamer.load_data(temp=55.0, goal_temp=60.0, out_temp=40.0, hum=95.0, pwr=0)
    my_streamer.send_data()
    print(my_streamer)
    my_streamer.cleanup()


if __name__ == "__main__":
    test()
