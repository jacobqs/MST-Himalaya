import os
import glob
import xarray as xr
import dask
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dask.config.set({"array.slicing.split_large_chunks": False})
class GeoTsObject:

    def __init__(self):
        self.home_dir = os.getenv("HOME")
        self.wfde5_path = self.home_dir + '/Documents/MST Himalaya/WFDE5/'
        # Paths to WFDE5 data
        self.psurf_path = glob.glob(self.wfde5_path + 'psurf/*.nc')
        self.qair_path = glob.glob(self.wfde5_path + 'qair/*.nc')
        self.rainf_path = glob.glob(self.wfde5_path + 'rainf/*.nc')
        self.snowf_path = glob.glob(self.wfde5_path + 'snowf/*.nc')
        self.swdown_path = glob.glob(self.wfde5_path + 'swdown/*.nc')
        self.tair_path = glob.glob(self.wfde5_path + 'tair/*.nc')
        self.wind_path = glob.glob(self.wfde5_path + 'wind/*.nc')
        self.asurf_path = glob.glob(self.wfde5_path + 'asurf/*.nc')
        
        # All forcing paths
        self.forcing_paths = [self.psurf_path, self.qair_path, self.rainf_path,
                            self.snowf_path, self.tair_path, self.swdown_path, self.wind_path]
        
        # Paths to cell data
        self.cell_data_path = glob.glob(self.wfde5_path + 'cell_data/*.nc')

        # Discharge data
        self.discharge_path = glob.glob(self.home_dir + '/Documents/MST Himalaya/discharge/*.txt')

        # Name of forcing variables
        self.forcing_variables = ['pressure_pa', 'specific_humidity_kgkg', 'rainfall_flux_kgms', 
                                'snowfall_flux_kgms', 'temperature_K','shortwave_down_wm',  
                                'wind_speed_ms']
        
    def read_netcdf(self, as_dataframe = False):
        forcing_data = dict()
        for i, name in enumerate(self.forcing_variables):
                forcing_data[name] = xr.open_mfdataset(self.forcing_paths[i])
        if as_dataframe:
            for i in forcing_data.keys():
                forcing_data[i] = forcing_data[i].to_dataframe()
        return forcing_data


def resample(forcing_dataset: dict, resolution: str ):

    resampled_dataset = dict()

    for i, name in enumerate(forcing_dataset.keys()):
            
            if resolution == 'D':
                if name == 'precipitation_mmh':
                    resampled_dataset[name] = forcing_dataset[name].resample(time = resolution).sum()
                elif name in {'shortwave_down_wm','sw_down_wm','temperature_degc','wind_speed_ms','specific_humidity_kgkg', 'psurf_hpa' ,'pressure_hpa'}:
                     resampled_dataset[name] = forcing_dataset[name].resample(time = resolution).sum()
                else:
                    print(f'Cannot resample {name}')
            elif resolution == 'M':
                if name == 'precipitation_mmh':
                    resampled_dataset[name] = forcing_dataset[name].resample(time = resolution).sum()
                elif name in {'shortwave_down_wm','sw_down_wm','temperature_degc','wind_speed_ms','specific_humidity_kgkg', 'psurf_hpa' ,'pressure_hpa'}:
                     resampled_dataset[name] = forcing_dataset[name].resample(time = resolution).mean()
                else:
                    print(f'Cannot resample {name}')
            elif resolution == 'Y':
                if name == 'precipitation_mmh':
                    resampled_dataset[name] = forcing_dataset[name].resample(time = resolution).sum()
                elif name in {'shortwave_down_wm','sw_down_wm','temperature_degc','wind_speed_ms','specific_humidity_kgkg', 'psurf_hpa' ,'pressure_hpa'}:
                     resampled_dataset[name] = forcing_dataset[name].resample(time = resolution).mean()
                else:
                    print(f'Cannot resample {name}')
            elif resolution == ('season' or 'S'):
                month_length = forcing_dataset[name].time.dt.days_in_month
                # Calculate the weights by grouping by 'time.season'.
                weights = (
                    month_length.groupby("time.season") / month_length.groupby("time.season").sum()
                )
                # Test that the sum of the weights for each season is 1.0
                np.testing.assert_allclose(weights.groupby("time.season").sum().values, np.ones(4))

                if name == 'precipitation_mmh':
                    # Calculate the weighted average
                    resampled_dataset[name] = (forcing_dataset[name] * weights).groupby("time.season").sum(dim="time")
                elif name in {'shortwave_down_wm','sw_down_wm','temperature_degc','wind_speed_ms','specific_humidity_kgkg', 'psurf_hpa' ,'pressure_hpa'}:
                     resampled_dataset[name] = (forcing_dataset[name] * weights).groupby("time.season").mean(dim="time")
                else:
                    print(f'Cannot resample {name}')
            else:
                print('Not a valid time resolution')
    
    return resampled_dataset

