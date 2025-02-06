from gsw.conversions import z_from_p

def append_depth(xarray):
    """
    Converts pressure to depth and appends it to the xarray
    Args:
        xarray: xarray.DataArray object that is of OG1 format

    Returns:
        xarray: xarray.DataArray with depth added.
    """
    p, lat = xarray.PRES.values, xarray.LATITUDE.values
    depth = z_from_p(p, lat)

    xarray['DEPTH'] = (('N_MEASUREMENTS',), depth)
    xarray.DEPTH.attrs = {'long_name': 'Depth calculated following TEOS-10, implementation by GSW, see'
                                       'https://github.com/TEOS-10/GSW-python. Dynamic height anomoly and'
                                       'sea surface geopotential are assimed to be 0',
                                       'units': 'm',
                                       'standard_name': 'Depth (z)',
                                       'valid_min': -10935,
                                       'valid_max': 0}

    return xarray