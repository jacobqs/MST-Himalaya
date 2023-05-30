'''
  DOWNLOAD WFDE5 data
  How to download the near-surface-meteorological-variables from the CDS API. Here version 2.1 is used.
  Each variable is downloaded and saved as a zip file with the name of each variable.
'''

import cdsapi

### Hindu Kush-Himalayan region extent 
# (Bajracharya, SR; Shrestha, B (eds) (2011) The status of glaciers in the Hindu Kush-Himalayan region. Kathmandu: ICIMOD)

north = 39.31
west = 60.85
south = 15.95
east = 105.04

#### Bundhi Gandaki catchment #####

#south = 27.8333
#north = 29.0000
#west = 84.5000
#east = 85.1667

c = cdsapi.Client()



variables = [#'near_surface_specific_humidity', 
            #'grid_point_altitude', 
            'near_surface_air_temperature', 
            #'near_surface_specific_humidity', 
            #'near_surface_wind_speed', 
            #'rainfall_flux', 
            #'snowfall_flux', 
            #'surface_air_pressure', 
           #'surface_downwelling_longwave_radiation',
           #'surface_downwelling_shortwave_radiation'
           ]

for variable in variables:
    c.retrieve(
        'derived-near-surface-meteorological-variables',
        {   'area': [north, west, south, east],
            'variable': f'{variable}',
            #cru_and_gpcc
            'reference_dataset': 'cru',
            'year': [
                '1990', '1991', '1992',
                '1993', '1994', '1995',
                '1996', '1997', '1998',
                '1999', '2000', '2001',
                '2002', '2003', '2004',
                '2005', '2006', '2007',
                '2008', '2009', '2010',
                '2011', '2012', '2013',
                '2014', '2015', '2016',
                '2017', '2018', '2019',
            ],
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'version': '2.1',
            'format': 'tgz'
            
        },
        f'{variable}.tgz')

