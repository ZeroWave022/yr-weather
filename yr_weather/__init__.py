"""A Python module for interaction with the MET API.

yr_weather supports multiple MET API products.
Please visit the docs to learn more:
https://yr-weather.readthedocs.io/en/latest/
"""

from .locationforecast import Locationforecast
from .radar import Radar
from .textforecast import Textforecast
from .sunrise import Sunrise
from .geosatellite import Geosatellite

__version__ = "0.3.0"
__author__ = "ZeroWave022"
