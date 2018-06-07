#!/usr/bin/env python3

import glob
import matplotlib
import os

# define path
current_path = os.getcwd()
# list all stylesheets
stylesheets = glob.glob('stylelib/*.mplstyle')

# locate the matplotlib config directory
configuration_path = matplotlib.get_configdir()

# make a list of all style sheets

for sheet in stylesheets:
    # symlink all style sheets to config directory
    src = os.path.join(current_path, sheet)
    dst = os.path.join(configuration_path)
    try:
        os.symlink(src, dst)
    except FileExistsError:
        print('Error: {} already exists!'.format(sheet))
