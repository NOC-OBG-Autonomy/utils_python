from .qc_xarray import *
from .interpolate_xarray import *
from .append_elapsed_time import *
from .grid_variable import *
import seaborn as sns
import numpy as np

def plot_glider_timeseries(xarray, y_label: str, z_label: str, colourbar_range = None,
                           gridding_settings = {'resolution': [300, 300],
                                                'operation': 'mean',
                                                'norm_function': 'linear'}, figsize=(12, 8)):
    """
    Plots a glider timeseries with ELAPSED_TIME [s] on the x-axis and user specified y and z dimensions. The figure is
    made of 3 plots: A raw data scatterplot, a gridded data timeseries and the KDE estimates of both. The KDE estimate
    plot has red and green lines representing the minimum and maximum colourbar values for the gridded and raw plots.
    These can be selected by the user through the colourbar_range argument but by default are set to the 1st and 99th
    percentile values of the raw data.

    Args:
        xarray: xarray.DataArray object that is of OG1 format
        y_label: string variable name of the y dimension for plotting
        z_label: string variable name of the z dimension for plotting - the z dimension is the colour of the points
        colourbar_range: Defines the minimum and maximum values of the colourbar. Default (None) uses the 1st and 99th
                         percentiles. User may override with a list [min, max] where min and max are float convertable.
        gridding_settings: See args for grid_variable.py
        figsize: tuple figure dimensions eg. (length, height)
    """

    # At the moment, QC and interpolation are nessescary for plotting due to most row inputs haveing at least one nan
    # input due to desynchronization of the sensor clocks. Without interpolating these nans, the majority of points are lost
    xarray = qc_xarray(xarray, labels=[y_label, z_label])
    xarray = interpolate_xarray(xarray, labels=[y_label, z_label])

    grid_data = grid_variable(xarray, 'ELAPSED_TIME', y_label, z_label,
                              resolution=gridding_settings['resolution'], operation=gridding_settings['operation'],
                              plotting=False, norm_function=gridding_settings['norm_function'])

    if colourbar_range is None:
        temp_array = xarray[z_label]
        temp_array = temp_array[~np.isnan(temp_array)]
        vmin, vmax = np.percentile(temp_array, [1, 99])  # Default sets vmin and vmax to the 1st and 99th percentiles
    else:
        vmin, vmax = colourbar_range

    axes_lims = [xarray.ELAPSED_TIME.min(), xarray.ELAPSED_TIME.max(), xarray[y_label].max(), xarray[y_label].min()]
    fig, axs = plt.subplots(nrows=3, figsize=figsize)

    # Plot histograms
    sns.histplot(x=xarray[z_label], bins=200, kde=True, stat='density', ax=axs[0], alpha=0.5, label='raw')
    sns.histplot(x=grid_data.flatten(), bins=200, kde=True, stat='density', ax=axs[0], color='grey', alpha=0.5, label='grid')
    axs[0].axvline(x=vmin, color='r', label='Colourbar Min'), axs[0].axvline(x=vmax, color='g', label='Colourbar Max')
    axs[0].set(title=f'{z_label} Raw and Gridded KDE')
    axs[0].legend()

    # Plot scatterplot
    sns.scatterplot(x=xarray.ELAPSED_TIME, y=xarray[y_label], hue=xarray[z_label], hue_norm=(vmin, vmax), ax=axs[1],
                    palette='viridis', legend=None, edgecolor=None, alpha=0.5, s=2)
    axs[1].set_xlim(axes_lims[:2]), axs[1].set_ylim(axes_lims[2:])
    axs[1].set(title='Raw Data')

    # Plot gridded data
    axs[2].imshow(grid_data.T, aspect='auto', norm='linear', extent=axes_lims, vmin=vmin, vmax=vmax)
    axs[2].sharex(axs[1]), axs[2].sharey(axs[1])
    axs[2].set(title='Gridded Data', xlabel='ELAPSED_TIME', ylabel=y_label)

    plt.tight_layout()
    plt.show(block=True)
