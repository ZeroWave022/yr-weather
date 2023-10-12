Types: Radar
============

Type aliases
------------

To learn more about the impact of these options, see the MET.no `documentation <https://api.met.no/weatherapi/geosatellite/1.4/documentation>`__.

.. data:: SatArea
   
   Represents a valid geosatellite image area.
   
   .. code-block:: python
      
      SatArea = Literal[
         "africa",
         "atlantic_ocean",
         "europe",
         "global",
         "mediterranean"
      ]
