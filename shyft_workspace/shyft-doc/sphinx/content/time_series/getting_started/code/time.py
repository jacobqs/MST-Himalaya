
from shyft.time_series import time, utctime_now

# The current timestamp in microsecond resolution is returned as follows.
now = utctime_now()                # time(1584352047.236503)

# Create a time from a well defined iso8601 string.
t0 = time('2018-10-15T16:30:15Z')  # time(1539621015)

# We can get the string back by using the built-int str
t0_string = str(t0)                # '2018-10-15T16:30:15Z'   

# Create a time from an integer (Seconds) or a float (microseconds).
t1 = time(3600)                    # time(3600)

t2 = time(0.123456)                # time(0.123456)

# NOTE: Any information after microseconds gets rounded.
t3 = time(0.1234568)               # time(0.123457)


from shyft.time_series import min_utctime, max_utctime, no_utctime 
print(min_utctime)  # time(-9223372036854.775391)
print(max_utctime)  # time(9223372036854.775391)
print(no_utctime)   # time(-9223372036854.775391)


from shyft.time_series import time, deltahours, deltaminutes

# Create a point in time
t1 = time(3600)  # time(3600)

# Add two hours aka 7200 seconds
t2 = t1 + deltahours(2)  # time(10800)

# Subtract a minute aka 60 seconds
t3 = t1 - deltaminutes(1)  # time(3540)

# time can be added or subtracted directly
t4 = t1 + time(3600)  # time(7200)

# converting back
my_int = int(t4)    # 7200
my_dbl = float(t4)  # 7200.0

# time integrates fine with operators on different types
is_equal1 = (t4 == 7200)    # True
is_equal2 = (t4 == 7200.0)  # True
unordered = [t4, 7200, 7199.9, 7199,  7200.1]
unordered.sort()            # [7199, 7199.9, time(7200), 7200, 7200.1]


from shyft.time_series import UtcPeriod, time

# ==== Creation
# create from integer epoch timestamps
period1 = UtcPeriod(1, 2)                  # [1970-01-01T00:00:01Z,1970-01-01T00:00:02Z>
# create from microseconds float epoch timestamps
period2 = UtcPeriod(1.000001, 2.000002)    # [1970-01-01T00:00:01.000001Z,1970-01-01T00:00:02.000002Z>
# create from time objects
period3 = UtcPeriod(time(4), time(5))      # [1970-01-01T00:00:04Z,1970-01-01T00:00:05Z>

# WARNING: The constructor WILL accept invalid values!
period4 = UtcPeriod(2, 1)    # [not-valid-period>
period5 = UtcPeriod()        # [not-valid-period>
# the type exposes a method to check if start<=end
is_valid4 = period4.valid()  # returns False
is_valid5 = period5.valid()  # returns False

# ==== contains
# Accepts int, float and time as input types
is_contains = period1.contains(1.000001)   # True
is_not_contains = period1.contains(3)      # False

# ==== overlaps
is_overlap = UtcPeriod.overlaps(period1, period2)      # True
is_not_overlap = UtcPeriod.overlaps(period1, period3)  # False

# ==== intersection
# Returns the intersection period between two periods
intersection_valid = UtcPeriod.intersection(period1, period2)   # [1970-01-01T00:00:01.000001Z,1970-01-01T00:00:02Z>
# It returns an invalid empty period, if the periods do not overlap
intersection_invalid = UtcPeriod.intersection(period1, period3) # [not-valid-period>

# ==== timespan 
delta_t = period1.timespan()  # time(1)

# ==== to_string
period_string = period1.to_string()  # '[1970-01-01T00:00:01Z,1970-01-01T00:00:02Z>'

# ==== start and end
p1_start = period1.start  # time(1)
p1_end = period1.end      # time(2)
