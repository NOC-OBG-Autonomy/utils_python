from functions.base_netCDF.load_netcdf import *
from functions.operations.qc_xarray import *
from functions.operations.interpolate_xarray import *
from functions.operations.grid_variable import *

# Path to a .nc file which is OG1 formatted. Put the file path in the quotation marks.
path = r""

vars = ['PRES', 'ELAPSED_TIME', 'CHLA']  # The variables we are interested in. Only these will be operated on.
xarray = load_netcdf(path)
xarray = qc_xarray(xarray, labels=vars)
xarray = interpolate_xarray(xarray, labels=vars)

# I'd like to grid the data and view the output to see if it's OK. If you hold CTRL and click the function name
# "grid_variable" then you will be taken to the function definition where the arguments are also defined.
grid_data = grid_variable(xarray, vars[1], vars[0], vars[2],
                          resolution=[100,300], operation='mean',
                          plotting=True, plotting_norm='linear')
