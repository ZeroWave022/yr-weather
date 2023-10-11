"""Tests for yr_weather.locationforecast"""

from datetime import datetime, timedelta
import pytest
import requests

from yr_weather import Locationforecast
from yr_weather.data.locationforecast import (
    Forecast,
    ForecastTime,
    ForecastTimeDetails,
    ForecastFuture,
    ForecastFutureDetails,
    ForecastFutureSummary,
    ForecastGeometry,
    ForecastUnits,
)

HEADERS = {"User-Agent": "testing/latest https://github.com/ZeroWave022/yr-weather"}


def api_available():
    """Checks if the API is available."""
    status_req = requests.get(
        "https://api.met.no/weatherapi/locationforecast/2.0/status",
        headers=HEADERS,
        timeout=30,
    )

    return status_req.ok


@pytest.fixture(name="client", scope="module")
def fixture_client():
    """The Locationforecast client"""
    return Locationforecast(HEADERS)


@pytest.fixture(name="forecast", scope="module")
def fixture_forecast(client: Locationforecast):
    """An example locationforecast"""
    return client.get_forecast(59.91, 10.75)


@pytest.mark.skipif(
    not api_available(),
    reason="Testing cannot continue: MET Locationforecast API is not responding.",
)
class TestLocationforecast:
    """Test yr_weather.Locationforecast"""

    def test_headers(self):
        """Test that headers are required"""
        with pytest.raises(ValueError, match="A custom 'User-Agent' is required"):
            Locationforecast({})

    def test_forecast(self, forecast: Forecast):
        """Test initial Forecast data"""
        assert isinstance(forecast, Forecast)
        assert isinstance(forecast.type, str)
        assert isinstance(forecast.geometry, ForecastGeometry)
        assert isinstance(forecast.updated_at, str)
        assert isinstance(forecast.units, ForecastUnits)

    def test_forecast_now(self, forecast: Forecast):
        """Test Forecast.now()"""
        now = forecast.now()

        assert isinstance(now, ForecastTime)
        assert isinstance(now.details, ForecastTimeDetails)
        assert isinstance(now.next_hour, ForecastFuture)
        assert isinstance(now.next_6_hours, ForecastFuture)
        assert isinstance(now.next_12_hours, ForecastFuture)

    def test_forecast_get_time(self, forecast: Forecast):
        """Test Forecast.get_forecast_time()"""
        datetime_in_3_hrs = datetime.now() + timedelta(hours=3)
        in_3_hrs = forecast.get_forecast_time(datetime_in_3_hrs)

        assert isinstance(in_3_hrs, ForecastTime)
        assert isinstance(in_3_hrs.details, ForecastTimeDetails)
        assert isinstance(in_3_hrs.next_hour, ForecastFuture)
        assert isinstance(in_3_hrs.next_6_hours, ForecastFuture)
        assert isinstance(in_3_hrs.next_12_hours, ForecastFuture)

    def test_future_forecast(self, forecast: Forecast):
        """Test ForecastFuture data"""
        now = forecast.now()

        assert isinstance(now.next_hour.details, ForecastFutureDetails)
        assert isinstance(now.next_hour.summary, ForecastFutureSummary)

        assert isinstance(now.next_6_hours.details, ForecastFutureDetails)
        assert isinstance(now.next_6_hours.summary, ForecastFutureSummary)

        assert isinstance(now.next_12_hours.details, ForecastFutureDetails)
        assert isinstance(now.next_12_hours.summary, ForecastFutureSummary)

    def test_air_temperature(self, client: Locationforecast):
        """Test air temperature function"""
        air_temp_1 = client.get_air_temperature(59.91, 10.75)
        air_temp_2 = client.get_air_temperature(59.91, 10.75, 100)

        assert isinstance(air_temp_1, float)
        assert isinstance(air_temp_2, float)

    def test_instant_data(self, client: Locationforecast):
        """Test instant data function"""
        data = client.get_instant_data(59.91, 10.75)
        data_2 = client.get_instant_data(59.91, 10.75, 100)

        assert isinstance(data, ForecastTimeDetails)
        assert isinstance(data_2, ForecastTimeDetails)
