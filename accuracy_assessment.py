# Import packages
import arcpy
from arcpy.sa import *
arcpy.env.overwriteOutput = True
import pandas as pd


# Set workspace
arcpy.env.workspace = r"D:\phragmites\phrag_class_3_27\phrag_class"

# Set output folder
path_out = "D:\phragmites\phrag_class_3_27\phrag_class"

# Read in data
    # Feature class to clip the data to
points = 'phrag_3_27_test.shp'
    # Set field name from the feature class that contains the name of the zones

raster = r"D:\phragmites\phrag_class_3_27\phrag_class\phrag_class.gdb\phrag_3pca_mask"

ExtractValuesToPoints(points, raster, 'raster_points.shp')

arcpy.analysis.Frequency('raster_points.shp', 'accuracy_frequency.shp', ["RASTERVALU", 'class'])

arcpy.management.PivotTable('accuracy_frequency.dbf', 'RASTERVALU', 'class', 'Frequency', 'accuracy_matrix.csv')
