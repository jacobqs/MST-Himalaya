.. _ConceptTimeSeries:

What is a time series?
======================

A time series in Shyft is considered to be a function of time, f(t) -> float.

This is more general, and different from many systems and popular libraries,
that consider and represents, time-series as a sequence of time-value pairs,
often tied together using some clever indexing scheme.

We enable users to work with time-series as a function, and thus also enabling
the mathematical and statistical skills of the users.

This also allows for composition, of functions, expressions that have well defined
and known results. Another important aspect is that it allows for defining expressions,
and evaluating those lazy, later, at another server(the backend).

So, in Shyft, time-series are f(t).

A simple example to illustrate how this changes the focus of the code into generic,
always valid mathematical formulas and definitions.

.. code-block:: python

    from shyft.time_series import (TimeSeries,TimeAxis)


    def income_rate(spot_price: TimeSeries, production: TimeSeries) -> TimeSeries:
        """"
        Args:
           spot_price: in units [EUR/J]
           production: in units [J/s]
        Returns:
         income rate in SI units [EUR/s]
        """
        return spot_price * production  # unit analysis: [EUR/J] x [J/s] -> [ EUR/s]


    def periodic_income(income_rate:TimeSeries,income_periods:TimeAxis) -> TimeSeries:
        """
        Args:
          income_rate: in units [EUR/s]
          income_periods: to compute income for
        Returns:
          income in SI unit [EUR] for each of the income_periods specified
        """
        return income_rate.integral(income_periods) # unit analysis: [EUR/s] x dt[s] -> [EUR]

For a classical definition of time-series, please check `Wikipedia - Time series <https://en.wikipedia.org/wiki/Time_series>`_.
And also important reference to functions, also check `Wikipedia - Functions <https://en.wikipedia.org/wiki/Function_(mathematics)>`_.

