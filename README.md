<div align="center">

<a href="https://github.com/ZeroWave022/yr-weather/graphs/contributors">![Contributors](https://img.shields.io/github/contributors/ZeroWave022/yr-weather)</a>
<a href="https://github.com/ZeroWave022/yr-weather/network/members">![Forks](https://img.shields.io/github/forks/ZeroWave022/yr-weather)</a>
<a href="https://github.com/ZeroWave022/yr-weather/issues">![Issues](https://img.shields.io/github/issues/ZeroWave022/yr-weather)</a>
<a>![Code Size](https://img.shields.io/github/languages/code-size/ZeroWave022/yr-weather)</a>
<a href="https://github.com/ZeroWave022/yr-weather/blob/main/LICENSE">![Licence](https://img.shields.io/github/license/ZeroWave022/yr-weather)</a>

</div>

# yr-weather
Retrieve weather data from Yr (by the Norwegian Meteorogical Institute) easily.
`yr-weather` is an API wrapper for some of the products from [Yr's API](https://api.met.no/).

**Available on [PyPI](https://pypi.org/project/yr-weather)**:

![Package version](https://img.shields.io/pypi/v/yr-weather)
![Python version](https://img.shields.io/pypi/pyversions/yr-weather)
![Package status](https://img.shields.io/pypi/status/yr-weather)

Supported products are:
- Locationforecast (v2.0)
- Radar (v2.0)
- Textforecast (v2.0)

# Installing
To use `yr-weather`, simply install it using `pip`.

For Windows:
```
pip install yr-weather
```

For Linux/macOS:
```
python3 -m pip install yr-weather
```

# Getting started
To get started with Locationforecast, instantiate a `Locationforecast` class and use the provided functions.
A simple example follows (more features are available).
```py
import yr_weather

# Replace with your own User-Agent. See MET API Terms of Service for correct User-Agents.
headers = {
    "User-Agent": "Your User-Agent"
}

yr_client = yr_weather.Locationforecast(headers=headers)

# Get air temperature in Oslo, Norway
oslo_temp = yr_client.get_air_temperature(59.91, 10.75)

# Get full weather data for Oslo, Norway
weather_data = yr_client.get_forecast(59.91, 10.75)

print(oslo_temp)
# Output: 8.0

# Get data from a typed dict
print(weather_data["properties"]["timeseries"][0]["data"]["instant"]["details"])
# Example output:
#    {
#        "air_pressure_at_sea_level": 1034.7,  
#        "air_temperature": -1.5,
#        "air_temperature_percentile_10": -2.5,
#        "air_temperature_percentile_90": -0.9,
#        "cloud_area_fraction": 99.9,
#        "cloud_area_fraction_high": 90.9,     
#        "cloud_area_fraction_low": 62.9,      
#        "cloud_area_fraction_medium": 95.7,   
#        "dew_point_temperature": -4.4,        
#        "fog_area_fraction": 0.0,
#        "relative_humidity": 82.1,
#        "ultraviolet_index_clear_sky": 0.0,
#        "wind_from_direction": 11.3,
#        "wind_speed": 0.2,
#        "wind_speed_of_gust": 0.7,
#        "wind_speed_percentile_10": 0.3,
#        "wind_speed_percentile_90": 0.7
#    }
```

All functions and classes are documented with docstrings.
Further documentation will be made at a later point in time.

## Caching
By default, the library makes a cache file named `yr_cache.sqlite` in the working directory.
To disable caching, set `use_cache` to `False` like so:
```py
yr_weather.Locationforecast(headers=headers, use_cache=False)
```
MET's Terms of Service encourage using caching, to avoid extra load on the network. Therefore, this feature is not recommended.

# Future objectives (TODOs)
- [ ] Add Read the Docs documentation
- [ ] Add further features from MET's API
- [ ] Improve support for earlier Python versions

# License
This project is licensed under the [GNU General Public License v3](https://github.com/ZeroWave022/yr-weather/blob/main/LICENSE).

# Disclaimer
`yr-weather` is not associated with yr.no or the Norwegian Meteorological Institute (MET).
Any usage of the APIs provided by MET must follow their [API Terms of Service](https://api.met.no/doc/TermsOfService).
