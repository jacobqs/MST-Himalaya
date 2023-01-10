import os
import glob
import xarray as xr
import dask

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
        self.forcing_variables = ['pressure', 'specific_humidity', 'rainfall_flux', 
                                'snowfall_flux', 'temperature','shortwave_down',  
                                'wind_speed']
        
    def read_netcdf(self, as_dataframe = False):
        forcing_data = dict()
        for i, name in enumerate(self.forcing_variables):
                forcing_data[name] = xr.open_mfdataset(self.forcing_paths[i])
        if as_dataframe:
            for i in forcing_data.keys():
                forcing_data[i] = forcing_data[i].to_dataframe()
        return forcing_data