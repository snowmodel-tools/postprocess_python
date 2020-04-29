### Remote sensing validation scripts
---
---
#### Ryan Crumley, 2020; ryanlcrumley@gmail.com
---
---

This workflow is designed to use gdat output from SnowModel and created aligned and resampled geotiffs ready for spatial analysis in section 02.

This workflow uses:
1. SnowModel output gdat files
1. QGIS
1. Jupyter Notebooks

---
---

**(Step_01)**

* Use the *gdat_to_geotiff* script to convert the SnowModel output from a particular a date (SnowModel iteration) to geotiff.
* There can be multiple dates or multiple SnowModel runs, as in the case of ensemble runs based on different assimilation inputs.
* Save these to the geotiffs folder.

---
---

**(Step_02)**

* Convert the remotely sensed (RS) data to geotiff, make sure to reproject to the correct CRS.
* Also make sure the new RS geotiff has been interpolated where 'holes' in the data due to vegetation effects are corrected.
* At this point, the RS geotiff and the SM output does not need to have an aligned grid or the same resolution.
* NOTE: The RS original resolution datasets are not included in the example geotiff folders because of their size. However, the aligned and resampled example RS geotiffs are included in the data/aligned_resampled folders.

---
---

**(Step_03)**

* Align and resample the RS product and the SM output geotiffs using QGIS3 > Raster > Align Raster tool.
* Make sure to choose the RS product as the reference layer. 
* Use the RS product CRS that will need to be previously reprojected to the SnowModel CRS.
* Change the cell size to match the SnowModel cell size (this will set the grid to the reference layer's grid) 
* Do not set the Grid Offset
* Check the Clip to Extent box
* Add every additional geotiff that needs to be aligned by clicking the green plus symbol at the top.
	* Select the input layer geotiff from the list (it must already be added to the QGIS map)
	* Choose a filename and folder that makes sense
	* IMPORTANT: for resampling method, choose 'Average' or choose another method based on your needs
* Click OKAY
* Now the RS product and the SnowModel geotiffs will be on the exact same grid and clipped to the extent of the RS product.

Move to folder 02 to generate statistics and figures. 
