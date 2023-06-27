"""A module with classes for the Locationforecast API."""

from datetime import datetime
from typing import Optional, Literal, Dict, List
from dataclasses import dataclass, fields

from .client import APIClient


class _ForecastData:
    """A base class for dataclasses which use certain classmethods."""

    @classmethod
    def create(cls, given_dict):
        """Instantiate this class with all possible keyword arguments from the given dict.
        This function filters and removes any unexpected keyword arguments which will cause an exception.
        """

        parameters = [field.name for field in fields(cls)]
        return cls(**{k: v for k, v in given_dict.items() if k in parameters})


@dataclass
class ForecastTimeDetails(_ForecastData):
    """Details of weather data for a forecast time."""

    air_pressure_at_sea_level: Optional[float] = None
    air_temperature: Optional[float] = None
    air_temperature_percentile_10: Optional[float] = None
    air_temperature_percentile_90: Optional[float] = None
    cloud_area_fraction: Optional[float] = None
    cloud_area_fraction_high: Optional[float] = None
    cloud_area_fraction_low: Optional[float] = None
    cloud_area_fraction_medium: Optional[float] = None
    dew_point_temperature: Optional[float] = None
    fog_area_fraction: Optional[float] = None
    relative_humidity: Optional[float] = None
    ultraviolet_index_clear_sky: Optional[float] = None
    wind_from_direction: Optional[float] = None
    wind_speed: Optional[float] = None
    wind_speed_of_gust: Optional[float] = None
    wind_speed_percentile_10: Optional[float] = None
    wind_speed_percentile_90: Optional[float] = None


@dataclass
class ForecastFutureSummary(_ForecastData):
    """Summary for a forecast predicting the weather in the future."""

    symbol_code: Optional[str] = None
    symbol_confidence: Optional[str] = None


@dataclass
class ForecastFutureDetails(_ForecastData):
    """Details for a forecast predicting the weather in the future."""

    air_pressure_at_sea_level: Optional[float] = None
    air_temperature: Optional[float] = None
    air_temperature_max: Optional[float] = None
    air_temperature_min: Optional[float] = None
    air_temperature_percentile_10: Optional[float] = None
    air_temperature_percentile_90: Optional[float] = None
    cloud_area_fraction: Optional[float] = None
    cloud_area_fraction_high: Optional[float] = None
    cloud_area_fraction_low: Optional[float] = None
    cloud_area_fraction_medium: Optional[float] = None
    dew_point_temperature: Optional[float] = None
    fog_area_fraction: Optional[float] = None
    precipitation_amount: Optional[float] = None
    precipitation_amount_max: Optional[float] = None
    precipitation_amount_min: Optional[float] = None
    probability_of_precipitation: Optional[float] = None
    probability_of_thunder: Optional[float] = None
    relative_humidity: Optional[float] = None
    ultraviolet_index_clear_sky: Optional[float] = None
    wind_from_direction: Optional[float] = None
    wind_speed: Optional[float] = None
    wind_speed_of_gust: Optional[float] = None
    wind_speed_percentile_10: Optional[float] = None
    wind_speed_percentile_90: Optional[float] = None


@dataclass
class ForecastUnits(_ForecastData):
    """Class storing units used by a forecast."""

    air_pressure_at_sea_level: Optional[str] = None
    air_temperature: Optional[str] = None
    air_temperature_max: Optional[str] = None
    air_temperature_min: Optional[str] = None
    air_temperature_percentile_10: Optional[str] = None
    air_temperature_percentile_90: Optional[str] = None
    cloud_area_fraction: Optional[str] = None
    cloud_area_fraction_high: Optional[str] = None
    cloud_area_fraction_low: Optional[str] = None
    cloud_area_fraction_medium: Optional[str] = None
    dew_point_temperature: Optional[str] = None
    fog_area_fraction: Optional[str] = None
    precipitation_amount: Optional[str] = None
    precipitation_amount_max: Optional[str] = None
    precipitation_amount_min: Optional[str] = None
    probability_of_precipitation: Optional[str] = None
    probability_of_thunder: Optional[str] = None
    relative_humidity: Optional[str] = None
    ultraviolet_index_clear_sky: Optional[str] = None
    wind_from_direction: Optional[str] = None
    wind_speed: Optional[str] = None
    wind_speed_of_gust: Optional[str] = None
    wind_speed_percentile_10: Optional[str] = None
    wind_speed_percentile_90: Optional[str] = None


@dataclass
class ForecastGeometry(_ForecastData):
    """Geometry data for a forecast."""

    type: Optional[str] = None
    coordinates: Optional[List[int]] = None


class ForecastFuture:
    """A class holding a forecast predicting the weather in the future from a specified time.

    Attributes
    ----------
    summary: ForecastFutureSummary
        A summary for this forecast.
    details: ForecastFutureDetails
        The forecast data for this forecast.
    """

    def __init__(self, data):
        self.summary = ForecastFutureSummary.create(data["summary"])

        if "details" in data:
            self.details = ForecastFutureDetails.create(data["details"])
        else:
            self.details = None


