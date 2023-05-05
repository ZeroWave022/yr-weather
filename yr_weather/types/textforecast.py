"""Types for text forecasts."""

from typing import TypedDict, Union, List


class Meta(TypedDict):
    """Text forecast metadata"""

    licenseurl: str


class ForecastArea(TypedDict):
    """A text forecast for an area"""

    name: str
    id: str
    text: str


class ForecastType(TypedDict):
    """The type of text forecast"""

    name: str
    location: List[ForecastArea]


# Use alternative syntax to allow 'from' to be typed.
TimedForecast = TypedDict(
    "TimedForecast",
    {"from": str, "to": str, "forecasttype": Union[ForecastType, List[ForecastType]]},
)


class TextForecasts(TypedDict):
    """Text forecasts for areas"""

    meta: Meta
    time: List[TimedForecast]


class TextArea(TypedDict):
    """An area with a text forecast"""

    id: str
    areaDesc: str
    polygon: str


class TextAreas(TypedDict):
    """Areas with text forecasts"""

    area: List[TextArea]
