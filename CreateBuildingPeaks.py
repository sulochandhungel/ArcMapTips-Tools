# for (i in 5:10)
# Buffer by i*-2 ft increments
# Convert buffered polygon to line
# Convert Line to raster
# Use raster Calc to make the raster value to Build_Terr_10ft + i*0.05
# Mosaic to existing raster


import arcpy
from arcpy import env
from arcpy.sa import *
arcpy.CheckOutExtension ("Spatial")
arcpy.env.overwriteOutput = True

outFolder = "C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\PeakB"
env.workspace=outFolder


Fp_Poly = "C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\PeakB\Building_Poly.shp"
Exist_Ras = "C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\PeakB\Mosaicked.tif"
Build_10ftRas = "C:/Users/sulochan.dhungel/Sulochan/Puunene/GISandCAD/building footprints/Building_Max_Terr_plus_10ft.tif"


#Projec = "PROJCS['NAD_1983_HARN_StatePlane_Hawaii_2_FIPS_5102_Feet',GEOGCS['GCS_North_American_1983_HARN',DATUM['D_North_American_1983_HARN',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-156.6666666666667],PARAMETER['Scale_Factor',0.9999666666666667],PARAMETER['Latitude_Of_Origin',20.33333333333333],UNIT['Foot_US',0.3048006096012192]]"
for i in range(79,100):
    buff_dist = -i*2
    buff_poly = "C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\PeakB\Poly_.shp"#+str(i)+".shp"
    arcpy.Buffer_analysis(Fp_Poly, buff_poly, buff_dist)
    
    buff_line = "C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\PeakB\Line_.shp"#+str(i)+".shp"
    arcpy.FeatureToLine_management(buff_poly, buff_line)
    
    line_ras = "C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\PeakB\LineRas_.tif"#_"+str(i)+".tif"
    arcpy.env.snapRaster = Build_10ftRas
    arcpy.FeatureToRaster_conversion(buff_line, "FID", line_ras, 2)
    
    ans_ras = "C:\Users\sulochan.dhungel\Sulochan\Puunene\GISandCAD\PeakB\AnsRas_"+str(i)+".tif"
    arcpy.env.snapRaster = Build_10ftRas
    OutRas = Raster(line_ras) - Raster(line_ras) + Build_10ftRas + (i*0.05)
    OutRas.save(ans_ras)








