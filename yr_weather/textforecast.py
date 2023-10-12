"""A module with classes for the Textforecast API."""

from typing import Literal, List
from xml.parsers.expat import ExpatError
import xmltodict
from .client import APIClient

from .data.textforecast import TextForecasts, TextForecastArea
from .api_types.textforecast import APITextArea


class Textforecast(APIClient):
    """A client for interacting with the Yr Textforecast API."""

    def __init__(self, headers=None, use_cache=True) -> None:
        super().__init__(headers, use_cache)

        self._base_url += "textforecast/2.0/"

    def get_forecasts(
        self,
        forecast: Literal[
            "landoverview", "coast_en", "coast_no", "sea_en", "sea_no", "sea_wmo"
        ],
    ) -> TextForecasts:
        """Get text forcasts for a selected area.

        Parameters
        ----------
        forecast: Literal["landoverview", "coast_en", "coast_no", "sea_en", "sea_no", "sea_wmo"]
            One of the possible forecast areas.

        Returns
        -------
        :class:`.TextForecasts`
            A class with text forecasts for the selected area defined in the forecast parameter.
        """
        forecast_types = [
            "landoverview",
            "coast_en",
            "coast_no",
            "sea_en",
            "sea_no",
            "sea_wmo",
        ]
        if forecast not in forecast_types:
            raise ValueError(
                f"The 'forecast' argument must be one of the following: {', '.join(forecast_types)}."
            )

        url = self._base_url + f"?forecast={forecast}"

        request = self.session.get(url)

        try:
            parsed = xmltodict.parse(request.text, attr_prefix="", cdata_key="text")
        except ExpatError as exc:
            raise RuntimeError(
                "Parsing XML failed (this could be caused by a bad status code or wrong XML format)."
            ) from exc

        return TextForecasts(parsed["textforecast"], forecast)

    def get_areas(
        self, area_type: Literal["land", "sea", "coast"]
    ) -> List[TextForecastArea]:
        """Get available areas and their polygons.

        Parameters
        ----------
        forecast: Literal["land", "sea", "coast"]
            One of the possible areas.

        Returns
        -------
        list[:class:`TextForecastArea`]
            A list of land, coast or sea areas, their polygons and names.
        """
        area_types = ["land", "sea", "coast"]
        if area_type not in area_types:
            raise ValueError(
                f"The 'area_type' argument must be one of the following: {', '.join(area_types)}."
            )

        url = self._base_url + f"areas?type={area_type}"

        request = self.session.get(url)

        try:
            parsed = xmltodict.parse(request.text, attr_prefix="", cdata_key="text")
        except ExpatError as exc:
            raise RuntimeError(
                "Parsing XML failed (this could be caused by a bad status code or wrong XML format)."
            ) from exc

        raw_areas: List[APITextArea] = parsed["areas"]["area"]

        areas: List[TextForecastArea] = []
        for area in raw_areas:
            areas.append(
                TextForecastArea(
                    id=area["id"], name=area["areaDesc"], polygon=area["polygon"]
                )
            )

        return areas
