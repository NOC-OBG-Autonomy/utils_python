import numpy as np
import xarray as xr

def qc_xarray(xr, labels: list):
    """
    Applies quality control dropping any bad values from the xarray.
    Args:
        xr: xarray.DataArray object that is of OG1 format
        labels: list of (str) labels that are the names of the variables QC will be applied to. Note that this
                variable needs to have a corresponding ancillary _QC variable.

    Returns:
        xr_qc: xarray.DataArray object where any QC flagged values have been converted to nans.
    """
    xr_qc = xr.copy()
    for label in labels:
        if (label + '_QC') in xr_qc.keys():
            qc_vals = np.where(np.isnan(xr_qc[label + '_QC'].values), np.float32(np.nan), xr_qc[label].values)
            xr_qc[label].values = qc_vals
        else:
            print(f'"{label}_QC" not found. Skipping...')
    return xr_qc