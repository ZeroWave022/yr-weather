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
    weather_data = my_client.get_forecast(59.91, 10.75, "compact")

    print(weather_data)
    # Example output:
    # {
    #   "type": "Feature",
    #   "geometry": {
    #     "type": "Point",
    #     "coordinates": [
    #       10.75,
    #       59.91,
    #       3
    #     ]
    #   },
    #   "properties": {
    #     "meta": {
    #       "updated_at": "2023-01-28T10:36:35Z",
    #       "units": {
    #         "air_pressure_at_sea_level": "hPa",
    #         "air_temperature": "celsius",
    #         "cloud_area_fraction": "%",
    #         "precipitation_amount": "mm",
    #         "relative_humidity": "%",
    #         "wind_from_direction": "degrees",
    #         "wind_speed": "m/s"
    #       }
    #     },
    #     "timeseries": [
    #       {
    #         "time": "2023-01-28T10:00:00Z",
    #         "data": {
    #           "instant": {
    #             "details": {
    #               "air_pressure_at_sea_level": 1018.0,
    #               "air_temperature": -2.3,
    #               "cloud_area_fraction": 82.2,
    #               "relative_humidity": 94.0,
    #               "wind_from_direction": 42.7,
    #               "wind_speed": 0.4
    #             }
    #           },
    #           "next_12_hours": {
    #             "summary": {
    #               "symbol_code": "cloudy"
    #             }
    #           },
    #           "next_1_hours": {
    #             "summary": {
    #               "symbol_code": "partlycloudy_day"
    #             },
    #             "details": {
    #               "precipitation_amount": 0.0
    #             }
    #           },
    #           "next_6_hours": {
    #             "summary": {
    #               "symbol_code": "partlycloudy_day"
    #             },
    #             "details": {
    #               "precipitation_amount": 0.0
    #             }
    #           }
    #         }
    #       }, ...
    #     ]
    #   }
    # }

