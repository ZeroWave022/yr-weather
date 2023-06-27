"""A module with classes for the Textforecast API."""

from typing import Literal, Union
import warnings
from xml.parsers.expat import ExpatError
import xmltodict
from .client import APIClient

from .types.textforecast import TextForecasts, TextAreas


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
    ) -> Union[TextForecasts, str]:
        """Get text forcasts for a selected area.

        Parameters
        ----------
        forecast: Literal["landoverview", "coast_en", "coast_no", "sea_en", "sea_no", "sea_wmo"]
            One of the possible forecast areas.

        Returns
        -------
        TextForecasts | str
            A typed dict with text forecasts for the selected area, defined in the forecast parameter.
            If XML conversion fails, the response text for the request is returned instead.
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
        except ExpatError:
            warnings.warn(
                "Parsing XML failed (this could be caused by a non-200 status code).\nFalling back to response text."
            )
            return request.text

        forecasts: TextForecasts = parsed["textforecast"]
        return forecasts

    def get_areas(
        self, area_type: Literal["land", "sea", "coast"]
    ) -> Union[TextAreas, str]:
        """Get available areas and their polygons.

        Parameters
        ----------
        forecast: Literal["land", "sea", "coast"]
            One of the possible areas.

        Returns
        -------
        TextAreas | str
            A typed dict with land, sea or coast areas, their polygons and names.
            If XML conversion fails, the response text for the request is returned instead.
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
        except ExpatError:
            warnings.warn(
                "Parsing XML failed (this could be caused by a non-200 status code).\nFalling back to response text."
            )
            return request.text

        areas: TextAreas = parsed["areas"]
        return areas
