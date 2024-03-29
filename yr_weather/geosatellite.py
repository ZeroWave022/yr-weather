"""A module with classes for the MET Geosatellite API."""

from typing import Optional, Literal, get_args
import requests
from .client import APIClient

from .api_types.geosatellite import SatArea


class Geosatellite(APIClient):
    """A client for interacting with the MET Geosatellite API."""

    def __init__(self, headers=None, use_cache=True) -> None:
        super().__init__(headers, use_cache)

        self._base_url += "geosatellite/1.4/"

    def get_image(
        self,
        area: SatArea = "europe",
        img_type: Literal["infrared", "visible"] = "infrared",
        time: Optional[str] = None,
        size: Literal["normal", "small"] = "normal",
    ) -> requests.Response:
        """Get a geosatellite image.

        Parameters
        ----------
        area: :data:`.SatArea`
            Optional: The area for the image. Must be a valid :data:`.SatArea`. Default is ``"europe"``.
        img_type: Literal["infrared", "visible"]
            Optional: The image type. Either "infrared" or "visible". Default is ``"infrared"``.
        time: :class:`str`
            Optional: The time formatted as described in MET.no's documentation. Default is :class:`None`.
        size: Literal["normal, small"]
            Optional: Image resolution. Either "normal" or "small" for thumbnails. Default is ``"normal"``.

        Returns
        -------
        :class:`requests.Response`
            A Response class enabling saving or further management of the data received.
        """
        area_args = list(get_args(SatArea))
        type_args = ["infrared", "visible"]
        size_args = ["normal", "small"]

        if area not in area_args:
            raise ValueError(
                f"The 'area' parameter must be one of the possible SatAreas: {area_args}"
            )

        if img_type not in type_args:
            raise ValueError(
                f"The 'img_type' parameter must be one of the possible image types: {type_args}"
            )

        if size not in size_args:
            raise ValueError(
                f"The 'size' parameter must be one of the possible sizes: {size_args}"
            )

        url = self._base_url + f"?area={area}&type={img_type}&size={size}"

        if time:
            url += f"&time={time}"

        request = requests.get(url, stream=True, timeout=60)

        if not request.ok:
            raise requests.HTTPError(
                f"Unsuccessful response received: {request.status_code} {request.reason}.",
                request=None,
                response=request,
            )

        return request
