.. _UsageTimeSeries:

TimeSeries
==========

After the successful creation of a :ref:`UsageTimeAxis`, a Shyft ``TimeSeries`` can be 
instantiated. In Shyft we see the ``TimeSeries`` as a function that can be evaluated at any time 
point ``f(t)``. If we evaluate the ``TimeSeries`` outside of any interval we have set it will
return ``NaN``. Inside defined intervals it will interpolate between values, how it will
be interpolated will depend on what type of ``TimeSeries`` we use.

A time series can be instantiated by giving a ``TimeAxis``, ``ta``, a set of values, ``values``,
and the point intepretation, ``point_fx``, you want the time series to have.
The available point interpretations are ``POINT_INSTANT_VALUE`` and ``POINT_AVERAGE_VALUE``.
These are available in ``shyft.time_series.point_interpretation_policy``.

Time series types
"""""""""""""""""

``POINT_INSTANT_VALUE``
^^^^^^^^^^^^^^^^^^^^^^^

A ``POINT_INSTANT_VALUE`` is a time series where a value is linearly interpolated between
the start and end points of each interval. 
So if we create a 4 interval time axis and input the values ``[0, 3, 1, 4]`` as shown below

.. literalinclude:: code/time_series_intro.py
   :language: python
   :lines: 1-12

it will produce a time series on the form

.. code-block:: python
                   
                t3_____t4
          t1     /
          /\    /
         /  \  /
        /    \/
    t0 /     t2

and evaluating the time series at different time points we can see how it 
interpolates between the points.

.. literalinclude:: code/time_series_intro.py
   :language: python
   :lines: 14-18

.. note:: 

    Worth noticing is that in the last time interval it extrapolates the last value
    as a straight line since it does not have a last value to interpolate to.
    

``POINT_AVERAGE_VALUE``
^^^^^^^^^^^^^^^^^^^^^^^

A ``POINT_AVERAGE_VALUE`` is a time series type where the whole interval has 
the same value. 

.. literalinclude:: code/time_series_intro.py
   :language: python
   :lines: 20-24

.. code-block:: python

                   t3______t4
         t1_____    |
           |   |    |
           |   |    |
           |   |____|
    t0_____|   t2  


And evaluating the average time series at the same points as the instant series
shows the differences between their interpolation

.. literalinclude:: code/time_series_intro.py
    :language: python
    :lines: 27-31


Inspection functions
""""""""""""""""""""

To inspect the time series there exists a few utility functions we should
know about.

TimeSeries(t: int/float/time)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If we call the time series with an ``int``, ``float`` or ``time`` object it will
evaluate itself on the specific time point and return the value.

.. literalinclude:: code/time_series_intro.py
    :language: python
    :lines: 36-45

point_interpretation()
^^^^^^^^^^^^^^^^^^^^^^

Returns the point interpretation of the time series.

.. literalinclude:: code/time_series_intro.py
    :language: python
    :lines: 47-47

size()
^^^^^^

Returns the number of intervals in the time series

.. literalinclude:: code/time_series_intro.py
    :language: python
    :lines: 49-49

time_axis
^^^^^^^^^

Returns the time axis of the time series

.. literalinclude:: code/time_series_intro.py
    :language: python
    :lines: 51-51

values.to_numpy()
^^^^^^^^^^^^^^^^^

Returns a numpy array with the values it was set up with

.. literalinclude:: code/time_series_intro.py
    :language: python
    :lines: 53-53


General time series manipulation
""""""""""""""""""""""""""""""""
For a comprehensive list of available functions see :meth:`shyft.time_series.TimeSeries`.
The time series in Shyft are thought of as mathematical expressions and not indexed values.
This makes the manipulation of time series a bit different than with numpy arrays or pandas series.
We set up some convenience functions to inspect the time series.

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 1-9

Arithmetics
^^^^^^^^^^^
Doing basic arithmetics with time series is as simple as with numbers.

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 11-34

We can also do the same arthmetic on two time series

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 35-47

One thing to notice when we do arithmetics on time series is if they have different 
time axis. So if we for example have two time series with partial overlap in time, 
only overlapping time intervals will be defined.

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 48-103

Since ``ts2`` is not defined in the intervals 1 to 11, the resulting time series
will not be defined in that period either. The same goes for where ``ts1`` is not defined.


Mathematical operations
^^^^^^^^^^^^^^^^^^^^^^^
There are many built-in functions to help with manipulating time series in Shyft. These examples are
not exhaustive, so please refer to the documentation on :meth:`shyft.time_series.TimeSeries` for a complete
list.

Average
+++++++
The average function takes only one argument, and that is a time axis. It then calculates
the true average over that time axis. We create two time axis, both with a period of a week,
but one with daily resolution and one with hourly resolution. Then we create two hourly time series,
one stair case and one linear, with linearly increasing values. After that we average both of them
with the daily time axis.

.. math::
    \begin{align*}
    \bar{f}(T) &= \frac{1}{n}\sum_{t=T_{\text{start}}}^{T_{\text{end}}} f(t) &&\text{if } f(t) \neq NaN\\
    \text{where}&\\
    T &= \text{period to average over}\\
    n &= \text{number of non-NaN points in period}\\
    \end{align*}


.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 106-131

.. note::
    
    The point interpretation of a time series that is created from an averaging will always be
    a stair case series

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 133-136

Accumulate
++++++++++
Accumulate takes a time axis as input and returns a new time series where the i'th value
is the integral from ``t0`` to ``ti``.

.. math::
    \begin{align*}
    TS(t_i) &= \int_{t=t_0}^{t=t_i}ts(t)dt\\
    \text{where}&\\
    TS &= \text{Accumulated time series}\\
    ts &= \text{original time series}\\
    \end{align*}

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 138-149

.. note::
    Integral operations on shyft time series are done with a ``dt`` of seconds, which means
    we have to divide by the ``dt`` of the time axis we accumulate over


Derivative
++++++++++
We can derivate a time series forwards, backwards or center. As with accumulate the operations
happen on second resolution and therefore we need to multiply by the ``dt`` of the time axis.

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 151-161


Integral
++++++++
We can integrate a time series over a specified time axis.

.. math::
    \begin{align*}
    TS(T) &= \int_{t=T_{\text{start}}}^{T_{\text{end}}}ts(t)dt &&\text{if } ts(t) \neq NaN\\
    \text{where}&\\
    TS &= \text{integrated time series}\\
    ts &= \text{original time series}\\
    T &= \text{period to integrate over}\\
    \end{align*}

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 163-165

Statistics
++++++++++
With the statistics function we can directly get the different percentiles over a specified
time axis.

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 167-177


Utility functions
^^^^^^^^^^^^^^^^^
Here is a small collection of helpful functions when manipulating or extracting information
from time series.

Inside
++++++
This function creates a new time series with values where it is either inside or outside a 
defined range. We can set the minimum and maximum value of the range, the value it should use where
it  meets ``NaN``, and also the values to set where it is inside or outside the range.
By default ``NaN`` will continue to be ``NaN``, inside range will be 1 and outside range 0.

.. math::
    \begin{equation*}
    TS(t) =
    \begin{cases}
    1, &\text{if } \text{min_v} \leq ts(t) \lt \text{max_v}\\
    0 &\text{otherwise}
    \end{cases}
    \end{equation*}

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 180-191

To have no upper or lower limit we set the ``min_v`` or ``max_v`` to ``NaN``.

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 193-195

Here we check if values are inside the range 25-65 and set map inside values to 10 and outside values
to 20.

Max/min
+++++++
These function returns a new time series with filled in values of whichever value that is 
maximum/minimum of the input value or value in the time series.

.. math::
    \begin{equation*}
    max_v = 10\\
    TS(t) = 
    \begin{cases}
    10, &\text{if } ts(t) \leq 10\\
    ts(t) &\text{if } ts(t) \gt 10
    \end{cases}
    \end{equation*}
    

.. math::
    \begin{equation*}
    min_v = 10\\
    TS(t) = 
    \begin{cases}
    ts(t), &\text{if } ts(t) \leq 10\\
    10 &\text{if } ts(t) \gt 10
    \end{cases}
    \end{equation*}
    
.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 197-203

Time shift
++++++++++
This function shifts the values forward or backward in time on the basis of a ``dt``.
It moves forward for positive time step and backwards for negative time step. 

.. literalinclude:: code/time_series_expressions.py
    :language: python
    :lines: 205-214

As we can see here the values stay the same, but the time axis has been shifted an hour forward.

