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

Getting text forecast for first location in API list
----------------------------------------------------

At the time of writing, text forecasts for land are only available in Norwegian.

.. code-block:: python
    
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

Getting available land areas
----------------------------

.. code-block:: python

    areas = my_client.get_areas("land")
    
    print(areas)
    # Example output:
    # {
    #   "area": [
    #     {
    #       "id": "0502",
    #       "areaDesc": "Agder",
    #       "polygon": "58.089167,8.215333 58.246167,8.525500 ..., ..."
    #     },
    #     {
    #       "id": "0502_0608",
    #       "areaDesc": "Telemark og Agder",
    #       "polygon": "59.672167,7.213167 59.653333,7.097667 ..., ..."
    #     },
    #     {
    #       "id": "0503",
    #       "areaDesc": "Østlandet",
    #       "polygon": "59.043667,10.653167 58.939167,10.904167 ..., ..."
    #     },
    #     {
    #       "id": "0503_0608",
    #       "areaDesc": "Østlandet og Telemark",
    #       "polygon": "58.930000,9.784667 58.956500,10.048167 ..., ..."
    #     },
    #     {
    #       "id": "0503_0608_0609_0610",
    #       "areaDesc": "Agder, Telemark, Østlandet",
    #       "polygon": "58.089167,8.215333 58.246167,8.525500 ..., ..."
    #     },
    #     {
    #       "id": "0504",
    #       "areaDesc": "Trøndelag",
    #       "polygon": "64.598333,9.853500 64.531333,9.714667 ..., ..."
    #     }, ...
    #   ]
    # }

Getting coast forecasts in English
----------------------------------

.. code-block:: python

    forecasts = loc_cli.get_forecasts("coast_en")

    print(forecasts)
    # Example output:
    # {
    #   "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    #   "xsi:noNamespaceSchemaLocation": "https://schema.api.met.no/schemas/textforecast-0.3.xsd",
    #   "meta": {
    #     "licenseurl": "https://www.met.no/en/free-meteorological-data/Licensing-and-crediting"
    #   },
    #   "time": [
    #     {
    #       "from": "2023-01-28T18:00:00",
    #       "to": "2023-01-29T00:00:00",
    #       "forecasttype": [
    #         {
    #           "name": "normal",
    #           "location": [
    #             {
    #               "name": "Outer Skagerrak",
    #               "id": "0818",
    #               "text": "West occasionally force 6. Mainly dry and good. Significant wave height: 0,5-1,5 m."
    #             },
    #             {
    #               "name": "Inner Skagerrak",
    #               "id": "0817",
    #               "text": "West force 5. Dry. Good. Significant wave height: 0,5-1,5 m."
    #             }
    #           ]
    #         },
    #         {
    #           "name": "normal",
    #           "location": [
    #             {
    #               "name": "Inner Oslofjord",
    #               "id": "0816",
    #               "text": "West and southwest force 4. Cloudy or partly cloudy. Dry. Good. Significant wave height: 0,5 m or less."
    #             },
    #             {
    #               "name": "Swedish border - Lyngoer",
    #               "id": "51699",
    #               "text": "West and southwest occasionally force 5. Cloudy or partly cloudy. Dry. Good. Significant wave height: around 0,5 m."
    #             },
    #             {
    #               "name": "Lyngoer - Aana Sira",
    #               "id": "51676",
    #               "text": "West up to force 5. In west scattered rain showers, in east cloudy or partly cloudy, dry. Moderate in precipitation. Significant wave height: 0,5-1,5 m."
    #             },
    #             {
    #               "name": "Aana-Sira - Karmoey",
    #               "id": "9028_9029",
    #               "text": "West and northwest up to force 5, occasionally force 6 in southernmost part. Periods of rain showers. Moderate in precipitation. Significant wave height: 1,5-2,5 m."
    #             },
    #             {
    #               "name": "Karmoey - Stad",
    #               "id": "9030_9031_9032_9033_9034",
    #               "text": "Decreasing west force 4. Rain showers. Moderate in precipitation. Significant wave height: 2-4 m, highest in northernmost part,"
    #             }, ...
    #           ]
    #         }
    #       ]
    #     }, ...
    #   ]
    # }
