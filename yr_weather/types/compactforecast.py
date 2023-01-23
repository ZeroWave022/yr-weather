from typing import TypedDict, List

class ForecastUnits(TypedDict):
    air_pressure_at_sea_level: str
    air_temperature: str
    cloud_area_fraction: str
    precipitation_amount: str
    relative_humidity: str
    wind_from_direction: str
    wind_speed: str

class ForecastInstantDetails(TypedDict):
    air_pressure_at_sea_level: float
    air_temperature: float
    cloud_area_fraction: float
    relative_humidity: float
    wind_from_direction: float
    wind_speed: float

class ForecastFutureSummary(TypedDict):
    symbol_code: str

class ForecastFutureDetails(TypedDict):
    precipitation_amount: float

class ForecastInstantData(TypedDict):
    details: ForecastInstantDetails

class ForecastFutureData(TypedDict):
    summary: ForecastFutureSummary
    details: ForecastFutureDetails

class ForecastTimeData(TypedDict):
    instant: ForecastInstantData
    next_1_hours: ForecastFutureData
    next_6_hours: ForecastFutureData
    next_12_hours: ForecastFutureData

class ForecastTime(TypedDict):
    time: str
    data: ForecastTimeData

class ForecastMeta(TypedDict):
    updated_at: str
    units: ForecastUnits

class ForecastProperties(TypedDict):
    meta: ForecastMeta
    timeseries: List[ForecastTime]

class ForecastGeometry(TypedDict):
    type: str
    coordinates: List[int]

class CompactForecast(TypedDict):
    type: str
    geometry: ForecastGeometry
    properties: ForecastProperties
