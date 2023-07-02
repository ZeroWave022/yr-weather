"""Tests for yr_weather.client"""

import pytest
from requests import Session as UncachedSession
from requests_cache import CachedSession

from yr_weather.client import APIClient


def test_init():
    """Test correct instantiation."""
    APIClient()

    with pytest.raises(TypeError):
        APIClient(123)


def test_headers():
    """Test headers."""
    init_headers = {"User-Agent": "Test"}
    client = APIClient(init_headers)
    assert client._global_headers == init_headers

    new_headers = {"User-Agent": "Test", "Authorization": "Test"}
    client.set_headers(new_headers)
    assert client._global_headers == new_headers


def test_cache():
    """Test cache usage."""
    client = APIClient()
    assert isinstance(client.session, CachedSession)

    with pytest.raises(TypeError):
        client.toggle_cache()

    client.toggle_cache(False)
    assert isinstance(client.session, UncachedSession)

    client.toggle_cache(False)
    assert isinstance(client.session, UncachedSession)

    client.toggle_cache(True)
    assert isinstance(client.session, CachedSession)

    client.toggle_cache(True)
    assert isinstance(client.session, CachedSession)
