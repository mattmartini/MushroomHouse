"""Keep config vars in a file.  Read/write/check if modified."""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import os
import pkgutil
from rich import inspect
from mushrooms import log

PKG_PATH = str(pkgutil.resolve_name("mushrooms").__path__[0])
DEFAULTCONFIGFILE = PKG_PATH + "/mushrooms.conf"


class Config:
    """Class to hold configuration variables for PID."""

    def __init__(
        self,
        set_point,
        k_p,
        k_i,
        k_d,
        cycle_time,
        config_file=DEFAULTCONFIGFILE,
    ):
        """Initialize Config object."""
        self.set_point = set_point
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.cycle_time = cycle_time
        self.config_file = config_file
        self.mtime = 0
        self.logger = log.get_logger()

        self.create_config()
        self.logger.debug("Initialize Config")

    def __del__(self):
        """Delete Config"""
        self.logger.debug("Delete Config")

    def __repr__(self):
        """Config repr"""
        string = f"Config({self.set_point:0.1f}, "
        string += f"{self.k_p:0.3f}, "
        string += f"{self.k_i:0.3f}, "
        string += f"{self.k_d:0.3f}, "
        string += f"{self.cycle_time:0.1f}"
        # string += f"{self.config_file}"
        string += ")"
        return string

    def __str__(self):
        """Print Config."""
        string = "┌──────────────────────────────┐\n"
        string += "│ Config:                      │\n"
        string += f"│ Set Point(°f)={self.set_point:0.1f}           │\n"
        string += f"│ Cycle Time(s)={self.cycle_time:0.1f}           │\n"
        string += f"│ Kp={self.k_p:0.3f}, Ki={self.k_i:0.3f}, Kd={self.k_d:0.3f} │\n"
        string += f"│ Config File={self.config_file}\n"
        string += "└──────────────────────────────┘"
        return string

    def create_config(self):
        """write the values to the config file"""
        if not os.path.isfile(self.config_file):
            with open(self.config_file, "w", encoding="utf-8") as file:
                file.write(
                    f"{self.set_point},{self.k_p},{self.k_i},{self.k_d},{self.cycle_time}"
                )
        else:
            self.logger.warning(
                "Warning: using existing configuration file\n%s", self.config_file
            )
        self.mtime = self.stat_config()

    def stat_config(self):
        """get the modification time of the config file"""
        if os.path.isfile(self.config_file):
            stat_info = os.stat(self.config_file)
            return stat_info.st_mtime
        return 0

    def config_modified(self):
        """check if config file has been modified"""
        curr_time = self.stat_config()
        if curr_time > self.mtime:
            self.mtime = curr_time
            return True
        return False

    def read_config2(self):
        """read the values from the config file"""
        self.logger.debug("Read Config")
        config = (
            pkgutil.get_data("mushrooms", "mushrooms.conf")
            .decode("utf-8")
            .rstrip("\n")
            .split(",")
        )
        inspect(config)
        return config

    def read_config(self):
        """read the values from the config file"""
        with open(self.config_file, "r", encoding="utf-8") as file:
            config = file.readline().split(",")
            inspect(config)
            self.set_point = float(config[0])
            self.k_p = float(config[1])
            self.k_i = float(config[2])
            self.k_d = float(config[3])
            self.cycle_time = float(config[4])
            return self.set_point, self.k_p, self.k_i, self.k_d, self.cycle_time


def test():
    """test config methods"""
    from pathlib import Path

    print("--------------------------------------------------------------\n")
    TEST_CONFIG_FILE = PKG_PATH + "/../../tests/mushroom.conf"
    my_config = Config(75, 3.0, 0.1, 0.6, 10, config_file=TEST_CONFIG_FILE)
    print(repr(my_config))

    print("config:")
    print(my_config.read_config())
    print("config2:")
    print(my_config.read_config2())

    print("stat config:")
    print(my_config.stat_config())

    print(my_config)

    Path(my_config.config_file).touch()

    if my_config.config_modified():
        print("Configuration Modified!!")
        print(my_config.stat_config())
    else:
        print("Configuration Not Modified")


if __name__ == "__main__":
    test()
