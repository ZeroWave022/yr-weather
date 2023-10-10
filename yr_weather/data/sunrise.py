"""Classes storing data used by yr_weather.sunrise"""

from dataclasses import dataclass
from typing import Optional, Literal, List


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
