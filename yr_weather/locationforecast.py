import requests
from requests_cache import CachedSession
from typing import Optional, Literal, Union

from .base import BaseClient
from .types.completeforecast import CompleteForecast, CompleteUnits
from .types.compactforecast import CompactForecast, CompactInstantDetails


class Locationforecast(BaseClient):
    """A client for interacting with the Yr Locationforecast API.

    The client has multiple functions which can be used for retrieving data from the API.
    
    It must be initialized with a 'headers' dict, which at least includes a User-Agent.
    The headers will be used with the requests library.
    
    Example 1. Getting a location forecast for a specified location:
    ```
    import yr_weather

    headers = {
        "User-Agent": "Your User-Agent"
    }

    yr_client = yr_weather.Locationforecast(headers=headers)

    # Get weather data for Oslo, Norway.
    weather_data = yr_client.get_forecast(59.91, 10.75)
    ```
    """
    
    def __init__(self, headers: dict, use_cache: Optional[bool] = True) -> None:
        if "User-Agent" not in headers.keys():
            raise ValueError("A custom 'User-Agent' property is required in the 'headers' dict.")
        
        super().__init__(headers, use_cache)

        self._baseURL += "locationforecast/2.0/"
            
    def get_forecast(self, lat: float, lon: float, forecast_type: Optional[Literal["complete", "compact"]] = "complete") -> Union[CompleteForecast, CompactForecast]:
        """Retrieve a complete or compact forecast for a selected location.

        Parameters
        ----------
        lat: float | int
            The latitude of the location.
        lon: float | int
            The longitude of the location.
        forecast_type: Optional[Literal["complete", "compact"]]
            Optionally specify the type of forecast.
            Possible values: "complete" or "compact".
        
        Returns
        -------
        CompleteForecast | CompactForecast
            An object with all possible values from the API, including temperature, air pressure, humidity and so on.
        """
        
        if forecast_type not in ["complete", "compact"]:
            raise ValueError("Value of forecast_type must be 'complete', or 'compact'.\nNote that 'classic' is not supported, as it's obsolete.")
        
        request = self.session.get(self._baseURL + f"{forecast_type}?lat={lat}&lon={lon}")

        if forecast_type == "complete":
            weatherData: CompleteForecast = request.json()
        elif forecast_type == "compact":
            weatherData: CompactForecast = request.json()
        
        return weatherData

    def get_air_temperature(self, lat: float, lon: float, altitude: Optional[int] = None) -> float:
        """Retrieve the air temperature at a given location.
        
        This function returns the latest data available, meaning it provides the current air temperature.

        Parameters
        ----------
        lat: float | int
            The latitude of the location.
        lon: float | int
            The longitude of the location.
        altitude: Optional[int]
            The altitude of the location, given in whole meters.
        
        Returns
        -------
        float
            The air temperature, given in the current scale used by the Yr Locationforecast API (this is normally degrees Celsius).
        """

        URL = self._baseURL + f"compact?lat={lat}&lon={lon}"
        
        if altitude:
            if type(altitude) != int:
                raise TypeError("Type of altitude must be int.")
            URL += f"&altitude={altitude}"
        
        request = self.session.get(URL)
        data: CompactForecast = request.json()

        return float(data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])
    
    def get_instant_data(self, lat: float, lon: float, altitude: Optional[int] = None) -> CompactInstantDetails:
        """Retrieve current weather information about a location.

        This includes air pressure, temperature, humidity, wind and more.

        Parameters
        ----------
        lat: float | int
            The latitude of the location.
        lon: float | int
            The longitude of the location.
        altitude: Optional[int]
            The altitude of the location, given in whole meters.
        
        Returns
        -------
        CompactInstantDetails
            A typed dict with data received from the API.
        """

        URL = self._baseURL + f"complete?lat={lat}&lon={lon}"
        
        if altitude:
            if type(altitude) != int:
                raise TypeError("Type of altitude must be int.")
            URL += f"&altitude={altitude}"
        
        request = self.session.get(URL)
        data: CompleteForecast = request.json()

        instant_data: CompactInstantDetails = data["properties"]["timeseries"][0]["data"]["instant"]["details"]

        return instant_data

    def get_units(self) -> CompleteUnits:
        """Retrieve a list of units used by the Yr Locationforecast API.

        Returns
        -------
        CompleteUnits
            A typed dict with units currently used.
        """

        request = self.session.get(self._baseURL + "complete?lat=0&lon=0")

        data: CompleteForecast = request.json()
        units: CompleteUnits = data["properties"]["meta"]["units"]

        return units

