"""MET API types for sunrise data."""

from typing import TypedDict, List, Literal


class APIEventGeometry(TypedDict):
    """Geometry data"""

    type: str
    coordinates: List[float]


class APIEventWhen(TypedDict):
    """API Event interval"""

    interval: List[str]


class APIEventTimeWithAzimuth(TypedDict):
    """API event time with azimuth"""

    time: str
    azimuth: float


class APIEventTimeWithElevation(TypedDict):
    """API event time with disc_centre_elevation"""

    time: str
    disc_centre_elevation: float
    visible: bool


class APISunEventsProperties(TypedDict):
    """Custom properties for sun events"""

    body: Literal["Sun"]
    sunrise: APIEventTimeWithAzimuth
    sunset: APIEventTimeWithAzimuth
    solarnoon: APIEventTimeWithElevation
    solarmidnight: APIEventTimeWithElevation


class APIMoonEventsProperties(TypedDict):
    """Custom properties for moon events"""

    body: Literal["Moon"]
    moonrise: APIEventTimeWithAzimuth
    moonset: APIEventTimeWithAzimuth
    high_moon: APIEventTimeWithElevation
    low_moon: APIEventTimeWithElevation
    moonphase: float


class APIEventData(TypedDict):
    """Common API event data"""

    copyright: str
    licenseURL: str
    type: str
    geometry: APIEventGeometry
    when: APIEventWhen


class APISunData(APIEventData):
    """Full sun events data"""

    properties: APISunEventsProperties


class APIMoonData(APIEventData):
    """Full moon events data"""

    properties: APIMoonEventsProperties
