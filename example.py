from functions.base_netCDF.load_netcdf import *
from functions.operations.qc_xarray import *
from functions.operations.interpolate_xarray import *
from functions.operations.plot_glider_timeseries import *

# Path to a .nc file which is OG1 formatted. Put the file path in the quotation marks.
path = r"C:\Users\banga\Desktop\Repos\Phyto-Phys\Data\Churchill_501_R.nc"

vars = ['PRES', 'ELAPSED_TIME', 'CHLA']  # The variables we are interested in. Only these will be operated on.
xarray = load_netcdf(path)
xarray = qc_xarray(xarray, labels=vars)
xarray = interpolate_xarray(xarray, labels=vars)

# I'd like to plot some timeseries data to see if it's OK. If you hold CTRL and click the function name
# "plot_glider_timeseries" then you will be taken to the function definition where the arguments are also defined.
# NOTE: The QC and interpolation functions prior to this are not necessary as the function will try to repeat them on
# the variables it has been parsed anyway.
plot_glider_timeseries(xarray, 'PRES', 'TEMP')


