"""PWM Module"""

from RPiSim.constants import MODE_PWM


class PWM:
    """PWM Class"""

    def __init__(self, command_pipe, pin, channel, freq):
        """Initialize PWM"""
        self.command_pipe = command_pipe
        self.channel = channel
        self.freq = freq
        self.dc = 0
        self.pin = pin

        pin.mode = MODE_PWM
        # print("setup PWM on {} @ {} Hz".format(bcm_channel, freq))

        command_pipe.put(("setup pwm", (channel, freq), None))

    def start(self, dc):
        """Start PWM"""
        self.dc = dc
        # print("starting PWM on {} @ {} Hz, dc = {} %".format(
        #     self.bcm_channel, self.freq, dc)
        # )
        self.pin.value = dc / 100
        self.command_pipe.put((
            'update pwm',
            (self.channel, self.freq, self.dc),
            None
        ))

    def stop(self):
        """Stop PWM"""
        self.command_pipe.put((
            'update pwm',
            (self.channel, 0, self.dc),
            None
        ))

    def ChangeDutyCycle(self, dc):
        """PWM Change Duty Cycle"""
        # print("pwm on {}: {} %".format(self.bcm_channel, dc))
        self.dc = dc
        self.pin.value = dc / 100
        self.command_pipe.put((
            'update pwm',
            (self.channel, self.freq, self.dc),
            None
        ))

    def ChangeFrequency(self, freq):
        """PWM Change Frequency"""
        self.freq = freq
        self.command_pipe.put((
            'update pwm',
            (self.channel, self.freq, self.dc),
            None
        ))
