import xarray as xr
from .append_elapsed_time import append_elapsed_time

def interpolate_xarray(xarray, labels: list, interp_method='linear'):
    """
    Performs time interpolation on variables specified by labels.
    Args:
        xarray: xarray.DataArray that is of OG1 format.
        labels: list of (str) labels that the user would like to apply time interpolation to.
        interp_method: Choice of interpolation method. ('cubic' will give smoother transitions)

    Returns:
        xarray: xarray.DataArray that has had time-interpolation applied to the selected labels.
    """
    temp_xarray = xarray.copy()
    if 'ELAPSED_TIME' not in temp_xarray.keys():
        temp_xarray = append_elapsed_time(temp_xarray)

    for label in labels:
        temp_xarray[label] = (temp_xarray[label].swap_dims({'N_MEASUREMENTS': 'ELAPSED_TIME'})
                              .interpolate_na(dim='ELAPSED_TIME', method=interp_method)
                              ).swap_dims({'ELAPSED_TIME': 'N_MEASUREMENTS'})
    return temp_xarray