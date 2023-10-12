"""MET API types for text forecasts."""

from typing import TypedDict, Union, List


class APIMeta(TypedDict):
    """Text forecast metadata"""

    licenseurl: str


class APIForecastArea(TypedDict):
    """A text forecast for an area"""

    name: str
    id: str
    text: str


class APIForecastWrapper(TypedDict):
    """The wrapper for a text forecast location"""

    name: str
    location: List[APIForecastArea]


# Use alternative syntax to allow the 'from' key to be typed.
APITimedForecast = TypedDict(
    "APITimedForecast",
    {
        "from": str,
        "to": str,
        "forecasttype": Union[APIForecastWrapper, List[APIForecastWrapper]],
    },
)


class APITextForecasts(TypedDict):
    """Text forecasts for areas"""

    meta: APIMeta
    time: List[APITimedForecast]


class APITextArea(TypedDict):
    """An area with a text forecast"""

    id: str
    areaDesc: str
    polygon: str


class APITextAreas(TypedDict):
    """Areas with text forecasts"""

    area: List[APITextArea]
