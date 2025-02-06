from gsw.conversions import SP_from_C, SA_from_SP
from .interpolate_xarray import *
from .qc_xarray import *


def append_salinity_from_conductivity(xarray, unit_conversion_const=1):
    """
    Converts conductivity measurements to practical and abosolute salinity which are appended to the xarray
    Args:
        xarray: xarray.DataArray object that is of OG1 format
        unit_conversion_const: float value to convert conductivity units to mS/cm. OG1 format should have this as
                               default, but sometimes data can be in mhos/m (== 10 mS/cm)

    Returns:
        xarray: xarray.DataArray with practical and absolute salinity measurements added.
    """
    xarray = qc_xarray(xarray, labels=['PRES', 'TEMP', 'CNDC', 'LATITUDE', 'LONGITUDE'])
    xarray = interpolate_xarray(xarray, labels=['PRES', 'TEMP', 'CNDC', 'LATITUDE', 'LONGITUDE'])

    C = xarray.CNDC.values * unit_conversion_const  # 1 mhos/m == 10 mS/cm
    T, P, lat, long = xarray.TEMP.values, xarray.PRES.values, xarray.LATITUDE.values, xarray.LONGITUDE.values
    prac_salinity = SP_from_C(C, T, P)
    abs_salinity = SA_from_SP(prac_salinity, P, long, lat)

    xarray['PRAC_SALINITY'] = (('N_MEASUREMENTS',), prac_salinity)
    xarray.PRAC_SALINITY.attrs = {'long_name': 'Practical salinity calculated following TEOS-10, implementation by GSW, see'
                                               'https://github.com/TEOS-10/GSW-python. Values follow PSS-78 scale',
                                  'units': 'unitless',
                                  'standard_name': 'Practical Salinity (SP)',
                                  'valid_min': 0,
                                  'valid_max': np.inf}
    xarray['ABS_SALINITY'] = (('N_MEASUREMENTS',), abs_salinity)
    xarray.ABS_SALINITY.attrs = {'long_name': 'Absolute salinity calculated following TEOS-10, implementation by GSW, see'
                                               'https://github.com/TEOS-10/GSW-python.',
                                 'units': 'g/kg',
                                 'standard_name': 'Absolute Salinity (SA)',
                                 'valid_min': 0,
                                 'valid_max': np.inf}
    return xarray