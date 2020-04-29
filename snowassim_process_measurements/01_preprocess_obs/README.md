### Workflow from CSV download of measurements on the CSO website to CSV inputs for the 
---
---
This is not a comprehensive guide, but gives an idea of all of the things that need to happen 
complete the workflow from CSV data on the website to the SnowAssim input files. 

---
---
**(Step 1)**

Pull CSO raw data from the website:

Inputs: Lat/Long Bounding Box
Min_Long, Max_Lat, Max_Long, Min_Lat
-146.4828057, 61.538588, -144.879882, 60.9651385
Outputs: A CSV with all the snow depths and other information

---
---
**(Step 2)**

Do a lot of data clean up and re-org.
1. Save the csv original copy to reference later
1. Create a new .xlsx copy as the working copy
1. Use text to columns to divide the date into Month, Day, Year by hand
1. Delete unnecessary columns
1. Make sure the LAT and LON columns have the same number of decimal digits
1. Add a column with snow depth in meters
1. Add a column with snow depth in mm
1. Relabel column headers appropriately

---
---
**(Step 3)**

Get the albers_x, albers_y, and sturm classification data added

For Albers X,Y:
1. Open the QGIS Add Albers Geometry map
1. Create a copy of the working excel file, but save as csv
1. import the csv using the csv import tool, make sure to import LON as X and LAT as Y
1. make sure to import as WGS84, even though the project CRS is albers
1. Go to Vector >> Geometry Tool >> Export/Add XY Columns
	* make sure input layer is in WGS84
	* choose calculate using >> project CRS 
1. Save temporarily, open attribute table, select all, copy to clipboard, open 
	working excel sheet, paste into a new worksheet, text to columns, save only
	the X and Y columns into the working excel sheet

---
---
**(Step 4)**

Add a column with Hill depth-to-SWE model
1. Go to https://github.com/communitysnowobs/snowdensity to find the code for converting snow depth measurements to SWE.
1. Run the code on your column and add to the CSV.

