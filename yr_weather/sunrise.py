"""A module with classes for the Sunrise API."""

from datetime import datetime
from typing import Optional, Union
import requests
from .client import APIClient

from .data.sunrise import SunEvents, MoonEvents
from .api_types.sunrise import APISunData, APIMoonData


class Sunrise(APIClient):
    """A client for interacting with the Yr Sunrise API."""

    def __init__(self, headers, use_cache=True) -> None:
        super().__init__(headers, use_cache)

        self._base_url += "sunrise/3.0/"

    def _get_events(self, event_type: str, **kwargs) -> Union[APISunData, APIMoonData]:
        date = kwargs.get("date")
        lat = kwargs.get("lat")
        lon = kwargs.get("lon")
        offset = kwargs.get("offset")

        # Ensure correct variable types.
        if not isinstance(date, str):
            raise ValueError("Type of 'date' must be str.")

        if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
            raise ValueError("Type of 'lat' and 'lon' must be int or float.")

        if offset:
            if not isinstance(offset, str):
                raise ValueError("Type of 'offset' must be str.")

            # Ensure offset is valid.
            if not self._ensure_valid_offset(offset):
                raise ValueError(
                    "The 'offset' parameter is not a valid timezone offset."
                )

        # Check if the date provided is valid.
        try:
            splitted = [int(num) for num in date.split("-")]
            datetime(splitted[0], splitted[1], splitted[2])
        except Exception as exc:
            raise ValueError("The 'date' parameter must be a valid date.") from exc

        url = self._base_url + event_type

        request = self.session.get(
            url,
            params={"date": date, "lat": str(lat), "lon": str(lon), "offset": offset},
        )

        if not request.ok:
            raise requests.HTTPError(
                f"Unsuccessful response received: {request.status_code} {request.reason}.",
                request=None,
                response=request,
            )

        return request.json()

    def get_sun_events(
        self,
        date: str,
        lat: float,
        lon: float,
        offset: Optional[str] = None,
    ) -> SunEvents:
        """Get sun events data (sunrise, sunset, etc).

        For more information, please see: https://api.met.no/weatherapi/sunrise/3.0/documentation

        Parameters
        ----------
        date: :class:`str`
            A date formatted in ISO 8601 format, like so: `YYYY-MM-DD`.
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        offset: Optional[:class:`str`]
            The timezone offset, given in the following format: `+HH:MM` or `-HH:MM`.

        Returns
        -------
        :class:`.SunEvents`
        """
        data: APISunData = self._get_events("sun", date=date, lat=lat, lon=lon, offset=offset)  # type: ignore[assignment]

        return SunEvents(data)

    def get_moon_events(
        self,
        date: str,
        lat: float,
        lon: float,
        offset: Optional[str] = None,
    ) -> MoonEvents:
        """Get moon events data (moonrise, moonset, etc).

        For more information, please see: https://api.met.no/weatherapi/sunrise/3.0/documentation

        Parameters
        ----------
        date: :class:`str`
            A date formatted in ISO 8601 format, like so: `YYYY-MM-DD`.
        lat: :class:`float` | :class:`int`
            The latitude of the location.
        lon: :class:`float` | :class:`int`
            The longitude of the location.
        offset: Optional[:class:`str`]
            The timezone offset, given in the following format: `+HH:MM` or `-HH:MM`.

        Returns
        -------
        :class:`.MoonEvents`
        """
        data: APIMoonData = self._get_events("moon", date=date, lat=lat, lon=lon, offset=offset)  # type: ignore[assignment]

        return MoonEvents(data)

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
            except ValueError:
                return False

        if int(splitted[0]) < 10 and not splitted[0].startswith("0"):
            return False

        return True
