import requests
from typing import Optional, get_args
from .base import BaseClient
from datetime import datetime

from .types.sunrise import SunriseData, DetailLiteral


class Sunrise(BaseClient):
    """A client for interacting with the Yr Sunrise API."""

    def __init__(self, headers: dict = {}, use_cache: bool = True) -> None:
        super().__init__(headers, use_cache)

        self._baseURL += "sunrise/2.0/"

    def get_sunrise(
        self,
        date: str,
        lat: float,
        lon: float,
        offset: str,
        days_forward: Optional[int] = None,
        height: Optional[float] = None,
    ) -> SunriseData:
        """Get sunrise data.

        For more information, please see: https://api.met.no/weatherapi/sunrise/2.0/documentation

        Parameters
        ----------
        date: :class:`str`
            A date formatted in ISO 8601 format, like so: `YYYY-MM-DD`.
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        offset: :class:`str`
            The timezone offset, given in the following format: `+HH:MM` or `-HH:MM`.
        days_forward: Optional[:class:`int`]
            Optional: The number of future days which should be included. Default is :class:`None`.
        height: Optional[:class:`float` | :class:`int`]
            Optional: The altitude above the ellipsoid in kilometers (km). Default is :class:`None`.

        Returns
        -------
        :class:`.SunriseData`
            A typed dict containing sunrise data.
        """
        # Ensure correct variable types.
        if not isinstance(date, str):
            raise ValueError("Type of 'data' must be str.")

        if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
            raise ValueError("Type of 'lat' and 'lon' must be int or float.")

        if not isinstance(offset, str):
            raise ValueError("Type of 'offset' must be str.")

        # Check if the date provided is valid.
        try:
            splitted = [int(num) for num in date.split("-")]
            datetime(splitted[0], splitted[1], splitted[2])
        except:
            raise ValueError("The 'date' parameter must be a valid date.")

        # Ensure offset is valid.
        if not self._ensure_valid_offset(offset):
            raise ValueError("The 'offset' parameter is not a valid timezone offset.")

        # Set up URL and add optional parameters if present and valid.
        URL = self._baseURL + f".json?date={date}&lat={lat}&lon={lon}&offset={offset}"

        if isinstance(days_forward, int):
            URL += f"&days={days_forward}"
        elif days_forward is not None:
            raise ValueError("Type of 'days_forward' must be int.")

        if isinstance(height, (int, float)):
            URL += f"&height={height}"
        elif height is not None:
            raise ValueError("Type of 'height' must be int or float.")

        request = self.session.get(URL)

        if not request.ok:
            raise requests.HTTPError(
                f"Unsuccessful response received: {request.status_code} {request.reason}."
            )

        sunrise_data: SunriseData = request.json()

        return sunrise_data

    def get_detail(
        self,
        detail: DetailLiteral,
        date: str,
        lat: float,
        lon: float,
        offset: str,
        height: Optional[float] = None,
    ) -> dict:
        """Get data about the specified event or detail.

        This will get the newest sunrise data, and return the event/detail dict, if available.
        For more information, please see: https://api.met.no/weatherapi/sunrise/2.0/documentation

        Parameters
        ----------
        detail: :data:`.DetailLiteral`
            The detail/event to get data for. See :data:`.DetailLiteral` for valid values.
        date: :class:`str`
            A date formatted in ISO 8601 format, like so: `YYYY-MM-DD`.
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        offset: :class:`str`
            The timezone offset, given in the following format: `+/-HH:MM`.
        height: Optional[:class:`float` | :class:`int`]
            The altitude above the ellipsoid in kilometers (km).

        Returns
        -------
        :class:`dict`
            Details about the chosen event or detail.
        """
        literals = get_args(DetailLiteral)

        if detail not in literals:
            raise ValueError(
                f"The 'detail' parameter must be one of the possible DetailLiterals: {literals}"
            )

        data = self.get_sunrise(date, lat, lon, offset, height=height)

        try:
            return data["location"]["time"][0][detail]
        except:
            raise Exception(
                "This detail is not available for this combination of date and location."
            )

    def _ensure_valid_offset(self, offset: str) -> bool:
        """Ensures that a valid offset is given.

        Returns a bool, indicating whether the offset is valid.
        """
        if not offset.startswith(("+", "-")):
            return False

        time = offset.replace("+", "").replace("-", "")

        splitted = time.split(":")

        if len(splitted) != 2:
            return False

        for i in splitted:
            if len(i) != 2:
                return False
            try:
                int(i)
            except:
                return False

        if int(splitted[0]) < 10 and not splitted[0].startswith("0"):
            return False

        return True
