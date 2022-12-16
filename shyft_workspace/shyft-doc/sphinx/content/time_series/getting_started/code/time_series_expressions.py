from shyft.time_series import (
        time, TimeSeries, TimeAxis, POINT_AVERAGE_VALUE as stair_case,
        POINT_INSTANT_VALUE as linear, Calendar,
        FORWARD as d_forward, BACKWARD as d_backward, CENTER as d_center
        )


def show_values(text: str, ts: TimeSeries):
    print(f'{text}:\n {ts.values.to_numpy()}')


HOUR = time(3600)
values = list(range(24))

ta = TimeAxis(start=time('2021-01-01T00:00:00Z'), delta_t=HOUR, n=len(values))
ts = TimeSeries(ta=ta, values=values, point_fx=stair_case)

show_values('Initial TimeSeries', ts)
# Initial TimeSeries:
# [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17.
# 18. 19. 20. 21. 22. 23.]

ts_addition = ts + 2
ts_multiplication = ts*2

show_values('TimeSeries + 2', ts_addition)
#TimeSeries + 2:
# [ 2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17. 18. 19.
# 20. 21. 22. 23. 24. 25.]

show_values('TimeSeries*2', ts_multiplication)
#TimeSeries*2:
# [ 0.  2.  4.  6.  8. 10. 12. 14. 16. 18. 20. 22. 24. 26. 28. 30. 32. 34.
# 36. 38. 40. 42. 44. 46.]

values.reverse()
ts_reversed = TimeSeries(ta=ta, values=values, point_fx=stair_case)

show_values('TimeSeries + TimeSeries', ts + ts_reversed)
#TimeSeries + TimeSeries:
# [23. 23. 23. 23. 23. 23. 23. 23. 23. 23. 23. 23. 23. 23. 23. 23. 23. 23.
# 23. 23. 23. 23. 23. 23.]

show_values('TimeSeries*TimeSeries', ts*ts_reversed)
#TimeSeries*TimeSeries:
# [  0.  22.  42.  60.  76.  90. 102. 112. 120. 126. 130. 132. 132. 130.
# 126. 120. 112. 102.  90.  76.  60.  42.  22.   0.]

values.reverse()
ta1 = TimeAxis(start=time('2021-01-01T00:00:00Z'), delta_t=HOUR, n=len(values))
# time axis shifted 12 hours
ta2 = TimeAxis(start=time('2021-01-01T12:00:00Z'), delta_t=HOUR, n=len(values))

ts1 = TimeSeries(ta=ta1, values=values, point_fx=stair_case)
ts2 = TimeSeries(ta=ta2, values=values, point_fx=stair_case)
ts_addition = ts1 + ts2

show_values('TimeSeries.time_axis1 + TimeSeries.time_axis2', ts_addition)
#TimeSeries.time_axis1 + TimeSeries.time_axis2:
# [12. 14. 16. 18. 20. 22. 24. 26. 28. 30. 32. 34.]

print(f'{"t":15}{"ts1":10}{"ts2":10}{"ts1 + ts2":10}')
for t in map(int, sorted(set(list(ta1.time_points) + list(ta2.time_points)))):
    print(f'{t:<15}{ts1(t):<10}{ts2(t):<10}{ts_addition(t):<10}')

#t              ts1       ts2       ts1 + ts2 
#1609459200     0.0       nan       nan       
#1609462800     1.0       nan       nan       
#1609466400     2.0       nan       nan       
#1609470000     3.0       nan       nan       
#1609473600     4.0       nan       nan       
#1609477200     5.0       nan       nan       
#1609480800     6.0       nan       nan       
#1609484400     7.0       nan       nan       
#1609488000     8.0       nan       nan       
#1609491600     9.0       nan       nan       
#1609495200     10.0      nan       nan       
#1609498800     11.0      nan       nan       
#1609502400     12.0      0.0       12.0      
#1609506000     13.0      1.0       14.0      
#1609509600     14.0      2.0       16.0      
#1609513200     15.0      3.0       18.0      
#1609516800     16.0      4.0       20.0      
#1609520400     17.0      5.0       22.0      
#1609524000     18.0      6.0       24.0      
#1609527600     19.0      7.0       26.0      
#1609531200     20.0      8.0       28.0      
#1609534800     21.0      9.0       30.0      
#1609538400     22.0      10.0      32.0      
#1609542000     23.0      11.0      34.0      
#1609545600     nan       12.0      nan       
#1609549200     nan       13.0      nan       
#1609552800     nan       14.0      nan       
#1609556400     nan       15.0      nan       
#1609560000     nan       16.0      nan       
#1609563600     nan       17.0      nan       
#1609567200     nan       18.0      nan       
#1609570800     nan       19.0      nan       
#1609574400     nan       20.0      nan       
#1609578000     nan       21.0      nan       
#1609581600     nan       22.0      nan       
#1609585200     nan       23.0      nan       
#1609588800     nan       nan       nan       


t0 = time('2021-01-01T00:00:00Z')
ta_hourly = TimeAxis(start=t0, delta_t=HOUR, n=24*7)
ta_daily = TimeAxis(start=t0, delta_t=24*HOUR, n=7)

