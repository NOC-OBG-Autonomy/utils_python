from gsw.density import rho
from .append_conservative_temp import *

def append_density(xarray):
    """
    Calculates density following TEOS-10 using conservative temp., absolute salinity and pressure. The result is
    appended to the xarray
    Args:
        xarray: xarray.DataArray object that is of OG1 format

    Returns:
        xarray: xarray.DataArray with density added.
    """

    if 'CONS_TEMP' not in xarray.keys():
        xarray = append_conservative_temp(xarray)
        print('\nCONS_TEMP was not found in the data. It has been calculated (and appended to the data) automatically \n'
              'assuming that all required inputs have the correct units.')

    SA, CT, p = xarray.ABS_SALINITY.values, xarray.CONS_TEMP.values, xarray.PRES.values
    density = rho(SA, CT, p)

    xarray['DENSITY'] = (('N_MEASUREMENTS',), density)
    xarray.DENSITY.attrs = {'long_name': 'Density calculated following TEOS-10, implementation by GSW,'
                                           ' see https://github.com/TEOS-10/GSW-python.',
                              'units': 'kg/m^3',
                              'standard_name': 'Density (rho)',
                              'valid_min': 0,
                              'valid_max': np.inf}

    return xarray