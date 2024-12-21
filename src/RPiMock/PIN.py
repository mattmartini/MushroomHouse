"""Pin value class"""

from RPiSim.constants import PUD_OFF, MODE_IN


class PIN:
    """PIN class"""

    def __init__(self, mode, value=None, pull_up_down=None):
        """Initialize PIN"""
        self.mode = mode
        self.pull_up_down = pull_up_down or PUD_OFF
        self.value = value or 0

    def __str__(self):
        """Print the PIN"""
        if self.mode == MODE_IN:
            mymode = "IN"
        else:
            mymode = "OUT"
        return f"<PIN {mymode} @ {self.value}>"

    def __repr__(self):
        """PIN repr"""
        return f"PIN({self.mode}, {self.value}, {self.pull_up_down})"