values = [i for i in range(ta_hourly.size())]
ts_stairs = TimeSeries(ta=ta_hourly, values=values, point_fx=stair_case)
ts_linear = TimeSeries(ta=ta_hourly, values=values, point_fx=linear)

show_values('Original stairs', ts_stairs)
#Original stairs:
# [  0.   1.   2.   3.   4. ... 163. 164. 165. 166. 167.]

show_values('Original linear', ts_linear)
#Original linear:
# [  0.   1.   2.   3.   4. ... 163. 164. 165. 166. 167.]

ts_stairs_avg = ts_stairs.average(ta_daily)
ts_linear_avg = ts_linear.average(ta_daily)

show_values('Daily stairs average', ts_stairs_avg)
#Daily stairs average:
# [ 11.5  35.5  59.5  83.5 107.5 131.5 155.5]

show_values('Daily linear average', ts_linear_avg)
#Daily linear average:
# [ 12.   36.   60.   84.  108.  132.  155.5]

print(f'Point interpretation of ts_stairs_avg: {ts_stairs_avg.point_interpretation()}\n'
      f'Point interpratation of ts_linear_avg: {ts_linear_avg.point_interpretation()}')
#Point interpretation of ts_stairs_avg: POINT_AVERAGE_VALUE
#Point interpratation of ts_linear_avg: POINT_AVERAGE_VALUE

ts_linear_hourly_acc = ts_linear.accumulate(ta_hourly)
ts_linear_daily_acc = ts_linear.accumulate(ta_daily)

show_values('Hourly accumulation', ts_linear_hourly_acc/HOUR)
#Hourly accumulation::
# [0.00 0.50 2.00 4.50 8.00 12.50
#  ... 
#  13122.0 13284.5 13448.0 13612.5 13778.0 13944.5]

show_values('Daily accumulation', ts_linear_daily_acc/(HOUR*24))
#Daily accumulation::
# [  0.  12.  48. 108. 192. 300. 432.]

show_values('Daily derivative forward', ts_stairs_avg.derivative(d_forward)*(HOUR*24))
#Daily derivative forward:
# [24. 24. 24. 24. 24. 24.  0.]

show_values('Daily derivative backward', ts_stairs_avg.derivative(d_backward)*(HOUR*24))
#Daily derivative backward:
# [ 0. 24. 24. 24. 24. 24. 24.]

show_values('Daily derivative center', ts_stairs_avg.derivative(d_center)*(HOUR*24))
#Daily derivative center:
# [12. 24. 24. 24. 24. 24. 12.]

show_values('Daily integral', ts_stairs.integral(ta=ta_daily)/(HOUR*24))
#Daily integral:
# [ 11.5  35.5  59.5  83.5 107.5 131.5 155.5]

show_values('Daily 10 percentile', ts_linear.statistics(ta=ta_daily, p=10))
#Daily 10 percentile:
# [  2.3  26.3  50.3  74.3  98.3 122.3 146.3]

show_values('Daily 50 percentile', ts_linear.statistics(ta=ta_daily, p=50))
#Daily 50 percentile:
# [ 11.5  35.5  59.5  83.5 107.5 131.5 155.5]

show_values('Daily 90 percentile', ts_linear.statistics(ta=ta_daily, p=90))
#Daily 90 percentile:
# [ 20.7  44.7  68.7  92.7 116.7 140.7 164.7]


t0 = time('2021-01-01T00:00:00Z')
ta = TimeAxis(start=t0, delta_t=HOUR, n=10)
values = [i*10 for i in range(ta.size())]
ts = TimeSeries(ta=ta, values=values, point_fx=linear)

show_values('Smaller than 50', ts.inside(min_v=float('nan'), max_v=50))
#Smaller than 50:
# [1. 1. 1. 1. 1. 0. 0. 0. 0. 0.]

show_values('Larger than 50', ts.inside(min_v=50, max_v=float('nan')))
#Larger than 50:
# [0. 0. 0. 0. 0. 1. 1. 1. 1. 1.]

show_values('Between 25 and 65', ts.inside(min_v=25, max_v=65, inside_v=10, outside_v=20))
#Between 25 and 65:
# [20. 20. 20. 10. 10. 10. 10. 20. 20. 20.]

show_values('Max of 40', ts.max(number=40))
#Max of 40:
# [40. 40. 40. 40. 40. 50. 60. 70. 80. 90.]

show_values('Min of 40', ts.min(number=40))
#Min of 40:
# [ 0. 10. 20. 30. 40. 40. 40. 40. 40. 40.]

ts_hour_shift = ts.time_shift(HOUR)

show_values('Shifted time series', ts_hour_shift)
#Shifted time series:
# [ 0. 10. 20. 30. 40. 50. 60. 70. 80. 90.]

print(ts.time_axis)
#TimeAxis('2021-01-01T00:00:00Z', 3600s, 10)
print(ts_hour_shift.time_axis)
#TimeAxis('2021-01-01T01:00:00Z', 3600s, 10)

