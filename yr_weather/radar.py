import requests
from requests_cache import CachedSession
from typing import Optional, Literal, Union, get_args
from .base import BaseClient
from datetime import datetime

from .types.radar import RadarOptions, RadarStatus, RadarArea, RadarType, RadarContentType

class Radar(BaseClient):
    """A client for interacting with the Yr Radar API."""
    def __init__(self, headers: Optional[dict] = {}, use_cache: Optional[bool] = True) -> None:
        super().__init__(headers, use_cache)

        self._baseURL += "radar/2.0/"

    def get_radar(self, area: str, radar_type: str, content: Optional[RadarContentType] = "image", time: Optional[str] = None) -> requests.Response:
        """Get a radar image (png) or animation (gif).

        For more information about what arguments are valid, please see:
        https://api.met.no/weatherapi/radar/2.0/documentation

        Parameters
        ----------
        area: :data:`.RadarArea`
            A string of one the of the possible values for area, based on valid Radar Yr API literals.
        radar_type: :data:`.RadarType`
            A string of one of the possible values for type, based on valid Radar Yr API literals.
        content: Optional[:data:`.RadarContentType`]
            Either the string "image" or "animation", based on the desired result from the API.
        time: Optional[:class:`str`]
            An optional string containing the time when the image was taken, provided in ISO 8601 format.
        
        Returns
        -------
        :class:`requests.Response`
            A Response class, enabling for further saving or managing of the data received from the open stream.

        Examples
        --------

        Example 1: Basic usage:

        .. code-block:: python

            import yr_weather

            radar = yr_weather.Radar()

            result = radar.get_radar("central_norway", "5level_reflectivity", "image")

            with open("image.png", "wb") as f:
                for chunk in result:
                    f.write(chunk)

        Example 2. Getting a radar image from a few hours back:

        .. code-block:: python

            import yr_weather
            from datetime import datetime

            radar = yr_weather.Radar()

            # Replace with your time
            time_now = datetime(2023, 1, 20, 12, 00, 00)
            time_str = time_now.isoformat(timespec="seconds") + "Z"

            result = radar.get_radar("central_norway", "5level_reflectivity", "image", time_str)

            if result.status_code != 404:
                with open("image.png", "wb") as f:
                    for chunk in result:
                        f.write(chunk)
            else:
                print("Couldn't get this radar image/animation!")
        """
        area_args = list(get_args(RadarArea))
        type_args = list(get_args(RadarType))
        
        if (area not in area_args):
            raise ValueError(f"The 'area' argument must be one of the possible RadarAreas: {area_args}")
        
        if (radar_type not in type_args):
            raise ValueError(f"The 'radar_type' argument must be one of the possible RadarTypes: {type_args}")
        
        if (content not in ["image", "animation"]):
            raise ValueError("The 'content' argument must be 'image' or 'animation'.")

        URL = self._baseURL + f"?area={area}&type={radar_type}&content={content}"

        if time:
            try:
                datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
                URL += f"&time={time}"
            except:
                raise ValueError("The 'time' argument must be of type 'str' and ISO 8601 format.")
        
        return self.session.get(URL, stream=True)
    
    def get_available_radars(self) -> RadarOptions:
        """Get a dict of available typed of radars.

        This function retrieves all types of radars, as well as which areas they are available in.
        The dict also includes available types of content (image or animation).

        Returns
        -------
        :class:`.RadarOptions`
            A TypedDict with available radars and additional info.
        """
        URL = self._baseURL + "radaroptions"

        request = self.session.get(URL)

        options: RadarOptions = request.json()

        return options

    def get_status(self) -> RadarStatus:
        """Get the operational status of all radars.
        
        Returns
        -------
        :class:`.RadarStatus`
            A TypedDict with statuses of radars.
        """
        URL = self._baseURL + "status"

        request = self.session.get(URL)

        status: RadarStatus = request.json()

        return status
