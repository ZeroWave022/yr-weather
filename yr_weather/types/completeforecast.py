from typing import TypedDict, Union, List

class CompleteUnits(TypedDict):
    air_pressure_at_sea_level: str
    air_temperature: str
    air_temperature_max: str
    air_temperature_min: str
    cloud_area_fraction: str
    cloud_area_fraction_high: str
    cloud_area_fraction_low: str
    cloud_area_fraction_medium: str
    dew_point_temperature: str
    fog_area_fraction: str
    precipitation_amount: str
    relative_humidity: str
    ultraviolet_index_clear_sky: str
    wind_from_direction: str
    wind_speed: str

class CompleteInstantDetails(TypedDict):
    air_pressure_at_sea_level: float
    air_temperature: float
    cloud_area_fraction: float
    cloud_area_fraction_high: float
    cloud_area_fraction_low: float
    cloud_area_fraction_medium: float
    dew_point_temperature: float
    fog_area_fraction: float
    relative_humidity: float
    ultraviolet_index_clear_sky: float
    wind_from_direction: float
    wind_speed: float

class CompleteFutureSummary(TypedDict):
    symbol_code: str

class CompleteFutureDetails(TypedDict):
    air_temperature_max: Union[float, None]
    air_temperature_min: Union[float, None]
    precipitation_amount: Union[float, None]

class CompleteInstantData(TypedDict):
    details: CompleteInstantDetails

class CompleteFutureData(TypedDict):
    summary: CompleteFutureSummary
    details: CompleteFutureDetails

class CompleteTimeData(TypedDict):
    instant: CompleteInstantData
    next_1_hours: CompleteFutureData
    next_6_hours: CompleteFutureData
    next_12_hours: CompleteFutureData

class CompleteTime(TypedDict):
    time: str
    data: CompleteTimeData

class CompleteMeta(TypedDict):
    updated_at: str
    units: CompleteUnits

class CompleteProperties(TypedDict):
    meta: CompleteMeta
    timeseries: List[CompleteTime]

class CompleteGeometry(TypedDict):
    type: str
    coordinates: List[int]

class CompleteForecast(TypedDict):
    type: str
    geometry: CompleteGeometry
    properties: CompleteProperties
