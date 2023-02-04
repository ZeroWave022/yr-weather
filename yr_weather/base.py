import requests
from requests_cache import CachedSession
from typing import Optional, Literal, Union

class BaseClient():
    def __init__(self, headers: dict, use_cache: Optional[bool] = True) -> None:
        self._baseURL = "https://api.met.no/weatherapi/"
        self._global_headers = headers

        if use_cache:
            self.session = CachedSession(
                cache_name = "yr_cache",
                cache_control = True
            )
        else:
            self.session = requests.Session()

        self.session.headers = self._global_headers

        if type(headers) != dict:
            raise TypeError("The 'headers' argument must be of type 'dict'.")
    
    def set_headers(self, headers: dict) -> dict:
        """Set new headers of the client.
        
        This will override any old headers, and replace them with the new headers from the ``headers`` parameter.

        Parameters
        ----------
        headers: :class:`dict`
            The new headers, which will override the old ones.
        
        Returns
        -------
        :class:`dict`
            The headers which were set.
        """
        if type(headers) != dict:
            raise TypeError("The 'headers' argument must be of type 'dict'.")

        if "User-Agent" not in headers.keys():
            raise ValueError("A custom 'User-Agent' property is required in the 'headers' dict.")
        
        self._global_headers = headers
        self.session.headers = headers
        return self.session.headers
    
    def toggle_cache(self, toggle: bool) -> bool:
        """Toggle the usage of cache on or off.

        Parameters
        ----------
        toggle: :class:`bool`
            Whether cache should be used, or whether to disable it.
        
        Returns
        -------
        :class:`bool`
            The new state of the cache (on/off).
        """
        if (toggle):
            if type(self.session) != CachedSession:
                self.session = CachedSession(
                    cache_name = "yr_cache",
                    cache_control = True
                )
                self.session.headers = self._global_headers
            return True
        else:
            if type(self.session) != requests.Session:
                self.session = requests.Session()
                self.session.headers = self._global_headers
            return False

