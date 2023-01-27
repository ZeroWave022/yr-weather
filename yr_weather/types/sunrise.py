from typing import TypedDict, List, Literal

class SunriseMeta(TypedDict):
    licenseurl: str

class SunriseDetails(TypedDict):
    desc: str
    elevation: str
    time: str

class SunriseDetailsSimple(TypedDict):
    desc: str
    time: str

class Moonposition(TypedDict):
    azimuth: str
    desc: str
    elevation: str
    phase: str
    range: str
    time: str

class Moonshadow(TypedDict):
    azimuth: str
    desc: str
    elevation: str
    time: str

class SunriseDate(TypedDict):
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
    height: str
    latitude: str
    longitude: str
    time: List[SunriseDate]

class SunriseData(TypedDict):
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
    "moonshadow"
]
