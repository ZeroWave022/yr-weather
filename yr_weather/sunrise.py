"""A module with classes for the Sunrise API."""

from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Literal, List
import requests
from .client import APIClient


@dataclass
class EventsGeometry:
    """A dataclass holding coordinates."""

    coordinates: List[float]
    type: Literal["Point"]


@dataclass
class CommonEventsData:
    """A dataclass with common event data for both sun and moon events."""

    type: Optional[str] = None
    copyright: Optional[str] = None
    license_url: Optional[str] = None
    geometry: Optional[EventsGeometry] = None
    interval: Optional[List[str]] = None

    def __post_init__(self):
        if self.geometry:
            self.geometry = EventsGeometry(**self.geometry)


@dataclass
class TimeWithAzimuth:
    """A dataclass with event time data with azimuth."""

    time: str
    azimuth: float


@dataclass
class TimeWithElevation:
    """A dataclass with event data with disc centre elevation."""

    time: str
    disc_centre_elevation: float
    visible: bool


class SunEvents(CommonEventsData):
    """A class with sun event data."""

    def __init__(self, data: dict):
        super().__init__(
            type=data["type"],
            copyright=data["copyright"],
            license_url=data["licenseURL"],
            geometry=data["geometry"],
            interval=data["when"]["interval"],
        )

        props = data["properties"]

        self.body: Literal["Sun"] = props["body"]
        self.sunrise = TimeWithAzimuth(**props["sunrise"])
        self.sunset = TimeWithAzimuth(**props["sunset"])
        self.solarnoon = TimeWithElevation(**props["solarnoon"])
        self.solarmidnight = TimeWithElevation(**props["solarmidnight"])


class MoonEvents(CommonEventsData):
    """A class with moon event data."""

    def __init__(self, data: dict):
        super().__init__(
            type=data["type"],
            copyright=data["copyright"],
            license_url=data["licenseURL"],
            geometry=data["geometry"],
            interval=data["when"]["interval"],
        )

        props = data["properties"]

        self.body: Literal["Moon"] = props["body"]
        self.moonrise = TimeWithAzimuth(**props["moonrise"])
        self.moonset = TimeWithAzimuth(**props["moonset"])
        self.high_moon = TimeWithElevation(**props["high_moon"])
        self.low_moon = TimeWithElevation(**props["low_moon"])
        self.moonphase: float = props["moonphase"]


class Sunrise(APIClient):
    """A client for interacting with the Yr Sunrise API."""

    def __init__(self, headers, use_cache=True) -> None:
        super().__init__(headers, use_cache)

        self._base_url += "sunrise/3.0/"

    def _get_events(self, event_type: str, **kwargs) -> dict:
        date = kwargs.get("date")
        lat = kwargs.get("lat")
        lon = kwargs.get("lon")
        offset = kwargs.get("offset")

        # Ensure correct variable types.
        if not isinstance(date, str):
            raise ValueError("Type of 'date' must be str.")

        if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
            raise ValueError("Type of 'lat' and 'lon' must be int or float.")

        if offset:
            if not isinstance(offset, str):
                raise ValueError("Type of 'offset' must be str.")

            # Ensure offset is valid.
            if not self._ensure_valid_offset(offset):
                raise ValueError(
                    "The 'offset' parameter is not a valid timezone offset."
                )

        # Check if the date provided is valid.
        try:
            splitted = [int(num) for num in date.split("-")]
            datetime(splitted[0], splitted[1], splitted[2])
        except Exception as exc:
            raise ValueError("The 'date' parameter must be a valid date.") from exc

        url = self._base_url + event_type

        request = self.session.get(
            url,
            params={"date": date, "lat": str(lat), "lon": str(lon), "offset": offset},
        )

        if not request.ok:
            raise requests.HTTPError(
                f"Unsuccessful response received: {request.status_code} {request.reason}."
            )

        return request.json()

    def get_sun_events(
        self,
        date: str,
        lat: float,
        lon: float,
        offset: Optional[str] = None,
    ) -> SunEvents:
        """Get sun events data (sunrise, sunset, etc).

        For more information, please see: https://api.met.no/weatherapi/sunrise/3.0/documentation

        Parameters
        ----------
        date: :class:`str`
            A date formatted in ISO 8601 format, like so: `YYYY-MM-DD`.
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        offset: Optional[:class:`str`]
            The timezone offset, given in the following format: `+HH:MM` or `-HH:MM`.

        Returns
        -------
        :class:`.SunEvents`
        """
        data = self._get_events("sun", date=date, lat=lat, lon=lon, offset=offset)

        return SunEvents(data)

    def get_moon_events(
        self,
        date: str,
        lat: float,
        lon: float,
        offset: Optional[str] = None,
    ) -> MoonEvents:
        """Get moon events data (moonrise, moonset, etc).

        For more information, please see: https://api.met.no/weatherapi/sunrise/3.0/documentation

        Parameters
        ----------
        date: :class:`str`
            A date formatted in ISO 8601 format, like so: `YYYY-MM-DD`.
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        offset: Optional[:class:`str`]
            The timezone offset, given in the following format: `+HH:MM` or `-HH:MM`.

        Returns
        -------
        :class:`.MoonEvents`
        """
        data = self._get_events("moon", date=date, lat=lat, lon=lon, offset=offset)

        return MoonEvents(data)

    def _ensure_valid_offset(self, offset: str) -> bool:
        """Ensures that a valid offset is given.

        Returns a bool, indicating whether the offset is valid.
        """
        if not offset.startswith(("+", "-")):
            return False

        time = offset.replace("+", "").replace("-", "")

        splitted = time.split(":")

        if len(splitted) != 2:
            return False

        for i in splitted:
            if len(i) != 2:
                return False
            try:
                int(i)
            except ValueError:
                return False

        if int(splitted[0]) < 10 and not splitted[0].startswith("0"):
            return False

        return True
