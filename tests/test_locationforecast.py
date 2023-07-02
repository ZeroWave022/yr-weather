"""Tests for yr_weather.locationforecast"""

from datetime import datetime, timedelta
import pytest
import requests

from yr_weather import Locationforecast
from yr_weather.locationforecast import (
    Forecast,
    ForecastTime,
    ForecastTimeDetails,
    ForecastGeometry,
    ForecastUnits,
)


@pytest.fixture(scope="module")
def client():
    headers = {"User-Agent": "testing/latest https://github.com/ZeroWave022/yr-weather"}
    return Locationforecast(headers)


@pytest.fixture(scope="module")
def api_available(client):
    """Test if the API is available."""
    status_req = requests.get(
        "https://api.met.no/weatherapi/locationforecast/2.0/status",
        headers=client._global_headers,
        timeout=30,
    )

    # API testing can't continue if the API isn't functional
    if not status_req.ok:
        return False

    return True


class TestLocationforecast:
    def _raise_if_api_unavailable(self, api_available):
        if not api_available:
            raise RuntimeError(
                "MET Locationforecast API is not responding. Testing cannot continue."
            )

    def test_headers(self):
        """Test that headers are required."""
        with pytest.raises(ValueError, match="A custom 'User-Agent' is required"):
            Locationforecast({})

    def test_forecast(self, api_available, client):
        """Test various Locationforecast methods and classes."""
        self._raise_if_api_unavailable(api_available)

        forecast = client.get_forecast(59.91, 10.75)

        assert isinstance(forecast, Forecast)
        assert isinstance(forecast.type, str)
        assert isinstance(forecast.geometry, ForecastGeometry)
        assert isinstance(forecast.updated_at, str)
        assert isinstance(forecast.units, ForecastUnits)

        now = forecast.now()

        assert isinstance(now, ForecastTime)

        datetime_in_3_hrs = datetime.now() + timedelta(hours=3)

        forecast_in_3_hrs = forecast.get_forecast_time(datetime_in_3_hrs)

        assert isinstance(forecast_in_3_hrs, ForecastTime)

    def test_air_temperature(self, api_available, client):
        """Test air temperature function."""
        self._raise_if_api_unavailable(api_available)

        air_temp_1 = client.get_air_temperature(59.91, 10.75)
        air_temp_2 = client.get_air_temperature(59.91, 10.75, 100)

        assert isinstance(air_temp_1, float)
        assert isinstance(air_temp_2, float)

    def test_instant_data(self, api_available, client):
        """Test instant data function."""
        self._raise_if_api_unavailable(api_available)

        data = client.get_instant_data(59.91, 10.75)
        data_2 = client.get_instant_data(59.91, 10.75, 100)

        assert isinstance(data, ForecastTimeDetails)
        assert isinstance(data_2, ForecastTimeDetails)
