"""Classes storing data used by yr_weather.textforecast"""
from typing import Optional, List
from dataclasses import dataclass
from datetime import datetime
import pytz

from yr_weather.api_types.textforecast import (
    APITextForecasts,
    APIForecastArea,
    APIForecastWrapper,
)


@dataclass
class TextForecastArea:
    """A text forecast area from the /areas endpoint"""

    id: str
    name: str  # Renamed from API name (areaDesc)
    polygon: str


@dataclass
class ForecastLocation:
    """A text forecast location"""

    name: str
    id: str
    text: str


class TextForecastLocations:
    """A class storing location data for a text forecast"""

    def __init__(self, locations: List[APIForecastArea]) -> None:
        self._raw = locations

    def get(self, location: str) -> Optional[ForecastLocation]:
        """Get a specific location

        Parameters
        ----------
        location: :class:`str`
            The location to search for

        Returns
        -------
        Optional[:class:`TextForecastArea`]
            The location which has been found, or None if not found.
        """
        found_areas = list(filter(lambda loc: loc["name"] == location, self._raw))

        if len(found_areas) == 0:
            return None

        return ForecastLocation(**found_areas[0])

    @property
    def names(self) -> List[str]:
        """All location names occuring in this TextForecastLocations instance"""
        return [location["name"] for location in self._raw]


class TextForecastTime:
    """A class storing a specific text forecast time data"""

    def __init__(
        self, from_time: str, to_time: str, locations: List[APIForecastArea]
    ) -> None:
        self.from_time = from_time
        self.to_time = to_time
        self.locations = TextForecastLocations(locations)


class TextForecasts:
    """A class storing text forecasts"""

    def __init__(self, data: APITextForecasts, forecast_type: str) -> None:
        self.license_url = data["meta"]["licenseurl"]
        self.times: List[TextForecastTime] = []

        # Data processing for sea forecasts
        if forecast_type in ["sea_no", "sea_en", "sea_wmo"]:
            wrappers: List[APIForecastWrapper] = data["time"]["forecasttype"]  # type: ignore
            locations = []
            for wrapper in wrappers:
                location = wrapper.get("location")
                if isinstance(location, list):
                    locations.extend(location)
                elif location:
                    locations.append(location)

            self.times.append(
                TextForecastTime(
                    from_time=data["time"]["from"],  # type: ignore
                    to_time=data["time"]["to"],  # type: ignore
                    locations=locations,
                )
            )
            return

        # Data processing for landoverview, coast_en and coast_no
        for time in data["time"]:
            # If time["forecasttype"] has wrappers, flatten the structure
            if isinstance(time["forecasttype"], list):
                locations = []
                for wrapper in time["forecasttype"]:
                    locations.extend(wrapper["location"])
            else:
                locations = time["forecasttype"]["location"]

            self.times.append(
                TextForecastTime(
                    from_time=time["from"], to_time=time["to"], locations=locations
                )
            )

    def now(self) -> TextForecastTime:
        """Get the TextForecastTime which applies now"""
        # The times from textforecast seem to be given in Europe/Oslo time
        oslo_timezone = pytz.timezone("Europe/Oslo")
        now = datetime.now(oslo_timezone)

        for time in self.times:
            start = datetime.fromisoformat(time.from_time).replace(tzinfo=oslo_timezone)
            end = datetime.fromisoformat(time.to_time).replace(tzinfo=oslo_timezone)
            if start <= now <= end:
                return time

        return self.times[0]
