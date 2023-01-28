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
- Sunrise (v2.0)

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
To get started, check out the [documentation](https://yr-weather.readthedocs.io/en/latest/gettingstarted.html).

For specific API Products, check their separate section on the documentation:
- [Locationforecast](https://yr-weather.readthedocs.io/en/latest/locationforecast/index.html)
- [Radar](https://yr-weather.readthedocs.io/en/latest/radar/index.html)
- [Textforecast](https://yr-weather.readthedocs.io/en/latest/textforecast/index.html)
- [Sunrise](https://yr-weather.readthedocs.io/en/latest/sunrise/index.html)

For the best developer experience, all functions and classes are typed and documented with docstrings.

## Caching
By default, the library makes a cache file named `yr_cache.sqlite` in the working directory.
To disable caching, set `use_cache` to `False` like so:
```py
yr_weather.Locationforecast(headers=headers, use_cache=False)
```
MET's Terms of Service encourage using caching, to avoid extra load on the network. Therefore, this feature is not recommended.

# Future objectives (TODOs)
- [x] Add Read the Docs documentation
- [ ] Add further features from MET's API
- [ ] Improve support for earlier Python versions

# License
This project is licensed under the [GNU General Public License v3](https://github.com/ZeroWave022/yr-weather/blob/main/LICENSE).

# Disclaimer
`yr-weather` is not associated with yr.no or the Norwegian Meteorological Institute (MET).
Any usage of the APIs provided by MET must follow their [API Terms of Service](https://api.met.no/doc/TermsOfService).
