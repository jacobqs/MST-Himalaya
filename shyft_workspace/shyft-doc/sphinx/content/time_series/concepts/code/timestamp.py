# -*- coding: utf-8 -*-
"""
This script contains an example showing the complexity of correctly handling
timezone and UTC using Python datetime objects.
"""

from datetime import datetime

from pytz import utc, timezone

# Express this point in time in Python datetime
# Most often, users leave out the time zone information, which is ambiguous.
my_day = datetime(2018, 3, 15)
print(f"{str(my_day)}       is tz unaware, but is assumed to be your local computer tz!")
# this is converted to the UTC based epoch timestamp
my_day_ts = my_day.timestamp()
print(f"{str(my_day)}       in your local computer tz as UTC epoch timestamp: {my_day_ts}")

print("===================")
# EXAMPLE: Convert timestamp back to datetime
print("WARNING: The reverse operation also depends on your local computer tz!")
# convert into tz unaware object, but UTC values
a = datetime.fromtimestamp(my_day_ts)
print(f"datetime.fromtimestamp(a)       : {str(a)} (in local computer TZ value)")
b = datetime.utcfromtimestamp(my_day_ts)
print(f"datetime.utcfromtimestamp(a)    : {str(b)} (UTC converted from local computer TZ)")
c = datetime.fromtimestamp(my_day_ts, utc)
print(f"datetime.fromtimestamp(a, utc)  : {str(c)} (UTC converted from local computer TZ)")
d = datetime.fromtimestamp(my_day_ts, timezone("America/La_Paz"))
print(f"datetime.fromtimestamp(a, LaPaz): {str(d)} (La Paz converted value, relative to local computer TZ)")
print("WARNING: The timestamp again depends on your local computer tz, if no timezone is defined!")
print(f"{str(a)}       as UTC epoch timestamp: {a.timestamp()}")
print(f"{str(b)}       as UTC epoch timestamp: {b.timestamp()} (!!!!)")
print(f"{str(c)} as UTC epoch timestamp: {c.timestamp()}")
print(f"{str(d)} as UTC epoch timestamp: {d.timestamp()}")

# PITFALL:
print("===================")
print("WARNING: Setting a time zone on an unaware datetime object does not convert!")
my_day_utc = utc.localize(my_day)
print(f"{str(my_day_utc)} the day set as UTC time zone (NOT a conversion!)")
my_day_utc_ts = my_day_utc.timestamp()
print(f"{str(my_day_utc)} as epoch timestamp: {my_day_utc_ts} (!!!!)")

print("===================")
print("The epoch time stamp uniquely identifies a point in time!")
print("Python datetime objects must be time zone aware to do the same and is cumbersome.")
