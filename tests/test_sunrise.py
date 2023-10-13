"""Tests for yr_weather.sunrise"""

import pytest
import requests
from yr_weather.sunrise import Sunrise

from yr_weather.data.sunrise import (
    SunEvents,
    MoonEvents,
    EventsGeometry,
    TimeWithAzimuth,
    TimeWithElevation,
)

HEADERS = {"User-Agent": "testing/latest https://github.com/ZeroWave022/yr-weather"}


def api_available():
    """Test if the API is available."""
    status_req = requests.get(
        "https://api.met.no/weatherapi/sunrise/3.0/healthz",
        timeout=30,
    )

    return status_req.ok


@pytest.fixture(name="client", scope="module")
def fixture_client():
    """The Sunrise client"""
    return Sunrise(headers=HEADERS, use_cache=False)


@pytest.mark.skipif(
    not api_available(),
    reason="Testing cannot continue: MET Sunrise API is not responding.",
)
class TestSunrise:
    """Test yr_weather.Sunrise"""

    @pytest.fixture
    def valid_offsets(self):
        return ["-10:00", "-08:00", "-00:00", "+00:00", "+08:00", "+10:00"]

    @pytest.fixture
    def invalid_offsets(self):
        return ["123", "test", "01:00", "10:00", "-8:00", "+8:00"]

    def test_params(self, client: Sunrise):
        """Test that correct parameters are required when getting events."""

        with pytest.raises(TypeError, match="Type of 'date' must be str"):
            client.get_sun_events(123, 123, 123)

        with pytest.raises(
            TypeError, match="Type of 'lat' and 'lon' must be int or float"
        ):
            client.get_sun_events("2023-10-12", "test", "test")

        with pytest.raises(
            TypeError,
            match="Type of 'offset' must be str",
        ):
            client.get_sun_events("2023-10-12", 10, 10, 10)

    def test_offset(self, client: Sunrise, valid_offsets, invalid_offsets):
        """Test valid/invalid offset usage"""

        for offset in valid_offsets:
            assert client._ensure_valid_offset(offset)

        for offset in invalid_offsets:
            assert client._ensure_valid_offset(offset) is False

    def test_sun_events(self, client: Sunrise):
        """Test getting sun events"""
        events = client.get_sun_events("2023-10-12", 59.91, 10.75)

        assert isinstance(events, SunEvents)

        # Common event data
        assert isinstance(events.type, str)
        assert isinstance(events.copyright, str)
        assert isinstance(events.license_url, str)
        assert isinstance(events.geometry, EventsGeometry)
        assert isinstance(events.interval, list)

        # Sun event data
        assert isinstance(events.body, str)
        assert isinstance(events.sunrise, TimeWithAzimuth)
        assert isinstance(events.sunset, TimeWithAzimuth)
        assert isinstance(events.solarnoon, TimeWithElevation)
        assert isinstance(events.solarmidnight, TimeWithElevation)

    def test_moon_events(self, client: Sunrise):
        """Test getting moon events"""
        events = client.get_moon_events("2023-10-12", 59.91, 10.75)

        assert isinstance(events, MoonEvents)

        # Common event data
        assert isinstance(events.type, str)
        assert isinstance(events.copyright, str)
        assert isinstance(events.license_url, str)
        assert isinstance(events.geometry, EventsGeometry)
        assert isinstance(events.interval, list)

        # Sun event data
        assert isinstance(events.body, str)
        assert isinstance(events.moonrise, TimeWithAzimuth)
        assert isinstance(events.moonset, TimeWithAzimuth)
        assert isinstance(events.high_moon, TimeWithElevation)
        assert isinstance(events.low_moon, TimeWithElevation)
        assert isinstance(events.moonphase, float)
