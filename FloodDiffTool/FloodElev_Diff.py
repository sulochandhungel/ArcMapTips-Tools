import arcpy
from arcpy import env
from arcpy.sa import *


########## Input Variables ####################################################
Pr_100yr = r"C:\Users\sudh\Desktop\JUNK\SMS_try\Chad2\100yr_Proposed_Water_Elev_ft_48.tif"
Ex_100yr = r"C:\Users\sudh\Desktop\JUNK\SMS_try\Chad2\100yr_Existing_Water_Elev_ft_24.tif"
Poly_layerfile = r"C:\Users\sudh\Desktop\JUNK\SMS_try\Chad2\Mosaicked_Polygon2.lyrx"
Ras_layerfile = r"C:\Users\sudh\Desktop\JUNK\SMS_try\Chad2\Diff_Layer2.lyrx"
Output_folder = r"C:\Users\sudh\Desktop\JUNK\SMS_try\Chad2"
SiteID = "101100"

# Create working GDB
workGDB = SiteID + "_working"
workGDB_path = Output_folder + "\\" + workGDB + ".gdb"
if arcpy.Exists(workGDB_path):
    print(workGDB + " file geodatabase already exists")
else:
    print("Creating " + workGDB + " file geodatabase")
arcpy.CreateFileGDB_management(Output_folder,workGDB)

working_gdb = workGDB_path
arcpy.env.workspace = working_gdb
arcpy.env.scratchWorkspace = working_gdb
arcpy.env.transferDomains = True
arcpy.env.overwriteOutput = True


# PROCESS
Ex_Minus_Pr = Raster(Pr_100yr) - Raster(Ex_100yr)
Ex_Minus_Pr.save("Ex_minus_Pr")

Ex_only = Con(Raster(Ex_100yr)>0, 1, 0)
Pr_only = Con(Raster(Pr_100yr)>0, 3, 2)
Common_Pr_Ex = Raster(Ex_only) + Raster (Pr_only)

Mos_rasName = "Mosaicked"
Mos_Poly = "MosPoly"
Mos_Ras = arcpy.MosaicToNewRaster_management(input_rasters = [Ex_only, Pr_only, Common_Pr_Ex], output_location = working_gdb,\
                                   raster_dataset_name_with_extension = Mos_rasName, pixel_type = "8_BIT_UNSIGNED",\
                                   number_of_bands = "1", mosaic_method = "SUM",\
                                   mosaic_colormap_mode = "FIRST")

arcpy.RasterToPolygon_conversion(Mos_Ras, Mos_Poly, "NO_SIMPLIFY", "VALUE")
arcpy.ApplySymbologyFromLayer_management(Mos_Poly, Poly_layerfile)

print ("Done!")

#Apply symbology
arcpy.ApplySymbologyFromLayer_management(Ex_Minus_Pr, Ras_layerfile)





