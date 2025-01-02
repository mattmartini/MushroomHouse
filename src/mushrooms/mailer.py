"""Send status messages via email"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import signal
import smtplib
from mushrooms import log


class Mailer:
    """Send email (and SMS via email) on alert condition."""

    def __init__(self, subject, message):
        """Initialize streamer."""
        self.subject = subject
        self.message = message
        self.header = ""
        self.silence = False
        self.sender = "martini@mushroomhouse.home.arpa"
        self.receivers = [
            "matt.martin@gmail.com",
            "martini@cathal.home.arpa",
            "5167965796@vtext.com",
        ]
        self.logger = log.get_logger()
        self.logger.debug("Initialize Mailer")

    def __del__(self):
        """Ensure cleanup."""
        self.cleanup()
        self.logger.debug("Delete Mailer")

    def send(self):
        """Send prepaired message via smtp"""
        self.header = """From: MushroomHouse Controller <martini@mushroomhouse.home.arpa>
To: Matt Martini <matt.martini@gmail.com>
CC: <5167965796@vtext.com>, <martini@cathal.home.arpa>
"""
        self.header = self.header + "Subject: " + self.subject + "\n\n"
        self.message = self.header + self.message
        if not self.silence:
            try:
                smtp_obj = smtplib.SMTP("cathal.home.arpa")
                smtp_obj.sendmail(self.sender, self.receivers, self.message)
                self.logger.debug("Successfully sent email")
                self.stall()
            except smtplib.SMTPException:
                self.logger.debug("Error: unable to send email")

    def stall_handler(self, *args):
        """Reset silence flag afer alarm goes off."""
        self.silence = False

    def stall(self):
        """Wait 10 minutes before sending another email."""
        self.silence = True
        signal.signal(signal.SIGALRM, self.stall_handler)
        signal.alarm(600)
        self.logger.debug("Wait 10 minutes before sending another email")

    def cleanup(self):
        """Cleanup alarm."""
        signal.alarm(0)
        self.silence = False
        self.logger.debug("Mailer cleanup")


def test():
    """Test config methods."""
    subject = "Alert Test"
    message = "You can ignore this test message. But you should only get one."
    msg = Mailer(subject, message)
    print("DEBUG: Sending message, it should send.")
    print(msg.message)
    msg.send()

    msg.subject = "Alert Silence Test"
    msg.message = "You should not receive this message. It should be silenced."

    print("DEBUG: Attempting second message during silence period, should not send.")
    msg.send()
    print("DEBUG: This line should print even as the second email was not sent.")

    msg.cleanup()


if __name__ == "__main__":
    test()
