import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace="C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD"

inRaster="C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\elevation_datasets\Recieved\downloadedfromnoaa\Job615571_2007_Hawaiian_Islands.tif"

inRaster="C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\NOAA_Void_Filled_1.tif"

arcpy.CheckOutExtension ("Spatial")

outCon=Con(IsNull(inRaster), FocalStatistics (inRaster, NbrRectangle (4,4, "CELL"), "MEAN"), inRaster)

outCon.save ("C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\NOAA_Void_Filled_2.tif")
