Types: Radar
============

.. automodule:: yr_weather.types.radar
   :members:
   :undoc-members:
   :show-inheritance:

Type aliases
------------

To learn more about the impact of these options, see the MET.no `documentation <https://api.met.no/weatherapi/radar/2.0/documentation>`__.

.. data:: RadarArea
   
   Represents a valid radar area.
   
   .. code-block:: python
      
      Literal[
         "central_norway",
         "eastern_norway",
         "finnmark",
         "nordic",
         "nordland",
         "northern_nordland",
         "northwestern_norway",
         "norway",
         "southeastern_norway",
         "southern_nordland",
         "southern_norway",
         "southwestern_norway",
         "troms",
         "western_norway",
         "xband"
      ]

.. data:: RadarContentType

   Represents a valid radar content type.

   .. code-block:: python
      
      Literal["image", "animation"]

.. data:: RadarType

   Represents a valid radar type. This will decide what will be shown on the radar image/animation.

   .. code-block:: python

      Literal[
         "5level_reflectivity",
         "accumulated_01h",
         "accumulated_02h",
         "accumulated_03h",
         "accumulated_04h",
         "accumulated_05h",
         "accumulated_06h",
         "accumulated_07h",
         "accumulated_08h",
         "accumulated_09h",
         "accumulated_10h",
         "accumulated_11h",
         "accumulated_12h",
         "accumulated_13h",
         "accumulated_14h",
         "accumulated_15h",
         "accumulated_16h",
         "accumulated_17h",
         "accumulated_18h",
         "accumulated_19h",
         "accumulated_20h",
         "accumulated_21h",
         "accumulated_22h",
         "accumulated_23h",
         "accumulated_24h",
         "fir_preciptype",
         "lx_reflectivity",
         "preciptype",
         "reflectivity"
      ]