class ForecastTime:
    """A class holding data about a forecast for a specific time.

    Attributes
    ----------
    time: str
        The ISO 8601 timestamp in UTC time for this ForecastTime.
    details: ForecastTimeDetails
        The forecast data for this ForecastTime.
    next_hour: ForecastFuture
        A ForecastFuture with data about the forecast the next hour.
    next_6_hours: ForecastFuture
        A ForecastFuture with data about the forecast the 6 hours.
    next_12_hours: ForecastFuture
        A ForecastFuture with data about the forecast the 12 hours.
    """

    def __init__(self, time: dict) -> None:
        self.time: str = time["time"]
        self.details = ForecastTimeDetails.create(time["data"]["instant"]["details"])
        self.next_hour = ForecastFuture(time["data"]["next_1_hours"])
        self.next_6_hours = ForecastFuture(time["data"]["next_6_hours"])
        self.next_12_hours = ForecastFuture(time["data"]["next_12_hours"])


class Forecast:
    """A class holding a location forecast with multiple timeframes to choose from.

    Attributes
    ----------
    type: str
        MET API service type (always `"Feature"`).
    geometry: ForecastGeometry
        Geometry data for this forecast.
    updated_at: str
        The ISO 8601 timestamp in UTC time at which this forecast was last updated.
    units: ForecastUnits
        The units used by this forecast.
    """

    def __init__(self, forecast_data: dict) -> None:
        self.type: str = forecast_data["type"]
        self.geometry = ForecastGeometry.create(forecast_data["geometry"])

        meta = forecast_data["properties"]["meta"]
        self.updated_at: str = meta["updated_at"]
        self.units = ForecastUnits.create(meta["units"])

        # The timeseries used internally is kept as a dict
        self._timeseries = forecast_data["properties"]["timeseries"]

    def _conv_to_nearest_hour(self, date: datetime) -> datetime:
        if date.minute >= 30:
            return date.replace(microsecond=0, second=0, minute=0, hour=date.hour + 1)

        return date.replace(microsecond=0, second=0, minute=0)

    def now(self) -> ForecastTime:
        """Get the newest :class:`ForecastTime` for this Forecast.

        Returns
        -------
        ForecastTime
        """
        now = datetime.utcnow()
        time = self._conv_to_nearest_hour(now)

        nearest_hour = time.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Try to get the data for the nearest hour from API data
        filtered_time: List[dict] = list(
            filter(lambda t: t["time"] == nearest_hour, self._timeseries)
        )

        if filtered_time:
            return ForecastTime(filtered_time[0])

        return ForecastTime(self._timeseries[0])

    def get_forecast_time(self, time: datetime) -> Optional[ForecastTime]:
        """Get a certain :class:`ForecastTime` by specifying the time.
        The time will be rounded to the nearest hour.

        Parameters
        ----------
        time: datetime.datetime
            The datetime to use when retrieving the nearest forecast info.

        Returns
        -------
        ForecastTime | None
        """
        if not isinstance(time, datetime):
            raise ValueError(
                "Type of time should be datetime.datetime.\nFor more information, see https://docs.python.org/3/library/datetime.html"
            )

        time = self._conv_to_nearest_hour(time)
        formatted_time = time.strftime("%Y-%m-%dT%H:%M:%SZ")

        found_time: List[dict] = list(
            filter(lambda t: t["time"] == formatted_time, self._timeseries)
        )

        if found_time:
            return ForecastTime(found_time[0])

        return None


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
        Forecast
            An instance of :class:`Forecast` with helper functions and values from the API.
        """

        if forecast_type not in ["complete", "compact"]:
            raise ValueError(
                "Value of forecast_type must be 'complete', or 'compact'.\nNote that 'classic' is not supported, as it's obsolete."
            )

        request = self.session.get(
            self._base_url + f"{forecast_type}?lat={lat}&lon={lon}"
        )

        weather_data = request.json()

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
        data = request.json()

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
        ForecastTimeDetails
            A dataclass with info received from the API.
        """

        url = self._base_url + f"complete?lat={lat}&lon={lon}"

        if altitude:
            if not isinstance(altitude, int):
                raise TypeError("Type of altitude must be int.")
            url += f"&altitude={altitude}"

        request = self.session.get(url)
        data = request.json()

        forecast = Forecast(data)

        return forecast.now().details

    def get_units(self) -> ForecastUnits:
        """Retrieve a list of units used by the MET Locationforecast API.

        Returns
        -------
        ForecastUnits
            A dataclass with units currently used.
        """

        request = self.session.get(self._base_url + "complete?lat=0&lon=0")

        data = request.json()

        forecast = Forecast(data)

        return forecast.units
