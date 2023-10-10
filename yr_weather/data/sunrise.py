"""Classes storing data used by yr_weather.sunrise"""

from dataclasses import dataclass
from typing import Literal, List

from yr_weather.api_types.sunrise import APISunData, APIMoonData, APIEventData


@dataclass
class EventsGeometry:
    """A dataclass holding coordinates."""

    coordinates: List[float]
    type: str


class CommonEventsData:
    """A class with common event data for both sun and moon events."""

    def __init__(self, data: APIEventData):
        self.type = data["type"]
        self.copyright = data["copyright"]
        self.license_url = data["licenseURL"]
        self.geometry = EventsGeometry(**data["geometry"])
        self.interval = data["when"]["interval"]


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

    def __init__(self, data: APISunData):
        super().__init__(data)

        props = data["properties"]

        self.body: Literal["Sun"] = props["body"]
        self.sunrise = TimeWithAzimuth(**props["sunrise"])
        self.sunset = TimeWithAzimuth(**props["sunset"])
        self.solarnoon = TimeWithElevation(**props["solarnoon"])
        self.solarmidnight = TimeWithElevation(**props["solarmidnight"])


class MoonEvents(CommonEventsData):
    """A class with moon event data."""

    def __init__(self, data: APIMoonData):
        super().__init__(data)

        props = data["properties"]

        self.body: Literal["Moon"] = props["body"]
        self.moonrise = TimeWithAzimuth(**props["moonrise"])
        self.moonset = TimeWithAzimuth(**props["moonset"])
        self.high_moon = TimeWithElevation(**props["high_moon"])
        self.low_moon = TimeWithElevation(**props["low_moon"])
        self.moonphase: float = props["moonphase"]
