"""Classes storing data used by yr_weather.locationforecast"""

from datetime import datetime
from typing import Optional, List
from dataclasses import dataclass, field, fields


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


@dataclass
class ForecastFuture:
    """A class holding a forecast predicting the weather in the future from a specified time.

    Attributes
    ----------
    summary: :class:`.ForecastFutureSummary`
        A summary for this forecast.
    details: :class:`.ForecastFutureDetails`
        The forecast data for this forecast.
    """

    summary: Optional[ForecastFutureSummary] = None
    details: Optional[ForecastFutureDetails] = None

    def __post_init__(self):
        if self.summary:
            self.summary = ForecastFutureSummary.create(self.summary)

        if self.details:
            self.details = ForecastFutureDetails.create(self.details)


@dataclass
class ForecastTime:
    """A class holding data about a forecast for a specific time.

    Attributes
    ----------
    time: :class:`str`
        The ISO 8601 timestamp in UTC time for this ForecastTime.
    details: :class:`.ForecastTimeDetails`
        The forecast data for this ForecastTime.
    next_hour: :class:`.ForecastFuture`
        A ForecastFuture with data about the forecast the next hour.
    next_6_hours: :class:`.ForecastFuture`
        A ForecastFuture with data about the forecast the 6 hours.
    next_12_hours: :class:`.ForecastFuture`
        A ForecastFuture with data about the forecast the 12 hours.
    """

    _data: dict
    time: str = field(init=False)
    details: ForecastTimeDetails = field(init=False)
    next_hour: ForecastFuture = field(init=False)
    next_6_hours: ForecastFuture = field(init=False)
    next_12_hours: ForecastFuture = field(init=False)

    def __post_init__(self) -> None:
        self.time = self._data["time"]
        self.details = ForecastTimeDetails.create(
            self._data["data"]["instant"]["details"]
        )
        self.next_hour = ForecastFuture(**self._data["data"]["next_1_hours"])
        self.next_6_hours = ForecastFuture(**self._data["data"]["next_6_hours"])
        self.next_12_hours = ForecastFuture(**self._data["data"]["next_12_hours"])


class Forecast:
    """A class holding a location forecast with multiple timeframes to choose from.

    Attributes
    ----------
    type: :class:`str`
        MET API service type (always ``"Feature"``).
    geometry: :class:`.ForecastGeometry`
        Geometry data for this forecast.
    updated_at: :class:`str`
        The ISO 8601 timestamp in UTC time at which this forecast was last updated.
    units: :class:`.ForecastUnits`
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
        :class:`.ForecastTime`
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
        :class:`.ForecastTime` | None
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
