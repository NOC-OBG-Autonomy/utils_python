from ..operations.append_elapsed_time import append_elapsed_time
import xarray as xr
import numpy as np
import os, sys

def load_netcdf(file_path: str, convert_time=True):
    """
    Loads in the netCDF file from the file_path as a xarray object. Has options for adding a converted time column
    and time-interpolation of selected variables.
    Args:
        file_path: absolute or relative path to the netCDF file
        convert_time: If True, adds additional time columns (epoch seconds, elapsed seconds)

    Returns:
        xarray: xarray object containing the loaded netCDF file and any converted time columns
    """
    try:
        xarray = xr.open_dataset(os.path.normpath(file_path), engine="netcdf4")
    except Exception as e:
        print('ERROR: Something went wrong loading the netCDF file. ',
              'Try and absolute path and check it points to a .nc file.')
        print(f'Full error: {e}')
        sys.exit(1)
    if convert_time:
        xarray = append_elapsed_time(xarray)
    return xarray