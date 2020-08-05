"""
This tool provides the possibility to extract surface flow velocities from two 
sequential images using the Particle Image Velocimetry (PIV).

For this tool to work, OpenPIV is needed which can be installed using conda:
>>> conda install -c conda-forge openpiv

Or using pip:
>>> pip install numpy cython
>>> pip install openpiv --pre

These functions are based on OpenPIV v0.21.3
"""

import os
import numpy as np
import pylab
from openpiv import tools, process, scaling, pyprocess, validation, filters

def PIV(
    frame_0,
    frame_1,
    winsize,
    searchsize,
    overlap,
    frame_rate,
    scaling_factor,
    threshold=1.3,
    output='fil'
       ):
    """
    Particle Image Velocimetry processing for two sequential images.
    
    Input:
    ------
    frame_0 - first frame to indicate potential seeds.
    frame_1 - second frame to trace seed displacements.
    winsize - size of the individual (square) grid cells in pixels.
    searchsize - size of the search area in pixels in which the location with the highest similarity is found.
    overlap - overlap over the grid cells in pixels.
    frame_rate - frame rate of the video in frames per second (fps).
    scaling_factor - amount of pixels per meter.
    output - after which step the PIV processing is stopped ('raw', 'fil', or 'int'; default: 'fil')
    """

    # determine the timestep between the two sequential frames (1/fps)
    dt = 1./frame_rate

    # estimation of seed displacements in x and y direction
    # and the corresponding signal-to-noise ratio
    u, v, sig2noise = pyprocess.extended_search_area_piv(
                        frame_0,
                        frame_1,
                        window_size=winsize,
                        overlap=overlap,
                        dt=dt,
                        search_area_size=searchsize,
                        sig2noise_method='peak2peak')

    # xy-coordinates of the centre of each grid cell 
    x, y = pyprocess.get_coordinates(image_size=frame_0.shape,
                                     window_size=winsize,
                                     overlap=overlap)

    # if ouput is 'fil' or 'int':
    # filter out grid cells with a low signal-to-noise ratio
    if output == 'fil' or  output == 'int':
        u, v, mask = validation.sig2noise_val(u,
                                              v,
                                              sig2noise,
                                              threshold=threshold)

        # if output is 'int'
        # fill in missing values through interpolation
        if output == 'int':
            u, v = filters.replace_outliers(u,
                                            v,
                                            method='localmean',
                                            max_iter=50,
                                            kernel_size=3)

    # scale results based on the pixels per metres
    x, y, u, v = scaling.uniform(x,
                                 y,
                                 u,
                                 v,
                                 scaling_factor=scaling_factor)

    return x, y, u, v, sig2noise
