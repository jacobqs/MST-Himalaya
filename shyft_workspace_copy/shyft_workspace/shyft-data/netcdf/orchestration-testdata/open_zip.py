from zipfile import ZipFile
import glob
import xarray as xr

years = []
for i in range(1990,2020):
    years.append(str(i))

variable_names = ['/precipitation/precipitation', 'temperature/temperature', 'rel_hum/rel_hum', 'radiation/radiation']
file_names = []
for j in years:
    for k in variable_names:
        # specifying the zip file name
        file_name = f"{k}_{j}.nc.zip"
        file_names.append(file_name)
    
for l in file_names:
    # opening the zip file in READ mode
    with ZipFile(l, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        print(f'-----Extracting {variable_names} now...------')
        zip.extractall()

years = []
for i in range(1999,2017):
    years.append(str(i))

variable_names = ['wind_speed/wind_speed']
file_names = []

for j in years:
    for k in variable_names:
        # specifying the zip file name
        file_name = f"{k}_{j}.nc.zip"
        file_names.append(file_name)
    
for l in file_names:
    # opening the zip file in READ mode
    with ZipFile(l, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        print(f'-----Extracting {variable_names} now...------')
        zip.extractall()
        print('------Done extracting all data-------')

print('------Getting paths to files------')

precip_paths = glob.glob('precipitation*.nc')
temperature_paths = glob.glob('temperature*.nc')
rel_hum_paths = glob.glob('rel_hum*.nc')
radiation_paths = glob.glob('radiation*.nc')
wind_speed_paths = glob.glob('wind_speed*.nc')

print('------Opening files-------')

precip = xr.open_mfdataset(precip_paths)
temperature = xr.open_mfdataset(temperature_paths)
rel_hum = xr.open_mfdataset(rel_hum_paths)
radiation = xr.open_mfdataset(radiation_paths)
wind_speed = xr.open_mfdataset(wind_speed_paths)

print('-------Writing NETCDF4 files-------')

precip.to_netcdf(path = 'precipitation.nc', format = 'NETCDF4')
temperature.to_netcdf(path = 'temperature.nc', format = 'NETCDF4')
rel_hum.to_netcdf(path = 'relative_humidity.nc', format = 'NETCDF4')
radiation.to_netcdf(path = 'radiation.nc', format = 'NETCDF4')
wind_speed.to_netcdf(path = 'wind_speed.nc', format = 'NETCDF4')

print('-------Done making netCDF files. All files correctly extracted!-----')