"""test to see if HUP signal can be caught"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "1.0.0"

import signal
import time


class SignalHandler:
    """Gracefully handle a HUP signal to print data"""

    hupped_now = False

    def __init__(self):
        """Initialize signal handler."""
        signal.signal(signal.SIGHUP, self.hup_handler)

    def hup_handler(self, *args):
        """flag the hup"""
        self.hupped_now = True


def main():
    """Controller main loop"""
    hup_test = SignalHandler()
    while True:
        try:
            print("start")
            time.sleep(10)
            print("middle")
            if hup_test.hupped_now:
                print("HUP Received!!")
                hup_test.hupped_now = False
            print("end")
        except RuntimeError:
            pass


if __name__ == "__main__":
    main()
