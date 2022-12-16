.. _UsageTime:

Time
====

As outlined in the chapter :ref:`ConceptTime`, only epoch time stamps are truly unique and native Python datetime
objects have difficulties when dealing with time zones.

Shyft uses for time representation the UTC epoch time stamp which is an a floating point value whose value expresses
seconds before the comma and microseconds after the comma in form of a ``time`` object. This section gives an
introduction to the type.

Create a time object
^^^^^^^^^^^^^^^^^^^^
The creation of a ``time`` object is straightforward as the following code snippet demonstrates.

.. literalinclude:: code/time.py
   :language: python
   :lines: 2-19

.. note::

   Note that Shyft only parses a subset of ISO8601 so many perfectly valid time strings produces errors, and it does not even parse every time string it produces itself. For example replacing the Z with a +01 will not work and will return a RuntimeError


There are three time constants that represent respectivly the least and largest time representable, and invalid time.
The minimum and maximum time constructs are mostly usefull as default values, and for creating time periods spanning "all" of time.
Invalid time may be returned by some functions to represent that whatever operation it were to do did not work,
and some Shyft constructs initialize to it by default.

.. literalinclude:: code/time.py
   :language: python
   :lines: 22-25


Using a time object
^^^^^^^^^^^^^^^^^^^

The time object is the basis for all time operations within Shyft. Its main usage for end users is in conjunction with a
:ref:`UsageCalendar` object as outlined in section :ref:`UsageCalendarTime`. Nevertheless, basic arithmetic is possible.

.. literalinclude:: code/time.py
   :language: python
   :lines: 28-50


Containers
^^^^^^^^^^

The following types help collating time information. These are used as data containers
and do by themselves not provide additional functionality. Often, these are method
return types.

UtcPeriod
"""""""""

An instance of the type ``UtcPeriod`` defines the half-open utc-time interval [*start*..*end*> where
*end* is required to be equal or greater than *start*. Periods are building blocks of a
:ref:`UsageTimeAxis`.

.. literalinclude:: code/time.py
   :language: python
   :lines: 53-93


YMDhms
""""""

An instance of the type ``YMDhms`` defines the Calendar coordinates specifying Y, M, D, h, m, s and μs.
While this looks like a Python datetime, this type is specifically a container without any further
functionality. It is only used as return type and you can access the data via its properties.

YWdhms
""""""

An instance of the type ``YWdhms`` defines the Calendar coordinates y, iso-week number, iso-week day,
h, m, s and μs. It is only used as return type and you can access the data via its properties.
