"""A Python module for interaction with the Yr API.

To get started, initialize a Locationforecast client like so:

.. code-block:: python
    
    import yr_weather

    headers = {
        "User-Agent": "Your User-Agent"
    }

    my_client = yr_weather.Locationforecast(headers=headers)

For valid user agents, please see:
https://api.met.no/doc/TermsOfService

Using ``my_client``, you can receive forecasts for specified locations, get the air temperature, and more.
"""

from .locationforecast import Locationforecast
from .radar import Radar
from .textforecast import Textforecast
from .sunrise import Sunrise
from .geosatellite import Geosatellite

__version__ = "0.2.0"
__author__ = "ZeroWave022"
