import requests
from requests_cache import CachedSession
from typing import Optional, Literal, Union, get_args
from .base import BaseClient
from datetime import datetime
import xmltodict

from .textforecasttypes import TextForecasts

class Textforecast(BaseClient):
    """A client for interacting with the Yr Textforecast API."""
    def __init__(self, headers: Optional[dict] = {}, use_cache: Optional[bool] = True) -> TextForecasts:
        super().__init__(headers, use_cache)

    def get_forecasts(self, forecast: Literal["landoverview", "coast_en", "coast_no", "sea_en", "sea_no", "sea_wmo"]):
        forecast_types = ["landoverview", "coast_en", "coast_no", "sea_en", "sea_no", "sea_wmo"]
        if forecast not in forecast_types:
            raise ValueError(f"The 'forecast' argument must be one of the following: {', '.join(forecast_types)}.")
        
        URL = self._baseURL + f"textforecast/2.0/?forecast={forecast}"
        
        request = self.session.get(URL)

        forecasts: TextForecasts = xmltodict.parse(request.text, attr_prefix="", cdata_key="text")["textforecast"]

        return forecasts
