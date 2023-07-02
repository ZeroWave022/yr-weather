"""Tests for yr_weather.geosatellite"""

import pytest
import requests

from yr_weather import Geosatellite


@pytest.fixture(scope="module")
def api_available():
    """Test if the API is available."""
    status_req = requests.get(
        "https://api.met.no/weatherapi/geosatellite/1.4/healthz",
        timeout=30,
    )

    # API testing can't continue if the API isn't functional
    if not status_req.ok:
        return False

    return True


@pytest.fixture(scope="module")
def client():
    return Geosatellite()


class TestGeosatellite:
    def _raise_if_api_unavailable(self, api_available):
        if not api_available:
            raise RuntimeError(
                "MET Geosatellite API is not responding. Testing cannot continue."
            )

    def test_params(self, api_available, client):
        """Test correct parameters are required when using get_image()."""
        self._raise_if_api_unavailable(api_available)

        with pytest.raises(
            ValueError, match="'area' parameter must be one of the possible SatAreas"
        ):
            client.get_image("test", "infrared")

        with pytest.raises(
            ValueError,
            match="'img_type' parameter must be one of the possible image types",
        ):
            client.get_image("europe", "test")

        with pytest.raises(
            ValueError, match="'size' parameter must be one of the possible sizes"
        ):
            client.get_image("europe", "visible", size="totally_extreme")

    def test_return_data(self, api_available, client):
        """Test returned response when using get_image()."""
        self._raise_if_api_unavailable(api_available)

        response = client.get_image("europe", "infrared")

        assert isinstance(response, requests.Response)
        assert response.ok == True
