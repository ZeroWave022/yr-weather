"""A module with classes for the Locationforecast API."""

from typing import Optional, Literal, Dict
from .client import APIClient

from .data.locationforecast import Forecast, ForecastTimeDetails, ForecastUnits
from .api_types.locationforecast import APIForecast


class Locationforecast(APIClient):
    """A client for interacting with the MET Locationforecast API.

    The client has multiple functions which can be used for retrieving data from the API.

    It must be initialized with a ``headers`` dict, which at least includes a User-Agent.
    The headers will be used with the :mod:`requests` library.

    For usage examples, see the documentation.
    """

    def __init__(self, headers: Dict[str, str], use_cache=True) -> None:
        header_keys = [key.lower() for key in headers]
        if "user-agent" not in header_keys:
            raise ValueError("A custom 'User-Agent' is required in the 'headers' dict.")

        super().__init__(headers, use_cache)

        self._base_url += "locationforecast/2.0/"

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
        :class:`.Forecast`
            An instance of :class:`.Forecast` with helper functions and values from the API.
        """

        if forecast_type not in ["complete", "compact"]:
            raise ValueError(
                "Value of forecast_type must be 'complete', or 'compact'.\nNote that 'classic' is not supported, as it's obsolete."
            )

        request = self.session.get(
            self._base_url + f"{forecast_type}?lat={lat}&lon={lon}"
        )

        weather_data: APIForecast = request.json()

        return Forecast(weather_data)

    def get_air_temperature(
        self, lat: float, lon: float, altitude: Optional[int] = None
    ) -> Optional[float]:
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

        url = self._base_url + f"compact?lat={lat}&lon={lon}"

        if altitude:
            if not isinstance(altitude, int):
                raise TypeError("Type of altitude must be int.")
            url += f"&altitude={altitude}"

        request = self.session.get(url)
        data: APIForecast = request.json()

        forecast = Forecast(data)

        return forecast.now().details.air_temperature

    def get_instant_data(
        self, lat: float, lon: float, altitude: Optional[int] = None
    ) -> ForecastTimeDetails:
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
        :class:`.ForecastTimeDetails`
            A dataclass with info received from the API.
        """

        url = self._base_url + f"complete?lat={lat}&lon={lon}"

        if altitude:
            if not isinstance(altitude, int):
                raise TypeError("Type of altitude must be int.")
            url += f"&altitude={altitude}"

        request = self.session.get(url)
        data: APIForecast = request.json()

        forecast = Forecast(data)

        return forecast.now().details

    def get_units(self) -> ForecastUnits:
        """Retrieve a list of units used by the MET Locationforecast API.

        Returns
        -------
        :class:`.ForecastUnits`
            A dataclass with units currently used.
        """

        request = self.session.get(self._base_url + "complete?lat=0&lon=0")

        data: APIForecast = request.json()

        forecast = Forecast(data)

        return forecast.units
