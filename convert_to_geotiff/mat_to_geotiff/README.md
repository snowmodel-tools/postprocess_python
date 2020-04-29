#### Jupyter Notebook for processing matfiles and converting them to Geotiff.
---
---
Ryan L. Crumley, 2019; ryanlcrumley@gmail.com
---
---
**mat_to_geotiff.ipynb**
This Jupyter Notebook processes matfiles from a specific date/iteration of a SnowModel run using Python. The script has detailed commenting that explains each variable, and two functions.
1. The Grads_to_Array function reads in the gdat files to a Numpy Array.
1. The Array_to_Geotiff function uses GDAL to turn the Numpy Array into a geolocated geotiff.
1. The final cell in the Jupyter Notebook chooses the timeslices (that must correspond to the 
printed variable timesteps from the gdat) and prints only the selected subset to a geotiff in the 
geotiff folder. 

The matfiles used in this script were created by the *mk_matrix_for_date.m* script found in the postprocessing_matlab repository.