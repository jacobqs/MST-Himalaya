.. _ConceptTime:

Dealing with time
=================

UTC / GMT and DST
-----------------

`Coordinated Universal Time (UTC) <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_
was introduced as the more accurate replacement of
`Greenwich Mean Time (GMT) <https://en.wikipedia.org/wiki/Greenwich_Mean_Time>`_.
In 1963, the concept of UTC was established as the primary international
standard which would denote how other countries would regulate their time in
relation to UTC.

The primary reason why UTC was considered to be a more accurate system was the
fact that it used the rotation of Earth and atomic clocks for measurements.
Moreover, to maintain the consistent time system, UTC does not observe
`Daylight Saving Time (DST) <https://en.wikipedia.org/wiki/Daylight_saving_time>`_,
the shifting of time by an hour in summer and winter so that darkness falls at a
later clock time.

Although GMT and UTC share the same current time in practice, there is a basic
difference between the two:

   1. GMT is a time zone officially used in some European and African countries.
   2. UTC is not a time zone, but a time standard that is the basis for civil
      time and time zones worldwide. This means that no country or territory
      officially uses UTC as a local time.

Neither UTC nor GMT ever change for Daylight Saving Time (DST). However, some of
the countries that use GMT switch to different time zones during their DST
period. For example, the United Kingdom is not on GMT all year, it uses British
Summer Time (BST), which is one hour ahead of GMT, during the summer months.

**UTC represents absolute time and therefore should be used for all program internal date/time representations.**

For more information, please check `Wikipedia - Coordinated Universal Time <https://en.wikipedia.org/wiki/Coordinated_Universal_Time>`_.

Epoch Timestamp
---------------

Date and time are very difficult to deal with correctly. Instead of using a
datetime object, it is easier to use Unix time (also known as Epoch time, POSIX
time, seconds since the Epoch or UNIX Epoch time) which is represented as a
simple integer.

The Epoch timestamp is the number of seconds that have elapsed since the
Unix epoch, minus leap seconds. The Unix epoch is 1970-01-01 00:00:00.0 UTC.

**Within Shyft, time is represented as number, with fixed digits expressed down to microseconds.**

For more information, please check `Wikipedia - Epoch (computing) <https://en.wikipedia.org/wiki/Epoch_(computing)>`_.

Python datetime vs. epoch
-------------------------

The following example outlines the issues when dealing with Python native datetime objects.

.. literalinclude:: code/timestamp.py
    :language: python

.. warning::

   When DST is applied ins Europe/Oslo, we either move an hour in March from 02:00 to 03:00, missing the hour 02:00
   and in October we go back at 03:00 to 02:00, leading to 03:00 happening again an hour later.
   So, 03:00 in October DST change leads to two exactly identical datetime objects! This
   cannot be represented correctly with lists of datetime objects!

**Shyft uses UTC epoch timestamps internally exclusively, and provides an intelligent** :ref:`UsageCalendar` **avoiding this issue.**

For more information, please check `Wikipedia - Daylight saving time <https://en.wikipedia.org/wiki/Daylight_saving_time>`_.
