from gsw.conversions import CT_from_t
from. append_salinity_from_conductivity import *

def append_conservative_temp(xarray):
    """
    Converts conductivity measurements to practical and abosolute salinity which are appended to the xarray
    Args:
        xarray: xarray.DataArray object that is of OG1 format

    Returns:
        xarray: xarray.DataArray with conservative temperature added.
    """

    if 'ABS_SALINITY' not in xarray.keys():
        xarray = append_salinity_from_conductivity(xarray)
        mean_SA = float(xarray.ABS_SALINITY.mean())
        print('\nABS_SALINITY was not found in the data. It has been calculated (and appended to the data) automatically \n'
              'assuming that all required inputs have the correct units. \nThe mean of the calculated absolute salinity is:'
              f' {mean_SA} g/kg.')

    SA, t, p = xarray.ABS_SALINITY.values, xarray.TEMP.values, xarray.PRES.values
    conservative_temp = CT_from_t(SA, t, p)

    xarray['CONS_TEMP'] = (('N_MEASUREMENTS',), conservative_temp)
    xarray.CONS_TEMP.attrs = {'long_name': 'Conservative temperature calculated following TEOS-10, implementation by GSW,'
                                           ' see https://github.com/TEOS-10/GSW-python.',
                              'units': 'Degrees Celsius',
                              'standard_name': 'Conservative Temperature (CT)',
                              'valid_min': -273.15,
                              'valid_max': 100}
    return xarray