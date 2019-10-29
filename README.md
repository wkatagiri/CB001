# CB001
These codes are written for fluorescence image analysis image analysis over different time points.
Codes are written by python 3.6, and use common libraries, numpy, openCV2, and tqdm (optional).
We used these codes to analyse T cells which sizes are around 10 µm, respectively. If you want to use the program for other cells, you may need to edit the code as accordingly.

First file, "No1_Functions", contains two functions to recognize cells. One recognizes centers of cells, and the other considers only cells that did not move over time as signal.
Second file, "No2_Function", contains two functions to convert, sort informations for our purposes. One convert the location of the cells (coodinates of x-y Euclian Space) into irradiance which the cells experienced. The constant numbers for curve fitting are defined from independent experiments. Another is to sort the data based on two irradiance information.
Third file, "No3_Program", runs with previous two functions and analyze images and create summary xlsx file.
