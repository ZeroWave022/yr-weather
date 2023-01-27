from typing import Literal, TypedDict, List, Optional

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
    "xband"
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
    "reflectivity"
]

class AvailableAreas(TypedDict):
    area: List[RadarArea]
    content: RadarContentType

# Use alternative syntax to allow for properties starting with decimal.
RadarOptions = TypedDict("RadarOptions", {
    "5level_reflectivity": AvailableAreas,
    "accumulated_01h": AvailableAreas,
    "accumulated_02h": AvailableAreas,
    "accumulated_03h": AvailableAreas,
    "accumulated_04h": AvailableAreas,
    "accumulated_05h": AvailableAreas,
    "accumulated_06h": AvailableAreas,
    "accumulated_07h": AvailableAreas,
    "accumulated_08h": AvailableAreas,
    "accumulated_09h": AvailableAreas,
    "accumulated_10h": AvailableAreas,
    "accumulated_11h": AvailableAreas,
    "accumulated_12h": AvailableAreas,
    "accumulated_13h": AvailableAreas,
    "accumulated_14h": AvailableAreas,
    "accumulated_15h": AvailableAreas,
    "accumulated_16h": AvailableAreas,
    "accumulated_17h": AvailableAreas,
    "accumulated_18h": AvailableAreas,
    "accumulated_19h": AvailableAreas,
    "accumulated_20h": AvailableAreas,
    "accumulated_21h": AvailableAreas,
    "accumulated_22h": AvailableAreas,
    "accumulated_23h": AvailableAreas,
    "accumulated_24h": AvailableAreas,
    "fir_preciptype": AvailableAreas,
    "lx_reflectivity": AvailableAreas,
    "preciptype": AvailableAreas,
    "reflectivity": AvailableAreas,
})

class AreaStatus(TypedDict):
    Area: str
    DueDate: Optional[str]
    FaultCode: Optional[Literal["PS", "VP", "CO", "TE"]]
    Last: str
    Products: List[RadarArea]
    Sitename: str
    Stability: str

class RadarStatus(TypedDict):
    Last_update: str
    Radars: List[AreaStatus]
