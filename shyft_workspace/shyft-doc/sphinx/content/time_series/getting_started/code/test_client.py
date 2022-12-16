from typing import Tuple
import numpy as np
import argparse

from shyft.api import Calendar
from shyft.api import DoubleVector, IntVector
from shyft.api import DtsClient
from shyft.api import TimeAxis
from shyft.api import TimeSeries
from shyft.api import TsVector
from shyft.api import point_interpretation_policy as point_fx
from shyft.api import time, utctime_now


class TsGridStore:
    """ just a skeleton class to enforce naming convention for a grid-typed ts data store """

    def __init__(self, fc_type: str, n_x: int, n_y: int):
        self.fc_type: str = fc_type
        self.c: Calendar = Calendar()
        self.n_x: int = n_x
        self.n_y: int = n_y

    def ts_url(self, t: time, x: int, y: int) -> str:
        dt = self.c.calendar_units(t)
        return f'shyft://forecast/{dt.year:04}_{dt.month:02}_{dt.day:02}T{dt.hour:02}/c_{x:04}_{y:04}/{self.fc_type}'

    def fc_request(self, *, t: time, range_x: Tuple[int, int], range_y: Tuple[int, int]) -> TsVector:
        """ generate the named (unbound) time-series of the series we want to deal with, slice in the grid-area"""
        return TsVector([TimeSeries(self.ts_url(t, x, y)) for x in range(range_x[0], range_x[1]) for y in range(range_y[0], range_y[1])])

    def generate_forecast_data(self, *, t: time, fc_time_axis: TimeAxis) -> TsVector:
        """ Generate named time-series filled with sin(t) type data over the grid and specified time-axis"""
        x_y = float(self.n_x + self.n_y)
        return TsVector([
            TimeSeries(self.ts_url(t, x, y),
                       TimeSeries(fc_time_axis,
                                  DoubleVector.from_numpy(
                                      np.sin(float(x + y)/x_y + np.linspace(0, len(fc_time_axis)/(3.14*12), num=len(fc_time_axis), dtype=np.float64))),
                                  point_fx=point_fx.POINT_AVERAGE_VALUE)
                       )
            for x in range(self.n_x) for y in range(self.n_y)]
        )





def test_write_forecast(year:int, n_fc:int, dtss_host:str):
    utc = Calendar()
    n_hours = 66
    fc_interval = time(6*3600)  # every 6th hour
    t_begin = utc.time(year, 1, 1)  
    t_end = utc.add(t_begin, fc_interval, n_fc)  
    fc_times = TimeAxis(t_begin, fc_interval, utc.diff_units(t_begin, t_end, fc_interval))  # convinience, use time-axis for the sequence
    gs = TsGridStore(fc_type='precipitation_mm_h', n_x=100, n_y=100)  # Use the grid store.
    c = DtsClient(dtss_host)
    t_sum = 0.0  # sum used storage time
    mpt = 100*100*66/1.0e6
    for p in fc_times:
        ta = TimeAxis(p.start, time(3600), n_hours)
        fc = gs.generate_forecast_data(t=ta.time(0), fc_time_axis=ta)
        t0 = utctime_now()
        c.store_ts(fc, overwrite_on_write=True, cache_on_write=True)  # replace existing, cache while writing(speed up next read)
        t1 = utctime_now()
        t_sum += float(t1 - t0)
        print(f'{p.start} store_ts time was {float(t1-t0)} -> {mpt/float(t1-t0)} mill pts/sec')

    c.close()
    print(f'time used to store {n_fc} of 100x100 66h took {t_sum}')
    assert t_sum > 0.0


def test_read_forecast(year:int,n_fc:int,dtss_host:str):
    utc = Calendar()
    n_hours = 66
    fc_interval = time(6*3600)  # every 6th hour
    t_begin = utc.time(year, 1, 1)  # start in 2016
    t_end = utc.add(t_begin,fc_interval,n_fc)
    fc_times = TimeAxis(t_begin, fc_interval, utc.diff_units(t_begin, t_end, fc_interval))  # convinience, use time-axis for the sequence
    gs = TsGridStore(fc_type='precipitation_mm_h', n_x=100, n_y=100)  # Use the grid store.
    c = DtsClient(dtss_host)
    t_sum = 0.0  # sum used storage time
    mpt = 100*100*66/1.0e6
    for p in fc_times:
        ta = TimeAxis(p.start, time(3600), n_hours)
        fc_r = gs.fc_request(t=p.start, range_x=(0, 100), range_y=(0, 100))
        t0 = utctime_now()
        r = c.evaluate(fc_r, ta.total_period(), update_ts_cache=True)  # it defaults to use cache, if available, new reads updates cache
        t1 = utctime_now()
        t_sum += float(t1 - t0)
        print(f'{p.start} read time was {float(t1-t0)} -> {mpt/float(t1-t0)} mill pts/sec')

    c.close()
    print(f'time used to read {n_fc} of 100x100 ts=66h {t_sum} seconds')


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='Run a dts client against the server for testing')
    parser.add_argument('--port_no',type=int,default=20000,help='port number(default 20000) to use, typical range 10000..50000')
    parser.add_argument('--dtss_host',type=str,help='ip, or hostname where the dtss-server runs')
    parser.add_argument('--action',type=str,help='write_db or read_db')
    parser.add_argument('--year',type=int,help='start at specified year')
    parser.add_argument('--n_forecasts',type=int,help='number of forecasts to read or write start at specified year')
    a=parser.parse_args()
    dtss_host=f'{a.dtss_host}:{a.port_no}'
    if a.action=='write_db':
        test_write_forecast(a.year, a.n_forecasts, dtss_host)
    elif a.action=='read_db':
        test_read_forecast(a.year, a.n_forecasts, dtss_host)
    else:
        print('unknown --action argument "{a.action}"')
        parser.print_help()
    

