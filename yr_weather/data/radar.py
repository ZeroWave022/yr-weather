"""Classes storing data used by yr_weather.radar"""

from typing import Optional, Literal, List
from dataclasses import dataclass

from yr_weather.api_types.radar import RadarArea, RadarContentType


@dataclass
class RadarContentAvailable:
    """A dataclass storing available areas and content types for a radar type."""

    areas: List[RadarArea]
    content: RadarContentType


@dataclass
class RadarOptions:
    """A dataclass storing available options for various radar types."""

    five_level_reflectivity: RadarContentAvailable
    accumulated_01h: RadarContentAvailable
    accumulated_02h: RadarContentAvailable
    accumulated_03h: RadarContentAvailable
    accumulated_04h: RadarContentAvailable
    accumulated_05h: RadarContentAvailable
    accumulated_06h: RadarContentAvailable
    accumulated_07h: RadarContentAvailable
    accumulated_08h: RadarContentAvailable
    accumulated_09h: RadarContentAvailable
    accumulated_10h: RadarContentAvailable
    accumulated_11h: RadarContentAvailable
    accumulated_12h: RadarContentAvailable
    accumulated_13h: RadarContentAvailable
    accumulated_14h: RadarContentAvailable
    accumulated_15h: RadarContentAvailable
    accumulated_16h: RadarContentAvailable
    accumulated_17h: RadarContentAvailable
    accumulated_18h: RadarContentAvailable
    accumulated_19h: RadarContentAvailable
    accumulated_20h: RadarContentAvailable
    accumulated_21h: RadarContentAvailable
    accumulated_22h: RadarContentAvailable
    accumulated_23h: RadarContentAvailable
    accumulated_24h: RadarContentAvailable
    fir_preciptype: RadarContentAvailable
    lx_reflectivity: RadarContentAvailable
    preciptype: RadarContentAvailable
    reflectivity: RadarContentAvailable


@dataclass
class RadarStatus:
    """A dataclass storing a radar status."""

    area: str
    due_date: Optional[str]
    fault_code: Optional[Literal["PS", "VP", "CO", "TE"]]
    last: str
    products: List[RadarArea]
    sitename: str
    stability: str


@dataclass
class RadarGlobalStatus:
    """A dataclass storing statuses for all radars."""

    last_update: str
    radars: List[RadarStatus]
