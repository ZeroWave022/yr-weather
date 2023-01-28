Types: Sunrise
==============

.. automodule:: yr_weather.types.sunrise
   :members:
   :undoc-members:
   :show-inheritance:

Type aliases
------------

To learn more about the impact of these options, see the MET.no `documentation <https://api.met.no/weatherapi/sunrise/2.0/documentation>`__.

.. data:: DetailLiteral

   Represents a valid detail from a Sunrise API response.

   .. code-block:: python

      Literal[
         "high_moon",
         "low_moon",
         "moonphase",
         "solarmidnight",
         "solarnoon",
         "moonrise",
         "moonset",
         "sunrise",
         "sunset",
         "moonposition",
         "moonshadow"
      ]
