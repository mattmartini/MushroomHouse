"""OS Options"""

import platform

# On the production platform (Rapsberry Pi: Linux) use RPi for GPIO
# On the development environment (Mac: Darwin) use mock GPIO
if platform.system() == "Linux":
    from RPi import GPIO
else:
    from RPiMock import GPIO
