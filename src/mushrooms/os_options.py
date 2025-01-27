"""OS Options"""

__author__ = "Matt Martini"
__email__ = "matt.martini@imaginarywave.com"
__version__ = "0.3.0"

import platform

# On the production platform (Rapsberry Pi: Linux) use RPi for GPIO
# On the development environment (Mac: Darwin) use mock GPIO
if platform.system() == "Linux":
    from RPi import GPIO
else:
    from RPiMock import GPIO



# try:
#     import RPi.GPIO as GPIO
# except:
#     import Mock.GPIO as GPIO



# from mock import MagicMock, patch

# MockRPi = MagicMock()
# modules = {
#     "RPi": MockRPi,
#     "RPi.GPIO": MockRPi.GPIO,
# }
# patcher = patch.dict("sys.modules", modules)
# patcher.start()

# # Then for the actual test

# with patch("RPi.GPIO.output") as mock_gpio:

#     # Invoke the code to test GPIO
#     mock_gpio.assert_called_with(....)

