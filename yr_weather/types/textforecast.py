from typing import TypedDict, Union, List


class Meta(TypedDict):
    licenseurl: str


class ForecastArea(TypedDict):
    name: str
    id: str
    text: str


class ForecastType(TypedDict):
    name: str
    location: List[ForecastArea]


# Use alternative syntax to allow 'from' to be typed.
TimedForecast = TypedDict(
    "TimedForecast",
    {"from": str, "to": str, "forecasttype": Union[ForecastType, List[ForecastType]]},
)


class TextForecasts(TypedDict):
    meta: Meta
    time: List[TimedForecast]


class TextArea(TypedDict):
    id: str
    areaDesc: str
    polygon: str


class TextAreas(TypedDict):
    area: List[TextArea]
