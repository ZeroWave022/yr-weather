"""Types for compact Locationforecasts."""

from typing import TypedDict, List


class CompactUnits(TypedDict):
    """Units that can be used in the forecast data"""

    air_pressure_at_sea_level: str
    air_temperature: str
    cloud_area_fraction: str
    precipitation_amount: str
    relative_humidity: str
    wind_from_direction: str
    wind_speed: str


class CompactInstantDetails(TypedDict):
    """Details of instant weather data for a time"""

    air_pressure_at_sea_level: float
    air_temperature: float
    cloud_area_fraction: float
    relative_humidity: float
    wind_from_direction: float
    wind_speed: float


class CompactFutureSummary(TypedDict):
    """Summary for next x hours for a time"""

    symbol_code: str


class CompactFutureDetails(TypedDict):
    """Instant details for a forecast"""

    precipitation_amount: float


class CompactInstantData(TypedDict):
    """Instant data for a forecast"""

    details: CompactInstantDetails


class CompactFutureData(TypedDict):
    """Data for next x hours for a time"""

    summary: CompactFutureSummary
    details: CompactFutureDetails


class CompactTimeData(TypedDict):
    """Data for one time from a timeseries"""

    instant: CompactInstantData
    next_1_hours: CompactFutureData
    next_6_hours: CompactFutureData
    next_12_hours: CompactFutureData


class CompactTime(TypedDict):
    """A time in the forecast timeseries"""

    time: str
    data: CompactTimeData


class CompactMeta(TypedDict):
    """Forecast metadata"""

    updated_at: str
    units: CompactUnits


class CompactProperties(TypedDict):
    """Forecast properties"""

    meta: CompactMeta
    timeseries: List[CompactTime]


class CompactGeometry(TypedDict):
    """Geometry data"""

    type: str
    coordinates: List[int]


class CompactForecast(TypedDict):
    """Compact forecast data"""

    type: str
    geometry: CompactGeometry
    properties: CompactProperties
