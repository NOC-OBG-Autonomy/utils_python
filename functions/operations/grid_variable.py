import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def grid_variable(xarray, x_dim_label: str, y_dim_label: str, target: str, resolution=[10, 10], operation='mean',
                  plotting=False, plotting_norm='symlog'):
    """
    Applies an operation to the target variable in each grid element defined by the grid dimensions and resolution
    Args:
        xarray: xarray.DataArray object that is of OG1 format
        x_dim_label: string variable name of the x dimension of the grid
        y_dim_label: string variable name of the y dimension of the grid
        target: string variable name of the variable you would like to be operated on over the grid. May be interpreted
                as the z dimension of the grid.
        resolution: list of dimensions of the grid specified in number of cells. eg. a 2x5 grid would be [2, 5] and the
                    output grid would have 2 columns and 5 rows.
        operation: string name of the operation to be applied to the data in each grid cell. Options are: 'mean', 'std',
                   'median', 'count', 'sum', 'min', 'max', or a user-defined function which takes a 1D array of values,
                   and outputs a single numerical statistic.
        plotting: If True, will plot an image representation of the final grid.
        plotting_norm: Is the function used to map aray data values to a colour bar for image plotting.
                       Options are: 'asinh', 'function', 'functionlog', 'linear', 'log', 'logit', 'symlog'


    Returns:
        grid_data: 2D numpy array of gridded data.
    """

    x_dim, y_dim, z_dim = (xarray[x_dim_label].values,
                           xarray[y_dim_label].values,
                           xarray[target].values)

    x_dim_grid, y_dim_grid = (np.linspace(min(x_dim), max(x_dim), resolution[0]),
                              np.linspace(min(y_dim), max(y_dim), resolution[1]))

    grid_data = stats.binned_statistic_2d(x_dim, y_dim, z_dim, operation, bins=[x_dim_grid, y_dim_grid]).statistic

    if plotting:
        print('Close the figure to proceed')
        no_nan_grid = grid_data[~np.isnan(grid_data)]
        grid_mean, grid_std = no_nan_grid.mean(), no_nan_grid.std()
        vmin, vmax = grid_mean - 3*grid_std, grid_mean + 3*grid_std
        plt.imshow(grid_data.T[:, ::-1], aspect='auto', norm=plotting_norm, vmin=vmin, vmax=vmax)
        plt.show(block=True)

    return grid_data.T[:, ::-1]