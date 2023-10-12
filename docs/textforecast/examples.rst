.. currentmodule:: yr_weather

Textforecast: Examples
==========================

Setting up
-----------
The examples assume you have set up a :class:`Textforecast` client like so:

.. code-block:: python
    
    import yr_weather

    my_client = yr_weather.Textforecast()

.. admonition:: Important
    :class: attention
    
    All of the next examples will use ``my_client`` as a reference to your client.

Getting text forecast for a location
------------------------------------

At the time of writing, text forecasts for land are only available in Norwegian.

.. code-block:: python
    
    land_overview = my_client.get_forecasts("landoverview")

    forecast_now = land_overview.now()

    # Location names are available at Textforecast.get_areas()
    forecast_east = forecast_now.locations.get("Østlandet")

    print("The text forecast for Østlandet is:")
    print(forecast_east.text)
    # Example output:
    # Vestlig bris, frisk bris utsatte steder, liten kuling på kysten. Nordøst i Innlandet fylke enkelte sludd- og regnbyger, ellers oppholdsvær og perioder med sol.

Getting available areas
-----------------------

.. code-block:: python

    areas = my_client.get_areas("land") # Can also get areas for "coast"

    names = [area.name for area in areas]
    names_string = ", ".join(names)

    print(f"All available areas for textforecast are: {names_string}")
    # Example output:
    # All available areas for textforecast are: Agder, Telemark og Agder, Østlandet, Østlandet og Telemark, ...


Getting other types of forecasts
--------------------------------

For available types of forecasts, see Textforecast's `documentation <https://api.met.no/weatherapi/textforecast/2.0/documentation>`__.

.. code-block:: python

    coast_forecasts = my_client.get_forecasts("coast_no")

    forecast_now = coast_forecasts.now()

    # You can also get a forecast from the list manually
    second_forecast = coast_forecasts.times[1]

    print(f"Second forecast is valid from {second_forecast.from_time} and to {second_forecast.to_time}")
    # Example output:
    # Second forecast is valid from 2023-10-13T00:00:00 and to 2023-10-14T00:00:00
