from typing import TypedDict, Union, List

class ForecastUnits(TypedDict):
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

class ForecastInstantDetails(TypedDict):
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

class ForecastFutureSummary(TypedDict):
    symbol_code: str

class ForecastFutureDetails(TypedDict):
    air_temperature_max: Union[float, None]
    air_temperature_min: Union[float, None]
    precipitation_amount: Union[float, None]

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

class CompleteForecast(TypedDict):
    type: str
    geometry: ForecastGeometry
    properties: ForecastProperties


"""class CompleteForecast:
    def __init__(self, data: dict) -> None:
        self.type: str = data["type"]
        self.geometry = ForecastGeometry(data["geometry"]["type"], data["geometry"]["coordinates"])
        self.properties = ForecastProperties(data["properties"])
        
class ForecastGeometry:
    def __init__(self, type: str, coordinates: list[int]) -> None:
        self.type = type
        self.coordinates = coordinates


class ForecastProperties:
    def __init__(self, props):
        self.meta = ForecastMeta(props["meta"])

class ForecastMeta:
    def __init__(self, meta):
        self.updated_at = meta["updated_at"]
        self.units = meta["units"]
        print(meta)"""