.. currentmodule:: yr_weather

Radar: Examples
===============

Setting up
-----------
The examples assume you have set up a :class:`Geosatellite` client like so:

.. code-block:: python
    
    import yr_weather

    my_client = yr_weather.Geosatellite()

.. admonition:: Important
    :class: attention
    
    All of the next examples will use ``my_client`` as a reference to your client.

Valid types
-----------

For valid geosatellite areas, see :data:`types.geosatellite.SatArea`.

For other options, see MET.no's `documentation <https://api.met.no/weatherapi/geosatellite/1.4/documentation>`__.

Getting a geosatellite image
----------------------------

.. code-block:: python
    
    area = "europe"
    img_type = "infrared"
    size = "normal"

    result = my_client.get_image(area, img_type, size=size)

    with open("image.png", "wb") as f:
        for chunk in result:
            f.write(chunk)
