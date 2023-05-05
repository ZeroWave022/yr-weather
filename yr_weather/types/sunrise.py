"""Types for sunrise data."""

from typing import TypedDict, List, Literal


class SunriseMeta(TypedDict):
    """Sunrise metadata"""

    licenseurl: str


class SunriseDetails(TypedDict):
    """Data for a sunrise event"""

    desc: str
    elevation: str
    time: str


class SunriseDetailsSimple(TypedDict):
    """Data for a sunrise event (simple)"""

    desc: str
    time: str


class Moonposition(TypedDict):
    """Data for moon position"""

    azimuth: str
    desc: str
    elevation: str
    phase: str
    range: str
    time: str


class Moonshadow(TypedDict):
    """Data for a moon shadow"""

    azimuth: str
    desc: str
    elevation: str
    time: str


class SunriseDate(TypedDict):
    """Data for a specific sunrise date"""

    high_moon: SunriseDetails
    low_moon: SunriseDetails
    moonphase: SunriseDetails
    solarmidnight: SunriseDetails
    solarnoon: SunriseDetails

    moonrise: SunriseDetailsSimple
    moonset: SunriseDetailsSimple
    sunrise: SunriseDetailsSimple
    sunset: SunriseDetailsSimple

    moonposition: Moonposition
    moonshadow: Moonshadow


class SunriseLocation(TypedDict):
    """Data for a sunrise location"""

    height: str
    latitude: str
    longitude: str
    time: List[SunriseDate]


class SunriseData(TypedDict):
    """Data for a sunrise"""

    location: SunriseLocation
    meta: SunriseMeta


DetailLiteral = Literal[
    "high_moon",
    "low_moon",
    "moonphase",
    "solarmidnight",
    "solarnoon",
    "moonrise",
    "moonset",
    "sunrise",
    "sunset",
    "moonposition",
    "moonshadow",
]