def plot_months(dataset, title):
    notnull = pd.notnull(dataset[0])

    fig, axes = plt.subplots(nrows=6, ncols=2, figsize=(14, 12))

    # DJF

    dataset.sel(month = 1).where(notnull).plot.pcolormesh(
                    ax=axes[0, 0],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[0, 0].set_ylabel('January')

    dataset.sel(month = 2).where(notnull).plot.pcolormesh(
                    ax=axes[0, 1],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[0, 1].set_ylabel('February')

    dataset.sel(month = 3).where(notnull).plot.pcolormesh(
                    ax=axes[1, 0],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[1, 0].set_ylabel('March')

    dataset.sel(month = 4).where(notnull).plot.pcolormesh(
                    ax=axes[1, 1],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[1, 1].set_ylabel('April')

    dataset.sel(month = 5).where(notnull).plot.pcolormesh(
                    ax=axes[2, 0],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[2, 0].set_ylabel('May')

    dataset.sel(month = 6).where(notnull).plot.pcolormesh(
                    ax=axes[2, 1],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[2, 1].set_ylabel('June')

    dataset.sel(month = 7).where(notnull).plot.pcolormesh(
                    ax=axes[3, 0],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[3, 0].set_ylabel('July')

    dataset.sel(month = 8).where(notnull).plot.pcolormesh(
                    ax=axes[3, 1],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[3, 1].set_ylabel('August')

    dataset.sel(month = 9).where(notnull).plot.pcolormesh(
                    ax=axes[4, 0],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[4, 0].set_ylabel('September')

    dataset.sel(month = 10).where(notnull).plot.pcolormesh(
                    ax=axes[4, 1],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[4, 1].set_ylabel('October')

    dataset.sel(month = 11).where(notnull).plot.pcolormesh(
                    ax=axes[5, 0],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[5, 0].set_ylabel('November')

    dataset.sel(month = 12).where(notnull).plot.pcolormesh(
                    ax=axes[5, 1],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[5, 1].set_ylabel('December')

    for ax in axes.flat:
        ax.axes.get_xaxis().set_ticklabels([])
        ax.axes.get_yaxis().set_ticklabels([])
        ax.axes.axis("tight")
        ax.set_xlabel("")

    plt.tight_layout()

    fig.suptitle(title, fontsize=16, y=1.02)


def plot_monthly_mean(dataset_monthly: dict, variable_names: list):
    for var_name in variable_names:

        if var_name in {'pressure_pa', 'rainfall_flux_kgms', 'snowfall_flux_kgms', 'temperature_K'}:
            pass
        else:
            if var_name == 'temperature_degc':
                name = 'Tair_degc'
                #vmin = -25
                #vmax = 40
                title = 'Montly Surface Air Temperature'
                dataset_monthly_means = dataset_monthly[var_name][name].groupby('time.month').mean()
                plot_months(dataset_monthly_means, title)
            elif var_name == 'precipitation_mmh':
                name = 'Precip'
                #vmin= 0
                #vmax= 1.0
                title = 'Monthly Precipitation'
                dataset_monthly_means = dataset_monthly[var_name][name].groupby('time.month').sum()
                plot_months(dataset_monthly_means, title)
            elif var_name == 'pressure_hpa':
                name = 'PSurf_hpa'
                #vmin= 600
                #vmax=1015
                title = 'Monthly Surface pressure'
                dataset_monthly_means = dataset_monthly[var_name][name].groupby('time.month').mean()
                plot_months(dataset_monthly_means, title)
            elif var_name == 'specific_humidity_kgkg':
                name = 'Qair'
                #vmin= 0.001
                #vmax= 0.025
                title = 'Monthly Specific Humidity'
                dataset_monthly_means = dataset_monthly[var_name][name].groupby('time.month').mean()
                plot_months(dataset_monthly_means, title)
            elif var_name == 'shortwave_down_wm':
                name = 'SWdown'
                #vmin= 100
                #vmax= 345
                title = 'Monthly Short Wave Radiation'
                dataset_monthly_means = dataset_monthly[var_name][name].groupby('time.month').mean()
                plot_months(dataset_monthly_means, title)
            elif var_name == 'wind_speed_ms':
                name = 'Wind'
                #vmin= 0
                #vmax= 11
                title = 'Monthly Surface Wind Speed '
                dataset_monthly_means = dataset_monthly[var_name][name].groupby('time.month').mean()
                plot_months(dataset_monthly_means, title)


def plot_seasons(dataset, title):
    notnull = pd.notnull(dataset[0])

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 12))

    # DJF

    dataset.sel(season='DJF').where(notnull).plot.pcolormesh(
                    ax=axes[0, 0],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[0, 0].set_ylabel('DJF')

    dataset.sel(season='MAM').where(notnull).plot.pcolormesh(
                    ax=axes[0, 1],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[0, 1].set_ylabel('MAM')

    dataset.sel(season='JJA').where(notnull).plot.pcolormesh(
                    ax=axes[1, 0],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[1, 0].set_ylabel('JJA')

    dataset.sel(season='SON').where(notnull).plot.pcolormesh(
                    ax=axes[1, 1],
                    #vmin= vmin,
                    #vmax=vmax,
                    cmap="Spectral_r",
                    add_colorbar=True,
                    extend="both",
                )

    axes[1, 1].set_ylabel('SON')

    for ax in axes.flat:
        ax.axes.get_xaxis().set_ticklabels([])
        ax.axes.get_yaxis().set_ticklabels([])
        ax.axes.axis("tight")
        ax.set_xlabel("")

    plt.tight_layout()

    fig.suptitle(title, fontsize=16, y=1.02)


def plot_seasonal_mean(dataset_seasonally: dict, variable_names: list):

    

    for var_name in variable_names:

        if var_name in {'pressure_pa', 'rainfall_flux_kgms', 'snowfall_flux_kgms', 'temperature_K'}:
            pass
        else:
            if var_name == 'temperature_degc':
                name = 'Tair_degc'
                #vmin = -25
                #vmax = 40
                title = 'Seasonal Surface Air Temperature'
                plot_seasons(dataset_seasonally[var_name][name], title)
            elif var_name == 'precipitation_mmh':
                name = 'Precip'
                #vmin= 0
                #vmax= 1.0
                title = 'Seasonal Precipitation'
                plot_seasons(dataset_seasonally[var_name][name], title)
            elif var_name == 'pressure_hpa':
                name = 'PSurf_hpa'
                #vmin= 600
                #vmax=1015
                title = 'Seasonal Surface pressure'
                plot_seasons(dataset_seasonally[var_name][name], title)
            elif var_name == 'specific_humidity_kgkg':
                name = 'Qair'
                #vmin= 0.001
                #vmax= 0.025
                title = 'Seasonal Specific Humidity'
                plot_seasons(dataset_seasonally[var_name][name], title)
            elif var_name == 'shortwave_down_wm':
                name = 'SWdown'
                #vmin= 100
                #vmax= 345
                title = 'Seasonal Short Wave Radiation'
                plot_seasons(dataset_seasonally[var_name][name], title)
            elif var_name == 'wind_speed_ms':
                name = 'Wind'
                #vmin= 0
                #vmax= 11
                title = 'Seasonal Surface Wind Speed '
                plot_seasons(dataset_seasonally[var_name][name], title)

            