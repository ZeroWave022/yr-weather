<div align="center">

<a href="https://github.com/ZeroWave022/yr-weather/graphs/contributors">![Contributors](https://img.shields.io/github/contributors/ZeroWave022/yr-weather)</a>
<a href="https://github.com/ZeroWave022/yr-weather/network/members">![Forks](https://img.shields.io/github/forks/ZeroWave022/yr-weather)</a>
<a href="https://github.com/ZeroWave022/yr-weather/issues">![Issues](https://img.shields.io/github/issues/ZeroWave022/yr-weather)</a>
<a>![Code Size](https://img.shields.io/github/languages/code-size/ZeroWave022/yr-weather)</a>
<a href="https://github.com/ZeroWave022/yr-weather/blob/main/LICENSE">![Licence](https://img.shields.io/github/license/ZeroWave022/yr-weather)</a>

</div>

# yr-weather

Retrieve weather data from Norwegian Meteorological Institute's APIs easily.

`yr-weather` is an API wrapper for some of the products from [MET's API](https://api.met.no/).
To see an example on how these APIs can be used, take a look at [Yr](https://www.yr.no/), made by MET and NRK.

**Available on [PyPI](https://pypi.org/project/yr-weather)**:

![Package version](https://img.shields.io/pypi/v/yr-weather)
![Python version](https://img.shields.io/pypi/pyversions/yr-weather)
![Package status](https://img.shields.io/pypi/status/yr-weather)

Supported products are:

- Locationforecast (v2.0)
- Radar (v2.0)
- Textforecast (v2.0)
- Sunrise (v2.0)
- Geosatellite (v1.4)

# Requirements

This package requires Python 3.8 or newer.
To download the newest version, visit [Python's website](https://www.python.org/downloads/).

# Installing

To use `yr-weather`, simply install it using `pip`.

For Windows:

```console
pip install yr-weather
```

For Linux/macOS:

```console
python3 -m pip install yr-weather
```

# Getting started

To get started, check out the [documentation](https://yr-weather.readthedocs.io/en/latest/gettingstarted.html).

For specific API Products, check their separate section on the documentation:

- [Locationforecast](https://yr-weather.readthedocs.io/en/latest/locationforecast/index.html)
- [Radar](https://yr-weather.readthedocs.io/en/latest/radar/index.html)
- [Textforecast](https://yr-weather.readthedocs.io/en/latest/textforecast/index.html)
- [Sunrise](https://yr-weather.readthedocs.io/en/latest/sunrise/index.html)
- [Geosatellite](https://yr-weather.readthedocs.io/en/latest/geosatellite/index.html)

For the best developer experience, all functions and classes are typed and documented with docstrings.

## Caching

By default, the library makes a cache file named `yr_cache.sqlite` in the working directory.
To disable caching, set `use_cache` to `False` like so:

```py
yr_weather.Locationforecast(headers=headers, use_cache=False)
```

MET's Terms of Service encourage using caching to avoid extra load on the network. Therefore, disabling caching and not implementing it yourself is not recommended.

# Future objectives (TODOs)

- [x] Add Read the Docs documentation
- [ ] Add further features from MET's API
- [ ] Make sure Python >=3.8 is supported
- [ ] Add linter
- [ ] Add type checker

# License

This project is licensed under the [Apache License 2.0](https://github.com/ZeroWave022/yr-weather/blob/main/LICENSE).

# Disclaimer

`yr-weather` is not associated with yr.no or the Norwegian Meteorological Institute (MET).
Any usage of the APIs provided by MET must follow their [API Terms of Service](https://api.met.no/doc/TermsOfService).
