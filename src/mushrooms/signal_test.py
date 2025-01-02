"""test to see if HUP signal can be caught"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import signal
import time


def got_hup_signal(signum, frame):
    """say that a hup signal was received"""
    print("I got HUPped.")


signal.signal(signal.SIGHUP, got_hup_signal)


def got_usr1_signal(signum, frame):
    """say that a usr1 signal was received"""
    print("I got SIGUSR1ed.")


signal.signal(signal.SIGUSR1, got_usr1_signal)


def got_usr2_signal(signum, frame):
    """say that a usr2 signal was received"""
    print("I got SIGUSR2ed.")


signal.signal(signal.SIGUSR2, got_usr2_signal)

print("start")
time.sleep(3600)
print("end")
