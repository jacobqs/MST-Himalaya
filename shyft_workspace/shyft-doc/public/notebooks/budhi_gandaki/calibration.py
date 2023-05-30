# Pure python modules and jupyter notebook functionality
# first you should import the third-party python modules which you'll use later on
# the first line enables that figures are shown inline, directly in the notebook
print('Starting Shyft calibration program...\n')
print('\nWelcome! Please enter the folder name of your configuration files (.yaml)\n')
folder_name = input()
if type(folder_name) != str:
    raise Exception('Input must be of type string')
print('\nImporting packages...\n')
import os
import datetime as dt
from os import path
import sys
from matplotlib import pyplot as plt
import xarray as xr

from shyft.hydrology import shyftdata_dir


# shyftdata_dir should be set before starting jupyter notebook with shell command:
# $ export SHYFT_DATA = "path_to_shyft_data" 
# this export command can be added to ~/.bashrc profile

# try to auto-configure the path, -will work in all cases where doc and data
# are checked out at same level

# shyft_data_path = os.path.abspath("../../../../shyft-data/")
# if path.exists(shyft_data_path) and 'SHYFT_DATA' not in os.environ:
#     os.environ['SHYFT_DATA']=shyft_data_path
    
# shyft should be available either by it's install in python
# or by PYTHONPATH set by user prior to starting notebook.
# This is equivalent to the two lines below
#  shyft_path=path.abspath('../../../shyft')
#  sys.path.insert(0,shyft_path)
# importing the shyft modules needed for running a calibration
from shyft.hydrology.repository.default_state_repository import DefaultStateRepository
from shyft.hydrology.orchestration.configuration.yaml_configs import YAMLCalibConfig, YAMLSimConfig
from shyft.hydrology.orchestration.simulators.config_simulator import ConfigSimulator, ConfigCalibrator

print('\nPackages sucessfully imported...\n')
# conduct a configured simulation first.
config_file_path = os.path.join(shyftdata_dir, f"budhi_gandaki/yaml_config-tin/{folder_name}/budhi_gandaki_simulation_tin.yaml")

print('\nCreating simulation...\n')
cfg_sim = YAMLSimConfig(config_file_path, "budhi_gandaki")
simulator = ConfigSimulator(cfg_sim) 
# run the model, and we'll just pull the `api.model` from the `simulator`

simulator.run()
state = simulator.region_model.state

print('\nSimulation finished running\n')

print('\nSetting up config\n')
# # set up configuration using *.yaml configuration files
config_file_path = os.path.join(shyftdata_dir,f"budhi_gandaki/yaml_config-tin/{folder_name}/budhi_gandaki_calibration_tin.yaml") # here is the *.yaml file
cfg_conf = YAMLCalibConfig(config_file_path, "budhi_gandaki")

print('\nConfig setup finished\n')

# initialize an instance of the orchestration's ConfigCalcalibrator class, which has all the functionality needed
# to run a calibration using the above initiated configuration
print('\nInitializing ConfigCalcalibrator...\n')
calib = ConfigCalibrator(cfg_conf)
n_cells = calib.region_model.size()
state_repos = DefaultStateRepository(calib.region_model)  # Notice that this repository needs the real model
#                                                           so that it's able to generate a precise
#                                                           default state-with-id vector for this
#                                                           specific model

# once the calibrator is set up, all you need to do is running the calibration...
# the calibrated parameters are stored in a model.yaml. 
print('\nRunning calibration...\n')
results = calib.calibrate(cfg_conf.sim_config.time_axis, state_repos.get_state(0), 
                          cfg_conf.optimization_method['name'],
                          cfg_conf.optimization_method['params'])
print('\nCalibration finished...\n')
# Get NSE of calibrated run:
result_params = []
for i in range(results.size()):
    result_params.append(results.get(i))
print(f'\nFinal NSE = {1-calib.optimizer.calculate_goal_function(result_params)}\n')