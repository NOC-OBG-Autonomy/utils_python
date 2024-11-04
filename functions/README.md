# Functions folder

Here is a list of all the functions you can find here

## General.py

This script contains general useful functions. 

    - **slide** is a smoothing function (demo function)

## profiling.py

This script contains functions to detect profiles in a glider transect. It contains multiple functions that are called inside the main funtion.
The last part of the script is a reproducible example. 

    - **find_profile_by_depth** is the main function, it returns the indexes of the different profiles
    - **adjust_inflextions** remove bad inflections point (i.e. small variations of elevation speed inside the profile)
    - **find_surfacing** return the indexes of surfacing behavior points inside a glider profile
    - **interp_nan** interpolate NaN values for easy viz
    - **boxcar_smooth_dataset** is running mean smoothing function