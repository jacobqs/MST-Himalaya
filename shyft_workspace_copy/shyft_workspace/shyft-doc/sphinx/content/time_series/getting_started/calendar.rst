.. _UsageCalendar:

Calendar
========

The Shyft time series package provides a precise ``Calendar`` type that takes into account issues such as summer and
winter times as well as leap years. A ``Calendar`` instance is used to create :ref:`UsageTimeAxis` objects which in
return are the foundation for the creation of :ref:`UsageTimeSeries` objects.

Create a Calendar object
^^^^^^^^^^^^^^^^^^^^^^^^
The creation of a ``Calendar`` object is straightforward as the following code snippet demonstrates.

.. literalinclude:: code/calendar.py
   :language: python
   :lines: 1-10
 

.. _UsageCalendarTime:

Calendar and time
^^^^^^^^^^^^^^^^^

The calendar is integral in "understanding" time points. The ``Calendar`` object deals with all intricacies
of time zones without being cumbersome.
   
.. literalinclude:: code/calendar.py
   :language: python
   :lines: 13-73

Other methods to translate UTC epoch time stamps and date time using a ``Calendar`` instance.
For more information see `Wikipedia - ISO week date <https://en.wikipedia.org/wiki/ISO_week_date>`_.

.. literalinclude:: code/calendar.py
   :language: python
   :lines: 73-89


Python datetime to Shyft time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As outlined in the chapter :ref:`ConceptTime`, only epoch time stamps are truly unique and native Python ``datetime``
objects have difficulties when dealing with time zones.

Once in the Shyft space, you are safe, but the translation is unfortunately your responsibility.

.. literalinclude:: code/calendar.py
   :language: python
   :lines: 92-107
