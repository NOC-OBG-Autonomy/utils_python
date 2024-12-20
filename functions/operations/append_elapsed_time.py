import numpy as np
import xarray as xr

def append_elapsed_time(xarray):
    """
    Appends epoch and elapsed time to the xarray object
    Args:
        xarray: xarray object that is of OG1 format (requires the TIME variable)

    Returns:
        temp_xarray: xarray object with appended epoch and elapsed time
    """
    temp_xarray = xarray.copy()
    try:
        temp_xarray = xarray.assign(EPOCH_TIME=lambda x: x.TIME.astype('float'))
        temp_xarray.EPOCH_TIME.attrs = {'long_name': 'Time in nanoseconds since 01/01/1970',
                                        'units': 'ns',
                                        'standard_name': 'Epoch time',
                                        'valid_min': -np.inf,
                                        'valid_max': np.inf}
        temp_xarray = temp_xarray.assign(ELAPSED_TIME=lambda x: (x.EPOCH_TIME - x.EPOCH_TIME[0] ) *1e-9)
        temp_xarray.ELAPSED_TIME.attrs = {'long_name': 'Elapsed time in seconds since glider deployment',
                                          'units': 's',
                                          'standard_name': 'Elapsed time',
                                          'valid_min': 0,
                                          'valid_max': np.inf}
    except Exception as e:
        if type(e)==AttributeError:
            print('ERROR: The TIME variable does not appear in the netCDF file. These functions are only intended'
                  ' for use with OG1 format netCDF files.')
        else:
            print(f'{type(e)}: Something unexpected happened: \n {e}')
    return temp_xarray
    