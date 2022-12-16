*****************
shyft.time_series
*****************

This package contains the following classes and functions to use
by end-users. The namespace itself contains more classes and functions,
but these are used internally.

.. note::

   **Vector types**
   Because the actual code is written in C++ which is strongly typed,
   Shyft Python code uses the concept of "vector" classes which are basically
   lists of the named type e.g. *TsBindInfo* and *TsBindInfoVector*. These are
   not specifically documented here.

   However, some vector types like *TsVector* are documented, because they
   provide more functionality than a simple list.


Time
####

Elements in this category deal with date/time.

Function utctime_now
====================
.. autoclass:: shyft.time_series.utctime_now
    :members:

Function deltahours
===================
.. autoclass:: shyft.time_series.deltahours
    :members:

Function deltaminutes
=====================
.. autoclass:: shyft.time_series.deltaminutes
    :members:

Class time
==========
.. autoclass:: shyft.time_series.time
    :members:

Class YMDhms
============
.. autoclass:: shyft.time_series.YMDhms
    :members:

Class YWdhms
============
.. autoclass:: shyft.time_series.YWdhms
    :members:

Class TzInfo
============
.. autoclass:: shyft.time_series.TzInfo
    :members:

Class Calendar
==============
.. autoclass:: shyft.time_series.Calendar
    :members:

Class UtcPeriod
===============
.. autoclass:: shyft.time_series.UtcPeriod
    :members:

Class UtcTimeVector
===================
.. autoclass:: shyft.time_series.UtcTimeVector
    :members:

Time series
###########

Elements in this category are the actual time series.

Class TimeAxis
==============
.. autoclass:: shyft.time_series.TimeAxis
    :members:

Class TimeSeries
================
.. autoclass:: shyft.time_series.TimeSeries
    :members:

Class TsVector
==============
.. autoclass:: shyft.time_series.TsVector
    :members:

Time series expressions
#######################

The elements in this category implement the time series expressions solution.

Class TsBindInfo
================
.. autoclass:: shyft.time_series.TsBindInfo
    :members:

DTSS - The Distributed Time series System
#########################################

The elements in this category implements the the DTSS.
The DTSS provides ready to use services and components,
which is useful in itself.

In addition, the services are extensible by python hooks,
callbacks, that allow the user to extend/adapt the functionality
to cover other time-series data base backends and services.

Note that DTSS is not a data-base as such, but do have a built in high performance time-series db.
The DTSS is better viewed as **computing component/service**,
that are capable of evaluating time-series expressions, extracting the wanted information,
and sending it back to the clients.
One of the important properties of the DTSS is that we can bring the heavy computations to where
the data is located. In addition it as a specialized advanced caching system that allows evaluations
to run on memory(utilizing multi-core evaluations).

The open design allows it to utilize any existing legacy ts-databases/services through customization points.

Class DtsServer
===============
.. autoclass:: shyft.time_series.DtsServer
    :members:

Class DtsClient
===============
.. autoclass:: shyft.time_series.DtsClient
    :members:

Class TsInfo
============
.. autoclass:: shyft.time_series.TsInfo
    :members:

Class CacheStats
================
.. autoclass:: shyft.time_series.CacheStats
    :members:

Geo-location Time series
########################

The elements in this section integrate the generic time series concepts above
with a geo-spatial co-ordinate system. This functionality extends to co-ordinate
based queries in the time series storage.

Class GeoPoint
==============
.. autoclass:: shyft.time_series.GeoPoint
    :members:

Class GeoTimeSeries
===================
.. autoclass:: shyft.time_series.GeoTimeSeries
    :members:

Class GeoTimeSeriesVector
=========================
.. autoclass:: shyft.time_series.GeoTimeSeriesVector
    :members:

Class GeoQuery
==============
.. autoclass:: shyft.time_series.GeoQuery
    :members:

Class GeoSlice
==============
.. autoclass:: shyft.time_series.GeoSlice
    :members:

Class GeoTsMatrix
=================
.. autoclass:: shyft.time_series.GeoTsMatrix
    :members:

Class GeoMatrixShape
====================
.. autoclass:: shyft.time_series.GeoMatrixShape
    :members:

Class GeoGridSpec
=================
.. autoclass:: shyft.time_series.GeoGridSpec
    :members:

Class GeoEvalArgs
=================
.. autoclass:: shyft.time_series.GeoEvalArgs
    :members:

Class GeoTimeSeriesConfiguration
================================
.. autoclass:: shyft.time_series.GeoTimeSeriesConfiguration
    :members:

Working with time series
########################

The elements in this section define how code shall behave or are actual tools
dealing with time series.

Policies
========

The elements in this section describe how time series are interpreted.

Class convolve_policy
---------------------
.. autoclass:: shyft.time_series.convolve_policy
    :members:

Class derivative_method
-----------------------
.. autoclass:: shyft.time_series.derivative_method
    :members:

Class extend_fill_policy
------------------------
.. autoclass:: shyft.time_series.extend_fill_policy
    :members:

Class extend_split_policy
-------------------------
.. autoclass:: shyft.time_series.extend_split_policy
    :members:

Class interpolation_scheme
--------------------------
.. autoclass:: shyft.time_series.interpolation_scheme
    :members:

Class point_interpretation_policy
---------------------------------
.. autoclass:: shyft.time_series.point_interpretation_policy
    :members:

Class trim_policy
-----------------
.. autoclass:: shyft.time_series.trim_policy
    :members:

Tools
=====

The elements in this section work with time series.

Class KrlsRbfPredictor
----------------------
.. autoclass:: shyft.time_series.KrlsRbfPredictor
    :members:

Class QacParameter
------------------

Qac = Quality Assurance Controls

.. autoclass:: shyft.time_series.QacParameter
    :members:

Hydrology
=========

The elements in this section are hydrology specific.

Class IcePackingParameters
--------------------------
.. autoclass:: shyft.time_series.IcePackingParameters
    :members:

Class IcePackingRecessionParameters
-----------------------------------
.. autoclass:: shyft.time_series.IcePackingRecessionParameters
    :members:

Class ice_packing_temperature_policy
------------------------------------
.. autoclass:: shyft.time_series.ice_packing_temperature_policy
    :members:

Class RatingCurveFunction
-------------------------
.. autoclass:: shyft.time_series.RatingCurveFunction
    :members:

Class RatingCurveParameters
---------------------------
.. autoclass:: shyft.time_series.RatingCurveParameters
    :members:

Class RatingCurveSegment
------------------------
.. autoclass:: shyft.time_series.RatingCurveSegment
    :members:

Class RatingCurveSegments
-------------------------
.. autoclass:: shyft.time_series.RatingCurveSegments
    :members:

Class RatingCurveTimeFunction
-----------------------------
.. autoclass:: shyft.time_series.RatingCurveTimeFunction
    :members:

Class RatingCurveTimeFunctions
------------------------------
.. autoclass:: shyft.time_series.RatingCurveTimeFunctions
    :members:
