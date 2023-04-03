from typing import TypedDict, List


class CompactUnits(TypedDict):
    air_pressure_at_sea_level: str
    air_temperature: str
    cloud_area_fraction: str
    precipitation_amount: str
    relative_humidity: str
    wind_from_direction: str
    wind_speed: str


class CompactInstantDetails(TypedDict):
    air_pressure_at_sea_level: float
    air_temperature: float
    cloud_area_fraction: float
    relative_humidity: float
    wind_from_direction: float
    wind_speed: float


class CompactFutureSummary(TypedDict):
    symbol_code: str


class CompactFutureDetails(TypedDict):
    precipitation_amount: float


class CompactInstantData(TypedDict):
    details: CompactInstantDetails


class CompactFutureData(TypedDict):
    summary: CompactFutureSummary
    details: CompactFutureDetails


class CompactTimeData(TypedDict):
    instant: CompactInstantData
    next_1_hours: CompactFutureData
    next_6_hours: CompactFutureData
    next_12_hours: CompactFutureData


class CompactTime(TypedDict):
    time: str
    data: CompactTimeData


class CompactMeta(TypedDict):
    updated_at: str
    units: CompactUnits


class CompactProperties(TypedDict):
    meta: CompactMeta
    timeseries: List[CompactTime]


class CompactGeometry(TypedDict):
    type: str
    coordinates: List[int]


class CompactForecast(TypedDict):
    type: str
    geometry: CompactGeometry
    properties: CompactProperties
