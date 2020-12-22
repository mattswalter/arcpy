### Run Zonal statistics to table on all rasters in a folder and combine them into one csv.

# Import packages
import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
import pandas as pd
import glob
import os

# Set workspace
arcpy.env.workspace = r"C:\Users\Matt\Desktop\eth"

# Set output folder
path_out = "C:/Users/Matt/Desktop/eth/output/"

# Read in data
    # Feature class to clip the data to
zone = 'ethiopia_csa_fa2007_village_boundary.shp'
    # Set field name from the feature class that contains the name of the zones
field = 'kebname'
    # Read in all raster names in directory
rasters = arcpy.ListRasters("*", "*")

# Set stastic type for the zonal statistics
stat = 'MEAN'

# Run zonal statistics for all rasters in directory and export to excel file
#names = []
i=0
for image in rasters:
    n = image.split('.')[0]
    out = (path_out + str(n) + '.dbf')
    out1 = (path_out + str(n) + '.xls')
    print(out)
    i+=1
    outZSaT = ZonalStatisticsAsTable(zone, field, image,
                                     out, "NODATA", stat)
    table = arcpy.TableToExcel_conversion(outZSaT, out1)


# Set folder to read excel files from
all_files = glob.glob(path_out + "/*.xls")

# Read in excel files as pandas dataframes
li = []
i=0
for filename in all_files:
    df = pd.read_excel(filename, index_col=None)
    if i == 0:
        df = df[[field, stat]]
    else:
        df = df[[stat]]
    head, tail = os.path.split(filename)
    name = tail.split('.')[0]
    i+=1
    df = df.rename(columns={stat: name})
    li.append(df)

# Combine dataframes and export as csv
frame = pd.concat(li, axis=1)
print(frame)
frame.to_csv(path_out + 'test1.csv')