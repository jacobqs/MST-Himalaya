Time series expressions
=======================

As mentioned in time-series concept, we consider time-series as a function,

y = f(t),

where the type of y and t is a number.


Shyft provides all mathematical operators to work on time-series, they are f(t), in addition to
a convinient set of functions of general usage, as well as more domain specific functions.

Overloads for mathematical operators and functions are provided for both time-series and time-series vectors,
so that you can write code like this:

.. code-block:: python

    from shyft.time_series import (TimeSeries,TimeAxis)


    def example_fx(a:TimeSeries, b:TimeSeries, x:float) -> TimeSeries:
        return 3.14*(a*x + b).pow(1.9)

Notice that the inputs to the function are TimeSeries, that could be expressions!
Also note that the returned result is just another expression, that can be further used.

Also note that those inputs can be expressions of time-series that are unbound, symbolic,
so there are NO numbers/values involved (yet!).

Combined with the DTSS (the Distributed TimeSeries System), and the model-based approach, this
differentiate the this approach from many other popular libraries and systems.

It enables scaling, performance in both computational and abstractional(model) sense.

For more information, please check `Wikipedia - Time series <https://en.wikipedia.org/wiki/Time_series>`_.

And also important reference to functions, also check `Wikipedia - Functions <https://en.wikipedia.org/wiki/Function_(mathematics)>`_.
