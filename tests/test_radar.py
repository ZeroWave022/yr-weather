"""Tests for yr_weather.radar"""

from dataclasses import fields
import pytest
import requests
from yr_weather.radar import Radar

from yr_weather.data.radar import RadarOptions, RadarContentAvailable, RadarStatus

HEADERS = {"User-Agent": "testing/latest https://github.com/ZeroWave022/yr-weather"}


def api_available():
    """Test if the API is available."""
    status_req = requests.get(
        "https://api.met.no/weatherapi/radar/2.0/healthz",
        timeout=30,
    )

    return status_req.ok


@pytest.fixture(name="client", scope="module")
def fixture_client():
    """The Radar client"""
    return Radar(headers=HEADERS, use_cache=False)


@pytest.mark.skipif(
    not api_available(),
    reason="Testing cannot continue: MET Radar API is not responding.",
)
class TestRadar:
    """Test yr_weather.Radar"""

    def test_params(self, client: Radar):
        """Test correct parameters are required when using get_radar()."""

        with pytest.raises(
            ValueError, match="'area' argument must be one of the possible RadarAreas"
        ):
            client.get_radar("test", "5level_reflectivity")

        with pytest.raises(
            ValueError,
            match="'radar_type' argument must be one of the possible RadarTypes",
        ):
            client.get_radar("central_norway", "test")

    def test_get_radar(self, client: Radar):
        """Test Radar.get_radar()"""
        assert isinstance(
            client.get_radar("central_norway", "5level_reflectivity"), requests.Response
        )

    def test_available_radars(self, client: Radar):
        """Test Radar.get_available_radars()"""
        radars = client.get_available_radars()

        assert isinstance(radars, RadarOptions)

        for radar in fields(radars):
            assert radar.type == RadarContentAvailable

    def test_all_statuses(self, client: Radar):
        """Test Radar.get_all_statuses()"""
        statuses = client.get_all_statuses()

        assert isinstance(statuses.last_update, str)
        assert isinstance(statuses.radars, list)

        for radar in statuses.radars:
            assert isinstance(radar, RadarStatus)

    def test_radar_status(self, client: Radar):
        """Test Radar.get_status()"""
        status_1 = client.get_status("noand")
        status_2 = client.get_status(sitename="Andøya")

        assert isinstance(status_1, RadarStatus)
        assert isinstance(status_2, RadarStatus)
