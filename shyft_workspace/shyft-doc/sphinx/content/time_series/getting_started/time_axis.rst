.. _UsageTimeAxis:

TimeAxis
========

The chapter :ref:`ConceptTimeSeries` outlined that a sequence of time points can be interpreted as
a list of non-overlapping time periods. This is represented by a ``TimeAxis`` object which is able
to deal with fixed period time series as well as irregularly spaced time periods.

As the ``TimeAxis`` object is fundamental to a :ref:`UsageTimeSeries` object, it needs to be 
created before the actual TimeSeries can be created. Its usage requires understanding 
:ref:`UsageCalendarTime`.

There are several ways to create a ``TimeAxis`` and the right approach depends on the faced problem
and available data.

Create a TimeAxis object
^^^^^^^^^^^^^^^^^^^^^^^^
Fixed interval time axis
""""""""""""""""""""""""

The simplest time axis is defined by a start time, a delta time value and the number of periods.
This is also the most efficient one.
To create the time axis we need a starting point ``t0``, length of periods ``dt`` and how 
many periods ``n``. 
The code below will create a time axis from the 01.01.2020 UTC until 08.01.2020 UTC with 24 hour 
periods.

.. literalinclude:: code/time_axis.py
   :language: python
   :lines: 1-11


Ireggular interval time axis
""""""""""""""""""""""""""""
A time axis with irregularly spaced time periods can be created with the list of defined time
points. The input time points are the starting point of each period, and we must add a last 
argument ``t_end`` to declare the end of the last period. 

.. literalinclude:: code/time_axis.py
   :language: python
   :lines: 21-26

.. note::
   If the ``t_end`` is not supplied the time axis will assume that the last point in the list
   is the end of the last period.

Calendar time axis
""""""""""""""""""
The third option when creating a time axis is a calendar time axis, this will make the time axis
aware of what a month is in a calendar setting, as well as daylight savings time.

.. literalinclude:: code/time_axis.py
   :language: python
   :lines: 29-34

And we can compare this with a fixed time axis

.. literalinclude:: code/time_axis.py
   :language: python
   :lines: 37-48

Here we see that the calendar time axis (first column) always start the first of every calendar
month at the start of the day, while in the fixed time axis it naively goes 2592000 seconds
(``Calendar.MONTH``) forward.


A few helpful functions
^^^^^^^^^^^^^^^^^^^^^^^

A few helpful functions that helps us explore a given time axis.

``total_period()`` returns a ``UtcPeriod`` that spans the total period of the time axis.


.. literalinclude:: code/time_axis.py
   :language: python
   :lines: 43-44

``time_points`` returns an ``numpy.array`` with each starting point per period 
as well as the end of the last period.

.. literalinclude:: code/time_axis.py
   :language: python
   :lines: 46-48

.. note::
   ``time_points`` returns time points in second resolution, as of now we need to use
   ``time_points_double`` to get sub-second resolution

``size()`` returns the number of periods in the time axis.

.. literalinclude:: code/time_axis.py
   :language: python
   :lines: 50-51

