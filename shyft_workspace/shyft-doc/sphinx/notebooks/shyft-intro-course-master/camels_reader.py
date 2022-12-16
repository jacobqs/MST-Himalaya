import numpy as np
import pandas as pd

from shyft import api

class TestData():
    def __init__(self):
        self.met_filename = r"test_data/06191500_lump_cida_forcing_leap.txt"
        self.streamflow_filename = r"test_data/06191500_streamflow_qc.txt"
        self._station_info, self._df_met = self._get_met_data_from_camels_database()
        self._df_streamflow = self._get_streamflow_data_from_camels_database()
        self.temperature = self._df_met['temperature'].values
        self.precipitation = self._df_met['precipitation'].values
        self.radiation = self._df_met['radiation'].values
        self.relative_humidity = self._df_met['relative_humidity'].values
        self.wind_speed = self._df_met['wind_speed'].values
        self.time = self._df_met['time'].values
        self.discharge = self._df_streamflow.discharge
        self.area = self._station_info['area']
        # TODO assure time is same; assure same length of all;


    def _get_met_data_from_camels_database(self):
        station_info = {}
        with open(self.met_filename) as data:
            station_info['lat'] = float(data.readline())  # latitude of gauge
            station_info['z'] = float(data.readline())  # elevation of gauge (m)
            station_info['area'] = float(data.readline())  # area of basin (m^2)
        keys = ['Date', 'dayl', 'precipitation', 'radiation', 'swe', 'tmax', 'tmin', 'vp']
        df = pd.read_table(self.met_filename, skiprows=4, names=keys)
        df["temperature"] = (df["tmin"] + df["tmax"]) / 2.
        df.pop("tmin")
        df.pop("tmax")
        df["precipitation"] = df["precipitation"] / 24.0 # mm/h
        df["wind_speed"] = df["temperature"] * 0.0 + 2.0  # no wind speed in camels
        df["relative_humidity"] = df["temperature"] * 0.0 + 0.7  # no relative humidity in camels
        df["time"] = self._get_utc_time_from_daily_camels_met(df['Date'].values)
        return station_info, df

    def _get_streamflow_data_from_camels_database(self):
        keys = ['sgid','Year','Month', 'Day', 'discharge', 'quality']
        df = pd.read_table(self.streamflow_filename, names=keys, delim_whitespace=True)
        time = self._get_utc_time_from_daily_camels_streamgauge(df.Year, df.Month, df.Day)
        df['time'] = time
        df.discharge.values[df.discharge.values == -999] = np.nan
        df.discharge = df.discharge * 0.0283168466  # feet3/s to m3/s
        #df.discharge[df.discharge == -999] = np.nan  # set missing values to nan
        return df

    def _get_utc_time_from_daily_camels_met(self, datestr_lst):
        utc = api.Calendar()
        time = [utc.time(*[int(i) for i in date.split(' ')]).seconds for date in datestr_lst]
        return np.array(time) - 12*3600 # shift by 12 hours TODO: working nicer?

    def _get_utc_time_from_daily_camels_streamgauge(self, year, month, day):
        utc = api.Calendar()
        time = [utc.time(int(y), int(m), int(d)).seconds for y,m,d in zip(year, month, day)]
        return np.array(time)
