.. currentmodule:: yr_weather

Radar: Examples
===============

Setting up
-----------
The examples assume you have set up a :class:`Radar` client like so:

.. code-block:: python
    
    import yr_weather

    my_client = yr_weather.Radar()

.. admonition:: Important
    :class: attention
    
    All of the next examples will use ``my_client`` as a reference to your client.

Valid types
-----------

For valid areas, see :data:`types.radar.RadarArea`.
    
For valid radar types, see :data:`types.radar.RadarType`.

Getting a radar image
---------------------

.. code-block:: python
    
    area = "central_norway"
    r_type = "5level_reflectivity"
    content_type = "image"

    result = my_client.get_radar(area, r_type, content_type)

    with open("image.png", "wb") as f:
        for chunk in result:
            f.write(chunk)

Getting a radar image for a selected time
-----------------------------------------

.. code-block:: python

    from datetime import datetime

    # Replace with your time
    time_now = datetime(2023, 1, 20, 12, 00, 00)
    time_str = time_now.isoformat(timespec="seconds") + "Z"

    result = radar.get_radar("central_norway", "5level_reflectivity", "image", time_str)

    if result.ok:
        with open("image.png", "wb") as f:
            for chunk in result:
                f.write(chunk)
    else:
        print("Couldn't get this radar image/animation!")
