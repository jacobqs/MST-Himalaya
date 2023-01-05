from shyft.time_series import Calendar, TimeAxis, deltahours

# Create a utc-based calendar.
utc = Calendar()

t0 = utc.time(2020, 1, 1)
dt = deltahours(24) # alternatively: dt = Calendar.DAY
n = 7

ta = TimeAxis(start=t0, delta_t=dt, n=n)
# TimeAxis('2020-01-01T00:00:00Z', 86400s, 7)

# Create a list of irregular starting points of each period 
time_points = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Initialize a time axis with the time points
ta = TimeAxis(time_points=time_points, t_end=144)
# TimeAxis( '[1970-01-01T00:00:01Z,1970-01-01T00:02:24Z>', 10,array([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]))


osl = sts.Calendar('Europe/Oslo')

t0 = osl.time(2021, 3, 1)
dt = sts.Calendar.MONTH
n = 5
ta_osl = sts.TimeAxis(calendar=osl, start=t0, delta_t=dt, n=n)
# TimeAxis( Calendar('Europe/Oslo'), '2021-03-01T00:00:00+01', 2592000s, 5)

ta_fixed = sts.TimeAxis(t0, dt, n)
# TimeAxis('2021-03-28T20:00:00Z', 3600s, 5)

for t_osl, t_fix in zip(ta_osl.time_points, ta_fixed.time_points):
    print(f'{osl.to_string(int(t_osl))}  |  {osl.to_string(int(t_fix))}')

# 2021-03-01T00:00:00+01  |  2021-03-01T00:00:00+01
# 2021-04-01T00:00:00+02  |  2021-03-31T01:00:00+02
# 2021-05-01T00:00:00+02  |  2021-04-30T01:00:00+02
# 2021-06-01T00:00:00+02  |  2021-05-30T01:00:00+02
# 2021-07-01T00:00:00+02  |  2021-06-29T01:00:00+02
# 2021-08-01T00:00:00+02  |  2021-07-29T01:00:00+02


total_period = osl_ta.total_period()
# [2021-02-28T23:00:00Z,2021-07-31T22:00:00Z>

time_points = osl_ta.time_points
# array([1614553200, 1617228000, 1619820000, 1622498400, 1625090400,
#        1627768800])

size_ta = osl_ta.size()
# 5
