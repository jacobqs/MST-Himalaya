from shyft.time_series import Calendar

# Create a utc-based calendar.
utc = Calendar()

# Create a calendar representing a specific timezone.
osl = Calendar("Europe/Oslo")

# Create a calendar that has a fixed offset to UTC of 3600 sec (one hour).
std = Calendar(3600) # UTC+01


from shyft.time_series import Calendar

# define the calendar for Oslo
osl = Calendar("Europe/Oslo")

# A Calendar is more informative than the usual time zone
osl.tz_info.name()            # "Europe/Oslo"
osl.tz_info.base_offset()     # time(3600)

# List of all the region ID's available
print(list(Calendar.region_id_list()))

# Get the UTC epoch timestamp for a point in time in Oslo
# Please note that this is 1 hour before local DST change
# NOTE: minutes, seconds, microseconds also possible
t0 = osl.time(2021, 3, 28, 1)        # 2021-03-28T00:00:00Z

# Calendars has a `to_string` function which gives a ISO8601 string
print(osl.to_string(t0))             # 2021-03-28T01:00:00+01

# Add fixed time period
# This will add an absolute amount of time aka day = 86400 seconds
t1 = t0 + Calendar.DAY               # 2021-03-29T00:00:00Z

# Add time period through the calendar (aware of DST change)
# WARNING: this will miss an hour in absolute terms
t2 = osl.add(t0, Calendar.DAY, 1)    # 2021-03-28T23:00:00Z

# Subtraction works similarly.
# t3 is equal to t0.
t3 = osl.add(t2, Calendar.DAY, -1)

# Analyse time point differences
# WARNING: This rounds down
osl.diff_units(t0, t1, Calendar.DAY)    # 1
osl.diff_units(t0, t1, Calendar.WEEK)   # 0
osl.diff_units(t0, t1, Calendar.MONTH)  # 0 (!)

# Analyse time points
osl.tz_info.is_dst(t0)            
# returns True if daylight saving time, False otherwise
osl.tz_info.utc_offset(t0)  # time(3600)
osl.quarter(t0)             # 1
osl.day_of_year(t0)         # 87

# Calendars can be used to determine notable time points
# rounds the timestamp down to the beginning of the day
d = osl.trim(t0, Calendar.DAY)
# 2021-03-27T23:00:00Z aka 2021-03-28 00:00 OSL in UTC

# rounds the timestamp down to the beginning of the iso week (Monday)
w = osl.trim(t0, Calendar.WEEK)
# 2021-03-21T23:00:00Z aka 2021-03-22 00:00 OSL in UTC

# rounds the timestamp down to the beginning of the month
m = osl.trim(t0, Calendar.MONTH)
# 2021-02-28T23:00:00Z aka 2021-03-01 00:00 OSL in UTC

# rounds the timestamp down to the beginning of the quarter
q = osl.trim(t0, Calendar.QUARTER)
# 2020-12-31T23:00:00Z aka 2021-01-01 00:00 OSL in UTC

# rounds the timestamp down to the beginning of the year
y = osl.trim(t0, Calendar.YEAR)
# 2020-12-31T23:00:00Z aka 2021-01-01 00:00 OSL in UTC


from shyft.time_series import Calendar

# define the calendar for Oslo
osl = Calendar("Europe/Oslo")

# Create from ISO week information (year, iso week number, iso day number)
# NOTE: hours, minutes, seconds, microseconds also possible
t0 = osl.time_from_week(2021, 34, 1)

# The reverse is also possible
# Note that the return types YWdhms and YMDhms are simple containers
cal_1 = osl.calendar_week_units(t0)
cal_2 = osl.calendar_units(t0)

# Calendar instances also allow for conversion between time zones
lap = Calendar("America/La_Paz")
cal_3 = lap.calendar_units(t0)   # returns YMDhms(2021,8,22,18,0,0)


from datetime import datetime
from pytz import timezone
from shyft.time_series import Calendar, time

# The Python native datetime must be given a time zone
# or it is interpreted as your computer's local time zone.
tz = timezone("Europe/Oslo")
dt = datetime(2021, 3, 28, 1)
dt_tz = tz.localize(dt)

# The easiest conversion is via the timestamp
t = time(dt_tz.timestamp())

# Verify
osl = Calendar("Europe/Oslo")
cal_1 = osl.calendar_units(t)    # returns YMDhms(2021,3,28,1,0,0)

