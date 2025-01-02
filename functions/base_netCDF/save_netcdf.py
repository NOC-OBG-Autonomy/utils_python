import xarray as xr
import numpy as np
import os

def save_netcdf(xarray, save_path: str):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_format_set = set(np.genfromtxt(os.path.join(script_dir, r'config/save_format.txt'), dtype=str))
    data_vars_set = set(xarray.data_vars)

    if data_vars_set & save_format_set == save_format_set:
        save = True
        extra_vars_set = data_vars_set - save_format_set
        if not extra_vars_set:
            print(f'All required variables found. Saving to {save_path}')
        else:
            print(f'All required variables found. Extra variables {extra_vars_set} were also found.')
            dont_save_extras = input('Would you like them to be saved as well? [Y/n]: ').lower() == 'n'
            if dont_save_extras:
                xarray = xarray.drop_vars(list(extra_vars_set))
    else:
        save = False
        missing_vars_set = save_format_set - data_vars_set
        # numpy is being annoying and np.genfromtxt is returning np.str_ types instead of simple str so this print isn't pretty.
        print(f'The following required variables are missing {missing_vars_set}. Aborting...')

    if save:
        xarray.to_netcdf(save_path)
