from datetime import datetime
from typing import Optional, Literal

from .base import BaseClient
from .types.completeforecast import CompleteForecast, CompleteUnits, CompleteTime
from .types.compactforecast import CompactForecast, CompactInstantDetails, CompactTime


class ForecastTime:
    def __init__(self, time: CompleteTime | CompactTime) -> None:
        self.details = time["data"]["instant"]["details"]
        self.next_hour = time["data"]["next_1_hours"]
        self.next_6_hours = time["data"]["next_6_hours"]
        self.next_12_hours = time["data"]["next_12_hours"]


class Forecast:
    def __init__(self, forecastData: CompleteForecast | CompactForecast) -> None:
        self.type = forecastData["type"]
        self.geometry = forecastData["geometry"]
        self.updated_at = forecastData["properties"]["meta"]["updated_at"]
        self.units = forecastData["properties"]["meta"]["units"]
        self._timeseries = forecastData["properties"]["timeseries"]

    def _conv_to_nearest_hour(self, date: datetime) -> datetime:
        if date.minute >= 30:
            return date.replace(microsecond=0, second=0, minute=0, hour=date.hour + 1)
        else:
            return date.replace(microsecond=0, second=0, minute=0)

    def now(self) -> ForecastTime:
        """Get the newest :class:`ForecastTime` for this Forecast.

        Returns
        -------
        ForecastTime
        """
        now = datetime.utcnow()
        time = self._conv_to_nearest_hour(now)
        """if now.minute >= 30:
            nearest_hour = now.replace(microsecond=0, second=0, minute=0, hour=now.hour+1)
        else:
            nearest_hour = now.replace(microsecond=0, second=0, minute=0)"""

        nearest_hour = time.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Try to get the data for the nearest hour from API data
        filtered_time = list(
            filter(lambda t: t["time"] == nearest_hour, self._timeseries)
        )

        if filtered_time:
            return ForecastTime(filtered_time[0])
        else:
            return ForecastTime(self._timeseries[0])

    def get_forecast_time(self, time: datetime) -> ForecastTime | None:
        """Get a certain :class:`ForecastTime` by specifiying the time.
        The time will be rounded to the nearest hour.

        Parameters
        ----------
        time: datetime.datetime
            The datetime to use when retrieving the nearest forecast info.

        Returns
        -------
        ForecastTime
        """
        if not isinstance(time, datetime):
            raise ValueError(
                "Type of time should be datetime.datetime.\nFor more information, see https://docs.python.org/3/library/datetime.html"
            )

        formatted_time = time.strftime("%Y-%m-%dT%H:%M:%SZ")

        found_time = list(
            filter(lambda t: t["time"] == formatted_time, self._timeseries)
        )

        if found_time:
            return ForecastTime(found_time[0])
        else:
            return None


class Locationforecast(BaseClient):
    """A client for interacting with the Yr Locationforecast API.

    The client has multiple functions which can be used for retrieving data from the API.

    It must be initialized with a ``headers`` dict, which at least includes a User-Agent.
    The headers will be used with the :mod:`requests` library.

    Example 1. Getting a location forecast for a specified location:

    .. code-block:: python

        import yr_weather

        headers = {
            "User-Agent": "Your User-Agent"
        }

        yr_client = yr_weather.Locationforecast(headers=headers)

        # Get weather data for Oslo, Norway.
        weather_data = yr_client.get_forecast(59.91, 10.75)
    """

    def __init__(self, headers: dict, use_cache: bool = True) -> None:
        header_keys = [key.lower() for key in headers]
        if "user-agent" not in header_keys:
            raise ValueError("A custom 'User-Agent' is required in the 'headers' dict.")

        super().__init__(headers, use_cache)

        self._baseURL += "locationforecast/2.0/"

    def set_headers(self, headers: dict) -> dict:
        header_keys = [key.lower() for key in headers]
        if "user-agent" not in header_keys:
            raise ValueError("A custom 'User-Agent' is required in the 'headers' dict.")

        return super().set_headers(headers)

    def get_forecast(
        self,
        lat: float,
        lon: float,
        forecast_type: Literal["complete", "compact"] = "complete",
    ) -> Forecast:
        """Retrieve a complete or compact forecast for a selected location.

        Parameters
        ----------
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        forecast_type: Literal["complete", "compact"]
            Optional: Specify the type of forecast, either ``"complete"`` or ``"compact"``.
            Default is ``"complete"``.

        Returns
        -------
        Forecast
            An instance of :class:`Forecast` with helper functions and values from the API.
        """

        if forecast_type not in ["complete", "compact"]:
            raise ValueError(
                "Value of forecast_type must be 'complete', or 'compact'.\nNote that 'classic' is not supported, as it's obsolete."
            )

        request = self.session.get(
            self._baseURL + f"{forecast_type}?lat={lat}&lon={lon}"
        )

        weatherData = request.json()

        return Forecast(weatherData)

    def get_air_temperature(
        self, lat: float, lon: float, altitude: Optional[int] = None
    ) -> float:
        """Retrieve the air temperature at a given location.

        This function returns the latest data available, meaning it provides the current air temperature.

        Parameters
        ----------
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        altitude: Optional[:class:`int`]
            The altitude of the location, given in whole meters.

        Returns
        -------
        :class:`float`
            The air temperature, given in the current scale used by the Yr Locationforecast API (this is usually degrees Celsius).
        """

        URL = self._baseURL + f"compact?lat={lat}&lon={lon}"

        if altitude:
            if not isinstance(altitude, int):
                raise TypeError("Type of altitude must be int.")
            URL += f"&altitude={altitude}"

        request = self.session.get(URL)
        data = request.json()

        forecast = Forecast(data)

        return float(forecast.now().details["air_temperature"])

    def get_instant_data(
        self, lat: float, lon: float, altitude: Optional[int] = None
    ) -> CompactInstantDetails:
        """Retrieve current weather information about a location.

        This includes air pressure, temperature, humidity, wind and more.

        Parameters
        ----------
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        altitude: Optional[:class:`int`]
            The altitude of the location, given in whole meters.

        Returns
        -------
        CompactInstantDetails
            A typed dict with data received from the API.
        """

        URL = self._baseURL + f"complete?lat={lat}&lon={lon}"

        if altitude:
            if not isinstance(altitude, int):
                raise TypeError("Type of altitude must be int.")
            URL += f"&altitude={altitude}"

        request = self.session.get(URL)
        data = request.json()

        forecast = Forecast(data)

        return forecast.now().details

    def get_units(self) -> CompleteUnits:
        """Retrieve a list of units used by the Yr Locationforecast API.

        Returns
        -------
        CompleteUnits
            A typed dict with units currently used.
        """

        request = self.session.get(self._baseURL + "complete?lat=0&lon=0")

        data: CompleteForecast = request.json()

        forecast = Forecast(data)

        return forecast.units
