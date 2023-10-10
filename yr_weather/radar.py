"""A module with classes for the Radar API."""

from typing import Optional, get_args
from datetime import datetime
import requests
from .client import APIClient

from .data.radar import (
    RadarOptions,
    RadarContentAvailable,
    RadarGlobalStatus,
    RadarStatus,
)
from .api_types.radar import (
    RadarArea,
    RadarType,
    RadarContentType,
)


class Radar(APIClient):
    """A client for interacting with the MET Radar API."""

    def __init__(self, headers=None, use_cache=True) -> None:
        super().__init__(headers, use_cache)

        self._base_url += "radar/2.0/"

    def get_radar(
        self,
        area: str,
        radar_type: str,
        content: RadarContentType = "image",
        time: Optional[str] = None,
    ) -> requests.Response:
        """Get a radar image (png) or animation (gif).

        For more information about what arguments are valid, please see:
        https://api.met.no/weatherapi/radar/2.0/documentation

        Parameters
        ----------
        area: :data:`.RadarArea`
            A string of one the of the possible values for area, based on valid MET Radar API literals.
        radar_type: :data:`.RadarType`
            A string of one of the possible values for type, based on valid MET Radar API literals.
        content: :data:`.RadarContentType`
            Optional: Either the string "image" or "animation", based on the desired result from the API. Default is ``"image"``.
        time: Optional[:class:`str`]
            An optional string containing the time when the image was taken, provided in ISO 8601 format. Default is None.

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

        if area not in area_args:
            raise ValueError(
                f"The 'area' argument must be one of the possible RadarAreas: {area_args}"
            )

        if radar_type not in type_args:
            raise ValueError(
                f"The 'radar_type' argument must be one of the possible RadarTypes: {type_args}"
            )

        if content not in ["image", "animation"]:
            raise ValueError("The 'content' argument must be 'image' or 'animation'.")

        url = self._base_url + f"?area={area}&type={radar_type}&content={content}"

        if time:
            try:
                datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
                url += f"&time={time}"
            except Exception as exc:
                raise ValueError(
                    "The 'time' argument must be of type 'str' and ISO 8601 format."
                ) from exc

        return self.session.get(url)

    def get_available_radars(self) -> RadarOptions:
        """Get available types of radars.

        This function retrieves all types of radars, as well as which areas they are available in.
        The dataclass returned also includes available types of content (image or animation).

        Returns
        -------
        :class:`.RadarOptions`
            A dataclass with available radars and additional info.
        """
        url = self._base_url + "radaroptions"

        request = self.session.get(url)

        options: dict = request.json()

        # Rename to allowed attribute name for the dataclass which will be instantiated
        options["five_level_reflectivity"] = options["5level_reflectivity"]
        del options["5level_reflectivity"]

        # Convert all radar option dicts to dataclasses
        for option, value in options.items():
            options[option] = RadarContentAvailable(
                areas=value["area"], content=value["content"]
            )

        return RadarOptions(**options)

    def get_all_statuses(self) -> RadarGlobalStatus:
        """Get the operational status of all radars.

        Returns
        -------
        :class:`.RadarStatus`
            A dataclass with statuses of radars.
        """
        url = self._base_url + "status"

        request = self.session.get(url)

        status: dict = request.json()

        radars = []

        # This renames properties to match python style
        # Also converts from dicts to AreaStatus dataclasses
        for radar in status["Radars"]:
            radars.append(
                RadarStatus(
                    area=radar["Area"],
                    due_date=radar["DueDate"],
                    fault_code=radar["FaultCode"],
                    last=radar["Last"],
                    products=radar["Products"],
                    sitename=radar["Sitename"],
                    stability=radar["Stability"],
                )
            )

        return RadarGlobalStatus(last_update=status["Last_update"], radars=radars)

    def get_status(
        self, area: Optional[str] = None, sitename: Optional[str] = None
    ) -> Optional[RadarStatus]:
        """Get the operational status of a single radar.

        Either ``area`` or ``sitename`` must be used to find a radar.

        Parameters
        ----------
        area: Optional[:class:`str`]
            The name of the area of the radar to search for.
        sitename: Optional[:class:`str`]
            The sitename of the radar to search for.

        Returns
        -------
        Optional[:class:`.RadarStatus`]
            A dataclass with radar status. Can be None if no radar is found.
        """
        if not area and not sitename:
            raise ValueError("Neither an area or a sitename was specified.")

        url = self._base_url + "status"

        request = self.session.get(url)

        status: dict = request.json()

        if area:
            found = list(filter(lambda r: r["Area"] == area, status["Radars"]))
        else:
            found = list(filter(lambda r: r["Sitename"] == sitename, status["Radars"]))

        if len(found) == 0:
            return None

        radar = found[0]

        return RadarStatus(
            area=radar["Area"],
            due_date=radar["DueDate"],
            fault_code=radar["FaultCode"],
            last=radar["Last"],
            products=radar["Products"],
            sitename=radar["Sitename"],
            stability=radar["Stability"],
        )
