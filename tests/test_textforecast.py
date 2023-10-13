"""Tests for yr_weather.textforecast"""

import pytest
import requests
from yr_weather.textforecast import Textforecast

from yr_weather.data.textforecast import (
    TextForecasts,
    TextForecastTime,
    TextForecastLocations,
    ForecastLocation,
    TextForecastArea,
)

HEADERS = {"User-Agent": "testing/latest https://github.com/ZeroWave022/yr-weather"}


def api_available():
    """Test if the API is available."""
    status_req = requests.get(
        "https://api.met.no/weatherapi/textforecast/2.0/healthz",
        timeout=30,
    )

    return status_req.ok


@pytest.fixture(name="client", scope="module")
def fixture_client():
    """The Textforecast client"""
    return Textforecast(headers=HEADERS, use_cache=False)


@pytest.mark.skipif(
    not api_available(),
    reason="Testing cannot continue: MET Textforecast API is not responding.",
)
class TestTextforecast:
    """Test yr_weather.Textforecast"""

    @pytest.fixture
    def forecast_types(self):
        return [
            "landoverview",
            "coast_en",
            "coast_no",
            "sea_en",
            "sea_no",
            "sea_wmo",
        ]

    def test_params(self, client: Textforecast):
        """Test that correct parameters are required when getting a forecast."""

        with pytest.raises(
            ValueError, match="The 'forecast' argument must be one of the following"
        ):
            client.get_forecasts("test")

    def test_forecasts_no_error(self, client: Textforecast, forecast_types):
        """Test that all forecast types work correctly"""

        for forecast_type in forecast_types:
            assert isinstance(client.get_forecasts(forecast_type), TextForecasts)

    def test_forecast(self, client: Textforecast):
        """Test TextForecasts class instance from .get_forecasts()"""
        forecast = client.get_forecasts("landoverview")
        now = forecast.now()

        assert isinstance(now, TextForecastTime)
        assert isinstance(now.from_time, str)
        assert isinstance(now.to_time, str)
        assert isinstance(now.locations, TextForecastLocations)

        locations = now.locations.names

        assert isinstance(now.locations.get(locations[0]), ForecastLocation)

    def test_areas(self, client: Textforecast):
        """Test .get_areas()"""
        areas = client.get_areas("land")

        for area in areas:
            assert isinstance(area, TextForecastArea)
