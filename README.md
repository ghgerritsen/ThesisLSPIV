# ThesisLSPIV
Coding for MSc Thesis Flood Wave Monitoring using LSPIV - TU Delft

Link:
https://repository.tudelft.nl/islandora/object/uuid%3A5d856ba9-a207-4b61-8bb7-703322fe3154?collection=education

This filder contains four example notebooks containing the (basics) of the coding used for my thesis. These notebooks are:

- Part 1: Image preparation: lens distortion correction, 4-point orthorectification, gray scaling, contrast- and gamma correction. All using OpenCV;
- Part 2: PIV processing: PIV processing using OpenPIV. In this method filtering is applied based on the signal-to-noise ratio;
- Part 3: Post-processing: filtering and substitution of surface flow velocities and calculation of the (mean) discharge.
- Part 4: Alternative to the filtering process provided using Otsus Thresholding

The notebooks are based on the _example_video.mp4_ and for the last notebooks the .csv file containing the local bathymetry is used to determine the discharge.

The first two notebooks use functions defined in `imageprep.py` and `pivprocessing.py`.
