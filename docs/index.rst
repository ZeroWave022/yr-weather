.. yr-weather documentation master file, created by
   sphinx-quickstart on Fri Jan 27 10:43:17 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to yr-weather!
======================

Retrieve weather data from Norwegian Meteorological Institute's APIs easily.

``yr-weather`` is an API wrapper for some of the products from `MET's API <https://api.met.no/>`__.
To see an example on how these APIs can be used, take a look at `Yr <https://www.yr.no/>`__, made by MET and NRK.


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents

   Home <self>
   gettingstarted
   locationforecast/index
   textforecast/index
   radar/index
   sunrise/index
   geosatellite/index
   APIClient <client>

**Available on** `PyPI <https://pypi.org/project/yr-weather>`__:

.. image:: https://img.shields.io/pypi/v/yr-weather
.. image:: https://img.shields.io/pypi/pyversions/yr-weather
.. image:: https://img.shields.io/pypi/status/yr-weather

Supported products are:

* Locationforecast (v2.0)
* Radar (v2.0)
* Textforecast (v2.0)
* Sunrise (v2.0)
* Geosatellite (v1.4)

Requirements
------------

This package requires Python 3.8 or newer.
To download the newest version, visit `Python's website <https://www.python.org/downloads/>`__.

Installing
----------

To use ``yr-weather``, simply install it using ``pip``.

For Windows:

.. code:: python

   pip install yr-weather

For Linux/macOS:

.. code:: python
   
   python3 -m pip install yr-weather

Getting started
---------------

To get started, check out the :doc:`Getting Started <gettingstarted>` page.

For specific API Products, check their separate section on the documentation:

- :doc:`Locationforecast <locationforecast/index>`
- :doc:`Radar <radar/index>`
- :doc:`Textforecast <textforecast/index>`
- :doc:`Sunrise <sunrise/index>`
- :doc:`Getsatellite <geosatellite/index>`

For the best developer experience, all functions and classes are typed and documented with docstrings.

Caching
^^^^^^^

By default, the library makes a cache file named ``yr_cache.sqlite`` in the working directory.
To disable caching, set ``use_cache`` to ``False`` like so:

.. code-block:: python
   
   yr_weather.Locationforecast(headers=headers, use_cache=False)

MET's Terms of Service encourage using caching to avoid extra load on the network. Therefore, disabling caching and not implementing it yourself is not recommended.

License
-------
This project is licensed under the `Apache License 2.0 <https://github.com/ZeroWave022/yr-weather/blob/main/LICENSE>`__.

Disclaimer
----------
``yr-weather`` is not associated with yr.no or the Norwegian Meteorological Institute (MET).
Any usage of the APIs provided by MET must follow their `API Terms of Service <https://api.met.no/doc/TermsOfService>`__.

Additional links
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
