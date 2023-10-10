.. currentmodule:: yr_weather

Getting Started
===============

``yr-weather`` provides support for multiple products from the `MET.no API <https://api.met.no>`_.
These have been created by the Norwegian Meteorological Institute (MET).

Before proceeding, make sure you agree with the current `API Terms of Service <https://api.met.no/doc/TermsOfService>`_.
Some products, for example `Locationforecast <https://api.met.no/weatherapi/locationforecast/2.0/documentation>`_ have some additional requirements, such as providing a custom User-Agent.

Select the product you want to explore:

* :ref:`tutorial_locforecast`
* :ref:`tutorial_textforecast`
* :ref:`tutorial_radar`
* :ref:`tutorial_sunrise`

.. _tutorial_locforecast:

Locationforecast
----------------

**This product requires a** `custom User-Agent <https://api.met.no/doc/FAQ>`__.

The Locationforecast API is used for getting weather data, such as air temperature, wind speed, and more.
You can read more about the API on it's own `documentation <https://api.met.no/weatherapi/locationforecast/2.0/documentation>`__.

To get started with Locationforecast using ``yr-weather``, instantiate a :class:`Locationforecast` object like so:

.. code-block:: python

    import yr_weather

    # Replace with your own User-Agent. See MET API Terms of Service for correct User-Agents.
    headers = {
        "User-Agent": "Your User-Agent"
    }

    my_client = yr_weather.Locationforecast(headers=headers)

    # Get air temperature in Oslo, Norway
    oslo_temp = my_client.get_air_temperature(59.91, 10.75)

    print(oslo_temp)
    # Example output: 8.0

    # Get full forecast for Oslo, Norway
    forecast = my_client.get_forecast(59.91, 10.75)

    # Select the forecast for the time right now (as it's possible to select a time further in the future)
    forecast_now = forecast.now()

    # You can now select from multiple data points. As an example, we show air pressure and wind speed.
    pressure = forecast_now.details.air_pressure_at_sea_level
    wind_speed = forecast_now.details.wind_speed

    print(f"Air pressure at sea level in Oslo, Norway, is {pressure} hPa and the wind speed is {wind_speed} m/s")


Like shown above, you can now use ``my_client`` to get full weather data, air temperature, and more.

Next steps:

* Checking some :doc:`examples <locationforecast/examples>`
* Or jumping into the :doc:`Locationforecast API Reference <locationforecast/api>`

.. _tutorial_textforecast:

Textforecast
------------

Textforecast is used to get text-based forecasts for selected areas in Norway.
The forecasts are provided by MET and you can read more about the API on their `documentation <https://api.met.no/weatherapi/textforecast/2.0/documentation>`__.

In the example below, a :class:`Textforecast` class is instantiated and the text forecast for the first location in the list (from the API) is given.

.. note:: 

    The ``"landoverview"`` forecast is only available in Norwegian. For more information, please see the links under the example.

.. code-block:: python

    import yr_weather

    text_client = yr_weather.Textforecast()

    land_overview = text_client.get_forecasts("landoverview")

    newest_forecast = land_overview["time"][0]["forecasttype"]

    first_location = newest_forecast["location"][0]

    print(first_location)
    # Example output:
    # {
    #     'name': 'Østlandet',
    #     'id': '0503_0608',
    #     'text': 'Skiftende eller sørvest bris, sørvest frisk bris på kysten. Oppholdsvær og noe sol.'
    # }

Next steps:

* Checking some :doc:`examples <textforecast/examples>`
* Or jumping into the :doc:`Textforecast API Reference <textforecast/api>`

.. _tutorial_radar:

Radar
-----

The API returns images and GIFs of radar images.
``yr-weather`` gives you the freedom to decide what you want to do with the data you receive.
For more information about the API itself, check `MET's documentation <https://api.met.no/weatherapi/radar/2.0/documentation>`__.

What you see below is an example of getting an animated radar image and saving it in the current working directory.

.. code-block:: python

    import yr_weather

    radar_client = yr_weather.Radar()

    result = radar_client.get_radar("central_norway", "5level_reflectivity", "image")

    with open("image.png", "wb") as f:
        for chunk in result:
            f.write(chunk)

Next steps:

* Checking some :doc:`examples <radar/examples>`
* Or jumping into the :doc:`Radar API Reference <radar/api>`

.. _tutorial_sunrise:

Sunrise
-------

The Sunrise submodule allows you to calculate various events, such as sunrises, sunsets, low moons, high moons and so on.
For more information about the API itself, check `MET's documentation <https://api.met.no/weatherapi/sunrise/3.0/documentation>`__.

In the example below, we use the :meth:`Sunrise.get_detail` function to get data about the sunset.

.. code-block:: python
    
    import yr_weather

    sunrise_client = yr_weather.Sunrise()

    # Get sunset for Oslo, Norway
    sunset = sunrise_client.get_detail("sunset", "2023-01-20", 59.91, 10.75, "+01:00")

    print(sunset)
    # Example output:
    # {
    #     'desc': 'LOCAL DIURNAL SUN SET',
    #     'time': '2023-01-20T16:00:36+01:00'}
    # }

Next steps:

* Checking some :doc:`examples <sunrise/examples>`
* Or jumping into the :doc:`Sunrise API Reference <sunrise/api>`
