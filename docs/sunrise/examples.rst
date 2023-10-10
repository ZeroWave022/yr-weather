.. currentmodule:: yr_weather

Sunrise: Examples
=================

Setting up
-----------
The examples assume you have set up a :class:`Sunrise` client like so:

.. code-block:: python
    
    import yr_weather

    # Replace with your own User-Agent. See MET API Terms of Service for correct user agents.
    headers = {
        "User-Agent": "Your User-Agent"
    }

    my_client = yr_weather.Sunrise(headers=headers)

.. admonition:: Important
    :class: attention
    
    All of the next examples will use ``my_client`` as a reference to your client.

Getting one event from Sunrise data
------------------------------------

.. code-block:: python

    # Get sun and moon events data for Oslo, Norway
    sun_events = client.get_sun_events("2023-10-10", 59.91, 10.75)
    moon_events = client.get_moon_events("2020-10-10", 59.91, 10.75)

    sunrise_time = sun_events.sunrise.time
    moonrise_time = moon_events.moonrise.time

    print(f"Sunrise will happen at {sunrise_time}")
    print(f"Moonrise will happen at {moonrise_time}")
