"""Types for radar data."""

from typing import Literal

RadarArea = Literal[
    "central_norway",
    "eastern_norway",
    "finnmark",
    "nordic",
    "nordland",
    "northern_nordland",
    "northwestern_norway",
    "norway",
    "southeastern_norway",
    "southern_nordland",
    "southern_norway",
    "southwestern_norway",
    "troms",
    "western_norway",
    "xband",
]

RadarContentType = Literal["image", "animation"]

RadarType = Literal[
    "5level_reflectivity",
    "accumulated_01h",
    "accumulated_02h",
    "accumulated_03h",
    "accumulated_04h",
    "accumulated_05h",
    "accumulated_06h",
    "accumulated_07h",
    "accumulated_08h",
    "accumulated_09h",
    "accumulated_10h",
    "accumulated_11h",
    "accumulated_12h",
    "accumulated_13h",
    "accumulated_14h",
    "accumulated_15h",
    "accumulated_16h",
    "accumulated_17h",
    "accumulated_18h",
    "accumulated_19h",
    "accumulated_20h",
    "accumulated_21h",
    "accumulated_22h",
    "accumulated_23h",
    "accumulated_24h",
    "fir_preciptype",
    "lx_reflectivity",
    "preciptype",
    "reflectivity",
]
