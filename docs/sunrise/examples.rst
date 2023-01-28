.. currentmodule:: yr_weather

Sunrise: Examples
=================

Setting up
-----------
The examples assume you have set up a :class:`Sunrise` client like so:

.. code-block:: python
    
    import yr_weather

    my_client = yr_weather.Sunrise()

.. admonition:: Important
    :class: attention
    
    All of the next examples will use ``my_client`` as a reference to your client.

Getting one detail from Sunrise data
------------------------------------

.. code-block:: python

    # Get sunset for Oslo, Norway
    sunset = my_client.get_detail("sunset", "2023-01-20", 59.91, 10.75, "+01:00")

    print(sunset)
    # Example output:
    # {
    #     'desc': 'LOCAL DIURNAL SUN SET',
    #     'time': '2023-01-20T16:00:36+01:00'}
    # }

Getting all data from Sunrise
-----------------------------

.. code-block:: python
    
    # Get sunrise data for Oslo, Norway
    sr_data = my_client.get_sunrise("2023-01-20", 59.91, 10.75, "+01:00")
    
    print(sr_data)
    # Example output:
    # {
    #   "location": {
    #     "height": "0",
    #     "latitude": "59.9",
    #     "longitude": "10.7",
    #     "time": [
    #       {
    #         "date": "2023-01-20",
    #         "high_moon": {
    #           "desc": "LOCAL DIURNAL MAXIMUM MOON ELEVATION (Max= 1.94192)",
    #           "elevation": "1.941923918",
    #           "time": "2023-01-20T11:01:37+01:00"
    #         },
    #         "low_moon": {
    #           "desc": "LOCAL DIURNAL MINIMUM MOON ELEVATION (Min= -57.28220)",
    #           "elevation": "-57.282202638",
    #           "time": "2023-01-20T23:33:17+01:00"
    #         },
    #         "moonphase": {
    #           "desc": "LOCAL MOON STATE * MOON PHASE= 92.4 (waning crescent)",
    #           "time": "2023-01-20T00:00:00+01:00",
    #           "value": "92.421478765"
    #         },
    #         "moonposition": {
    #           "azimuth": "34.784350684",
    #           "desc": "LOCAL MOON POSITION Elv: -54.742 deg, Azi: 34.784, Rng: 365364.7 km",
    #           "elevation": "-54.741908062",
    #           "phase": "92.421478765",
    #           "range": "365364.745236254",
    #           "time": "2023-01-20T00:00:00+01:00"
    #         },
    #         "moonrise": {
    #           "desc": "LOCAL DIURNAL MOON RISE",
    #           "time": "2023-01-20T09:14:14+01:00"
    #         },
    #         "moonset": {
    #           "desc": "LOCAL DIURNAL MOON SET",
    #           "time": "2023-01-20T12:48:59+01:00"
    #         },
    #         "moonshadow": {
    #           "azimuth": "261.058146106",
    #           "desc": "LOCAL MOON STATE * SHADOW ANGLES (azi=261.1,ele=-62.5)",
    #           "elevation": "-62.546205058",
    #           "time": "2023-01-20T00:00:00+01:00"
    #         },
    #         "solarmidnight": {
    #           "desc": "LOCAL DIURNAL MINIMUM SOLAR ELEVATION (Min= -50.33184)",
    #           "elevation": "-50.331839434",
    #           "time": "2023-01-20T00:27:46+01:00"
    #         },
    #         "solarnoon": {
    #           "desc": "LOCAL DIURNAL MAXIMUM SOLAR ELEVATION (Max= 9.97480)",
    #           "elevation": "9.974802331",
    #           "time": "2023-01-20T12:28:23+01:00"
    #         },
    #         "sunrise": {
    #           "desc": "LOCAL DIURNAL SUN RISE",
    #           "time": "2023-01-20T08:56:14+01:00"
    #         },
    #         "sunset": {
    #           "desc": "LOCAL DIURNAL SUN SET",
    #           "time": "2023-01-20T16:00:36+01:00"
    #         }
    #       },
    #       {
    #         "date": "2023-01-21",
    #         "moonposition": {
    #           "azimuth": "9.904412311",
    #           "desc": "LOCAL MOON POSITION Elv: -57.270 deg, Azi: 9.904, Rng: 362762.3 km",
    #           "elevation": "-57.27009424",
    #           "phase": "96.365027217",
    #           "range": "362762.2610191",
    #           "time": "2023-01-21T00:00:00+01:00"
    #         }
    #       }
    #     ]
    #   },
    #   "meta": {
    #     "licenseurl": "https://api.met.no/license_data.html"
    #   }
    # }
