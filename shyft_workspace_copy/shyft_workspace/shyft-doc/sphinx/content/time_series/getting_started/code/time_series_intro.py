from shyft.time_series import (
        TimeSeries, TimeAxis, Calendar, point_interpretation_policy
)

ta = TimeAxis(0, 1, 4)
values = [0, 3, 1, 4]

ts_instant = TimeSeries(
        ta=ta,
        values=values,
        point_fx=point_interpretation_policy.POINT_INSTANT_VALUE
        ) 

print(ts_instant(0))    # 0.0
print(ts_instant(1))    # 3.0
print(ts_instant(1.5))  # 2.0
print(ts_instant(3.5))  # 4.0
print(ts_instant(4.0))  # nan

ts_average = TimeSeries(
        ta=ta,
        values=values,
        point_fx=point_interpretation_policy.POINT_AVERAGE_VALUE
        ) 


print(ts_average(0))    # 0.0
print(ts_average(1))    # 3.0
print(ts_average(1.5))  # 3.0
print(ts_average(3.5))  # 4.0
print(ts_average(4.0))  # nan


## Utility functions

ta = TimeAxis(0, 1, 4)
values = [0, 3, 1, 4]

ts = TimeSeries(
        ta=ta,
        values=values,
        point_fx=point_interpretation_policy.POINT_AVERAGE_VALUE
        )

print(ts(1)) # 3.0

print(ts.point_interpretation()) # POINT_AVERAGE_VALUE

print(ts.size()) # 4

print(ts.time_axis) # TimeAxis('1970-01-01T00:00:00Z', 1s, 4)

print(ts.values.to_numpy()) # [0. 3. 1. 4.]

#from shyft.time_series import Calendar, TimeAxis, UtcTimeVector
#from pandas import DataFrame
#from numpy import arange, int64
#
## NUMPY
#dv_np = arange(10, dtype=int64)
#time_points = UtcTimeVector.from_numpy(dv_np)
#end_date = time_points[-1] + 1.0
#ta = TimeAxis(time_points=time_points, t_end=end_date)
#
## PANDAS
#df = DataFrame()
#df["dates"] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#time_points2 = UtcTimeVector.from_numpy(df["dates"])
#ta2 = TimeAxis(time_points=time_points2, t_end=end_date)
#
#
#from datetime import datetime
#from shyft.time_series import Calendar, TimeAxis, UtcTimeVector
#
## define a number of observations for this example
#utc = Calendar()
#
## create a list with times for some days in a strongly typed container
## NOTE: these are regularly spaced periods, but all examples work on irregular periods as well.
#time_points1 = UtcTimeVector([utc.time(2020, 1, x) for x in range(1, 4)])
#
## create time axis, adding an artificial point t_end to create a last period from
## the last data point
#ta1 = TimeAxis(time_points=time_points1, t_end=(time_points1[-1]+1.0))
#
## ===== get the index of a time on the axis
#idx = ta1.index_of(time_points1[-1])  # returns 2
## this does not need to be exactly a time point
#slightly_after = ta1.index_of(utc.time(2020, 1, 1, 12))  # returns 0 (index of the first point)
## note that this returns int.max when the index cannot be found
#before = ta1.index_of(utc.time(2019, 12, 31))  # returns 18446744073709551615
#after = ta1.index_of(utc.time(2020, 1, 31))  # returns 18446744073709551615
## alternatively, this returns the index that contains t, or is before t
## but: also returns int.max when time is before the start time
#before2 = ta1.open_range_index_of(utc.time(2019, 12, 31))  # returns 18446744073709551615
#after2 = ta1.open_range_index_of(utc.time(2020, 1, 31))  # returns 2
#
## ===== Periods
## get the total period that the time axis spans
## WARNING: This includes the point t_end that defines the last period!
#period = ta1.total_period()  # returns [2020-01-01T00:00:00Z,2020-01-03T00:00:01Z>
## get the i'th period between point i and i+1 in the axis
## here, this is the last defined period between the last data point date and t_end.
## NOTE: The underlying code is C++ and only deals with positive indices. The Python
##       ability to denote negative indices is not supported.
#idx_period = ta1.period(idx) # returns [2020-01-03T00:00:00Z,2020-01-03T00:00:01Z>
## you can also ask for the start time for the i'th period.
#idx_period_start = ta1.time(idx) # returns 2020-01-03T00:00:00Z
## get the number of periods in the axis
#number_of_periods = ta1.size()  # returns 3
## A time axis can be sliced by periods
## from given time index for a number of periods
#sub_ta = ta1.slice(0, 2)
## The list of periods can be iterated
#for p in ta1:
#    print(p)  # returns periods like [2020-01-03T00:00:00Z,2020-01-03T00:00:01Z>
#
## ===== merging
## Creates a new time-axis that contains the union of time-points/periods of the two time-axis.
## Create a TA for a period not overlapping the above
#time_points2 = UtcTimeVector([utc.time(2020, 2, x) for x in range(1, 4)])
#ta2 = TimeAxis(time_points=time_points2, t_end=(time_points2[-1]+1.0))
#ta3 = ta1.merge(ta2)
## Create a TA for a period overlapping ta3
#time_points3 = UtcTimeVector([utc.time(2020, 1, x) for x in range(2, 32)])
#ta4 = TimeAxis(time_points=time_points3, t_end=(time_points3[-1]+1.0))
#ta5 = ta4.merge(ta3)
#
## ===== accessing points
## as raw values
## NOTE: this will include the artificial last period end point t_end!
#list_of_ints = ta5.time_points
#list_of_flts = ta5.time_points_double
