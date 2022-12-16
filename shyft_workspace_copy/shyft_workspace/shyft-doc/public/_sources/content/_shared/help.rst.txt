.. note::

   This Python package is a wrapper around a C++ library. In contrast to Python, C++ allows
   `function overloading <https://en.wikipedia.org/wiki/Function_overloading>`_ which leads
   to some confusion in some `IDEs <https://en.wikipedia.org/wiki/Integrated_development_environment>`_
   like `PyCharm <https://www.jetbrains.com/pycharm/>`_ and to doc strings unfamiliar to pure
   Python developers i.e. full C++ call signatures.

   The code in this package is designed to make use of standard help functionality in Python.
   You are able to access help functionality using tab completion or `help()`. The "?" or "??"
   standards in IPython work, but seem at times to be limited with respect to some of the
   doc strings. Therefore, we encourage you to please use `help`.

   If you use `help(shyft_object)` and get something that is looks a bit overwhelming or unfamiliar,
   just realize that the methods are generally showing how to call a method and what it returns.
   If you see `(object)arg1` or `(object)self` as a first argument to a method, that simply means
   `the class itself is the first argument <https://www.programiz.com/article/python-self-why>`_.

   Example:

   .. code-block:: bash

      $ python
      Python 3.8.8 (default, Feb 24 2021, 15:54:32) [...]
      Type "help", "copyright", "credits" or "license" for more information.
      >>>import shyft.time_series
      >>>help(shyft.time_series.Calendar)

      [...]

      |  Static methods defined here:
      |
      |  __init__(...)
      |      __init__( (Calendar)arg1) -> None
      |
      |      __init__( (Calendar)arg1, (time)tz_offset) -> None :
      |          creates a calendar with constant tz-offset
      |
      |          Args:
      |              tz_offset (time): specifies utc offset, time(3600) gives UTC+01 zone
      |
      |
      |      __init__( (Calendar)arg1, (int)tz_offset) -> None :
      |          creates a calendar with constant tz-offset
      |
      |          Args:
      |              tz_offset (int): seconds utc offset, 3600 gives UTC+01 zone
      |
      |
      |      __init__( (Calendar)arg1, (str)olson_tz_id) -> None :
      |          create a Calendar from Olson timezone id, eg. 'Europe/Oslo'
      |
      |          Args:
      |              olson_tz_id (str): Olson time-zone id, e.g. 'Europe/Oslo'
      [...]

   What this means is that the *class* ``Calendar`` may be instantiated as either:

   1. ``Calendar()``, returning an UTC Calendar
   2. ``Calendar(200)``, indicating a fixed offset of 200 seconds from UTC
   3. ``Calendar('Europe/Oslo')`` where the calendar will be 'tied' to the "Europe/Oslo" timezone.