.. currentmodule:: yr_weather

Locationforecast: Examples
==========================

Setting up
-----------
The examples assume you have set up a :class:`Locationforecast` client with a valid User-Agent like so:

.. code-block:: python
    
    import yr_weather

    # Replace with your own User-Agent. See MET API Terms of Service for correct User-Agents.
    headers = {
        "User-Agent": "Your User-Agent"
    }

    my_client = yr_weather.Locationforecast(headers=headers)

.. admonition:: Important
    :class: attention
    
    All of the next examples will use ``my_client`` as a reference to your client.

Getting the air temperature
---------------------------

.. code-block:: python
    
    # Get air temperature for Oslo, Norway.
    air_temp = my_client.get_air_temperature(59.91, 10.75)

    print(air_temp)
    # Example output: 8.0

Getting full weather data
-------------------------

.. code-block:: python

    # Full weather data for Oslo, Norway.
    # Returns a typed dict for easy access to data.
    forecast = my_client.get_forecast(59.91, 10.75)

    forecast_now = forecast.now()

    air_temp = forecast_now.details.air_temperature

    print(f"Current air temperature is {air_temp} °C")

    # There are multiple attributes available, if the data is supplied by the MET API.
    # The complete forecast can give access to these details:
    # air_pressure_at_sea_level: float | None
    # air_temperature: float | None
    # air_temperature_percentile_10: float | None
    # air_temperature_percentile_90: float | None
    # cloud_area_fraction: float | None
    # cloud_area_fraction_high: float | None
    # cloud_area_fraction_low: float | None
    # cloud_area_fraction_medium: float | None
    # dew_point_temperature: float | None
    # fog_area_fraction: float | None
    # relative_humidity: float | None
    # ultraviolet_index_clear_sky: float | None
    # wind_from_direction: float | None
    # wind_speed: float | None
    # wind_speed_of_gust: float | None
    # wind_speed_percentile_10: float | None
    # wind_speed_percentile_90: float | None

Getting future weather predictions
----------------------------------

.. code-block:: python

    # Full weather data for Oslo, Norway.
    forecast = my_client.get_forecast(59.91, 10.75)

    forecast_now = forecast.now()

    # A ForecastFuture dataclass storing info about the weather in 6 hours
    next_6_hrs = forecast_now.next_6_hours

    expected_temp = next_6_hrs.details.air_temperature # This value may be None, if no value is received from the API

    print(f"In the next 6 hours, the expected temperature is {expected_temp} °C")
